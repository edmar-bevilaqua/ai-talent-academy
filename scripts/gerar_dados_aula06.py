# -*- coding: utf-8 -*-
"""
Gera dados sintéticos para o banco de fraude em cartão da Aula 6 (Semana 3, quinta-feira).

Estende o caso já usado nas Aulas 2 e 5 (clientes, lojistas, transações) para um
esquema de 6 tabelas, com volume suficiente para uma prática de SQL mais próxima do
dia a dia real: dezenas de milhares de transações, não só uma dezena de exemplo.

O FreeSQL web não tem importação de CSV. Por isso a forma recomendada de carregar os
dados grandes (transacoes e contestacoes) é conectar direto no banco por Python e
inserir linha a linha pelo driver oracledb, sem passar por arquivo nenhum: use --carregar.
Os arquivos CSV e o carga_manual.sql continuam sendo gerados, como referência e como
alternativa para as tabelas pequenas dentro do próprio worksheet.

Confirmado no painel "Schema Connection Details" do FreeSQL: a conexão usa TCPS puro,
sem wallet. O DSN tem este formato (host e porta são fixos da plataforma, só o nome do
serviço muda por conta):

    tcps://db.freesql.com:2484/<nome_do_servico_da_sua_conta>

Pré-requisito:
    pip install Faker
    pip install oracledb          (só necessário se for usar --carregar)
    pip install python-dotenv     (opcional, para ler um arquivo .env local)

Uso:
    python scripts/gerar_dados_aula06.py
    python scripts/gerar_dados_aula06.py --transacoes 100000 --seed 7

    # gera os dados e ja carrega direto no FreeSQL, sem CSV
    python scripts/gerar_dados_aula06.py --carregar --recriar \\
        --dsn "tcps://db.freesql.com:2484/SEU_SERVICO" --usuario SEU_USUARIO

    A senha nunca vai por linha de comando: defina FREESQL_PASSWORD no ambiente (ou
    num arquivo .env, veja abaixo), ou deixe o script perguntar na hora.

    Forma mais segura para o dia a dia, um arquivo .env na raiz do repositório (ele já
    está no .gitignore, nunca vai para o Git):

        FREESQL_DSN=tcps://db.freesql.com:2484/SEU_SERVICO
        FREESQL_USER=SEU_USUARIO
        FREESQL_PASSWORD=sua_senha_aqui

    Com o .env preenchido, basta rodar:
        python scripts/gerar_dados_aula06.py --carregar --recriar

Saída (em docs/aula-06/dados/):
    schema.sql          DDL das 6 tabelas, com chave estrangeira, pronto para o FreeSQL
    csv/*.csv            um arquivo por tabela, de referência (não há como importar
                          CSV no FreeSQL web; serve para conferência ou para uma
                          ferramenta externa como o SQL Developer, que tem assistente próprio)
    carga_manual.sql     INSERT em lote (INSERT ALL), só das tabelas pequenas, para
                          colar direto no worksheet do FreeSQL sem precisar de conexão externa
"""
from __future__ import annotations

import argparse
import csv
import getpass
import os
import random
from datetime import date, datetime, timedelta
from pathlib import Path

from faker import Faker

try:
    import oracledb
except ImportError:
    oracledb = None

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "aula-06" / "dados"
CSV_DIR = OUT / "csv"

DATA_INICIO = date(2025, 1, 1)
DATA_FIM = date(2026, 8, 1)

CATEGORIAS = [
    "Alimentação", "Eletrônicos", "Vestuário", "Farmácia", "Combustível",
    "Supermercado", "Joalheria", "Livraria", "Serviços", "Educação",
    "Lazer", "Transporte",
]
BANDEIRAS = ["Visa", "Mastercard", "Elo", "American Express"]
MOTIVOS_CONTESTACAO = [
    "Compra não reconhecida", "Cartão clonado", "Produto não recebido",
    "Cobrança duplicada",
]


# --------------------------------------------------------------------------
# Geração das tabelas
# --------------------------------------------------------------------------
def gerar_categorias():
    return [(i + 1, nome) for i, nome in enumerate(CATEGORIAS)]


