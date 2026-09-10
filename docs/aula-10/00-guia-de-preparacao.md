# Guia de preparação: Aula 10 (Semana 5, quinta-feira)

Este documento é o guia operacional para Edmar preparar, instalar e ensaiar a
Aula 10 antes de produzir os slides, não o material de sala. Cobre os dois cenários
combinados: Apache Airflow rodando na máquina do instrutor, e PySpark rodando no
Google Colab para a turma inteira, mais a atividade de pipeline que os alunos vão
executar.

## O que tem aqui

| Arquivo | O que é | Para quem |
|---|---|---|
| **`00-guia-de-preparacao.md`** | Este guia | Edmar |
| [`dag_fraude_aula10.py`](dag_fraude_aula10.py) | A DAG de demonstração do Airflow, pronta para copiar para a pasta `dags/` | Edmar |
| [`pyspark_aluno.ipynb`](pyspark_aluno.ipynb) | O notebook da atividade prática, com células de setup prontas e o pipeline com `# TODO` para completar | Alunos |
| [`pyspark_professor.ipynb`](pyspark_professor.ipynb) | O mesmo notebook, já resolvido, usado para a demonstração ao vivo e como gabarito | Edmar |

Os dois notebooks compartilham a mesma estrutura de passos (setup, extract,
transform, unify e load), incluindo a mesma tentativa de junção que dispara o erro
de coluna ambígua descrito na seção 4.3. No notebook do professor essa célula é
mantida de propósito, para reproduzir o erro ao vivo antes de mostrar a correção.

---

## 0. Uma correção de premissa, antes de seguir

O plano partiu da ideia de que "o Google Colab já oferece uma interface do PySpark".
Isso não é exato: o Colab vem com Python e um conjunto grande de bibliotecas
pré-instaladas, mas **nem Java nem PySpark fazem parte dessa lista**. Sem Java, o
Spark não roda, porque o motor do Spark é escrito em Scala/JVM por baixo do PySpark.

A boa notícia é que isso não compromete o objetivo de mínima fricção. A instalação
cabe em duas linhas de comando, roda em menos de dois minutos, e só precisa ser feita
uma vez por sessão do Colab. A seção 3 traz a célula de setup exata, testada, para
colar no início do notebook de cada aluno.

---

## 1. Visão geral dos dois cenários

| | Cenário 1: Apache Airflow | Cenário 2: PySpark |
|---|---|---|
| Quem instala | Só Edmar, na própria máquina | Cada aluno, dentro do Colab (sem instalar nada no computador) |
| Papel na aula | Demonstração ao vivo, ninguém mais toca | Todo mundo interage, é a base da atividade prática |
| Ambiente | Docker, na máquina local | Google Colab, na nuvem |
| O que mostra | Orquestração: DAG, agendamento, retomada após falha | Paralelismo: a mesma sintaxe de pandas processando em várias partições |
| Risco de fricção para o aluno | Nenhum, é só demonstração | Baixo, duas células de setup coladas e prontas |

Os dois cenários reaproveitam a base de fraude em cartão já conhecida da turma desde
a Aula 2 (categorias, clientes, lojistas, cartões, transações, contestações), mantendo
a continuidade que funcionou nas Aulas 5, 6, 7, 8 e 9.

---

## 2. Cenário 1: Apache Airflow, preparação do instrutor

> **Atualização:** esta seção foi adaptada depois que o Airflow já ficou de pé, via
> Docker dentro do WSL, em `http://localhost:8080`. O que falta não é mais instalar,
> é colocar a DAG de demonstração e os dados dentro do ambiente que já está rodando.
> A seção 2.6 mantém o passo a passo original de instalação, só para o caso de
> precisar refazer isso numa outra máquina.

### 2.1 O que já está pronto

Airflow rodando via Docker Compose dentro do WSL cobre exatamente a via recomendada
neste guia (a instalação por `pip` direto era o plano B, não o principal). Com o
WSL, os comandos de terminal são em bash, não PowerShell, o que muda a sintaxe dos
passos abaixo em relação a uma instalação feita direto no Windows, mas não muda nada
da estrutura do Airflow em si: mesmos containers, mesmas pastas `dags/`, `logs/`,
`plugins/`, mesma porta 8080.

