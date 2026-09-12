# Roteiro do apresentador: Aula 10 (Semana 5, quinta-feira)

> Gerado automaticamente a partir das notas do deck.
> Não edite este arquivo à mão: edite `scripts/gerar_slides_aula10.py` e rode
> `python scripts/gerar_slides_aula10.py && python scripts/exportar_roteiro_aula10.py`.

**Como usar:** imprima ou deixe aberto num segundo monitor. O texto entre aspas é
fala sugerida. Adapte para a sua voz, não decore: o que importa é a sequência de ideias.

---

## Slide 1 · PROGRAMA DE TRAINEES EM DADOS E INTELIGÊNCIA ARTIFICIAL

```
⏱ 19h00 às 19h10 (slide de espera)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Slide projetado desde 18h55. Fale a cada 2 ou 3 minutos enquanto a sala enche.

"Boa noite! Hoje é o dia que a Aula 9 prometeu: pipeline de verdade, rodando de
verdade, com vocês no teclado. Enquanto a sala enche, escreve no chat: alguém aqui
já instalou alguma coisa parecida com Airflow ou Spark antes?"

Não comece antes de 19h08.

──────────────────────────────────────────────────────────────
LEMBRETES
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- Moderador com o link do Discord e do notebook prontos para colar no chat.
- Confirmar ANTES da aula: containers do Airflow de pé (docker compose ps) e a DAG
  aula10_pipeline_fraude aparecendo sem erro de import. Ver docs/aula-10/00-guia-de-
  preparacao.md, secao 2.
```

## Slide 2 · ENQUANTO TODO MUNDO ENTRA

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Bem-vindos à Aula 10. Rapidinho, antes de começar:

Microfone sempre no mudo, câmera é opcional. Dúvida a qualquer momento, escreve no
chat, a gente tem moderação acompanhando o tempo todo. A aula fica gravada e o link
chega em até 24 horas.

O formato de hoje é diferente da segunda: eu mostro uma coisa rodando ao vivo, vocês
ganham uns 15 minutos de mecânica, e o resto da noite é vocês de mão na massa, com a
gente e os mentores circulando para ajudar.

