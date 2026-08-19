# Roteiro do apresentador: Aula 4 (Semana 2, quinta-feira)

> Gerado automaticamente a partir das notas do deck.
> Não edite este arquivo à mão: edite `scripts/gerar_slides_aula04.py` e rode
> `python scripts/gerar_slides_aula04.py && python scripts/exportar_roteiro_aula04.py`.

**Como usar:** imprima ou deixe aberto num segundo monitor. O texto entre aspas é
fala sugerida. Adapte para a sua voz, não decore: o que importa é a sequência de ideias.

---

## Slide 1 · PROGRAMA DE TRAINEES EM DADOS E INTELIGÊNCIA ARTIFICIAL

```
⏱ 19h00 às 19h10 (slide de espera)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Slide projetado desde 18h55. Enquanto a sala enche, fale a cada 2 ou 3 minutos:
"Boa noite! Hoje é a segunda quinta-feira do programa, e tem uma novidade: código.
Enquanto a sala enche, se puder, já abra o Colab pelo link fixado no Discord."

Não comece antes de 19h08.

──────────────────────────────────────────────────────────────
LEMBRETES
- Microfones em mudo, câmeras opcionais.
- Confirme a GRAVAÇÃO antes de 19h10.
- CRÍTICO HOJE: confirme que o link do Colab está fixado no canal do Discord ANTES de 19h00.
- Confirme que a chave de acesso da API está distribuída ou embutida no notebook.
```

## Slide 2 · ENQUANTO TODO MUNDO ENTRA

```
⏱ 19h00 às 19h10  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Leia os itens uma vez, por volta de 19h05. O objetivo é baixar a ansiedade de quem
nunca programou.

Insista no item do notebook: quem só tem celular precisa saber agora, não às 19h30.
```

## Slide 3 · GenAI na prática

```
⏱ 19h10 às 19h30 (20 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco curto de propósito, focado em dar vocabulário suficiente para que ninguém fique
perdido quando o Felipe abrir o Colab.

ESTRUTURA:
  O que é uma API              6 min
  O endpoint                   6 min
  SDK                          6 min
  Transição para o Colab       2 min

Ritmo rápido, sem pausa para pergunta longa. As dúvidas técnicas aparecem melhor
depois, com o código na tela.
```

## Slide 4 · GENAI NA PRÁTICA

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Primeiro conceito: API. Sigla para interface de programação de aplicações, mas o nome
não ajuda muito. Pensem assim: API é um contrato de conversa entre dois programas. Você
manda um pedido num formato combinado, e recebe a resposta nesse mesmo formato.

Uma analogia que ajuda: pensem num balcão de atendimento. Vocês não entram na cozinha do
restaurante para pegar o prato. Entregam o pedido no balcão, e o balcão traz pronto.

O modelo de linguagem que vocês vão usar hoje mora num servidor de outra empresa. A API
é a porta de entrada desse servidor. E cada provedor define suas próprias regras: que
informação mandar, em que formato, e o que volta como resposta."
```

## Slide 5 · GENAI NA PRÁTICA

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Segundo conceito: endpoint. É o link exato dentro da API para onde vocês mandam o
pedido, geralmente um endereço que começa com https.

Junto do link vai uma chave de acesso, que identifica quem está fazendo o pedido e evita
uso indevido. Guardem essa chave como uma senha, ela não deve aparecer publicada em
nenhum lugar.

E vai o corpo do pedido: o texto que vocês querem que o modelo responda, dentro de um
pacote estruturado. A resposta chega nesse mesmo formato, e o código extrai só o texto
que interessa.

Endereço, chave e pergunta. É só isso que uma chamada de LLM carrega."

──────────────────────────────────────────────────────────────
LEMBRETES
Reforce em voz alta: a chave de acesso nunca vai num repositório público. É a primeira regra de segurança que eles levam.
```

## Slide 6 · GENAI NA PRÁTICA

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Terceiro conceito, e o último antes do código: SDK. É um pacote Python que já sabe
montar a chamada. Vocês não escrevem o endereço, a chave e o formato à mão toda vez.

Instala uma vez com pip install, e importa no código com um simples import. O que seria
um bloco inteiro de configuração vira uma função.

É o caminho que vocês vão usar hoje no Colab. Dá para chamar uma API sem SDK, na unha,
escrevendo o pedido inteiro à mão. Hoje vocês começam pelo caminho mais rápido, e quando
fizer sentido, a gente mostra o caminho manual também, mais para frente no programa.

Passo o Felipe agora. Ele vai abrir o Colab de verdade e mostrar cada um desses três
conceitos aparecendo na tela."
```

## Slide 7 · Agora é com vocês

```
⏱ 19h30 às 20h45 (75 min)  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco principal da noite. Estrutura:
  Como vai funcionar a próxima hora     5 min
  O roteiro do notebook                 5 min
  Mão na massa, individual             65 min