def gerar_lojistas(fake, n, categorias):
    lojistas = []
    ids_categoria = [c[0] for c in categorias]
    for i in range(1, n + 1):
        nome = fake.company()
        id_categoria = random.choice(ids_categoria)
        cidade = fake.city()
        estado = fake.estado_sigla()
        data_cadastro = fake.date_between(
            start_date=DATA_INICIO - timedelta(days=365), end_date=DATA_INICIO)
        lojistas.append((i, nome, id_categoria, cidade, estado, data_cadastro))
    return lojistas


def gerar_clientes(fake, n):
    clientes = []
    for i in range(1, n + 1):
        nome = fake.name()
        cpf = fake.cpf()
        cidade = fake.city()
        estado = fake.estado_sigla()
        nascimento = fake.date_of_birth(minimum_age=18, maximum_age=75)
        cadastro = fake.date_between(
            start_date=DATA_INICIO - timedelta(days=800), end_date=DATA_FIM)
        telefone = fake.phone_number() if random.random() > 0.15 else None
        score_risco = round(random.uniform(0, 100), 1)
        clientes.append((i, nome, cpf, cidade, estado, nascimento, cadastro,
                          telefone, score_risco))
    return clientes


def gerar_cartoes(fake, clientes):
    cartoes = []
    id_cartao = 1
    for cliente in clientes:
        id_cliente, _, _, _, _, _, data_cadastro, *_ = cliente
        n_cartoes = random.choices([1, 2], weights=[70, 30])[0]
        for _ in range(n_cartoes):
            bandeira = random.choice(BANDEIRAS)
            final_cartao = f"{random.randint(0, 9999):04d}"
            data_emissao = fake.date_between(
                start_date=data_cadastro, end_date=DATA_FIM)
            limite = round(random.choice(
                [1000, 2000, 3000, 5000, 8000, 10000, 15000, 20000])
                * random.uniform(0.8, 1.2), 2)
            status = random.choices(
                ["ativo", "bloqueado", "cancelado"], weights=[90, 6, 4])[0]
            cartoes.append((id_cartao, id_cliente, bandeira, final_cartao,
                             data_emissao, limite, status))
            id_cartao += 1
    return cartoes


def gerar_transacoes(n, cartoes, lojistas):
    transacoes = []
    ids_cartao = [c[0] for c in cartoes]
    ids_lojista = [l[0] for l in lojistas]
    inicio_ts = datetime.combine(DATA_INICIO, datetime.min.time())
    fim_ts = datetime.combine(DATA_FIM, datetime.min.time())
    intervalo_segundos = int((fim_ts - inicio_ts).total_seconds())
    for i in range(1, n + 1):
        id_cartao = random.choice(ids_cartao)
        id_lojista = random.choice(ids_lojista)
        valor = round(min(max(random.lognormvariate(4.3, 1.0), 5), 15000), 2)
        data_hora = inicio_ts + timedelta(seconds=random.randint(0, intervalo_segundos))
        canal = random.choices(["presencial", "online"], weights=[65, 35])[0]
        status = random.choices(
            ["aprovada", "recusada", "contestada"], weights=[94, 4, 2])[0]
        pais = "Brasil" if random.random() > 0.02 else random.choice(
            ["Estados Unidos", "China", "Portugal", "Argentina"])
        transacoes.append((i, id_cartao, id_lojista, valor, data_hora, canal,
                            status, pais))
    return transacoes


def gerar_contestacoes(transacoes):
    contestacoes = []
    id_contestacao = 1
    for t in transacoes:
        id_transacao, _, _, _, data_hora, _, status, _ = t
        if status != "contestada":
            continue
        dias = random.randint(30, 90)
        data_contestacao = data_hora + timedelta(days=dias)
        motivo = random.choice(MOTIVOS_CONTESTACAO)
        resultado = random.choices(
            ["Estornado", "Negado", "Em análise"], weights=[55, 30, 15])[0]
        contestacoes.append((id_contestacao, id_transacao, data_contestacao,
                              motivo, resultado))
        id_contestacao += 1
    return contestacoes