Enquanto isso, escreve no chat: alguém aqui já instalou algo parecido com Airflow ou
Spark antes? Quero ver quantas mãos virtuais eu tenho na sala."
```

## Slide 3 · De volta à segunda

```
⏱ 19h10 às 19h25 (15 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Recapitulação rápida da Aula 9    5 min
  Os dois cenários de hoje          5 min
  Mecânica da noite                 5 min
```

## Slide 4 · RECAPITULANDO

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Relembrando rapidinho três nomes da Aula 9.

DAG é o grafo que decide a ordem das tarefas: extrair antes de transformar, transformar
antes de carregar.

Airflow é o orquestrador que dispara, agenda e reexecuta essas tarefas sem intervenção
manual.

Spark é o motor que divide um processamento grande entre várias máquinas ao mesmo
tempo, em vez de uma máquina só suando sozinha.

Na segunda, vocês viram a explicação. Hoje, os três rodam de verdade, na frente de
vocês."
```

## Slide 5 · OS DOIS CENÁRIOS DE HOJE

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Hoje tem dois cenários.

O primeiro é o Apache Airflow, já instalado e rodando na minha máquina. Isso aqui
ninguém mais precisa instalar: eu mostro funcionando, vocês acompanham o grafo, o
disparo e o log.

O segundo é PySpark, dentro do Google Colab, no navegador de cada um. Aqui é onde
vocês colocam a mão: o pipeline inteiro, do início ao fim, com o mesmo caso de fraude
que a gente usa desde a Aula 2."
```

## Slide 6 · MECÂNICA DA NOITE

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Antes da demonstração, a mecânica rápida.

O notebook de vocês já está no Discord, chamado Aula_10_Alunos_Engenharia_de_Dados_com_
PySpark. Onde aparecer TODO, tem uma dica do lado, não é para adivinhar do nada.

Travou, escreve no chat com o número do passo. A gente e os mentores estão de olho.

E um aviso: uma das etapas foi pensada para dar erro de propósito. Quando isso
acontecer, não é bug de vocês, é o próprio exercício."

──────────────────────────────────────────────────────────────
LEMBRETES
Felipe: fixar o link do notebook no Discord ANTES deste slide entrar no ar.
```

## Slide 7 · Apache Airflow

```
⏱ 19h25 às 19h45 (20 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  O que a DAG de hoje faz     5 min
  Demonstração ao vivo       12 min
  Perguntas rápidas           3 min

Antes de começar: já com http://localhost:8080 aberto e logado numa aba, DAG
aula10_pipeline_fraude visível na lista. Ver o roteiro completo em docs/aula-10/00-
guia-de-preparacao.md, seção 2.5.
```

## Slide 8 · A DAG DE HOJE

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"A DAG de hoje tem três tarefas encadeadas: extract, transform, load. A mesma sigla
que vocês viram na segunda, só que agora cada quadrado desse grafo é uma função Python
que realmente executa.

Extract lê o CSV de transações. Transform limpa: tira nulo, duplicado e valor
inválido, e registra no log quantas linhas entraram e quantas sobraram. Load agrupa
por lojista, soma o valor e grava o resultado final.

Vamos ver isso rodando."
```

## Slide 9 · AO VIVO

```
⏱ 12 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

ROTEIRO DA DEMONSTRAÇÃO (ver docs/aula-10/00-guia-de-preparacao.md, seção 2.5):

1. Mostrar a lista de DAGs, apontar aula10_pipeline_fraude.
   "Isso aqui é uma DAG, o grafo de dependência que vimos na semana passada. Cada
   quadrado é uma tarefa."

2. Clicar na DAG, abrir a visão de grafo. Mostrar extract -> transform -> load
   visualmente.

3. Disparar a execução manual (botão de play, "Trigger DAG").

4. Acompanhar as três tarefas mudando de cor conforme rodam (fila, execução,
   sucesso), narrando o que está acontecendo por trás.

5. Abrir os logs da tarefa transform, mostrar a linha com a contagem de linhas antes
   e depois da limpeza. Conectar com o bloco de qualidade de dados da Aula 9.

6. Encerrar mostrando o CSV de saída gerado, com os lojistas ordenados por valor
   total.

"Reparem: eu não rodei nenhum desses três passos na mão. Eu só disparei a DAG, e o
Airflow decidiu a ordem, executou cada tarefa, e guardou o log de cada uma. Se a
transform falhasse, o load nem começaria. É isso que separa um pipeline de produção
de um notebook rodado célula por célula."

──────────────────────────────────────────────────────────────
LEMBRETES
Se algo falhar ao vivo: usar o vídeo de backup gravado com antecedência (seção 2.7 do
guia). Não gastar mais que 2 minutos tentando debugar em tempo real.
```

## Slide 10 · O QUE PRESTAR ATENÇÃO

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Quatro coisas para levar dessa demonstração, além do resultado final: o grafo mostra
a ordem sem precisar ler código, o disparo manual de hoje podia ser automático numa
hora marcada, cada tarefa deixa seu próprio log, e se uma falhar, o Airflow reexecuta
só ela, não o pipeline inteiro de novo. Isso é o que separa orquestração de só rodar
um script."

Perguntas rápidas antes de seguir para o Spark.
```

## Slide 11 · PySpark no Colab

```
⏱ 19h45 às 20h00 (15 min)  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Uma correção antes de começar   4 min
  O pipeline de hoje, em visão geral   6 min
  Como abrir e navegar no notebook   5 min
```

## Slide 12 · ANTES DE COMEÇAR

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Uma correção rápida antes de começar. O Colab não vem com Spark instalado de fábrica,
só com Python e um conjunto grande de bibliotecas. Falta especificamente Java, que é
o que o motor do Spark precisa para rodar por baixo.

A primeira célula do notebook resolve isso: instala o Java e o PySpark, e leva menos
de 2 minutos. Vocês rodam essa célula uma vez por sessão. Se o Colab cair no meio da
aula, é só rodar de novo desde o início."
```

## Slide 13 · O PIPELINE DE HOJE

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O pipeline de hoje tem seis passos. Extract e transform seguem o mesmo espírito da
Aula 9: ler os dados, e garantir qualidade antes de seguir adiante. A diferença é que,
em vez de só descartar linha ruim, hoje vocês vão separar e guardar o motivo, isso se
chama quarentena de dados.

Depois vem unify, juntando as seis tabelas. Depois, um passo novo: bifurcação, separando
transações normais de transações que merecem atenção, cada uma seguindo para um destino
diferente. E fecha com reconciliação: provar que nenhuma linha sumiu sem explicação em
nenhuma etapa.

Isso é engenharia de dados de verdade: transformar importa, mas provar que a
transformação funcionou importa tanto quanto."
```

## Slide 14 · COMO VAI FUNCIONAR

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Para abrir: link no Discord, e a primeira coisa é fazer uma cópia para o próprio
Drive, Arquivo, Salvar uma cópia no Drive. Depois disso, o notebook é só seu.

Rodem uma célula de cada vez, em ordem, sem pular. Onde tiver TODO, tem uma dica do
lado. E um aviso: no passo 3, uma célula vai dar erro de propósito. Leiam o texto logo
depois da célula antes de tentar corrigir, ele explica exatamente por quê.

A partir do próximo slide, são 50 minutos só de prática. A gente e os mentores vamos
circular pelo chat o tempo todo."
```

## Slide 15 · Mão na massa

```
⏱ 20h00 às 20h50 (50 min)  |  ESSENCIAL  |  Apresenta: Edmar + Felipe
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

CHECKLIST DO MENTOR DURANTE A PRÁTICA:

- Circular pelo chat a cada 5 minutos, não esperar pergunta chegar sozinha.
- Quem travar no passo 3 (erro de referência ambígua): confirmar que leu o texto
  explicativo antes de dar a resposta pronta.
- Quem terminar antes do tempo: sugerir revisar as duas perguntas de conferência do
  final do notebook, ou conferir se a reconciliação do passo 6 realmente bateu.
- Aos 20h40, avisar no chat: "10 minutos para o fechamento, garantam que rodaram até
  a reconciliação."
```

## Slide 16 · AGORA É COM VOCÊS

```
⏱ 50 min (projetado o tempo todo)  |  ESSENCIAL  |  Apresenta: Edmar + Felipe
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Este slide fica projetado durante toda a prática, sem narração contínua. Circular
pelo chat, responder dúvida por dúvida.

Aos 20h40 (10 minutos do fim): avisar no chat pedindo para todo mundo garantir que
chegou pelo menos até o passo 6 (reconciliação), mesmo que as duas perguntas finais
ainda não estejam respondidas.
```

## Slide 17 · Encerramento

```
⏱ 20h50 às 21h00 (10 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Recapitulação            3 min
  O que vem pela frente    2 min
  Q&A                      4 min  (elástico, absorve atraso)
  Fechamento               1 min
```

## Slide 18 · ENCERRAMENTO

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Cinco ideias para levar de hoje.

Orquestração não é rodar célula por célula: o Airflow decide a ordem, agenda,
registra log de cada passo e reexecuta sozinho quando algo falha.

Quarentena vale mais que descartar em silêncio: guardar o motivo é o que permite
explicar depois por que uma linha sumiu.

Nem todo dado segue o mesmo caminho: separar por regra de negócio, e mandar cada
trilha para o destino certo, é decisão de projeto deliberada.

Um pipeline só está pronto quando reconcilia: contar de novo em cada etapa, e provar
que nada se perdeu sem explicação.

E a mais importante: vocês rodaram, sozinhos, um pipeline real, do extract até a
reconciliação. Isso sai direto da teoria da Aula 9 e vira prática nas suas mãos."
```

## Slide 19 · PRÓXIMOS ENCONTROS

```
⏱ 2 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O que vem pela frente.

Semana 6, segunda-feira: Machine Learning, do baseline ao primeiro modelo. Volta o
formato conceitual das segundas.

Quinta da mesma semana: primeiro laboratório de Machine Learning, no mesmo formato de
hoje, demonstração curta e o resto é prática. A mesma base de fraude em cartão continua
sendo a referência."
```

## Slide 20 · ANTES DE IR

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

PERGUNTAS PREVISÍVEIS DE HOJE:

- "Preciso decorar a sintaxe do PySpark?"
  Não. O que importa é reconhecer o padrão (extract, transform, unify, load) e saber
  quando cada peça entra. A sintaxe exata está sempre a uma busca de distância.

- "Por que minha trilha de atenção veio vazia, ou minha quarentena veio vazia?"
  Depende da base do dia. Base limpa gera quarentena vazia, o pipeline está
  confirmando que não havia nada para descartar hoje, e isso é sinal de dado bom.

- "Preciso instalar Airflow na minha máquina também?"
  Não. Só quem for demonstrar precisa. Para a atividade de vocês, o Colab com PySpark
  é suficiente.

- "Isso cai no projeto final?"
  Cai direto. Squads que lidam com dados de fontes diferentes vão precisar de um
  pipeline parecido com esse, ainda que mais simples.
```

## Slide 21 · Obrigado!

```
⏱ 1 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. Vocês saem daqui tendo rodado um pipeline real, não só
lido sobre ele. Revisem o notebook com calma até a próxima segunda, principalmente o
passo da bifurcação. Nos vemos lá. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Anotar quais passos do notebook geraram mais pergunta no chat, para calibrar o
  roteiro de mentoria da próxima turma.
- Derrubar o ambiente Airflow só depois de confirmar que ninguém mais precisa dele
  hoje (docker compose down, opcional, pode deixar rodando).
```