Hoje o trabalho muda de formato: cada um no próprio notebook, no próprio ritmo, diferente
do trabalho em grupo da quinta passada. Eu e o Edmar circulamos pelo chat.
```

## Slide 8 · ANTES DE COMEÇAR

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Vamos para a parte prática. Quatro avisos antes de começarmos.

Primeiro: o link do notebook já está fixado no Discord, no canal desta aula. Abram com a
mesma conta Google que vocês já usam para o Colab.

Segundo: hoje o trabalho é individual, diferente da quinta passada. Cada um no próprio
ritmo.

Terceiro: eu e o Edmar vamos estar direto no chat. Se travarem, escrevam o número da
célula onde travaram, isso acelera muito a nossa resposta.

Quarto, e esse é o mais importante: não tem pressa para terminar o notebook inteiro. O
objetivo de hoje é rodar a primeira chamada de verdade. Se você chegar só até ali, a
noite já cumpriu o que precisava cumprir."

──────────────────────────────────────────────────────────────
LEMBRETES
AÇÃO DO MODERADOR: fixar o link do Colab no topo do chat exatamente neste slide.
```

## Slide 9 · O ROTEIRO DO NOTEBOOK

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O notebook tem cinco partes, nessa ordem: instalar o SDK, guardar a chave de acesso,
fazer a primeira chamada, repetir com temperatura diferente, e anotar o que surpreendeu.

Ninguém vai escrever código do zero. Vocês editam o que já está lá, principalmente o
texto do prompt. É ali que entram os cinco elementos que o Edmar ensinou na segunda:
papel, tarefa, contexto, formato e restrição.

Guardem a última parte: anotar o que surpreendeu. A gente usa isso daqui a pouco, no
fechamento."
```

## Slide 10 · MÃO NA MASSA

```
⏱ 20h00 às 20h45 (65 min)  |  ESSENCIAL  |  Apresenta: os dois
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Este slide fica projetado na sala principal durante toda a atividade.

CHECKLIST DA DUPLA DURANTE OS 65 MINUTOS:

Minuto 0 a 10:  conferir no chat quem já instalou o SDK e quem travou no início.
Minuto 10 a 40: responder o chat em tempo real. Priorizar quem nunca programou antes.
Minuto 40 a 55: mandar aviso geral, "faltam 10 minutos, foco em rodar a primeira chamada".
Minuto 55 a 65: aviso de 5 minutos e reforçar que dá para continuar em casa depois.

SE ALGUÉM TRAVAR NA INSTALAÇÃO DO SDK:
Pergunte se está rodando no Colab mesmo, e não numa cópia local. É o erro mais comum.

SE ALGUÉM TERMINAR CEDO:
Peça para repetir a chamada mudando um dos cinco elementos do prompt, e comparar as duas
respostas lado a lado.
```

## Slide 11 · Encerramento

```
⏱ 20h45 às 21h00 (15 min)  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Ouvir o que surpreendeu   5 min  (pedir 3 ou 4 respostas direto no chat)
  Recapitulação             3 min
  O que vem na semana 3     3 min
  Q&A                       3 min
  Fechamento                1 min

Ao pedir relatos, puxe pelo chat: "quem quer colar aqui o que anotou como surpresa?"
Não force ninguém a abrir câmera ou microfone para isso.
```

## Slide 12 · O QUE A GENTE VIU HOJE

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Cinco ideias para levar de hoje.

A primeira: uma API é um contrato de conversa entre programas, e hoje vocês usaram um
pela primeira vez.

O endpoint carrega três coisas: endereço, chave de acesso e o texto do pedido.

Um SDK poupa o trabalho manual, e foi o caminho que vocês usaram no Colab.

Prompt bem montado muda a resposta. Os cinco elementos que o Edmar ensinou na segunda
apareceram na prática hoje, dentro do código de vocês.

E fecha com a temperatura: baixa repete, alta arrisca. Vocês viram isso ao vivo, não só
ouviram a explicação."
```

## Slide 13 · PRÓXIMOS ENCONTROS

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O que vem pela frente.

Segunda que vem, semana 3: a linguagem que fala direto com banco de dados. Como
transformar uma pergunta de negócio numa consulta. Ainda conceitual, como toda segunda.

E na quinta da semana 3, primeiro contato de verdade com ela, consultando dados reais.
Mesmo formato de hoje: a gente demonstra, e depois vocês fazem."
```

## Slide 14 · ANTES DE IR

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves + Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

PERGUNTAS PREVISÍVEIS DE HOJE:

- "Preciso saber programar para acompanhar?"
  Não. Hoje vocês só editaram o que já estava pronto no notebook.

- "A API que usamos hoje é a mesma que vou usar depois no programa?"
  Ainda não é definitivo. A confirmação sai no Discord antes da próxima aula com código.

- "Posso continuar meu notebook em casa?"
  Sim. Ele fica salvo na sua conta Google, e dá para reabrir quando quiser.

- "Isso vale nota?"
  Não hoje. É treino.

- "Perdi a aula de segunda, consigo acompanhar os cinco elementos de prompt?"
  Sim. A gravação e o material de apoio da Aula 3 estão no Discord.
```

## Slide 15 · Obrigado!

```
⏱ 1 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. Foi a primeira vez que a maioria de vocês rodou uma linha
de código, e boa parte também foi a primeira chamada de LLM da vida. Isso fica.

O notebook continua salvo na sua conta Google, entrem quando quiserem revisitar.

Nos vemos na segunda. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Recolher no chat quantas pessoas relataram travar na instalação do SDK, para calibrar
  o próximo notebook.
- 10 minutos de retrospectiva entre os dois: quantas pessoas nunca tinham programado
  antes, e como reagiram.
```