# --------------------------------------------------------------------------
# Saída: CSV
# --------------------------------------------------------------------------
def formatar_csv(valor):
    if valor is None:
        return ""
    if isinstance(valor, datetime):
        return valor.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(valor, date):
        return valor.isoformat()
    return valor


def escrever_csv(nome, cabecalho, linhas):
    CSV_DIR.mkdir(parents=True, exist_ok=True)
    caminho = CSV_DIR / f"{nome}.csv"
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cabecalho)
        for linha in linhas:
            w.writerow([formatar_csv(v) for v in linha])
    return caminho


# --------------------------------------------------------------------------
# Saída: SQL (schema e carga manual das tabelas pequenas)
# --------------------------------------------------------------------------
SCHEMA_SQL = """\
-- Schema da Aula 6: banco de fraude em cartão, versão estendida.
-- Estende o caso das Aulas 2 e 5 de 3 para 6 tabelas.
-- Ordem de criação importa: uma tabela com FOREIGN KEY só pode ser criada depois
-- da tabela que ela referencia.

CREATE TABLE categorias (
    id_categoria NUMBER PRIMARY KEY,
    nome         VARCHAR2(40)
);

CREATE TABLE clientes (
    id_cliente       NUMBER PRIMARY KEY,
    nome             VARCHAR2(80),
    cpf              VARCHAR2(14),
    cidade           VARCHAR2(60),
    estado           VARCHAR2(2),
    data_nascimento  DATE,
    data_cadastro    DATE,
    telefone         VARCHAR2(20),
    score_risco      NUMBER(5,1)
);

CREATE TABLE lojistas (
    id_lojista     NUMBER PRIMARY KEY,
    nome           VARCHAR2(80),
    id_categoria   NUMBER,
    cidade         VARCHAR2(60),
    estado         VARCHAR2(2),
    data_cadastro  DATE,
    CONSTRAINT fk_lojistas_categoria FOREIGN KEY (id_categoria)
        REFERENCES categorias (id_categoria)
);

CREATE TABLE cartoes (
    id_cartao    NUMBER PRIMARY KEY,
    id_cliente   NUMBER,
    bandeira     VARCHAR2(20),
    final_cartao VARCHAR2(4),
    data_emissao DATE,
    limite       NUMBER(10,2),
    status       VARCHAR2(20),
    CONSTRAINT fk_cartoes_cliente FOREIGN KEY (id_cliente)
        REFERENCES clientes (id_cliente)
);

CREATE TABLE transacoes (
    id_transacao NUMBER PRIMARY KEY,
    id_cartao    NUMBER,
    id_lojista   NUMBER,
    valor        NUMBER(10,2),
    data_hora    DATE,
    canal        VARCHAR2(20),
    status       VARCHAR2(20),
    pais         VARCHAR2(40),
    CONSTRAINT fk_transacoes_cartao FOREIGN KEY (id_cartao)
        REFERENCES cartoes (id_cartao),
    CONSTRAINT fk_transacoes_lojista FOREIGN KEY (id_lojista)
        REFERENCES lojistas (id_lojista)
);

CREATE TABLE contestacoes (
    id_contestacao   NUMBER PRIMARY KEY,
    id_transacao     NUMBER,
    data_contestacao DATE,
    motivo           VARCHAR2(60),
    resultado        VARCHAR2(20),
    CONSTRAINT fk_contestacoes_transacao FOREIGN KEY (id_transacao)
        REFERENCES transacoes (id_transacao)
);
"""

# Ordem inversa da criação: a tabela que tem a chave estrangeira sai primeiro.
DROP_SQL = """\
DROP TABLE contestacoes;
DROP TABLE transacoes;
DROP TABLE cartoes;
DROP TABLE lojistas;
DROP TABLE clientes;
DROP TABLE categorias;
"""