### 2.2 Achar a pasta do projeto

Tudo daqui para frente roda **dentro do terminal WSL**, não no PowerShell. Se a
janela do WSL usada para instalar já não estiver aberta, abra uma nova (`wsl` no
menu Iniciar, ou o app da distribuição instalada).

Primeiro, ache onde está o `docker-compose.yaml` do projeto:

```bash
docker compose ls
```

A coluna `CONFIG FILES` mostra o caminho completo. Entre nessa pasta:

```bash
cd "$(dirname "<caminho copiado da coluna CONFIG FILES>")"
ls dags logs plugins
```

Se as três pastas aparecerem, é o lugar certo.

### 2.3 Colocar a DAG e os dados no lugar, sem reiniciar nada

O Airflow já observa a pasta `dags/` continuamente, então dá para adicionar a DAG e
os dados sem derrubar os containers. Para não precisar editar o `docker-compose.yaml`
e recriar os containers só por causa de uma pasta de dados nova, o dado de
demonstração entra **dentro de `dags/`**, numa subpasta, já que essa é a única pasta
com garantia de estar montada em qualquer instalação padrão:

```bash
mkdir -p dags/data
cp "/mnt/c/Users/edmar/MeusProjetos/ai-talent-academy/docs/aula-10/dag_fraude_aula10.py" dags/
cp "/mnt/c/Users/edmar/MeusProjetos/ai-talent-academy/docs/aula-06/dados/csv/transacoes.csv" dags/data/
```

(Ajuste os dois caminhos de origem se o repositório estiver em outro lugar. No WSL,
o disco `C:` do Windows fica em `/mnt/c/`.)

O arquivo `dag_fraude_aula10.py` já está preparado para ler de
`/opt/airflow/dags/data/transacoes.csv`, que é exatamente onde o `cp` acima deixou o
CSV, visto de dentro do container.

Force o Airflow a reconhecer a DAG nova imediatamente, em vez de esperar o próximo
ciclo automático de varredura:

```bash
docker compose restart airflow-scheduler
```

Confirme que ela foi importada sem erro:

```bash
docker compose exec airflow-scheduler airflow dags list | grep aula10
docker compose exec airflow-scheduler airflow dags list-import-errors
```

Se a primeira linha mostrar `aula10_pipeline_fraude` e a segunda vier vazia, está
pronta para aparecer na interface web.

### 2.4 A DAG de demonstração

O arquivo [`dag_fraude_aula10.py`](dag_fraude_aula10.py) já está pronto neste pacote
e reaproveita a mesma lógica de extração, limpeza e agregação já testada contra a
base real de transações. Ela tem três tarefas encadeadas, no formato TaskFlow do
Airflow 3 (a forma atual recomendada, mais legível que a sintaxe antiga de
`PythonOperator` explícito):

- **`extract`**: lê o CSV de transações e grava em Parquet.
- **`transform`**: remove nulos nos campos obrigatórios, remove duplicidade de
  `id_transacao` e descarta valores não positivos. Imprime quantas linhas entraram e
  quantas sobraram, para o log ficar visível na demonstração.
- **`load`**: agrupa por lojista, soma o valor transacionado, ordena do maior para o
  menor e grava o resultado final em CSV.

Essas três fases são deliberadamente as mesmas ensinadas na Aula 9 (extract,
transform, load), agora executando de fato, orquestradas pelo Airflow, sobre dados
que a turma já reconhece.

### 2.5 Roteiro do que mostrar em aula

1. Abrir `http://localhost:8080` já logado, com a lista de DAGs na tela, antes de a
   aula começar. Evita perder tempo de aula com login.
2. Localizar `aula10_pipeline_fraude` na lista e apontar: "isso aqui é uma DAG, o
   grafo de dependência que vimos na semana passada. Cada quadrado é uma tarefa."
3. Clicar na DAG para abrir a visão de grafo, mostrando `extract → transform → load`
   visualmente.
4. Disparar a execução manual (botão de play, "Trigger DAG").
5. Acompanhar as três tarefas mudando de cor conforme rodam (fila, execução,
   sucesso), narrando o que está acontecendo por trás.
6. Abrir os logs da tarefa `transform` e mostrar a linha impressa com a contagem de
   linhas antes e depois da limpeza, conectando com o bloco de qualidade de dados da
   Aula 9.
