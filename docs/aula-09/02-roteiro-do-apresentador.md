# Roteiro do apresentador: Aula 9 (Semana 5, segunda-feira)

> Gerado automaticamente a partir das notas do deck.
> Não edite este arquivo à mão: edite `scripts/gerar_slides_aula09.py` e rode
> `python scripts/gerar_slides_aula09.py && python scripts/exportar_roteiro_aula09.py`.

**Como usar:** imprima ou deixe aberto num segundo monitor. O texto entre aspas é
fala sugerida. Adapte para a sua voz, não decore: o que importa é a sequência de ideias.

---

## Slide 1 · PROGRAMA DE TRAINEES EM DADOS E INTELIGÊNCIA ARTIFICIAL

```
⏱ 19h00 às 19h10 (slide de espera)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Slide projetado desde 18h55. Fale a cada 2 ou 3 minutos enquanto a sala enche.

"Boa noite! Semana 5, e hoje é o assunto que fecha uma pergunta que ficou em aberto
desde a Aula 1: de onde vêm os dados, e quem prepara eles antes de chegar em SQL ou em
pandas. Enquanto todo mundo entra, escreve no chat: antes de hoje, você sabia dizer o
que é engenharia de dados?"

Não comece antes de 19h08.

──────────────────────────────────────────────────────────────
LEMBRETES
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- Moderador com o link do Discord pronto para colar.
- Sem código ao vivo hoje. Os exemplos aparecem no slide, a prática é na quinta.
```

## Slide 2 · ENQUANTO TODO MUNDO ENTRA

```
⏱ 19h00 às 19h10  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Leia os itens uma vez, por volta de 19h05. As respostas do chat servem de termômetro
para calibrar o ritmo do bloco A.
```

## Slide 3 · A pergunta que ficou em aberto

```
⏱ 19h10 às 19h35 (25 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco de contexto. Objetivo: reabrir o pipeline de 8 fases da Aula 1 e mostrar que
hoje fecha duas fases que ficaram soltas até aqui.

ESTRUTURA:
  Onde estamos                4 min
  O pipeline revisitado         7 min
  Por que hoje importa            6 min
  O plano de hoje                   6 min
```

## Slide 4 · ONDE ESTAMOS

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Onde vocês estão. Semana 3 foi consultar dado que já estava pronto, num banco. Semana
4 foi manipular esse mesmo dado pronto, em pandas. Hoje a pergunta muda: como esse dado
chegou pronto, para começo de conversa?"
```

## Slide 5 · O PIPELINE REVISITADO

```
⏱ 7 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Lembram deste desenho, lá da Aula 1? As oito fases de qualquer solução de dados e IA.

Vocês já viveram a fase 1, entender o problema, na semana 1. E já viveram bastante a
fase 3, explorar, com SQL na semana 3 e Python na semana 4.

Mas reparem: as fases 2 e 4, conseguir os dados e preparar, ficaram soltas. Ninguém
explicou ainda de onde vem o CSV que vocês sempre receberam pronto, nem quem garantiu
que aquele dado estava limpo antes de chegar em vocês.

É exatamente isso que a aula de hoje fecha. Engenharia de dados, resumida de um jeito
simples, é o nome para as fases 2 e 4 desse desenho."
```

## Slide 6 · POR QUE HOJE IMPORTA

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Por que dedicar uma noite inteira a isso. Quatro razões.

Todo exemplo que vocês usaram até aqui, o CSV da Aula 6, a base da Aula 8, já chegou
pronto. Alguém decidiu de onde vinha, e alguém limpou antes de vocês verem.

Sem esse trabalho, SQL e pandas não têm em cima do que rodar. Nenhuma ferramenta
ajuda com dado que não existe, ou que está errado.

É também o trabalho que mais consome tempo num projeto real. Quem já ouviu que
oitenta por cento do trabalho de um projeto de dados é limpeza, essa conta vem daqui.

E é o trabalho mais invisível quando dá certo. Ninguém elogia um pipeline que nunca
quebrou, só repara quando quebra."
```

