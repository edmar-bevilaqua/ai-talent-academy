# Roteiro do apresentador: Aula 13 (Semana 7, segunda-feira)

> Gerado automaticamente a partir das notas do deck.
> Não edite este arquivo à mão: edite `scripts/gerar_slides_aula13.py` e rode
> `python scripts/gerar_slides_aula13.py && python scripts/exportar_roteiro_aula13.py`.

**Como usar:** imprima ou deixe aberto num segundo monitor. O texto entre aspas é
fala sugerida. Adapte para a sua voz, não decore: o que importa é a sequência de ideias.

---

## Slide 1 · PROGRAMA DE TRAINEES EM DADOS E INTELIGÊNCIA ARTIFICIAL

```
⏱ 19h00 às 19h10 (slide de espera)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Slide projetado desde 18h55. Fale a cada 2 ou 3 minutos enquanto a sala enche.

"Boa noite! Semana 7, e hoje é o assunto que a gente prometeu lá na Aula 3: agentes
de IA. Enquanto a sala enche, uma pergunta pro chat: você já usou alguma ferramenta
de IA que fez mais do que só responder, tipo pesquisar na internet, mexer num
arquivo ou executar alguma coisa sozinha?"

Não comece antes de 19h08.

──────────────────────────────────────────────────────────────
LEMBRETES
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- Moderador com o link do Discord pronto para colar.
- Aula desenhada para ficar mais enxuta que o padrão das segundas, por pedido
  explícito do usuário. Edmar e Felipe controlam o ritmo ao vivo: cortem à vontade
  o que já estiver claro para a sala.
```

## Slide 2 · ENQUANTO TODO MUNDO ENTRA

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Bem-vindos à Aula 13. Rapidinho: microfone no mudo, câmera à vontade, dúvida no
chat a qualquer momento, aula gravada com link em até 24h.

Aviso importante, diferente do padrão das outras segundas: hoje tem prática de
verdade, no meio da aula, não só teoria. Lá pelo Bloco 04 vocês vão construir um
agente com a própria mão. Por isso a quinta desta semana muda de formato, mais
sobre isso no fim da noite.