7. Encerrar mostrando o CSV de saída gerado em `dags/data/resumo_por_lojista.csv`,
   acessível também de dentro do WSL com `cat dags/data/resumo_por_lojista.csv`.

### 2.6 Se precisar reinstalar do zero, numa outra máquina

O caminho abaixo é o que teria sido seguido para instalar do início (mesma lógica do
que já foi feito no WSL), documentado aqui só como referência para o caso de precisar
repetir isso numa outra máquina. Como o ambiente atual já está de pé, **não rode isto
por cima do que já existe**.

```bash
mkdir -p ~/airflow-aula10 && cd ~/airflow-aula10
curl -LfO "https://airflow.apache.org/docs/apache-airflow/3.3.1/docker-compose.yaml"
mkdir -p dags logs plugins config
echo "AIRFLOW_UID=$(id -u)" > .env
docker compose up airflow-init
docker compose up -d
```

Depois de `airflow-init` terminar com `exited with code 0`, `docker compose up -d`
sobe os serviços em segundo plano, sem travar o terminal. A interface fica em
`http://localhost:8080` mesmo rodando dentro do WSL, porque o Windows encaminha
portas do WSL automaticamente para `localhost`. Login padrão: usuário `airflow`,
senha `airflow`.

Se o Docker não estiver disponível na máquina nova, existe também um caminho mais
leve via `pip`, mais sensível a versão, útil só como plano B:

```bash
python3 -m venv venv-airflow
source venv-airflow/bin/activate
pip install "apache-airflow==3.3.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.3.1/constraints-3.12.txt"
airflow standalone
```

### 2.7 Plano B, se algo falhar no dia

Ambiente local com Docker dentro do WSL ainda é a parte do guia com mais superfície
de risco (o WSL precisa estar rodando, a distribuição não pode ter sido desligada, a
porta 8080 não pode estar ocupada por outro programa). Antes da aula:

- Grave um vídeo curto (2 a 3 minutos) da demonstração completa funcionando, como
  visto na seção 2.5, e deixe pronto para tocar caso o ambiente falhe ao vivo.
- Confirme, na tarde do dia da aula, que os containers ainda estão de pé
  (`docker compose ps`, a partir da pasta do projeto) e que a porta 8080 responde. Se
  o computador reiniciou entre a preparação e a aula, o WSL e os containers não
  voltam sozinhos: é preciso abrir o terminal WSL e rodar `docker compose up -d` de
  novo.
- Confirme que a DAG ainda aparece com `docker compose exec airflow-scheduler airflow
  dags list | grep aula10`, pelo mesmo motivo.

---

## 3. Cenário 2: PySpark no Google Colab, preparação para a turma

### 3.1 A célula de setup

Esta célula entra no topo do notebook de cada aluno, com uma frase de contexto antes
dela explicando por que existe (ver seção 3.3). Leva de 1 a 2 minutos para rodar:

```python
# Celula 1: instala o Java (o motor do Spark precisa dele) e o PySpark.
# Roda uma vez por sessao do Colab. Leva de 1 a 2 minutos.
!apt-get install -y openjdk-17-jdk-headless -qq > /dev/null
!pip install pyspark -q

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-17-openjdk-amd64"

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("aula10").getOrCreate()
spark
```

A última linha, sozinha, exibe um resumo visual da sessão criada (versão do Spark,
link da interface de monitoramento). É a confirmação de que deu certo, sem precisar
de nenhum `print`.

Segunda célula, para conectar ao Drive onde os dados moram, no mesmo padrão já usado
desde a Aula 4:

```python
from google.colab import drive
drive.mount('/content/drive')

PASTA_DADOS = "/content/drive/MyDrive/AI Talent Academy/Aula 08/dados/csv"
```

### 3.2 Teste antes da aula

Rode as duas células acima num Colab novo, do zero, no dia anterior à aula (o Colab
às vezes atualiza a imagem base, e uma versão de Java ou pip pode mudar de
comportamento sem aviso). Cronometre o tempo de setup, porque isso entra direto no
cronômetro da aula: se levar mais de 2 minutos na sua conexão, ajuste a expectativa
que você passa aos alunos.

