# Dados sintéticos da Aula 6

Base estendida do caso de fraude em cartão, já usado nas Aulas 2 e 5. Aqui ele cresce
de 3 tabelas para 6, e de uma dezena de linhas de exemplo para dezenas de milhares de
transações, para a prática de SQL ficar mais próxima do dia a dia real.

> **Como isso chega até os alunos:** cada aluno tem a própria conta no FreeSQL, e vai
> montar o próprio banco, dentro do próprio Colab. Você (instrutor) gera os dados uma
> vez, aqui, com `scripts/gerar_dados_aula06.py`. Esse script fica só com você: os
> alunos não recebem ele, nem a lógica de geração. O que vai para os alunos, numa pasta
> compartilhada do seu Google Drive, são três coisas: `schema.sql`, a pasta `csv/`, e o
> notebook `carregar_dados_aluno.ipynb`. Cada aluno abre o notebook no próprio Colab,
> conecta na própria conta do FreeSQL e povoa o próprio schema com o mesmo dado.

---

## O esquema

| Tabela | O que guarda | Referência |
|---|---|---|
| `categorias` | Os tipos de lojista (eletrônicos, farmácia, supermercado, e mais) | nenhuma |
| `clientes` | Quem é o dono do cartão | nenhuma |
| `lojistas` | Onde a compra aconteceu | `categorias` |
| `cartoes` | Os cartões de cada cliente, um cliente pode ter mais de um | `clientes` |
| `transacoes` | Cada compra, a tabela grande | `cartoes`, `lojistas` |
| `contestacoes` | O chargeback de uma transação contestada | `transacoes` |

`cartoes` e `contestacoes` são a novidade em relação ao caso simples da Aula 5. Eles
existem para dar suporte a perguntas mais realistas: um cliente pode ter mais de um
cartão, e nem toda transação contestada tem o mesmo desfecho.

A data da contestação segue a mesma regra que a Aula 2 já ensinou: o chargeback demora
de 30 a 90 dias para chegar depois da transação.

---

## Passo 1, só o instrutor: gerar os dados

```bash
pip install Faker
python scripts/gerar_dados_aula06.py                              # padrão: 50 mil transações
python scripts/gerar_dados_aula06.py --transacoes 100000 --seed 7  # para escalar
```

Parâmetros disponíveis: `--clientes`, `--lojistas`, `--transacoes`, `--seed`. Rodar de
novo com o mesmo `--seed` gera exatamente os mesmos dados.

Volume gerado com os valores padrão: 12 categorias, 1.500 clientes, 300 lojistas,
quase 2.000 cartões, 50.000 transações e pouco mais de 1.000 contestações. O arquivo
`transacoes.csv` fica em torno de 3 MB nesse volume.

Isso recria os arquivos `schema.sql` e a pasta `csv/`, que são o que vai para os alunos
no passo 3.

### Opcional: você mesmo carregando no seu FreeSQL, direto do Python

Se você quiser popular a sua própria conta (por exemplo para o roteiro de queries que
já existe em `docs/aula-05/03-queries-freesql.md`), o mesmo script tem um modo de carga
direta, sem passar por CSV nem por notebook.

**Confirmado no painel "Schema Connection Details" do FreeSQL:** a conexão usa TCPS
puro, sem wallet. O host e a porta são fixos da plataforma, só o nome do serviço muda
por conta:

```
tcps://db.freesql.com:2484/<nome_do_serviço_da_sua_conta>
```

**Nunca cole a senha real num arquivo do repositório.** O jeito mais seguro é um
arquivo `.env` na raiz do projeto, que já está no `.gitignore`:

```
FREESQL_DSN=tcps://db.freesql.com:2484/SEU_SERVICO
FREESQL_USER=SEU_USUARIO
FREESQL_PASSWORD=sua_senha_aqui
```

Com o `.env` preenchido:

