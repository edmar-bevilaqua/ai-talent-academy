# Roteiro do apresentador: Aula 8 (Semana 4, quinta-feira)

> Gerado automaticamente a partir das notas do deck.
> Não edite este arquivo à mão: edite `scripts/gerar_slides_aula08.py` e rode
> `python scripts/gerar_slides_aula08.py && python scripts/exportar_roteiro_aula08.py`.

**Como usar:** imprima ou deixe aberto num segundo monitor. O texto entre aspas é
fala sugerida. Adapte para a sua voz, não decore: o que importa é a sequência de ideias.

---

## Slide 1 · PROGRAMA DE TRAINEES EM DADOS E INTELIGÊNCIA ARTIFICIAL

```
⏱ 19h00 às 19h10 (slide de espera)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Slide projetado desde 18h55. Fale a cada 2 ou 3 minutos enquanto a sala enche.

"Boa noite! Hoje é dia de colocar a mão na massa de verdade: pandas, NumPy, Matplotlib
e Seaborn, todos juntos, num banco de um milhão de linhas. Enquanto todo mundo entra,
escreve no chat: você já rodou algum notebook Python antes de hoje?"

Não comece antes de 19h08.

──────────────────────────────────────────────────────────────
LEMBRETES
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- CRÍTICO HOJE: confirme que o link do notebook e do Google Forms estão fixados no
  Discord ANTES de 19h00.
- Leia docs/aula-08/dados/historia_anomalia.md antes da aula. É o gabarito da
  investigação, e não pode aparecer em slide nem em chat.
```

## Slide 2 · ENQUANTO TODO MUNDO ENTRA

```
⏱ 19h00 às 19h10  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Leia os itens uma vez, por volta de 19h05. Insista no quarto item: quem espera uma
aula parecida com a segunda vai se surpreender, e é bom avisar logo de cara.
```

## Slide 3 · Hoje é dia de investigar

```
⏱ 19h10 às 19h30 (20 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco curto de propósito. O objetivo é explicar a mecânica e dar o gancho de
investigação, sem ensinar nada novo, para a turma sair direto para a prática com
clareza.

ESTRUTURA:
  Onde estamos              3 min
  O que muda hoje            4 min
  Como vai funcionar           5 min
  O convite                     4 min
  Regras de hoje                4 min
```

## Slide 4 · ONDE ESTAMOS

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Onde vocês estão. Segunda-feira foi a teoria inteira de Python: história da linguagem,
NumPy, pandas em profundidade, Matplotlib e Seaborn. Hoje é a prática de tudo isso,
numa base de dados muito maior do que qualquer exemplo de slide."
```

## Slide 5 · O QUE MUDA HOJE

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O que muda hoje. As últimas aulas foram teoria: SQL na segunda da semana 3, Python e
pandas em profundidade na segunda desta semana. Hoje é o oposto: quase a noite inteira
é vocês escrevendo e rodando código, a gente só acompanha.

O notebook de demonstração da Aula 7, com exemplo de NumPy, pandas, Matplotlib e
Seaborn, continua valendo como referência. Deixem ele aberto numa aba.

E uma mudança de escala: hoje o dado é grande de verdade, um milhão de transações, bem
diferente dos exemplos pequenos que couberam num slide."
```

## Slide 6 · COMO VAI FUNCIONAR

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Como vai funcionar, em quatro passos. Primeiro, abram o notebook que está fixado no
Discord: 20 perguntas, cada uma com uma célula de código vazia logo abaixo.

Segundo, a primeira parte do notebook carrega as mesmas 6 tabelas de sempre, agora com
1 milhão de transações.

Terceiro, respondam uma pergunta de cada vez: rodem a célula, confiram o resultado, e
só depois escrevam a resposta.

Quarto, colem a resposta no Google Forms, também fixado no Discord. É por ali que a
gente confere o desempenho de cada um."

──────────────────────────────────────────────────────────────
LEMBRETES
AÇÃO DO MODERADOR: fixar o link do notebook E o link do Forms no topo do chat exatamente neste slide.
```

## Slide 7 · O CONVITE

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"E aqui vai o convite de hoje. Essa base de 1 milhão de transações não é só grande por
ser grande. Tem alguma coisa estranha escondida nela, um padrão fora do comum, do
tamanho de um caso real de investigação.

Eu não vou contar o que é. É exatamente para isso que a análise exploratória serve:
começar largo, estranhar um número, e ir cavando até achar a explicação. Várias das 20
perguntas de hoje vão, sem avisar, ir te aproximando dessa resposta.

Quem achar algo estranho no meio do caminho, guarda a ideia. A gente conversa sobre
isso perto do fechamento."

──────────────────────────────────────────────────────────────
LEMBRETES
NÃO REVELE a resposta em nenhuma hipótese antes do fechamento. Consulte historia_anomalia.md com antecedência, é o gabarito da investigação.
```

## Slide 8 · REGRAS DE HOJE

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Últimas regras antes de soltar vocês.

75 minutos, sem pressa. Não precisa terminar as 20 perguntas para a noite valer a pena.

Travou em alguma pergunta? Escreve no chat com o número dela, a gente ou algum mentor
chega até você.