Teste também com a conta de e-mail que os alunos vão usar (Gmail pessoal, não conta
corporativa), porque restrição de permissão de Drive corporativo já causou atrito em
aulas anteriores do programa.

### 3.3 Como explicar aos alunos

Frase sugerida para abrir o bloco, sem soar como aviso técnico assustador: "O Colab
não vem com Spark de fábrica, então as duas primeiras células instalam o que falta.
Vocês vão rodar isso uma vez, esperar a mensagem verde de confirmação, e a partir daí
o resto do notebook funciona igual a qualquer outro que vocês já usaram." Isso
mantém a fricção real (duas células, cerca de 2 minutos) transparente, sem prometer
algo que o ambiente não entrega de verdade.

---

## 4. A atividade dos alunos: pipeline de extração, transformação e unificação

### 4.1 Dataset e objetivo

Reaproveita a base de fraude em cartão da Aula 8, já com 1 milhão de transações,
carregada em `PASTA_DADOS` (seção 3.1). O volume é grande o bastante para o
paralelismo do Spark fazer diferença perceptível, e a base já é familiar à turma.

Objetivo pedagógico: sair de seis tabelas separadas para **uma tabela única e limpa**,
aplicando extract, transform e load na prática, com PySpark, sozinhos.

### 4.2 Especificação da atividade, para o aluno

1. **Extract**: ler as seis tabelas (`categorias`, `clientes`, `lojistas`, `cartoes`,
   `transacoes`, `contestacoes`) com `spark.read.csv(..., header=True,
   inferSchema=True)`.
2. **Transform**: aplicar em `transacoes` os três critérios de qualidade já vistos na
   Aula 9: remover linhas com valores nulos nos campos obrigatórios, remover
   `id_transacao` duplicado, e descartar valores não positivos.
3. **Unify**: unir as seis tabelas numa só, ligando pelas chaves (`id_cartao`,
   `id_cliente`, `id_lojista`, `id_categoria`), de forma que o resultado final tenha,
   para cada transação, o nome do cliente, o nome e a categoria do lojista, e a
   bandeira do cartão.
4. **Entrega**: gravar o resultado em `/content/base_unificada`, em formato Parquet, e
   responder duas perguntas de conferência (quantas linhas sobraram depois da
   limpeza, e qual lojista teve o maior valor total transacionado).

### 4.3 A pegadinha didática real

Ao tentar o passo 3, o aluno vai bater numa mensagem de erro genuína, não simulada:
`clientes`, `lojistas` e `categorias` têm todas uma coluna chamada `nome`, com
significados diferentes em cada uma. `clientes` e `lojistas` também compartilham
`cidade`, `estado` e `data_cadastro`. Depois do `join`, o Spark reclama de referência
ambígua se alguém tentar usar `nome` sem dizer de qual tabela.

Isso funciona como gancho de ensino: a mensagem conecta direto com o critério de
**consistência** já apresentado no bloco de qualidade de dados da Aula 9
("o mesmo campo, `nome`, significando coisas diferentes em tabelas diferentes"). A
saída correta é renomear antes de unir, com `.alias()`, e vale a pena deixar o aluno
esbarrar nisso antes de mostrar a solução.

### 4.4 Gabarito de referência, só para o instrutor