def formatar_valor_sql(valor):
    if valor is None:
        return "NULL"
    if isinstance(valor, bool):
        return "1" if valor else "0"
    if isinstance(valor, (int, float)):
        return str(valor)
    if isinstance(valor, datetime):
        return f"TO_DATE('{valor.strftime('%Y-%m-%d %H:%M:%S')}', 'YYYY-MM-DD HH24:MI:SS')"
    if isinstance(valor, date):
        return f"DATE '{valor.isoformat()}'"
    texto = str(valor).replace("'", "''")
    return f"'{texto}'"


def gerar_insert_all(tabela, colunas, linhas, tamanho_lote=100):
    blocos = []
    for inicio in range(0, len(linhas), tamanho_lote):
        lote = linhas[inicio:inicio + tamanho_lote]
        partes = ["INSERT ALL"]
        for linha in lote:
            valores = ", ".join(formatar_valor_sql(v) for v in linha)
            partes.append(f"  INTO {tabela} ({', '.join(colunas)}) VALUES ({valores})")
        partes.append("SELECT * FROM DUAL;")
        blocos.append("\n".join(partes))
    return "\n\n".join(blocos)


TABELAS_CARGA_MANUAL = {
    "categorias": ["id_categoria", "nome"],
    "clientes": ["id_cliente", "nome", "cpf", "cidade", "estado",
                 "data_nascimento", "data_cadastro", "telefone", "score_risco"],
    "lojistas": ["id_lojista", "nome", "id_categoria", "cidade", "estado",
                 "data_cadastro"],
    "cartoes": ["id_cartao", "id_cliente", "bandeira", "final_cartao",
                "data_emissao", "limite", "status"],
}


# --------------------------------------------------------------------------
# Carga direta no Oracle, sem passar por CSV
# --------------------------------------------------------------------------
def executar_bloco_sql(cursor, bloco_sql, ignorar_erro=None):
    """Roda cada instrução de um bloco DDL separado por ';'. `ignorar_erro` é o
    código Oracle (por exemplo 942 para tabela inexistente) que não deve travar
    o script, útil no DROP quando a tabela ainda não existe."""
    for instrucao in [s.strip() for s in bloco_sql.split(";") if s.strip()]:
        try:
            cursor.execute(instrucao)
        except oracledb.DatabaseError as erro:
            codigo = erro.args[0].code
            if ignorar_erro is not None and codigo == ignorar_erro:
                continue
            raise


def carregar_tabela(cursor, conexao, nome, colunas, linhas, tamanho_lote=2000):
    if not linhas:
        return
    marcadores = ", ".join(f":{i + 1}" for i in range(len(colunas)))
    sql = f"INSERT INTO {nome} ({', '.join(colunas)}) VALUES ({marcadores})"
    total = len(linhas)
    for inicio in range(0, total, tamanho_lote):
        lote = linhas[inicio:inicio + tamanho_lote]
        cursor.executemany(sql, lote)
        conexao.commit()
        print(f"  {nome}: {min(inicio + tamanho_lote, total)}/{total}")