```bash
pip install oracledb python-dotenv
python scripts/gerar_dados_aula06.py --carregar --recriar
```

Sem `.env`, dá para passar `--dsn` e `--usuario` na linha de comando, e o script
pergunta a senha na hora, escondendo o que você digita.

---

## Passo 2: o que compartilhar com os alunos

Estes itens, numa pasta do Google Drive com o acesso liberado para a turma:

```
schema.sql
csv/categorias.csv
csv/clientes.csv
csv/lojistas.csv
csv/cartoes.csv
csv/transacoes.csv
csv/contestacoes.csv
carregar_dados_aluno.ipynb
exercicios_aluno.sql
```

**Não compartilhe** `scripts/gerar_dados_aula06.py`, `carga_manual.sql`,
`gabarito_respostas.sql` nem `gabarito_respostas.md`. Os dois primeiros são lógica de
geração e um plano B de carga, que ficam só com você. Os dois últimos são as respostas
prontas dos 18 exercícios: compartilhar qualquer um deles anula o exercício.

---

## Passo 3: o que cada aluno faz

Abre `carregar_dados_aluno.ipynb` no Google Colab, a partir da pasta do Drive
compartilhada. O notebook, célula por célula:

1. Instala o driver `oracledb`.
2. Monta o Google Drive do próprio aluno, para enxergar `schema.sql` e `csv/`.
3. Pede para o aluno confirmar o caminho da pasta dentro do Drive dele.
4. Pede DSN, usuário e senha do **próprio** schema do aluno (painel Schema Connection
   Details), com a senha escondida ao digitar.
5. Cria as 6 tabelas, com uma célula opcional de `DROP TABLE` para quem quiser
   recomeçar do zero.
6. Lê cada CSV e carrega na tabela correspondente, em lotes de 2 mil linhas, na ordem
   certa por causa das chaves estrangeiras.
7. Confere a contagem final de cada tabela.

Ao final, o aluno tem, na própria conta do FreeSQL, o mesmo banco de 6 tabelas e o
mesmo volume de dados usado na aula, pronto para rodar as consultas.

Depois disso, o aluno abre `exercicios_aluno.sql` no worksheet do FreeSQL e resolve as
18 perguntas, escrevendo a consulta de cada uma logo abaixo do enunciado, que fica como
comentário. `gabarito_respostas.sql` e `gabarito_respostas.md`, na mesma pasta, trazem
as respostas prontas, testadas contra os dados reais, para você conferir rápido durante
a mentoria ou usar de referência ao circular pelas salas.

---

## Integridade dos dados

Toda chave estrangeira gerada aqui foi conferida: nenhum lojista aponta para categoria
inexistente, nenhum cartão aponta para cliente inexistente, nenhuma transação aponta
para cartão ou lojista inexistente, e toda transação contestada tem exatamente uma
contestação correspondente. Se você regerar os dados com outros parâmetros, essa
garantia continua valendo, porque o script sempre gera as tabelas na ordem certa e sorteia
os identificadores a partir do que já existe.

A lógica de conversão de tipo do notebook (data, inteiro, decimal) foi testada contra
as 54.794 linhas geradas com os parâmetros padrão, sem nenhum erro de conversão.

---

## Arquivos deste pacote

```
schema.sql                      DDL das 6 tabelas, com chave estrangeira
carga_manual.sql                Plano B do instrutor: INSERT ALL das 4 tabelas pequenas
carregar_dados_aluno.ipynb      O notebook que cada aluno roda no próprio Colab
exercicios_aluno.sql            As 18 perguntas, para o aluno responder no worksheet
gabarito_respostas.sql          Instrutor: as 18 respostas, prontas para rodar
gabarito_respostas.md           Instrutor: as mesmas respostas, com explicação da técnica
csv/categorias.csv
csv/clientes.csv
csv/lojistas.csv
csv/cartoes.csv
csv/transacoes.csv
csv/contestacoes.csv
```