O notebook da Aula 7 é cola liberada, de propósito. Quase toda pergunta de hoje usa
alguma técnica que já apareceu lá.

E se terminar antes da hora, volte nas perguntas mais difíceis e tente explicar o
resultado com palavras, não só rodar o código. Isso conta tanto quanto a resposta
certa."
```

## Slide 9 · Agora é com vocês

```
⏱ 19h30 às 20h45 (75 min)  |  ESSENCIAL  |  Apresenta: os dois
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco principal da noite, sem slide de conteúdo novo. Este slide fica projetado na
sala principal durante toda a atividade.

CHECKLIST DA DUPLA DURANTE OS 75 MINUTOS:

Minuto 0 a 10:   conferir no chat quem já abriu o notebook e carregou os dados.
Minuto 10 a 55:  responder o chat em tempo real. Priorizar quem trava nas primeiras
                 perguntas, porque quem trava cedo tende a desistir.
Minuto 55 a 70:  mandar aviso geral, "faltam alguns minutos, aproveitem para revisar
                 as perguntas que pularam".
Minuto 70 a 75:  aviso de 5 minutos e reforçar que dá para continuar em casa depois.

SE ALGUÉM TRAVAR CARREGANDO 1 MILHÃO DE LINHAS:
Confirme se está rodando no Colab mesmo (não numa cópia local), e se o Drive terminou
de montar antes de rodar a célula de leitura. O arquivo é grande, o carregamento pode
levar alguns segundos a mais que o normal, isso é esperado.

SE ALGUÉM PERGUNTAR SE A RESPOSTA ESTÁ CERTA:
Não confirme nem negue. Peça para a pessoa explicar como chegou lá. Confirmar cedo
demais tira a graça de quem ainda está investigando.
```

## Slide 10 · MÃO NA MASSA

```
⏱ 0 min  |  ESSENCIAL  |  Apresenta: os dois
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Slide de apoio visual, fica projetado. Sem fala nova aqui, o que precisa ser dito já
foi dito no bloco anterior.
```

## Slide 11 · Encerramento

```
⏱ 20h45 às 21h00 (15 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  A revelação                4 min
  Recapitulação                3 min
  O que vem pela frente          3 min
  Q&A                              3 min
  Fechamento                        2 min

A revelação acontece em voz alta, puxando o fio a partir do chat: pergunte quem
estranhou algum número, deixe 2 ou 3 pessoas contarem o que acharam, e só então
confirme o padrão, seguindo docs/aula-08/dados/historia_anomalia.md. Não tem slide
para isso de propósito, é melhor ao vivo, olhando a reação da turma.
```

## Slide 12 · ENCERRAMENTO

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Cinco ideias para levar de hoje.

Análise exploratória começa largo, antes de focar. Vocês só chegaram onde chegaram
porque olharam o todo primeiro.

Um número fora da curva abre uma pergunta. A resposta só vem depois de investigar.

pandas, NumPy, Matplotlib e Seaborn se completam numa investigação real, cada um
entrou numa etapa diferente hoje.

Nem toda pergunta de negócio tem resposta fácil, e tudo bem, isso também é parte do
trabalho.

E a mais importante: o que vocês fizeram hoje foi trabalho de verdade de quem analisa
dado, o mesmo raciocínio de um caso real, aplicado dentro de um exercício de aula."
```

## Slide 13 · PRÓXIMOS ENCONTROS

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O que vem pela frente.

Segunda que vem, semana 5: engenharia de dados. Como construir os pipelines que
entregam dado limpo, no lugar certo. Ainda conceitual, como toda segunda.

E na quinta da semana 5, primeiro contato de verdade com pipeline, no mesmo formato de
hoje: demonstração curta, e o resto é prática."
```

## Slide 14 · ANTES DE IR

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar + Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

PERGUNTAS PREVISÍVEIS DE HOJE:

- "Não terminei as 20 perguntas, isso é um problema?"
  Não. O que importa é o esforço registrado no Forms até aqui. Dá para continuar em
  casa, o notebook e o Forms continuam abertos.

- "Como vocês descobriram esse padrão para colocar na aula?"
  Ele foi construído de propósito no gerador dos dados, para dar um objetivo real à
  análise. Mas o jeito de achar é o mesmo de um caso real.

- "Isso cai no projeto final?"
  Não direto, mas a mesma lógica de investigação serve para qualquer base que o grupo
  escolher no projeto.

- "Perdi a Aula 7, consigo acompanhar hoje?"
  Fica mais difícil. Recomendamos revisar o roteiro e o notebook da Aula 7 antes de
  continuar as perguntas de casa.
```

## Slide 15 · Obrigado!

```
⏱ 2 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. Vocês passaram por um caso pequeno, mas real, de como
uma investigação de dados de verdade acontece: começa largo, estranha um número, vai
fundo até achar a explicação.

O notebook e o Forms continuam abertos, terminem em casa se não deu tempo. Nos vemos
na segunda. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Exportar as respostas do Google Forms para uma planilha, e conferir contra
  gabarito_respostas em docs/aula-08 antes da próxima mentoria.
- Registrar quantas pessoas chegaram até a camada 3 da investigação sem ajuda, é um
  bom termômetro de quão bem a aula de segunda realmente fixou.
```