def carregar_no_oracle(dsn, usuario, senha, dados, recriar=False):
    if oracledb is None:
        raise SystemExit(
            "Para usar --carregar, instale antes: pip install oracledb")

    print("Conectando ao FreeSQL...")
    with oracledb.connect(user=usuario, password=senha, dsn=dsn) as conexao:
        with conexao.cursor() as cursor:
            if recriar:
                print("Apagando tabelas existentes, se houver...")
                executar_bloco_sql(cursor, DROP_SQL, ignorar_erro=942)
                conexao.commit()

            print("Criando as 6 tabelas...")
            executar_bloco_sql(cursor, SCHEMA_SQL)
            conexao.commit()

            for nome, colunas, linhas in [
                ("categorias", ["id_categoria", "nome"], dados["categorias"]),
                ("clientes", TABELAS_CARGA_MANUAL["clientes"], dados["clientes"]),
                ("lojistas", TABELAS_CARGA_MANUAL["lojistas"], dados["lojistas"]),
                ("cartoes", TABELAS_CARGA_MANUAL["cartoes"], dados["cartoes"]),
                ("transacoes",
                 ["id_transacao", "id_cartao", "id_lojista", "valor", "data_hora",
                  "canal", "status", "pais"], dados["transacoes"]),
                ("contestacoes",
                 ["id_contestacao", "id_transacao", "data_contestacao", "motivo",
                  "resultado"], dados["contestacoes"]),
            ]:
                print(f"Carregando {nome}...")
                carregar_tabela(cursor, conexao, nome, colunas, linhas)

    print("Carga concluída direto no FreeSQL, sem nenhum arquivo intermediário.")


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--clientes", type=int, default=1500)
    ap.add_argument("--lojistas", type=int, default=300)
    ap.add_argument("--transacoes", type=int, default=50000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--carregar", action="store_true",
                     help="conecta no FreeSQL e carrega os dados direto, sem CSV")
    ap.add_argument("--recriar", action="store_true",
                     help="apaga as tabelas antes de recriar, use junto com --carregar")
    ap.add_argument("--dsn", default=os.environ.get("FREESQL_DSN"),
                     help="ou defina a variável de ambiente FREESQL_DSN")
    ap.add_argument("--usuario", default=os.environ.get("FREESQL_USER"),
                     help="ou defina a variável de ambiente FREESQL_USER")
    args = ap.parse_args()

    random.seed(args.seed)
    fake = Faker("pt_BR")
    Faker.seed(args.seed)

    categorias = gerar_categorias()
    clientes = gerar_clientes(fake, args.clientes)
    lojistas = gerar_lojistas(fake, args.lojistas, categorias)
    cartoes = gerar_cartoes(fake, clientes)
    transacoes = gerar_transacoes(args.transacoes, cartoes, lojistas)
    contestacoes = gerar_contestacoes(transacoes)

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "schema.sql").write_text(SCHEMA_SQL, encoding="utf-8")

    escrever_csv("categorias", ["id_categoria", "nome"], categorias)
    escrever_csv("clientes", TABELAS_CARGA_MANUAL["clientes"], clientes)
    escrever_csv("lojistas", TABELAS_CARGA_MANUAL["lojistas"], lojistas)
    escrever_csv("cartoes", TABELAS_CARGA_MANUAL["cartoes"], cartoes)
    escrever_csv("transacoes",
                 ["id_transacao", "id_cartao", "id_lojista", "valor", "data_hora",
                  "canal", "status", "pais"], transacoes)
    escrever_csv("contestacoes",
                 ["id_contestacao", "id_transacao", "data_contestacao", "motivo",
                  "resultado"], contestacoes)

    dados_por_tabela = {
        "categorias": categorias, "clientes": clientes,
        "lojistas": lojistas, "cartoes": cartoes,
    }
    blocos_sql = [f"-- {nome}\n" + gerar_insert_all(nome, TABELAS_CARGA_MANUAL[nome],
                                                     dados_por_tabela[nome])
                  for nome in ["categorias", "clientes", "lojistas", "cartoes"]]
    (OUT / "carga_manual.sql").write_text(
        "-- Carga manual, só das tabelas pequenas. transacoes e contestacoes\n"
        "-- são grandes demais para colar num worksheet: use --carregar para essas.\n\n"
        + "\n\n".join(blocos_sql) + "\nCOMMIT;\n",
        encoding="utf-8")

    print("OK. Gerado em:", OUT)
    print("categorias:", len(categorias))
    print("clientes:", len(clientes))
    print("lojistas:", len(lojistas))
    print("cartoes:", len(cartoes))
    print("transacoes:", len(transacoes))
    print("contestacoes:", len(contestacoes))

    if args.carregar:
        if not args.dsn or not args.usuario:
            raise SystemExit(
                "Para usar --carregar, informe --dsn e --usuario "
                "(ou defina FREESQL_DSN e FREESQL_USER no ambiente).")
        senha = os.environ.get("FREESQL_PASSWORD") or getpass.getpass(
            "Senha do FreeSQL: ")
        dados = {
            "categorias": categorias, "clientes": clientes,
            "lojistas": lojistas, "cartoes": cartoes,
            "transacoes": transacoes, "contestacoes": contestacoes,
        }
        carregar_no_oracle(args.dsn, args.usuario, senha, dados,
                            recriar=args.recriar)


if __name__ == "__main__":
    main()