## Slide 7 · O PLANO DE HOJE

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Sete blocos hoje, mais do que o normal, de propósito: engenharia de dados tem muita
coisa boa para conhecer, e preferimos trazer tudo e ajustar depois do que deixar
faltar.

De onde vêm os dados. Onde eles moram. ETL contra ELT, com uma briga histórica de
verdade no meio. Qualidade de dados. Pipeline de produção, com Airflow e dbt.
Processamento distribuído, com Spark e Databricks. E fechamos amarrando tudo no caso
de fraude em cartão que vocês já conhecem."
```

## Slide 8 · De onde vêm os dados

```
⏱ 19h35 às 20h00 (25 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco de vocabulário e panorama. Objetivo: nomear as fontes de dados mais comuns, e
entender a diferença entre lote e fluxo com exemplo concreto de cada.

ESTRUTURA:
  Fontes comuns de dados     6 min
  Lote x fluxo                 6 min
  Exemplos do dia a dia          6 min
  Interação                       5 min
```

## Slide 9 · FONTES COMUNS DE DADOS

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Quatro fontes que aparecem o tempo todo. Banco transacional, o sistema que atende o
cliente na hora, o mesmo tipo de banco que vocês já consultaram com SQL.

API, outro sistema entregando dado sob pedido, o mesmo conceito de endpoint da Aula 4.

Arquivo, planilha ou CSV, o jeito mais simples de existir.

E evento, um registro de algo que aconteceu agora, chegando um de cada vez.

Quase todo pipeline real combina mais de uma dessas quatro ao mesmo tempo."
```

## Slide 10 · DUAS FORMAS DE PROCESSAR

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Duas formas de processar o mesmo dado. Lote processa um bloco de uma vez, de hora em
hora ou uma vez por dia. Mais simples de construir, aceita atraso de minutos ou horas
sem problema nenhum.

Fluxo processa cada evento assim que ele chega, rodando o tempo todo, sem pausa. Mais
complexo, mais caro de manter, e só compensa quando o atraso realmente importa.

E aqui vai uma verdade que surpreende: a maioria dos pipelines do mundo real é em
lote. Fluxo chama mais atenção, mas continua sendo a exceção."
```

## Slide 11 · EXEMPLOS DO DIA A DIA

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Quatro situações reais. Extrato bancário fechado à noite: lote, ninguém precisa ver o
saldo mudar no segundo exato.

Alerta de fraude no cartão, na hora da compra: fluxo, porque atraso de minutos já é
tarde demais, o dinheiro já saiu.

Relatório de vendas do mês: lote, roda uma vez, no início do mês seguinte.

Painel de estoque de um marketplace: fluxo, o estoque muda a cada venda em qualquer
lugar do site, o tempo todo.

A pergunta certa é sempre a mesma: o que a decisão de negócio realmente exige."
```

## Slide 12 · INTERAÇÃO

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Testando o que a gente acabou de ver. Um hospital quer saber, em tempo real, quando
um paciente internado tem um sinal vital fora da faixa segura. Qual dos dois serve
aqui?"

[aguarde 30 segundos]

Resposta: B. Aqui o atraso custa vida, é exatamente o caso em que fluxo compensa o
custo extra de manter. C está errado: o resultado final muda bastante, um paciente em
risco às vezes só apareceria no relatório do dia seguinte.
```

## Slide 13 · Onde os dados moram

```
⏱ 20h00 às 20h30 (30 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco de armazenamento. Objetivo: explicar por que uma empresa madura usa mais de um
tipo de banco ao mesmo tempo, cada um para um trabalho diferente.

ESTRUTURA:
  Banco transacional (OLTP)   5 min
  Data Warehouse (OLAP)         6 min
  Data Lake                       6 min
  Os três lado a lado               6 min
  Bônus: Data Lakehouse               4 min
  Transição                             3 min
```

## Slide 14 · BANCO TRANSACIONAL (OLTP)

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Primeiro tipo, o que vocês já conhecem. OLTP, Online Transaction Processing: o banco
que atende uma operação de cada vez, rápido. Toda consulta que vocês fizeram nas Aulas
5 e 6 rodou num banco deste tipo.

Ele é bom para escrever e ler pouco dado por vez, e ruim para somar milhões de linhas
de uma vez só. Isso vem de uma escolha de projeto: ele foi desenhado para o sistema
não travar enquanto vende. Análise fica para outra ferramenta, mais à frente."
```

## Slide 15 · DATA WAREHOUSE (OLAP)

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Segundo tipo. OLAP, Online Analytical Processing: banco desenhado para somar, agrupar
e cruzar muito dado de uma vez, exatamente o oposto do OLTP.

Os dados chegam de vários bancos transacionais diferentes, e um warehouse junta a
empresa inteira num lugar só, pronto para pergunta grande.

Ele fica lento para escrever um registro de cada vez, e é por isso que nenhum sistema
usa ele como banco principal. Os nomes que mais aparecem no mercado hoje são BigQuery,
Snowflake e Redshift."
```

## Slide 16 · DATA LAKE

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Terceiro tipo, o mais diferente dos dois primeiros. Data Lake guarda o dado bruto, do
jeito que ele chegou: estruturado, semiestruturado, ou nem isso, tipo imagem ou log de
sistema.

A frase que resume ele: schema on read, não schema on write. Você decide a estrutura
na hora de LER, não na hora de guardar. Isso dá flexibilidade, e o armazenamento fica
bem mais barato que um banco tradicional.

O risco mora no mesmo lugar da vantagem: sem organização, um data lake vira o que o
mercado chama de pântano de dados, um monte de arquivo que ninguém mais acha."
```

## Slide 17 · OS TRÊS LADO A LADO

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Os três lado a lado. Reparem que não existe um vencedor: cada linha desta tabela é
uma escolha de projeto diferente, não um ranking.

Uma empresa madura normalmente usa os três ao mesmo tempo. O banco transacional vende.
O data lake guarda tudo, bruto, barato. E o warehouse organiza o que interessa para
quem analisa. Cada um faz o trabalho que o outro faz mal."
```

## Slide 18 · BÔNUS: DATA LAKEHOUSE

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Um bônus rápido antes de seguir. Data Lakehouse é a ideia de juntar os dois últimos:
armazenamento barato de um lake, com a organização e a velocidade de consulta de um
warehouse.

Foi popularizado pela Databricks, por volta de 2020, como resposta direta ao problema
do pântano de dados que acabamos de falar. Guardem esse nome: a história completa por
trás da Databricks, e do motor que ela comercializa, tem um bloco inteiro reservado
mais à frente hoje."
```

## Slide 19 · ETL x ELT

```
⏱ 20h30 às 21h00 (30 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco de transformação. Objetivo: entender a diferença entre ETL e ELT, e por que a
escolha entre os dois já foi motivo de disputa séria no mercado de dados.

ESTRUTURA:
  O que é ETL              6 min
  O que é ELT                 6 min
  A rivalidade Inmon x Kimball  8 min
  ETL x ELT lado a lado           6 min
  Interação                         4 min
```

## Slide 20 · O QUE É ETL

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"ETL: Extract, Transform, Load. A ordem das três letras é literal. Extrai o dado da
fonte, transforma FORA do destino, e só carrega o que já está pronto.

Isso nasceu numa época em que processar e guardar dado era caro de verdade, então a
transformação acontecia antes, para não gastar espaço caro com dado bruto e
desorganizado.

A transformação roda numa ferramenta separada, fora do banco de destino. E ainda é o
padrão em muita empresa grande e mais antiga, principalmente onde o warehouse roda
fora da nuvem."
```

## Slide 21 · O QUE É ELT

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"ELT: Extract, Load, Transform. As mesmas três letras do ETL, ordem diferente. Extrai,
carrega o dado bruto direto no destino, e transforma DEPOIS, já lá dentro.

Isso só ficou viável com data warehouse em nuvem. Guardar e processar dado bruto ficou
barato o suficiente para não precisar economizar espaço antes de carregar.

A transformação roda em SQL, dentro do próprio warehouse, usando o poder de
processamento que a empresa já está pagando de qualquer jeito. E é exatamente o modelo
por trás do dbt, que a gente reencontra no bloco de pipeline."
```

## Slide 22 · A RIVALIDADE INMON X KIMBALL

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Uma história real, e ainda hoje citada em entrevista de emprego da área.

1992, Bill Inmon publica um livro chamado Building the Data Warehouse, defendendo um
warehouse único e central para a empresa inteira, construído de cima para baixo,
começando pelo modelo geral.

1996, Ralph Kimball publica The Data Warehouse Toolkit, defendendo o oposto: construir
por área de negócio, de baixo para cima, com um jeito de organizar tabela chamado
modelagem dimensional.

Nos anos 2000, as duas escolas dividem o mercado inteiro, e cada consultoria de dados
escolhe um lado, quase como time de futebol.

Nos anos 2010, a nuvem barateia processamento, e o ELT tira parte da urgência dessa
discussão: fica mais barato experimentar dos dois jeitos.

E hoje, as duas ideias convivem, muitas vezes dentro da mesma empresa. Ninguém venceu
de verdade, as duas viraram ferramenta do dia a dia."

──────────────────────────────────────────────────────────────
LEMBRETES
Se aparecer pergunta de entrevista sobre 'star schema' ou 'modelagem dimensional', a origem é o livro do Kimball de 1996.
```

## Slide 23 · ETL X ELT LADO A LADO

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Lado a lado, para fixar. ETL transforma antes de carregar, mais comum fora da nuvem,
com ferramenta separada, bom quando processar é caro.

ELT transforma depois, dentro do próprio banco, mais comum na nuvem, usando o SQL que
já está ali, bom quando armazenar e processar é barato.

Na dúvida, hoje a resposta mais comum do mercado é ELT. Mas ETL não desapareceu, ainda
é a escolha certa em muito contexto."
```

## Slide 24 · INTERAÇÃO

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Testando o bloco. Uma empresa pequena usa warehouse na nuvem, paga só pelo que
processa, e quer testar formatos diferentes de transformação sem compromisso. Qual
caminho combina mais?"

[aguarde 30 segundos]

Resposta: B. Carregar bruto primeiro dá liberdade para testar transformação diferente
sem repetir a extração, e o custo de guardar e processar na nuvem já é baixo. C está
errado, o custo muda bastante dependendo de quando o processamento pesado acontece.
```

## Slide 25 · Qualidade de dados

```
⏱ 21h15 às 21h40 (25 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Primeiro bloco depois do intervalo. Objetivo: dar nome técnico a um problema que a
turma já sentiu na prática, sem saber que tinha nome.

ESTRUTURA:
  Por que é o problema número um   5 min
  Quatro dimensões de qualidade      6 min
  A ponte com o que já viram           6 min
  Testes de dados                        6 min
  Transição                                2 min
```

## Slide 26 · POR QUE DADO SUJO É O PROBLEMA NÚMERO UM

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Depois do intervalo, o problema que mais gasta tempo de quem trabalha com dado de
verdade.

Todo o resto do pipeline depende da qualidade do que entra primeiro. Modelo bom com
dado ruim continua dando resposta ruim, sem exceção.

E o custo de um erro cresce quanto mais tarde ele é descoberto. Achar um erro na
fonte custa uma correção pequena. Achar o mesmo erro dentro do relatório que já foi
para o diretor custa reputação.

A meta nunca é zero erro, isso não existe. A meta é um pipeline que detecta o erro
antes que ele vire decisão errada de alguém."
```

## Slide 27 · QUATRO DIMENSÕES DE QUALIDADE

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Quatro perguntas que resumem qualidade de dado, e valem para qualquer pipeline do
mundo.

Completude: falta algum dado que deveria estar ali? Consistência: o mesmo dado aparece
igual em lugares diferentes, ou um sistema chama de uma forma e outro de outra?

Duplicidade: a mesma linha está contada mais de uma vez, inflando uma soma?

E validade de schema: o tipo e o formato de cada coluna são realmente o que deveriam
ser?"
```

## Slide 28 · A PONTE COM O QUE VOCÊS JÁ VIRAM

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"E aqui a notícia boa: vocês já praticavam qualidade de dado, só sem esse nome.

NULL, na Aula 5, já era SQL tratando valor ausente como um problema de completude.
NaN, na Aula 7, era pandas fazendo exatamente a mesma pergunta, com outro símbolo.

E dtype errado, também na Aula 7, é na prática um problema de validade de schema:
número que virou texto porque uma célula do arquivo original veio fora do padrão.

Faltava só um nome para organizar ideias que vocês já tinham na mão."
```

## Slide 29 · TESTES DE DADOS

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"E se qualidade é importante, tem que ter jeito de checar automaticamente, não só
olhando na mão. É para isso que existem os testes de dados: a mesma lógica de teste de
software, aplicada ao dado.

Exemplos comuns: essa coluna nunca pode estar vazia, esse valor sempre tem que ser
positivo, essa chave nunca pode se repetir.

As ferramentas mais citadas hoje são dbt tests e Great Expectations, e o dbt volta no
próximo bloco.

O objetivo nunca muda: quebrar o pipeline antes do dado ruim chegar em alguém que vai
tomar uma decisão real com ele."
```

## Slide 30 · Pipeline de verdade

```
⏱ 21h40 às 22h10 (30 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco de orquestração. Objetivo: mostrar o que separa um script solto de um pipeline
de produção, e nomear as duas ferramentas mais citadas do mercado hoje.

ESTRUTURA:
  Script x pipeline de produção   6 min
  DAG                                6 min
  Airflow                              6 min
  dbt e a engenharia analítica           6 min
  Interação                                4 min
```

## Slide 31 · O QUE SEPARA SCRIPT DE PIPELINE DE PRODUÇÃO

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Vocês já escreveram script antes, mesmo sem saber. A pergunta de hoje é: o que
transforma um script solto num pipeline de produção de verdade?

Um script roda quando alguém lembra de rodar ele. Um pipeline roda sozinho, no horário
certo, todo dia, sem ninguém precisar lembrar.

Um script quebra em silêncio, ninguém fica sabendo até reclamarem. Um pipeline de
produção avisa alguém quando quebra.

E um script não sabe o que já rodou antes dele. Um pipeline sabe a ordem certa, e o
que depende do quê.

A diferença mora no que cerca o código, no agendamento, no aviso de erro, na ordem
de dependência entre as tarefas."
```

## Slide 32 · DAG: O MAPA DE DEPENDÊNCIAS

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"DAG: grafo acíclico dirigido. Parece complicado, a ideia é simples: um jeito de
desenhar quais tarefas dependem de quais, sem formar um ciclo.

'Sem ciclo' quer dizer isto: a tarefa B nunca pode depender da tarefa A, se A já
depende de B. Senão nenhuma das duas nunca começaria.

Cada seta do desenho é uma regra: isso só roda depois daquilo terminar. E é assim que
a ferramenta de orquestração sabe a ordem certa, sem alguém decidir manualmente todo
santo dia."
```

## Slide 33 · AIRFLOW

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"A ferramenta de orquestração mais citada do mercado. Maxime Beauchemin criou o
Airflow em 2014, trabalhando no time de dados do Airbnb, numa época em que a empresa
crescia rápido demais para script solto continuar dando conta.

Cada pipeline vira um DAG, escrito em Python, o mesmo Python que vocês já usam desde a
Aula 7.

Hoje é um projeto da Apache Software Foundation, um dos orquestradores mais usados do
mundo. E não é a única opção: Dagster e Prefect são alternativas mais recentes, com a
mesma ideia central por trás."
```

## Slide 34 · DBT E A ENGENHARIA ANALÍTICA

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"E fechando com a ferramenta que já apareceu duas vezes hoje, sem apresentação
completa. dbt nasceu por volta de 2016, criado pela equipe que depois virou a dbt
Labs.

A ideia central: tratar SQL como se fosse software de verdade, com versionamento,
teste automático e documentação, não mais um arquivo solto que só uma pessoa entende.

Isso deu nome a uma função nova no mercado, engenheiro analítico, alguém entre quem só
escreve SQL solto e quem constrói pipeline inteiro do zero.

E ele roda direto dentro do warehouse, usando SQL puro. É o exemplo mais claro de ELT
na prática, do bloco de agora há pouco."
```

## Slide 35 · INTERAÇÃO

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Última pergunta antes do fechamento. Um time roda um script Python toda sexta-feira,
na mão, para atualizar um relatório. Ninguém sabe quando o script quebra, e às vezes
esquecem de rodar. O que falta para virar pipeline de verdade?"

[aguarde 30 segundos]

Resposta: B. A linguagem nunca foi o problema, do slide de script contra pipeline.
Falta rodar sozinho no horário certo, e avisar alguém quando quebra. C está errado,
isso ainda é exatamente o script solto que descrevemos.
```

## Slide 36 · Processamento distribuído

```
⏱ 22h10 às 22h50 (40 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco de aprofundamento, por pedido explícito do usuário depois da primeira versão da
aula: o conceito de processamento distribuído, e a história de Spark e Databricks.

ESTRUTURA:
  Por que processamento distribuído existe   6 min
  MapReduce, a ideia que começou tudo          6 min
  Spark, a mesma ideia na memória                6 min
  Um exemplo: pandas e Spark lado a lado           6 min
  Databricks                                         6 min
  Onde cada peça se encaixa                            5 min
  Interação                                              4 min
```

## Slide 37 · PROCESSAMENTO DISTRIBUÍDO

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Último conceito grande da noite, e um dos mais citados em vaga de dados. Toda conta
que vocês viram até aqui hoje, e em toda a aula de pandas, rodou numa máquina só: um
notebook, um banco, um warehouse, processando numa CPU de cada vez.

Em algum volume, uma máquina só não dá mais conta. Não importa quão potente ela seja,
existe um teto de memória e de processamento.

A solução é dividir o trabalho entre várias máquinas ao mesmo tempo, cada uma
processando um pedaço, com os resultados se juntando no final. Isso tem nome:
processamento distribuído."
```

## Slide 38 · MAPREDUCE, A IDEIA QUE COMEÇOU TUDO

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"A história começa com um paper. Em 2004, o Google publicou o paper do MapReduce,
descrevendo como eles processavam a escala gigantesca da própria busca.

A ideia central é separar o trabalho em duas etapas. Map processa cada pedaço dos
dados em paralelo, em máquinas diferentes. Reduce junta os resultados parciais numa
resposta só.

O Hadoop nasceu logo depois, como versão open source dessa ideia, criado por Doug
Cutting e Mike Cafarella. E o Hadoop dominou a década seguinte inteira.

Mas tinha um ponto fraco sério: a cada etapa, ele escrevia o resultado intermediário
em disco, que é bem mais lento que memória. Isso ia deixando tudo mais devagar."
```

## Slide 39 · SPARK: A MESMA IDEIA, MAS NA MEMÓRIA

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Matei Zaharia criou o Spark em 2009, durante o doutorado dele na UC Berkeley, no
laboratório AMPLab.

A virada foi processar em memória, não em disco. Isso tornou o Spark de dez a cem
vezes mais rápido que o Hadoop MapReduce, dependendo do tipo de tarefa.

E aqui vai a boa notícia para vocês: o DataFrame do Spark se parece muito com o
DataFrame do pandas que vocês já sabem usar. Mesma ideia de linhas e colunas, agora
espalhada por várias máquinas ao mesmo tempo.

Hoje o Spark é o motor de processamento distribuído mais usado do mercado.
Praticamente todo Data Lake de porte grande tem Spark rodando por trás."
```

## Slide 40 · PROCESSAMENTO DISTRIBUÍDO

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Um exemplo rápido, para fixar. Em cima, o mesmo groupby de pandas que vocês já usaram
hoje. Embaixo, a versão em PySpark, a biblioteca Python que fala com o Spark.

Reparem que a sintaxe é quase igual, de propósito: quem já sabe pandas reconhece a
maior parte do PySpark de cara.

Por trás, o Spark divide a tabela entre várias máquinas, cada uma agrupa e soma o
próprio pedaço, e os resultados se juntam no final, sem vocês precisarem escrever
nenhuma linha a mais para isso acontecer.

E a diferença entre usar um ou outro aparece só no volume. Um milhão de linhas, como o
banco de vocês da Aula 8, roda bem nos dois. Muitos bilhões de linhas só rodam de
forma distribuída."
```

## Slide 41 · DATABRICKS

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"E fechando a linha do tempo: os criadores do Spark fundaram a Databricks em 2013,
incluindo o próprio Matei Zaharia.

A empresa pegou um projeto de pesquisa de universidade e transformou em plataforma
comercial: hospedagem, interface, integração pronta, em vez de cada empresa precisar
instalar e configurar tudo na mão.

E é a mesma empresa por trás do termo Data Lakehouse, do bônus lá no bloco de
armazenamento. Agora vocês têm a história completa: Databricks nasceu do Spark, e o
Lakehouse foi a resposta dela para juntar lake e warehouse numa coisa só.

Hoje é uma das plataformas de dados mais usadas dentro de empresa grande. O que
começou como projeto de doutorado virou parte do dia a dia do mercado."
```

## Slide 42 · ONDE CADA PEÇA SE ENCAIXA

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Um resumo, juntando as cinco ferramentas que ganharam nome próprio hoje.

Hadoop processa de forma distribuída, em disco, foi o pioneiro. Spark faz a mesma
coisa em memória, e é o padrão de hoje. Databricks é a plataforma comercial construída
em cima do Spark. Airflow orquestra quando cada etapa roda. E dbt transforma dado com
SQL versionado.

Reparem que nenhuma delas faz o trabalho da outra. Cada uma resolve uma parte
diferente do mesmo pipeline, e é exatamente por isso que aparecem juntas com tanta
frequência numa vaga de emprego da área."
```

## Slide 43 · INTERAÇÃO

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Última pergunta antes do fechamento. Uma tabela de 50 mil linhas, que já processa em
segundos no pandas de um notebook comum. Faz sentido migrar para Spark?"

[aguarde 30 segundos]

Resposta: B. Distribuir tem custo de coordenação entre as máquinas, e esse custo só
compensa quando o volume realmente exige. Para 50 mil linhas, pandas sozinho já é mais
rápido, porque não perde tempo dividindo e juntando trabalho entre máquinas. C está
errado, a plataforma não é o que decide isso, o volume é.
```

## Slide 44 · Do problema ao pipeline

```
⏱ 22h50 às 23h05 (15 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco de fechamento e amarração. Objetivo: mostrar, num desenho só, tudo que a aula de
hoje cobriu, aplicado ao caso que a turma já conhece de cor.
```

## Slide 45 · DO PROBLEMA AO PIPELINE

```
⏱ 10 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Fechando com um desenho só. O mesmo caso de fraude em cartão que vocês já conhecem de
cor, agora mostrando tudo o que acontece antes de chegar em vocês.

A fonte: a maquininha e o banco emissor geram o registro bruto, no formato deles, não
no formato bonito que vocês sempre receberam.

A ingestão: um pipeline em lote traz essas transações a cada poucos minutos.

O armazenamento: o dado bruto entra num data lake primeiro, e só o que passa por
transformação vira tabela dentro do warehouse.

A qualidade: testes automáticos conferem completude, duplicidade e validade antes de
qualquer coisa seguir adiante.

A transformação: SQL dentro do warehouse organiza as seis tabelas exatas que vocês já
conhecem.

E só então chega o consumo: tudo que vocês fizeram nas Aulas 5 a 8, consultar,
filtrar, agrupar, investigar.

Guardem esta frase: as Aulas 5 a 8 inteiras aconteceram DEPOIS de tudo isso. Hoje
vocês viram o antes."
```

## Slide 46 · Encerramento

```
⏱ 23h05 às 23h20 (15 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Recapitulação            4 min
  O que vem pela frente    3 min
  Q&A                      6 min  (elástico, absorve atraso)
  Fechamento               2 min
```

## Slide 47 · ENCERRAMENTO

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Seis ideias para levar de hoje.

Engenharia de dados fecha as fases 2 e 4 do pipeline da Aula 1: conseguir os dados, e
prepará-los.

Lote é a regra, fluxo é a exceção que custa mais caro. Escolham pelo que a decisão de
negócio realmente exige.

Banco transacional, warehouse e data lake resolvem problemas diferentes, e uma empresa
madura normalmente usa os três juntos.

ETL e ELT são a mesma sigla embaralhada, por um motivo histórico real, e a nuvem mudou
qual ordem costuma valer mais a pena.

Um pipeline de produção se prova pelo que existe em volta do código, agendamento,
aviso de erro, ordem de dependência, não pelo código em si.

E a mais nova de hoje: processamento distribuído só compensa acima de um certo
volume. Spark existe para o dia em que uma máquina sozinha não aguenta mais, e é isso
que separa quem sabe o nome da ferramenta de quem sabe quando usar ela."
```

## Slide 48 · PRÓXIMOS ENCONTROS

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O que vem pela frente.

Na quinta desta semana, primeiro contato de verdade com pipeline, no mesmo formato de
sempre: demonstração curta, e o resto é prática.

E na segunda da semana 6, Machine Learning: do baseline ao primeiro modelo. Aí o foco
muda de descrever o passado para prever o futuro."
```

## Slide 49 · ANTES DE IR

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

PERGUNTAS PREVISÍVEIS DE HOJE:

- "Preciso decorar Airflow e dbt para a prova?"
  Não. O que importa é reconhecer o nome e saber para que serve. Sintaxe fica para
  quem for atuar direto nisso.

- "Isso ajuda no projeto final?"
  Ajuda direto. Todo grupo vai precisar decidir de onde vem a base, e como garantir
  que ela chega limpa, mesmo em pequena escala.

- "Toda empresa tem essa estrutura inteira, warehouse, lake, pipeline agendado?"
  Não. Empresa pequena às vezes só tem um banco e um script. A estrutura completa
  aparece conforme o volume de dado cresce.

- "Perdi a Aula 7, consigo acompanhar a prática da Aula 10?"
  Fica mais difícil. Recomendamos revisar o roteiro e o notebook da Aula 7 antes.
```

## Slide 50 · Obrigado!

```
⏱ 2 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. Foi bastante conteúdo, de propósito: engenharia de
dados é o trabalho que ninguém vê, mas que sustenta tudo que vocês já fizeram até
aqui.

Revisem os slides antes da quinta, principalmente o desenho do caso de fraude do
fechamento. Nos vemos lá. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Anotar quais dos seis blocos geraram mais pergunta no chat, para calibrar onde
  cortar se a Aula 9 precisar ficar mais curta numa próxima turma.
```