Enquanto isso, escreve no chat: que ferramenta de IA já fez mais do que só
responder, para você? Já pesquisou sozinha, já mexeu num arquivo, já executou
alguma coisa? Vou puxar algumas respostas daqui a pouco."
```

## Slide 3 · De volta à promessa da Semana 2

```
⏱ 19h10 às 19h25 (15 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Recap de uma frase por conceito    7 min
  Panorama de hoje                   8 min

Bloco deliberadamente curto. Toda a base já foi plantada nas Aulas 1 e 3, o trabalho
aqui é só reconectar o que já foi dito.
```

## Slide 4 · LEMBRANDO

```
⏱ 7 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Cinco coisas que vocês já ouviram, rapidinho.

A Aula 1 já definiu agente numa frase: uma GenAI que não só responde, planeja, usa
ferramentas e executa tarefas.

A Aula 1 colocou agentes como o marco mais recente da história da IA, logo depois do
ChatGPT.

A Aula 3 prometeu este dia, no próprio roteiro do curso: "Semana 7, Agentes de IA,
da resposta à ação".

A Aula 3 já cobriu Transformer, janela de contexto e prompt, a base técnica que um
agente usa por baixo.

E a Aula 3 já cobriu RAG, buscar informação externa antes de responder, que é
literalmente uma das ferramentas que um agente pode ter na caixa.

Hoje a gente não reexplica nada disso. A gente vai direto para o que ainda não foi
dito."
```

## Slide 5 · O PANORAMA DE HOJE

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O panorama de hoje, em seis perguntas, exatamente na ordem que faz sentido
responder: quando isso surgiu, o que é de verdade, o que muda em relação a uma
chamada única de LLM, como controlamos, quais são as principais soluções, e qual é
o estado da arte agora.

Cada bloco responde uma pergunta só. Vamos."
```

## Slide 6 · Quando isso surgiu

```
⏱ 19h25 às 19h50 (25 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Linha do tempo, parte 1 (2022 a 2023)     8 min
  AutoGPT, a febre viral                    9 min
  Linha do tempo, parte 2 (2023 a hoje)     8 min
```

## Slide 7 · A VIRADA

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"A história começa antes do que a maioria imagina.

Outubro de 2022, um mês antes do ChatGPT: pesquisadores do Google Research e da
Princeton publicam o paper ReAct, Reasoning and Acting. A ideia central: em vez de o
modelo só responder, ele intercala pensar e agir, num loop só. Essa é literalmente a
arquitetura que quase todo agente usa até hoje.

Novembro de 2022, ChatGPT, já visto na Aula 1.

Fevereiro de 2023, a Meta publica o Toolformer: um modelo treinado para decidir
sozinho quando vale a pena chamar uma calculadora, um buscador, um tradutor. Uso de
ferramenta deixou de ser truque de prompt e virou capacidade aprendida.

Março de 2023, um desenvolvedor independente chamado Toran Bruce Richards publica o
AutoGPT: você dá um objetivo, e o modelo gera suas próprias tarefas, executa,
avalia, gera mais tarefas, sem parar. Vamos ver o que aconteceu com isso."
```

## Slide 8 · UMA FEBRE REAL

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O AutoGPT não foi um projeto de pesquisa discreto. Foi uma febre. Em poucas
semanas, virou um dos repositórios de crescimento mais rápido da história do
GitHub, hoje com mais de 185 mil estrelas.

A promessa era gigante: dá um objetivo qualquer para o modelo, e ele se vira
sozinho, sem supervisão, até terminar."
```

## Slide 9 · O QUE ACONTECEU NA PRÁTICA

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"E na prática? A entrega não acompanhou a promessa. Loops que não terminavam,
gerando tarefa atrás de tarefa sem convergir. Custo alto e imprevisível, porque cada
passo do loop custa uma chamada de API nova. E nenhum controle real sobre o que o
modelo estava fazendo, exatamente o risco que a Fase 5 da Aula 1 já tinha avisado:
"perder controle e rastreabilidade".

O hype esfriou. Mas a pergunta que ficou, como dar autonomia sem perder controle, é
o fio que puxa quase tudo que vem no resto de hoje."
```

## Slide 10 · DA BAGUNÇA À PADRONIZAÇÃO

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Depois da fase de bagunça criativa, a indústria passou a resolver o problema de
encanamento.

Em meados de 2023, a OpenAI lança function calling: o modelo passa a poder escolher,
de forma estruturada, qual função chamar e com quais parâmetros. É a peça técnica
que transforma "o modelo decide algo" em "o código de fora consegue confiar
nessa decisão e executar".

Em novembro de 2024, a Anthropic lança o MCP, Model Context Protocol: um jeito
aberto e padronizado de conectar qualquer modelo a qualquer ferramenta ou fonte de
dado, resolvendo um problema que a indústria chamava de N vezes M, ou seja, antes
disso, cada combinação de modelo e ferramenta precisava de uma integração própria.
Hoje já existem mais de 16 mil servidores MCP publicados.

E de 2025 para cá, os três grandes, OpenAI, Google e Anthropic, lançaram kits
oficiais de desenvolvimento para construir agente de produção, não mais só
experimento. A gente volta nisso no bloco de soluções."
```

## Slide 11 · O que é um agente, de verdade

```
⏱ 19h50 às 20h15 (25 min)  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Definição formal              6 min
  O loop ReAct, passo a passo   12 min
  O que é "ferramenta", tecnicamente   7 min
```

## Slide 12 · DEFINIÇÃO FORMAL

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Vamos destrinchar a frase da Aula 1. Um agente tem quatro peças.

Um modelo de linguagem, que decide o que fazer a seguir.

Um loop de raciocínio: pensa, age, observa o resultado dessa ação, pensa de novo, e
repete, quantas vezes for preciso.

Ferramentas reais: funções que o modelo pode chamar para agir no mundo de verdade,
não só descrever o que faria.

E estado que persiste entre os passos: o agente lembra o que já tentou e o que já
descobriu, ao longo de toda a tarefa, não só numa resposta isolada.

Um agente é essas quatro peças trabalhando juntas, rumo a um objetivo."
```

## Slide 13 · O LOOP REACT, NA PRÁTICA

```
⏱ 12 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Isso aqui é o loop ReAct, do paper de outubro de 2022, na prática, usando o caso de
fraude que vocês já conhecem de cor.

Pergunta: qual lojista teve mais contestação este mês?

Pensa: preciso consultar o banco de dados para responder isso. Age: chama a
ferramenta de SQL, passando uma query de contagem por lojista. Observa: a ferramenta
devolve uma tabela de resultado. Pensa de novo: já tenho a resposta, não preciso
agir mais. Responde com o dado real.

Três coisas para prestar atenção. Primeira: cada linha dessas é um passo real de
execução, o modelo genuinamente para e espera o resultado antes de continuar,
isso não é uma metáfora de apresentação.

Segunda: a ferramenta de SQL é código escrito por uma pessoa, separado do modelo. O
modelo só decide quando chamar essa ferramenta e com qual parâmetro. Quem executa a
query de verdade é o banco de dados.

Terceira: se o resultado voltasse estranho, tipo vazio ou com erro, o modelo poderia
pensar de novo e tentar uma query diferente, sozinho, sem ninguém pedir. É isso que
separa um agente de um script fixo."
```

## Slide 14 · O QUE É "FERRAMENTA", TECNICAMENTE

```
⏱ 7 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Última peça deste bloco: o que é uma ferramenta, tecnicamente.

É uma função comum, de código comum, com um nome e uma descrição dos parâmetros que
ela espera. O modelo lê essa descrição, junto com o pedido do usuário, e decide se e
quando vale a pena chamar.

Ponto crucial: o modelo NUNCA executa a ferramenta sozinho. Ele só devolve um pedido
estruturado, "quero chamar tal função, com tais parâmetros". Quem executa de
verdade é o código em volta do modelo, escrito por uma pessoa.

É exatamente essa separação, entre decidir e executar, que abre espaço para todo o
controle que existe hoje sobre agente. A gente aprofunda isso no Bloco 06, depois do
intervalo.

Consultar banco, chamar API, ler e escrever arquivo, mandar mensagem: tudo isso já
foi usado como ferramenta de agente, em algum produto real."
```

## Slide 15 · Mão na massa: seu primeiro agente

```
⏱ 20h15 às 20h45 (30 min)  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Mecânica e abertura do notebook    8 min
  Prática guiada                    22 min

Mudança de plano do curso: esta prática entrou na segunda de propósito, para a
quinta-feira (Aula 14) ficar inteira livre para mentoria individual de squad, com a
Semana 8 e o Demo Day se aproximando. Isso quebra a regra padrão das segundas (zero
código ao vivo), de forma deliberada.
```

## Slide 16 · COMO VAI FUNCIONAR

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Mecânica rápida antes de começar. O notebook está no Discord, chamado
Aula_13_Alunos_Construindo_Primeiro_Agente. Vocês vão precisar de uma chave gratuita
da NVIDIA, o próprio notebook explica como gerar em menos de um minuto.

O código já vem pronto, é leitura guiada, sem lacuna para preencher: hoje o foco é
ver o loop pensa, age, observa, responde rodando de verdade, não decorar sintaxe de
Python.

E a ferramenta que o agente vai usar não é simulada: é um servidor MCP de verdade,
rodando dentro do próprio notebook, com uma única ferramenta que consulta a taxa de
contestação de um lojista, na mesma base que vocês já conhecem."
```

## Slide 17 · AGORA É COM VOCÊS

```
⏱ 22 min (projetado o tempo todo)  |  ESSENCIAL  |  Apresenta: Edmar + Felipe
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Este slide fica projetado durante toda a prática, sem narração contínua. Circular
pelo chat, responder dúvida por dúvida.

Checklist do mentor:
- Quem travar gerando a chave da NVIDIA: confirmar que copiou a chave inteira,
  incluindo o prefixo nvapi-.
- Quem terminar antes do tempo: sugerir testar com um id_lojista diferente, ou
  perguntar algo que não precise da ferramenta, para ver o agente decidir sozinho.
- Aos 20h40 (5 minutos do fim): avisar no chat pedindo para todo mundo garantir que
  rodou pelo menos até o Passo 4 (a ferramenta funcionando), mesmo que o Passo 6 (o
  loop completo) ainda não tenha terminado.
```

## Slide 18 · O que muda em relação a uma chamada única

```
⏱ 20h45 às 21h05 (20 min)  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Comparação lado a lado    7 min
  Exemplo concreto           7 min
  Interação                  6 min
```

## Slide 19 · COMPARANDO

```
⏱ 7 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Lado a lado. Chamada única: um prompt entra, uma resposta sai, e acabou. Não guarda
nada entre uma chamada e outra, não age no mundo de verdade, só descreve o que
faria. E se a resposta vier errada, a conversa simplesmente acaba ali, sem
correção automática.

Agente: um objetivo entra, e vários passos acontecem até chegar numa resposta.
Guarda estado ao longo de toda a tarefa. Age de verdade, através de ferramentas.
E se um passo falhar, pode tentar de novo sozinho, sem ninguém pedir.

A frase que fecha isso: a diferença não está no modelo, o mesmo modelo pode fazer
as duas coisas. Está no que existe em volta dele, o loop, as ferramentas, o
estado."
```

## Slide 20 · UM EXEMPLO CONCRETO

```
⏱ 7 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Exemplo simples, de propósito, para ficar bem claro. Pergunta: qual o clima em
Curitiba agora?

Só o LLM, sem ferramenta nenhuma: ele não tem acesso a dado em tempo real, só
conhece o que estava nos dados de treino. Duas saídas possíveis, e nenhuma boa:
inventa uma resposta plausível, ou admite que não sabe.

O mesmo modelo, agora como agente: ele reconhece que precisa de um dado atual, chama
uma ferramenta de clima de verdade, lê o resultado real, e responde com o número
certo de agora.

O modelo é o mesmo. A diferença inteira está em ter, ou não ter, uma ferramenta e um
loop em volta dele."
```

## Slide 21 · INTERAÇÃO RÁPIDA

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"No chat: para cada cenário, escreva única ou agente.

Resumir um texto que já está na conversa? Única, não precisa de ferramenta nem de
ação no mundo.

Reservar o hotel mais barato numa data? Agente, precisa buscar preços reais e
executar uma reserva de verdade.

Traduzir uma frase? Única.

Investigar por que as vendas caíram, consultando o banco sozinho? Agente, na
veia: loop, ferramenta, e provavelmente mais de um passo até achar a causa."
```

## Slide 22 · INTERVALO

```
⏱ 15 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Intervalo. Sem apresentação.
```

## Slide 23 · Como controlamos um agente

```
⏱ 21h20 às 21h50 (30 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Callback ao risco da Aula 1    3 min
  Mecanismos de controle        14 min
  Observabilidade e avaliação    8 min
  MCP como parte do controle     5 min
```

## Slide 24 · LEMBRANDO

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Vocês já ouviram esse risco na Aula 1. Hoje a gente aprende, de verdade, como
evitar que ele aconteça."
```

## Slide 25 · MECANISMOS DE CONTROLE

```
⏱ 14 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Quatro camadas de controle, cada uma resolvendo um pedaço do problema.

Permissão e escopo: o agente só enxerga as ferramentas que alguém deu para ele. Um
agente de atendimento ao cliente não deveria nem saber que existe uma ferramenta de
apagar registro do banco.

Humano no loop: ações irreversíveis, mandar dinheiro, apagar dado, publicar
conteúdo, esperam aprovação explícita de uma pessoa antes de executar de verdade.

Sandbox: o agente roda num ambiente isolado, sem acesso direto ao sistema de
produção, até provar que se comporta de forma confiável.

Limite de custo e de passos: um teto de quantas ferramentas ele pode chamar e quanto
tempo pode gastar numa única tarefa. Isso, sozinho, já evita o loop infinito que
matou a credibilidade do AutoGPT."
```

## Slide 26 · OBSERVABILIDADE E AVALIAÇÃO

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Controlar também é conseguir enxergar. Tracing é um log de cada passo do loop:
toda decisão, toda chamada de ferramenta, todo resultado, guardado e revisável
depois.

Isso é literalmente o que resolve a palavra "rastreabilidade" do risco da Aula 1.
Sem log passo a passo, ninguém consegue explicar por que o agente fez o que fez,
mesmo quando ele acerta.

E avaliação automatizada: testar o agente contra casos conhecidos, com resposta
certa já sabida, antes de confiar nele em produção. Sem isso, toda atualização de
prompt vira uma aposta às cegas. Com isso, vira um experimento medido, igual ao que
vocês já viram com treino e teste, lá na Aula 11."
```

## Slide 27 · O MCP TAMBÉM É CONTROLE

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Uma última conexão antes de seguir: o MCP, que vocês viram no Bloco 02 como marco
histórico, também é uma peça de controle.

Um servidor MCP declara exatamente o que oferece, de forma explícita e documentada.
Isso facilita demais a permissão e o escopo: em vez de auditar função por função
escondida dentro do código, dá para decidir "sim" ou "não" para um servidor MCP
inteiro, sabendo exatamente o que ele expõe."
```

## Slide 28 · Principais soluções para criar um agente

```
⏱ 21h50 às 22h20 (30 min)  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Framework landscape          12 min
  MCP como padrão comum         8 min
  Caminho sem programar        10 min
```

## Slide 29 · O CARDÁPIO DE HOJE

```
⏱ 12 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Seis nomes que vocês vão ouvir bastante no mercado, cada um com uma força
diferente.

LangGraph, da LangChain: hoje é quem mais tem cliente grande de verdade, nomes como
Uber, LinkedIn, JPMorgan, porque foi desenhado para produção, com estado bem
controlado e trilha de auditoria.

CrewAI: mais leve para prototipar rápido. Teve mais de 2 bilhões de execuções de
agente registradas em doze meses, e aparece em quase metade das empresas da Fortune
500 em algum experimento.

AutoGen, hoje também chamado AG2, da Microsoft: forte em múltiplos agentes
conversando entre si, cada um especialista numa parte da tarefa.

E os três kits oficiais dos grandes laboratórios: OpenAI Agents SDK, Google ADK, e
Claude Agent SDK da Anthropic, este último com a integração mais profunda com MCP e
foco forte em agente de codificação, o tipo de agente que, aliás, ajudou a montar
o material desta própria aula."
```

## Slide 30 · MCP COMO PADRÃO COMUM

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O MCP atravessa quase toda a tabela anterior. Praticamente todo framework grande
já fala esse protocolo, não é mais recurso exclusivo de um fornecedor.

Isso resolve o problema antigo do N vezes M: antes, cada combinação de modelo e
ferramenta precisava da própria integração feita à mão. Hoje já são mais de 16 mil
servidores MCP publicados, cobrindo banco de dados, planilha, sistema interno, quase
tudo.

Consequência prática: escolher o framework virou menos decisivo do que escolher bem
quais ferramentas MCP conectar."
```

## Slide 31 · E QUEM NÃO PROGRAMA

```
⏱ 10 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Última coisa deste bloco, importante para a turma mista que vocês são: não precisa
programar para montar um agente simples.

Plataformas visuais de automação já oferecem bloco pronto de "agente de IA",
ligando gatilho, modelo e ferramenta sem escrever uma linha de código.

O trade-off é real: menos controle fino, menos flexibilidade do que os frameworks
que vimos. Mas é um caminho de verdade para quem está começando, ou só quer testar
uma ideia rápido antes de investir em código."
```

## Slide 32 · O estado da arte hoje

```
⏱ 22h20 às 22h45 (25 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Agentes de codificação    8 min
  Adoção empresarial real   8 min
  Onde ainda trava          9 min
```

## Slide 33 · O EXEMPLO MAIS PRÓXIMO DE VOCÊS

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Vou dar o exemplo mais próximo que existe: este material, os slides que vocês
estão vendo agora, o roteiro que estamos seguindo, foi construído com a ajuda de um
agente de codificação.

Isso é a categoria de agente que mais amadureceu nos últimos dois anos: ferramentas
como Claude Code, Cursor, e o modo agente do GitHub Copilot leem um repositório
inteiro, escrevem código, rodam testes de verdade, leem o resultado, e corrigem
sozinhas o que deu errado, tudo dentro do mesmo loop que a gente viu no Bloco 03.
É ferramenta real de trabalho, usada todo dia por quem programa profissionalmente."
```

## Slide 34 · ADOÇÃO REAL, COM NÚMERO

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Números reais, não projeção. LangGraph tem cliente grande de verdade rodando em
produção: Uber, LinkedIn, JPMorgan, Klarna, Cisco.

CrewAI passou de 2 bilhões de execuções de agente em doze meses, e está presente em
quase metade das empresas da Fortune 500, mesmo que em fase de experimento em
muitas delas.

E o Claude Agent SDK, lançado em 2025, cresceu com adoção concentrada em ferramenta
de desenvolvedor, o tipo de agente de codificação que citei no slide anterior.

Isso não é mais hype de 2023. É ferramenta rodando em empresa grande, hoje."
```

## Slide 35 · ONDE AINDA TRAVA

```
⏱ 9 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"E para fechar com os pés no chão: o estado da arte também tem limite conhecido.

Tarefa muito longa ainda acumula erro: quanto mais passos no loop, maior a chance de
um erro no início contaminar tudo que vem depois.

Custo ainda é imprevisível em tarefa complexa, porque mais passos significam mais
chamadas de modelo.

Avaliar um agente continua mais difícil que avaliar um modelo simples, porque não
existe uma resposta certa só, existe um caminho inteiro de decisões para julgar.

E viés e erro do modelo se multiplicam dentro do loop, um erro pequeno cedo pode se
propagar.

Quem promete hoje um agente perfeito, sem limite nenhum, ainda está vendendo o hype
de 2023, não o estado da arte real de agora."
```

## Slide 36 · Encerramento

```
⏱ 22h45 às 23h05 (20 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Recapitulação             4 min
  O que vem pela frente     3 min
  Q&A                       10 min  (elástico, absorve atraso)
  Fechamento                3 min
```

## Slide 37 · ENCERRAMENTO

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Sete ideias para levar de hoje.

Agente não nasceu com o hype de 2023: o paper do loop é de outubro de 2022.

Um agente é modelo mais loop mais ferramenta mais estado, as quatro peças juntas.

E vocês construíram isso com a própria mão, hoje: um agente real, com uma
ferramenta servida por MCP de verdade.

A diferença de uma chamada única mora no que existe em volta do modelo.

Controlar um agente é possível, camada em cima de camada.

O mercado já tem várias soluções consolidadas, de framework robusto a plataforma sem código.

E o estado da arte é real, mas tem limite conhecido: tarefa longa, custo e avaliação
continuam sendo o desafio em aberto."
```

## Slide 38 · PRÓXIMOS ENCONTROS

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Reparem que a quinta desta semana muda de formato. Vocês já construíram o agente
hoje, então não tem laboratório novo guiado na quinta. A noite inteira vira mentoria
aberta, com Edmar e Felipe disponíveis para dúvida de squad, de projeto, ou de
qualquer coisa que sobrou de hoje.

E a Semana 8 já é a reta final da Etapa 1, com o Demo Day se aproximando."
```

## Slide 39 · ANTES DE IR

```
⏱ 10 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

PERGUNTAS PREVISÍVEIS DE HOJE:

- "Preciso escolher um framework para aprender já?"
  Não. O importante hoje é reconhecer os nomes e saber o que cada um resolve melhor.
  A escolha de ferramenta vem depois, quando o problema real estiver na mesa.

- "Agente substitui programador?"
  Não do jeito que a pergunta sugere. Ele muda o trabalho de quem programa, mas
  ainda precisa de alguém definindo objetivo, revisando resultado e decidindo o que
  aprovar. O próprio material desta aula teve revisão humana o tempo todo.

- "Dá para usar agente sem saber programar?"
  Sim, com as plataformas sem código do Bloco 07, embora com menos controle fino do
  que os frameworks de produção. E vocês acabaram de ver que mesmo com código, um
  agente de uma ferramenta só cabe em um notebook curto, no Bloco 04.

- "Isso cai no projeto final?"
  Cai direto, principalmente para quem escolher a trilha de GenAI ou Programação na
  Etapa 2.
```

## Slide 40 · Obrigado!

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. Vocês saem daqui sabendo, de verdade, o que é um
agente por dentro, não só o nome bonito. Revisem os slides antes de quinta,
principalmente o loop do Bloco 03. Nos vemos lá. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Anotar quais dos seis blocos geraram mais pergunta no chat, para calibrar o corte
  se uma próxima turma precisar de uma versão ainda mais curta.
```