```python
from pyspark.sql import functions as F

# Extract
categorias   = spark.read.csv(f"{PASTA_DADOS}/categorias.csv",   header=True, inferSchema=True)
clientes     = spark.read.csv(f"{PASTA_DADOS}/clientes.csv",     header=True, inferSchema=True)
lojistas     = spark.read.csv(f"{PASTA_DADOS}/lojistas.csv",     header=True, inferSchema=True)
cartoes      = spark.read.csv(f"{PASTA_DADOS}/cartoes.csv",      header=True, inferSchema=True)
transacoes   = spark.read.csv(f"{PASTA_DADOS}/transacoes.csv",   header=True, inferSchema=True)
contestacoes = spark.read.csv(f"{PASTA_DADOS}/contestacoes.csv", header=True, inferSchema=True)

# Transform: os mesmos tres criterios de qualidade da Aula 9
transacoes_limpo = (
    transacoes
    .dropna(subset=["id_transacao", "id_cartao", "id_lojista", "valor"])
    .dropDuplicates(["id_transacao"])
    .filter(F.col("valor") > 0)
)

# nome, cidade, estado e data_cadastro existem em mais de uma tabela.
# Renomear antes de unir evita a referencia ambigua depois do join.
clientes_r = clientes.select(
    "id_cliente",
    F.col("nome").alias("nome_cliente"),
)

lojistas_r = lojistas.select(
    "id_lojista",
    "id_categoria",
    F.col("nome").alias("nome_lojista"),
)

categorias_r = categorias.select(
    "id_categoria",
    F.col("nome").alias("nome_categoria"),
)

# Unify
base_unificada = (
    transacoes_limpo
    .join(cartoes.select("id_cartao", "id_cliente", "bandeira"), on="id_cartao", how="inner")
    .join(clientes_r, on="id_cliente", how="inner")
    .join(lojistas_r, on="id_lojista", how="inner")
    .join(categorias_r, on="id_categoria", how="left")
)

base_unificada.write.mode("overwrite").parquet("/content/base_unificada")

# Perguntas de conferencia
print("Linhas depois da limpeza:", base_unificada.count())
(
    base_unificada.groupBy("nome_lojista")
    .sum("valor")
    .orderBy(F.desc("sum(valor)"))
    .show(5)
)
```

Em uma sessão padrão do Colab, esse pipeline completo (leitura, limpeza, quatro
junções e gravação, sobre 1 milhão de linhas) deve rodar em menos de um minuto. Se
algum aluno relatar tempo muito maior, o mais provável é um `join` faltando a
renomeação (gerando produto cartesiano acidental) ou uma tabela lida do caminho
errado, não um limite real do Colab.

---

## 5. Checklist consolidado antes da aula

**Uma semana antes:**
- [x] Airflow instalado e rodando via Docker dentro do WSL, em `localhost:8080`
- [ ] Seguir a seção 2.2 e 2.3 para localizar a pasta do projeto e colocar
      `dag_fraude_aula10.py` e `transacoes.csv` dentro de `dags/`, sem reiniciar os
      containers
- [ ] Confirmar com `airflow dags list-import-errors` (seção 2.3) que a DAG importou
      sem erro, e disparar uma execução de teste seguindo o roteiro da seção 2.5
- [ ] Testar as células de setup do PySpark (seção 3.1) num Colab novo, com a conta
      pessoal de Gmail

**Na véspera:**
- [ ] Confirmar que `docs/aula-08/dados/csv/` está numa pasta do Drive acessível para
      toda a turma (mesma checagem já feita para a Aula 8)
- [ ] Gravar o vídeo de backup da demonstração do Airflow (seção 2.7)
- [ ] Rodar o gabarito da seção 4.4 do início ao fim, cronometrando

**No dia da aula:**
- [ ] Abrir o terminal WSL e confirmar os containers de pé com `docker compose ps`
      (a partir da pasta do projeto); se o computador reiniciou desde a véspera, subir
      de novo com `docker compose up -d`
- [ ] Deixar `http://localhost:8080` já logado numa aba, antes de a aula começar
- [ ] Fixar, no Discord, o link do notebook base com as duas células de setup do
      PySpark já coladas, para o aluno só copiar

---

## 6. Pendências e decisões abertas

- [ ] Decidir se a atividade da seção 4 vira avaliação com Google Forms (padrão da
      Aula 8) ou entrega livre em notebook, sem nota
- [ ] Depois de validado este guia, produzir os slides da Aula 10 com
      `scripts/gerar_slides_aula10.py`, cobrindo a teoria mínima antes da prática
      (o que é um DAG executando de verdade, o que é uma partição no Spark), sem
      repetir o que a Aula 9 já ensinou em teoria
- [x] Notebooks da atividade criados: `pyspark_aluno.ipynb` (com `# TODO`) e
      `pyspark_professor.ipynb` (gabarito). Falta só rodar os dois de ponta a
      ponta num Colab real antes da aula, como já pede a seção 3.2
- [ ] Confirmar a duração real da aula (padrão das quintas é 2h) contra o tempo de
      demonstração do Airflow (seção 2.5) mais o tempo de prática do PySpark (seção
      4), e ajustar o corte se necessário
