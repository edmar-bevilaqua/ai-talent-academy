# Roteiro do apresentador: Aula 3 (Semana 2, segunda-feira)

> Gerado automaticamente a partir das notas do deck.
> Não edite este arquivo à mão: edite `scripts/gerar_slides_aula03.py` e rode
> `python scripts/gerar_slides_aula03.py && python scripts/exportar_roteiro_aula03.py`.

**Como usar:** imprima ou deixe aberto num segundo monitor. O texto entre aspas é
fala sugerida. Adapte para a sua voz, não decore: o que importa é a sequência de ideias.

---

## Slide 1 · PROGRAMA DE TRAINEES EM DADOS E INTELIGÊNCIA ARTIFICIAL

```
⏱ 19h00 às 19h10 (slide de espera)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Slide projetado desde 18h55. Fale a cada 2 ou 3 minutos enquanto a sala enche.

"Boa noite! Segunda aula da semana 2, e hoje a noite inteira é sobre IA generativa.
Enquanto todo mundo entra, escreve no chat: qual foi a última coisa que você pediu para
uma IA fazer? Pode ser qualquer coisa."

Não comece antes de 19h08.

──────────────────────────────────────────────────────────────
LEMBRETES
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- Moderador com o link do Discord pronto para colar.
- Guardar 3 ou 4 respostas boas do chat: elas viram exemplo no bloco 1.
```

## Slide 2 · ENQUANTO TODO MUNDO ENTRA

```
⏱ 19h00 às 19h10  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Leia os itens uma vez, por volta de 19h05, e insista no último. As respostas do chat
servem de material vivo para o bloco 1: quando você mostrar as seis tarefas que a GenAI
faz bem, dá para apontar quais delas apareceram no chat.
```

## Slide 3 · Por que uma noite inteira sobre isso

```
⏱ 19h10 às 19h20 (10 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco curto de contextualização. O objetivo é situar a turma no programa e justificar a
noite inteira num tema só. Ritmo rápido, 3 slides.
```

## Slide 4 · ONDE ESTAMOS

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Antes de começar, vamos situar onde vocês estão.

Na semana 1 a gente fez o panorama: o que é IA, o ciclo de vida de uma solução, e na
quinta vocês preencheram o Canvas do Problema em grupo.

Hoje começa a parte em que cada semana pega uma ferramenta e vai fundo. E a gente começou
por IA generativa de propósito, e eu explico o motivo no próximo slide.

Repara na sequência: SQL na semana 3, Python na 4, engenharia de dados na 5, machine
learning na 6, agentes na 7. Faz sentido nessa ordem, porque você precisa saber consultar
e limpar dado antes de modelar. E agentes vem no fim porque agente é a IA generativa de
hoje com ferramentas na mão."

──────────────────────────────────────────────────────────────
LEMBRETES
Este cronograma foi ajustado com as lideranças e difere da proposta original. Se alguém perguntar, é decisão combinada.
```

## Slide 5 · POR QUE AGORA

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Por que uma noite inteira sobre IA generativa, se o programa tem oito semanas?

Primeira razão: é a porta de entrada mais acessível dessa área inteira. Para trabalhar com
machine learning você precisa de estatística, de Python, de dado limpo. Para trabalhar com
IA generativa você precisa entender o problema e saber pedir bem. A barreira técnica é
mais baixa, e isso é uma oportunidade real para quem está começando agora.

Segunda: é onde estão as vagas mais novas. Lembram do slide de carreiras da semana 1?
AI Engineer praticamente não existia quatro anos atrás.

Terceira, e essa é a que quase ninguém fala: é também onde estão os piores projetos. Tem
muita empresa gastando dinheiro usando IA generativa em problema que uma consulta de banco
resolveria melhor. E o pior é que falha em silêncio, porque a resposta sempre parece boa.

E a quarta: na semana 1 a gente abriu a caixa preta por noventa segundos e eu prometi que
a gente voltaria. Hoje a gente volta com calma."
```

## Slide 6 · O PLANO DA NOITE

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"A noite tem quatro blocos.

O primeiro é IA generativa na prática: o que ela faz de verdade hoje, com aplicações
concretas de trabalho.

O segundo abre a caixa preta: token, embedding e atenção. Sem fórmula, sem código. E eu
garanto que depois desse bloco o comportamento estranho dele para de ser mistério.

Aí a gente faz o intervalo, e o Felipe assume.

O terceiro bloco é sobre prompt e contexto: como escrever um pedido que funciona, quais
técnicas funcionam, e quais são folclore de internet.

E o quarto fecha com a parte que mais pesa na carreira de vocês: onde a GenAI resolve e
onde ela atrapalha. Esse é o bloco que economiza dinheiro de empresa."
```

## Slide 7 · IA Generativa na prática

```
⏱ 19h20 às 19h55 (35 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco de motivação e repertório. A meta é sair daqui com a turma sabendo nomear as tarefas
que a GenAI faz bem, com exemplo de trabalho para cada uma.

ESTRUTURA:
  As quatro famílias                    4 min
  Os seis verbos                        8 min
  Tabela de aplicações reais            8 min
  Caso aprofundado: triagem             6 min
  O que mudou de verdade                4 min
  Interação                             3 min

Controle: às 19h40 você precisa estar na tabela de aplicações.
```

## Slide 8 · TRÊS ANOS

```
⏱ 2 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Vamos começar com uma constatação.

Em três anos, a IA generativa saiu de curiosidade de laboratório para ferramenta de
trabalho diária. Isso é rápido demais. Nenhuma tecnologia recente entrou tão rápido na
rotina de tanta gente.

E aí vem a segunda parte, que é a que interessa para vocês: a maior parte das empresas
ainda usa ela como brinquedo caro. Assinam a licença, mandam todo mundo usar, e ninguém
mede se melhorou alguma coisa.

A diferença entre brincar e trabalhar com isso está em saber exatamente que tarefa você
está entregando para ela. É disso que trata este bloco."
```

## Slide 9 · O TERRITÓRIO

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"IA generativa não é uma coisa só. São quatro famílias, e elas amadureceram em ritmos
diferentes.

Texto é a mais madura: escreve, resume, classifica, traduz, extrai informação de
documento. É a que mais aparece em trabalho de escritório.

Imagem gera e edita a partir de descrição. Marketing e design usam bastante.

Áudio e voz transcreve reunião, gera narração, e hoje já clona timbre de voz. A parte de
transcrição já está boa o suficiente para uso profissional de verdade.

E código: sugere trecho, explica erro, escreve teste. É onde o ganho de produtividade é
mais fácil de medir, porque dá para contar quantas linhas foram aceitas.

Hoje a gente foca em texto, porque é a família que mais encosta no trabalho de dados."
```

## Slide 10 · O QUE ELA FAZ BEM

```
⏱ 8 min  |  ESSENCIAL, slide-âncora do bloco  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Este é o slide mais prático do bloco. Vá com calma, e conecte com o que apareceu no chat
na abertura.

"Estes seis verbos cobrem quase tudo que a IA generativa faz bem em trabalho de verdade.
Eu recomendo que vocês anotem.

RESUMIR: pegar texto longo e reduzir mantendo o que importa. Ata de reunião, aquela thread
de e-mail com quarenta respostas, relatório de quarenta páginas.

CLASSIFICAR: ler um texto e dizer em que categoria ele cai. Qual o motivo daquele chamado
de suporte, se a avaliação do cliente é positiva ou negativa, que tipo de documento é
aquele. Isso aqui é ouro em operação, e volta no próximo slide.

EXTRAIR: tirar campo estruturado de texto bagunçado. Você tem mil notas fiscais em PDF e
quer valor, data e fornecedor numa tabela. Antes isso exigia um sistema por tipo de
documento.

TRANSFORMAR: reescrever mudando formato, tom ou público. Pegar um texto técnico e virar
linguagem de negócio para a diretoria.

GERAR: produzir a primeira versão. Rascunho de e-mail, descrição de produto.

CONVERSAR: responder pergunta em linguagem natural, com contexto. É a busca interna da
empresa, o assistente de suporte.

E a linha de baixo é a régua que eu quero deixar com vocês: se a sua tarefa não cabe em um
desses seis verbos, desconfie antes de escolher IA generativa. Provavelmente o problema
pede outro degrau da escada."

──────────────────────────────────────────────────────────────
LEMBRETES
Se guardou respostas do chat na abertura, aponte quais verbos apareceram: cria conexão imediata.
```

## Slide 11 · APLICAÇÃO REAL

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Agora, onde isso vira trabalho de verdade. Seis aplicações que vocês vão encontrar em
qualquer empresa que esteja levando isso a sério.

Triagem de chamados: o modelo lê o texto do chamado e classifica motivo e urgência. O
cuidado é que classe errada manda o cliente para a fila errada, e ele espera mais.

Extração de documento: tira campo de contrato, nota, laudo. Cuidado com documento de valor
legal, que exige conferência humana antes de virar decisão.

Resumo de reunião: transcreve e devolve tópicos e ações. E aqui um detalhe que vocês vão
encontrar na prática: nome próprio e número são exatamente onde ele mais erra. Ele troca
nome parecido e erra valor. Confira sempre essas duas coisas.

Copiloto de código: sugere trecho, explica erro, escreve teste. O cuidado é cultural:
código sugerido por IA passa na revisão como qualquer outro código. Não entra direto.

Busca interna: responde pergunta com base nos documentos da empresa. E o cuidado aqui
define se o projeto vive ou morre: sem mostrar a fonte junto com a resposta, ninguém
confia. A gente volta nisso no bloco do Felipe.

Primeira versão de texto: rascunho. E rascunho é ponto de partida. Alguém assina no final,
e essa pessoa é responsável pelo que está escrito.

Repara numa coisa: toda linha tem um cuidado. Nenhuma dessas aplicações roda sozinha."
```

## Slide 12 · CASO APROFUNDADO

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Vamos aprofundar uma dessas, porque ela mostra bem como o ganho aparece.

Triagem de chamados, antes. O chamado chega em texto livre, escrito pelo cliente do jeito
que ele conseguiu explicar. Um atendente lê e escolhe a categoria na mão. E aí começa o
problema: cada pessoa classifica com critério próprio. O que para um é 'problema técnico',
para outro é 'dúvida de uso'. A fila cresce mais rápido do que a triagem anda. E no fim do
mês o relatório de motivos sai errado, porque a categoria nunca foi consistente.

Depois. O modelo lê o texto e sugere motivo e urgência. O atendente confirma ou corrige,
em vez de escolher do zero. Repara que o critério agora fica igual para todo mundo, porque
é o mesmo prompt rodando em todos os chamados. A fila anda mais rápido e o caso urgente
sobe na hora. E as correções que o atendente faz viram material para melhorar o prompt.

E aqui está a leitura que eu quero que vocês levem, que está na linha de baixo: o ganho
não foi tirar o humano do processo. Foi trocar a tarefa dele. Ele parou de escolher do
zero e passou a conferir. Conferir é muito mais rápido do que decidir."
```

## Slide 13 · O QUE MUDOU DE VERDADE

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Se vocês forem levar uma frase deste bloco, que seja esta.

A IA generativa não baixou o custo de pensar. Ela baixou o custo da PRIMEIRA VERSÃO.

Pensa no que isso significa na prática. Antes, escrever o primeiro rascunho de qualquer
coisa custava caro em tempo e em energia mental. A folha em branco trava. Hoje o rascunho
sai em segundos.

Mas decidir se aquele rascunho está certo, se faz sentido para o seu contexto, se o número
ali confere: isso continua custando exatamente o mesmo que custava antes. Ninguém terceirizou
essa parte.

Quem entende isso usa a ferramenta como rascunho e revisa. Quem não entende usa como
resposta final, e é assim que aparece petição com jurisprudência inventada. Lembram do caso
de Londrina, da semana 1?"
```

## Slide 14 · INTERAÇÃO

```
⏱ 3 min  |  DESCARTÁVEL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Antes de a gente abrir a caixa preta, uma pergunta rápida. Dos seis verbos, qual você
usaria hoje, no seu trabalho ou no seu estudo?"

[aguarde 30 a 45 segundos e comente o resultado]

Comente o vencedor. Se "resumir" ou "gerar" ganharem, é o padrão esperado, e vale dizer
que classificar e extrair costumam gerar mais valor em operação, mesmo sendo menos
lembrados.

Feche com o gancho: "Guardem a resposta de vocês. No último bloco a gente vai testar se
ela sobrevive à pergunta de quando NÃO usar."

──────────────────────────────────────────────────────────────
LEMBRETES
Enquete nativa da plataforma. Ver o plano de interação da aula 1 para a configuração.
```

## Slide 15 · Como um LLM funciona por dentro

```
⏱ 19h55 às 20h30 (35 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco mais técnico da noite. A meta é que a turma saia entendendo o mecanismo bem o
suficiente para explicar por que ele alucina, por que ele esquece e por que ele responde
diferente para a mesma pergunta.

REGRA DESTE BLOCO: nenhuma fórmula, nenhuma matriz, nenhum código. Só analogia concreta.
Se você sentir vontade de escrever "vetor de 768 dimensões" na lousa, respire.

ESTRUTURA:
  Recap da semana 1                     3 min
  Token                                 4 min
  Embedding                             8 min
  Atenção                               8 min
  Como o texto sai                      4 min
  Temperatura e treino                  5 min
  Agora a alucinação faz sentido        3 min
```

## Slide 16 · DE ONDE A GENTE PAROU

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Rápido, para quem faltou na semana 1 e para refrescar a memória de quem estava aqui.

A gente viu que o modelo quebra o texto em pedaços chamados tokens, e que a única coisa
que ele aprendeu a fazer é prever qual é o próximo token mais provável. Uma coisa só,
repetida milhões de vezes.

E a consequência disso: não existe um banco de respostas dentro dele. Ele COMPÕE a
resposta na hora, em vez de consultar. Por isso ele às vezes inventa com uma confiança
absoluta.

Isso foi o que a gente falou em noventa segundos, na semana passada. Hoje a gente abre
cada uma dessas caixas: o que é um token de verdade, o que ele faz com esse token, e como
ele decide qual vem depois."
```

## Slide 17 · PEÇA 1 DE 3 · TOKEN

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Peça número um: token.

O modelo não lê letra, e não lê palavra inteira. Ele lê pedaços de palavra. Esses pedaços
se chamam token.

Em português, uma palavra costuma virar dois ou três tokens. Uma palavra muito comum, tipo
'casa', vira um token só. Uma palavra rara ou técnica vira vários pedaços.

Cada token vira um número de identificação, e é com esse número que a máquina trabalha
daqui para a frente. O texto some, ficam os números.

E agora a parte que importa no bolso de vocês: preço de API e tamanho da janela de contexto
são contados em TOKEN, não em palavra. Quando alguém disser que um modelo aceita duzentos
mil tokens, isso equivale a bem menos que duzentas mil palavras.

E tem um detalhe que afeta a gente diretamente: português gasta mais token que inglês. O
mesmo texto traduzido pode custar uns trinta por cento a mais. Quem for construir produto
com isso precisa saber."
```

## Slide 18 · PEÇA 2 DE 3 · EMBEDDING

```
⏱ 8 min  |  ESSENCIAL, conceito mais difícil da noite  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Vá devagar. Use a analogia da cor até a turma acompanhar, e só depois pule para palavra.

"Peça número dois, e essa é a mais difícil da noite. Embedding.

Vamos começar com cor, que todo mundo entende. Toda cor na tela do computador vira três
números: quanto de vermelho, quanto de verde, quanto de azul. Vermelho puro é 255, 0, 0.
Isso é a coordenada daquela cor.

E repara numa coisa: cores parecidas têm números parecidos. Vermelho e vinho ficam perto
nesse mapa de três dimensões. Vermelho e azul ficam longe. A distância entre os números
representa a semelhança entre as cores.

Palavra funciona exatamente igual, com uma diferença: em vez de três números, são
centenas. Cada palavra vira uma coordenada num mapa de centenas de dimensões. Ninguém
consegue desenhar isso, e tudo bem, porque a ideia é a mesma.

E o que acontece nesse mapa é bonito: palavras de sentido próximo caem perto. 'Demitir',
'desligar' e 'rescindir' viram vizinhas, mesmo sem ter uma letra em comum.

Agora, por que isso importa para vocês na prática. Isso permite buscar por SIGNIFICADO, e
não por letra. Você procura por 'demissão' e o sistema acha um documento que só usa a
palavra 'desligamento'. Busca tradicional nunca acharia.

E é exatamente isso que faz a busca interna da empresa funcionar. O Felipe vai voltar
nisso depois do intervalo, quando falar de RAG."

──────────────────────────────────────────────────────────────
LEMBRETES
Se alguém perguntar de "rei menos homem mais mulher igual rainha": é real, é o exemplo clássico, mas só use se sobrar tempo.
```

## Slide 19 · PEÇA 3 DE 3 · ATENÇÃO

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Este é o slide que faz a turma entender por que o Transformer mudou tudo. Leia as duas
frases em voz alta, com pausa, e deixe a sala resolver sozinha.

"Peça número três: atenção. E eu vou explicar com um exemplo, porque é mais fácil sentir
do que definir.

Leiam comigo: 'o prefeito negou a licença aos manifestantes'. Agora eu vou completar de
dois jeitos.

Primeiro: 'porque ELE temia violência'. Quem é 'ele'? [pausa] O prefeito.

Segundo: 'porque ELES pregavam violência'. Quem são 'eles'? [pausa] Os manifestantes.

Uma letra. Uma letra muda o dono da frase inteira. E vocês resolveram isso agora, sem
esforço nenhum, provavelmente sem perceber que resolveram.

Como vocês fizeram? Vocês olharam a frase inteira de uma vez. Não leram palavra por
palavra em ordem, decorando o que veio antes. Vocês pesaram: 'temia' combina com quem
tinha medo, 'pregavam' combina com quem estava protestando.

Atenção é o mecanismo que faz o modelo fazer exatamente isso. Para cada palavra que ele
vai gerar, ele calcula o quanto cada outra palavra do texto importa naquele momento.

E a linha de baixo é o marco histórico: antes de 2017, os modelos liam em ordem, uma
palavra de cada vez, e esqueciam o começo de textos longos. A arquitetura Transformer
trouxe a atenção, que olha tudo junto. É isso que está por trás de toda IA generativa que
vocês usam hoje."
```

## Slide 20 · JUNTANDO AS TRÊS PEÇAS

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Agora juntando as três peças. O que acontece quando você digita uma pergunta e aperta
enter.

Entra o texto: a sua pergunta, mais tudo que já foi dito naquela conversa.

Esse texto vira token, cada pedaço com seu número.

Cada token vira coordenada no mapa de significados, o embedding.

A atenção entra e pesa: para cada posição, o que importa no contexto.

E aí sai uma coisa que quase ninguém sabe: não sai um token. Sai uma LISTA de
probabilidades. A chance de cada token possível ser o próximo. Tipo: 'aprovado' com
quarenta por cento, 'negado' com trinta, 'pendente' com dez, e assim por diante.

Aí um token é escolhido dessa lista, e o processo inteiro recomeça, agora com esse token
fazendo parte do texto.

Olha o passo seis de novo. Ele refaz tudo isso a cada palavra que escreve. Uma resposta de
duzentas palavras passou por esse ciclo umas trezentas vezes."
```

## Slide 21 · A ESCOLHA

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Do passo cinco sai aquela lista de candidatos com probabilidade. Alguém precisa escolher
um. E existe um botão que controla como essa escolha acontece: temperatura.

Temperatura baixa, perto de zero: ele escolhe sempre o candidato mais provável. Resposta
previsível, repetível, sem graça.

Temperatura alta: ele dá chance aos candidatos menos prováveis. Texto mais variado, mais
surpreendente, e às vezes mais errado.

Por isso consistência e criatividade brigam. Você escolhe uma e paga na outra. Não tem
configuração mágica que dê as duas.

Na prática: se você está extraindo campo de documento ou classificando chamado, use
temperatura baixa. Você quer a mesma resposta toda vez, porque é operação. Se você está
gerando ideia de campanha ou rascunho de texto, temperatura alta ajuda.

E quando alguém reclamar que 'a IA respondeu diferente da última vez', quase sempre é
isto aqui."
```

## Slide 22 · COMO ELE FICOU ASSIM

```
⏱ 3 min  |  DESCARTÁVEL se atrasado  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Rápido, porque ajuda a entender diferença entre modelos.

Fase um, pré-treino: ele leu texto numa escala absurda e aprendeu a completar frase. No fim
dessa fase ele sabe muito e não sabe conversar. Se você perguntasse alguma coisa, ele podia
responder com outra pergunta parecida, porque na internet pergunta costuma vir seguida de
pergunta.

Fase dois, ajuste por instrução: ele aprendeu que, quando recebe um pedido, deve atender o
pedido. É aqui que ele para de completar texto e passa a responder.

Fase três, alinhamento: pessoas compararam respostas e disseram qual preferiam. É o que
deixa ele educado, prestativo, e recusando pedido perigoso.

E a linha de baixo explica uma coisa prática: a fase três é a que mais muda entre um modelo
e outro. Quando vocês sentem que um modelo tem 'personalidade' diferente do outro, ou é
mais formal, ou recusa mais, é daí que vem."
```

## Slide 23 · O LIMITE FÍSICO

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Última peça antes de fechar o bloco: janela de contexto.

Imaginem uma mesa de trabalho onde cabe uma quantidade fixa de papel. Tudo que está em
cima da mesa, ele enxerga. O que não está, para ele não existe.

E o que disputa espaço nessa mesa? A sua pergunta, o histórico inteiro da conversa, e
qualquer arquivo que você colou. Tudo junto.

Quando a mesa enche, o começo cai. E ele nunca mais vê aquilo. Por isso, numa conversa
longa, ele esquece o que vocês combinaram no início. E por isso repetir a informação
resolve o problema: você está colocando aquele papel de volta na mesa.

Duas consequências práticas. Mesa cheia custa mais caro e responde mais devagar, porque
você paga por token de entrada também, não só pela resposta. E informação enfiada no meio
de um texto muito longo tende a se perder: coloque o que importa no começo ou no fim.

E o mais importante, que está embaixo: ele não tem memória entre conversas. Cada conversa
nova começa com a mesa vazia. Quando um produto parece lembrar de você, é porque alguém
programou para recolocar aquilo na mesa toda vez."
```

## Slide 24 · AGORA DÁ PARA EXPLICAR

```
⏱ 3 min  |  ESSENCIAL, fechamento do bloco  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Fechamento do bloco. Amarre com o caso da semana 1.

"Agora, com as três peças na mão, dá para explicar direito uma coisa que na semana passada
eu pedi para vocês aceitarem: a alucinação.

Ele escolhe o token mais provável, dada a sequência anterior. Só isso. E 'provável' e
'verdadeiro' são coisas diferentes.

Lembram do advogado de Londrina, que apresentou petição com número de processo inventado?
Agora vocês conseguem explicar tecnicamente o que aconteceu. Um número de processo tem uma
FORMA muito previsível: tantos dígitos, ponto, traço, ano, tribunal. Para o modelo, gerar
uma sequência com essa forma é altamente provável. Ele não tem nenhum mecanismo interno
que consulte se aquele processo existe. Ele não sabe que existe uma diferença entre gerar
a forma certa e gerar o fato certo.

Então a alucinação é o mecanismo funcionando exatamente como foi construído. Nenhuma
versão futura vai consertar isso, porque não existe o que consertar.

O que muda, e o Felipe vai mostrar depois do intervalo, é COMO a gente trabalha em volta
disso."
```

## Slide 25 · INTERVALO

```
⏱ 20h30 às 20h45 (15 min)  |  ESSENCIAL  |  Apresenta: os dois
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DURANTE O INTERVALO:
- Deixe o slide na tela com o horário de retorno visível.
- Moderador posta o link do Discord e recolhe as dúvidas do bloco técnico.
- Alinhem em 2 minutos: o bloco 2 atrasou? O Felipe corta o quê?
- Confirme que a gravação continua rodando.

VOLTA: comece 20h45 em ponto, mesmo com gente faltando.
```

## Slide 26 · Prompt, contexto e limites

```
⏱ 20h45 às 21h36 (51 min)  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

ABERTURA DO SEU BLOCO (retomada pós-intervalo, ~1 min):

"Bem-vindos de volta. O Edmar mostrou o que a IA generativa faz e como ela funciona por
dentro. Agora eu vou mostrar como conversar com ela de um jeito que produza trabalho útil.

Um aviso rápido de agenda: este bloco cresceu, porque vamos incluir dois assuntos a mais,
banco vetorial e fine-tuning. Isso significa que hoje vamos até uns dez minutos depois das
22h. Se alguém precisar sair no horário exato, sem problema, o conteúdo inteiro fica
gravado.

E eu vou começar com uma provocação: a maior parte das reclamações de que 'a IA respondeu
mal' nasce de um pedido mal escrito."

ESTRUTURA:
  Prompt como especificação             4 min
  Os cinco elementos                    6 min
  Três antes e depois                  12 min
  Três técnicas que funcionam           8 min
  O que é folclore                      5 min
  RAG (o pipeline)                      5 min
  Banco vetorial                        6 min
  RAG × fine-tuning                     5 min

Este bloco cresceu 11 minutos em relação ao desenho original, com a entrada de banco
vetorial e fine-tuning. A decisão foi esticar a aula em vez de cortar conteúdo já
existente: a noite agora fecha por volta de 22h11, não 22h00. Avisar a turma disso
explicitamente no início do bloco, para ninguém ficar surpreso perto do fim.
```

## Slide 27 · A PROVOCAÇÃO DE ABERTURA

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Vou começar com uma provocação.

Prompt é especificação de trabalho. E especificação vaga produz entrega vaga.

Pensa numa situação que vocês já viveram. Você pede para alguém 'dar uma olhada naquele
relatório'. A pessoa volta com uma coisa completamente diferente do que você esperava. De
quem é a culpa?

É do pedido. Você não disse o que era 'dar uma olhada', não disse o que te preocupava, não
disse em que formato queria a resposta, e não disse quando.

Com modelo de linguagem é igual, com um agravante: ele nunca vai te perguntar 'o que
exatamente você quer dizer com isso?'. Ele vai chutar o que você quis dizer, com
confiança, e entregar.

Então a habilidade que vocês vão treinar neste bloco chama-se escrever especificação. E
ela serve para a carreira inteira de vocês, mesmo sem IA nenhuma envolvida."
```

## Slide 28 · A ANATOMIA

```
⏱ 6 min  |  ESSENCIAL, slide-âncora do bloco  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Este é o slide de referência do bloco. Vale pedir para fotografarem.

"Cinco elementos. Não precisa dos cinco toda vez, mas todo prompt ruim está sem pelo menos
três deles.

PAPEL: quem o modelo deve ser ao responder. 'Você é um analista de dados explicando para
um gerente comercial.' Isso muda vocabulário e profundidade de uma vez só.

TAREFA: o verbo, e específico. Lembram dos seis verbos do bloco do Edmar? Use um deles.
'Classifique cada chamado abaixo' funciona muito melhor que 'analise esses chamados',
porque 'analisar' não diz o que fazer.

CONTEXTO: o material que ele precisa ter em mãos. O texto da política, os dados, o
histórico. Cola junto. Ele não sabe nada da sua empresa.

FORMATO: como você quer receber. 'Uma linha de tabela por item, com estas três colunas.'
Sem isso, você recebe três parágrafos de texto corrido e tem que reformatar na mão.

RESTRIÇÃO: tamanho, tom, o que evitar, e principalmente o que fazer na dúvida. Aquele
último pedaço é o que mais gente esquece: 'se faltar informação, escreva NÃO SEI'. Sem
isso, ele preenche o buraco com invenção.

Vale fotografar este slide."
```

## Slide 29 · ANTES E DEPOIS · 1

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Primeiro par. Especificidade.

À esquerda: 'escreva sobre nosso produto'. O que volta? Um texto genérico que serviria para
qualquer empresa de qualquer setor. Você lê e pensa 'está ok, mas não é isso'. E aí você
fica reescrevendo na mão, e perdeu o ganho todo.

À direita, repara no que foi decidido antes de pedir: quantos parágrafos, qual produto,
para QUEM (dono de pequeno supermercado, não 'clientes'), qual o ponto principal (perda por
vencimento), qual o tom, e qual o tamanho.

E olha a linha de baixo, que é a lição: o que separa os dois é quantas decisões você tomou
antes de pedir. Se você não sabe para quem está escrevendo, o modelo também não vai saber."
```

## Slide 30 · ANTES E DEPOIS · 2

```
⏱ 4 min  |  ESSENCIAL, o par mais importante  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Este é o par mais importante do bloco. Insista nele.

"Segundo par. Contexto. E este é o mais importante dos três.

À esquerda, alguém pergunta sobre a política de férias da empresa. Sem colar a política. O
que acontece? Ele responde com base no que leu na internet sobre políticas de férias em
geral. Pode até acertar por sorte, porque muita empresa segue a CLT. Ou pode inventar com
convicção total, e a pessoa acredita porque a resposta é fluente.

À direita, a política vai colada. E tem três coisas ali que valem ouro.

Primeiro, o texto vem antes da pergunta.

Segundo: 'com base APENAS no texto acima'. Isso restringe a fonte.

Terceiro, e esse é o que mais salva: 'se o texto não disser, responda NÃO CONSTA'. Você deu
para ele uma saída honesta. Sem essa linha, o modelo tende a preencher o buraco, porque a
tarefa dele é produzir texto plausível.

Guardem esse padrão. Ele resolve boa parte dos problemas de alucinação em uso corporativo."
```

## Slide 31 · ANTES E DEPOIS · 3

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Terceiro par. Formato.

À esquerda: 'analise esses cinquenta chamados e me diga o que você achou'. Volta um texto
corrido de quatro parágrafos, bem escrito e completamente inútil para trabalho. Não dá para
colocar em planilha, não dá para contar, não dá para comparar com o mês passado.

À direita, três decisões: qual a estrutura de cada linha, quais são as categorias
possíveis, e o que fazer com o resto. Repara que as categorias foram FECHADAS: acesso,
cobrança, técnico, outro. Sem isso, ele inventa uma categoria nova para cada chamado, e
você fica com cinquenta categorias diferentes.

E aquela última linha, 'não escreva nada fora da tabela', evita que ele mande um parágrafo
educado de introdução antes dos dados, que quebra qualquer processamento automático.

A lição está embaixo: formato definido transforma texto em dado. E dado você consegue
contar."
```

## Slide 32 · O QUE FUNCIONA

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Três técnicas que valem o esforço de aprender.

DAR EXEMPLOS. Em vez de descrever o formato que você quer em três parágrafos, mostre dois
ou três exemplos com entrada e saída. Isso funciona muito bem porque o modelo é bom em
reconhecer padrão. Use quando o formato é difícil de descrever mas fácil de mostrar. Tem
nome técnico, few-shot, mas o que importa é a ideia.

PEDIR O RACIOCÍNIO. 'Explique seu raciocínio antes de dar a resposta final.' Isso melhora
resultado em tarefa que tem etapas, comparação ou conta. Mas custa mais token e demora
mais, então não use em tarefa simples. Se você só quer classificar um chamado, pedir
raciocínio é desperdício.

DEFINIR PAPEL E PÚBLICO. 'Você é um auditor explicando para alguém sem formação técnica.'
Isso muda vocabulário e profundidade de uma vez só. É muito mais barato que gerar o texto
técnico e depois pedir para simplificar."
```

## Slide 33 · O QUE É FOLCLORE

```
⏱ 5 min  |  ESSENCIAL, bom momento de leveza  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Este slide costuma render riso e engajamento. Aproveite.

"Agora a parte divertida: o que circula por aí e não se sustenta.

Dizer 'por favor' e 'obrigado'. Não existe efeito confiável na qualidade da resposta. Se
você faz por educação ou por hábito, tudo bem, mas não é técnica de prompt.

Prometer gorjeta ou ameaçar o modelo. Isso virou meme na internet. Não é técnica.

Escrever tudo em caixa alta para enfatizar. Gasta mais token, porque caixa alta costuma
quebrar em mais pedaços, e não obriga nada.

Repetir a mesma instrução três vezes. Instrução repetida não vira instrução mais forte.

Prompt gigante é sempre melhor. Esse é o mais perigoso dos cinco, porque parece razoável.
Prompt longo com instrução contraditória no meio piora o resultado. Se você escreveu 'seja
conciso' no começo e 'explique detalhadamente' no fim, ele vai obedecer um dos dois e você
não controla qual.

E o último, que é o mais útil: dizer só o que NÃO fazer funciona pior do que dizer o que
fazer. 'Não use jargão técnico' é pior que 'escreva como se fosse para um leigo'. Diga o
alvo, e não o que evitar.

A régua está embaixo: na dúvida entre duas técnicas, prefira a que você consegue explicar
por que funciona."
```

## Slide 34 · QUANDO O CONTEXTO VEM DE FORA

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Último tema do meu bloco, e ele conecta direto com o embedding que o Edmar explicou.

Vocês já entenderam que o modelo não sabe nada da sua empresa, e que tudo que ele sabe do
seu caso, você colou. Mas você não vai colar dez mil documentos a cada pergunta. Não cabe
na mesa, e custaria caro demais.

A solução tem nome: RAG. E funciona em quatro passos.

A pergunta chega. O sistema busca, nos documentos da empresa, os trechos mais próximos em
significado. E repara: em significado, não em palavra exata. É o mapa de coordenadas do
bloco anterior trabalhando. Alguém pergunta sobre 'demissão' e o sistema acha o documento
que fala em 'desligamento'.

Os trechos encontrados são colados no prompt junto com a pergunta. E o modelo responde com
base no que foi colado, citando de onde tirou.

Duas consequências que vocês precisam levar. Primeira: com RAG, a resposta vem com fonte, e
fonte é o que faz o usuário confiar. Segunda: se a busca do passo dois trouxer o trecho
errado, o modelo responde errado com toda a confiança do mundo. A qualidade do RAG depende
mais da busca do que do modelo."

──────────────────────────────────────────────────────────────
LEMBRETES
Assunto aprofundado nos dois slides a seguir: banco vetorial e fine-tuning.
```

## Slide 35 · BANCO VETORIAL

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Vocês entenderam o embedding: texto vira coordenada num mapa de significados. Mas esse
mapa precisa morar em algum lugar, e precisa ser buscável rápido. É isso que é um banco
vetorial.

Cada pedaço de documento vira uma linha nesse banco: o texto original, mais a coordenada
dele. E quando a pergunta chega, ela também vira coordenada na hora, e o banco procura os
vizinhos mais próximos.

Pensa num aplicativo de mapa achando o restaurante mais perto de você. Ele não compara a
distância até cada restaurante do país, um por um. Existe um índice que já organiza tudo
por proximidade, e a busca sai instantânea. Banco vetorial faz exatamente isso, só que a
'distância' é semelhança de significado, e não metro na rua.

E esse índice é o que permite buscar entre milhões de coordenadas em milissegundos. Sem
ele, RAG funciona numa pasta de vinte documentos e trava numa base de verdade.

Último ponto, e ele importa para quem for montar isso na prática: busca por coordenada,
que tem nome técnico de busca densa, acha sentido parecido. Mas ela pode perder uma
palavra-chave exata, tipo um código de produto ou o número de um artigo de lei, porque
esses tokens específicos às vezes não carregam significado nenhum sozinhos. Por isso um
sistema de busca bem feito combina busca densa com busca por palavra exata, chamada de
esparsa. Um pega o sentido, o outro pega a forma exata."

──────────────────────────────────────────────────────────────
LEMBRETES
Se sobrar tempo e quiserem citar exemplo de produto: Pinecone, Weaviate, pgvector. Cite como exemplo, sem recomendar nenhum.
```

## Slide 36 · DUAS FORMAS DE ADAPTAR

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Última peça antes da interação. RAG resolve um problema. Fine-tuning resolve outro. E
muita gente confunde os dois.

RAG: você entrega os documentos certos na hora da pergunta. Resolve conhecimento que muda,
tipo política, preço, estoque. Atualiza na hora, você troca o documento e pronto. E o jeito
de responder do modelo continua igual, você só mudou o que ele sabe.

Fine-tuning: você retreina o modelo com exemplos do seu padrão de resposta. Resolve
comportamento: tom, formato, jargão do seu setor. Quer que ele sempre responda no formato
da sua empresa, sempre com aquele tom? Fine-tuning ensina isso. Mas atualizar exige treinar
de novo, é processo mais lento e mais caro. E um detalhe importante: fine-tuning ensina
jeito de responder, não fato confiável. Ele não substitui RAG para conhecimento que muda.

Guardem a régua de baixo: na dúvida, comecem por RAG. Ele resolve a maior parte dos casos
reais de conhecimento desatualizado, que é o problema mais comum. Fine-tuning entra quando
o alvo do ajuste é o comportamento do modelo."
```

## Slide 37 · INTERAÇÃO

```
⏱ 3 min  |  DESCARTÁVEL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Uma última antes de fechar. Qual destes quatro pedidos você melhoraria primeiro?"

[aguarde 30 a 45 segundos]

Comentário: o C é o pior dos quatro. "Analise os dados e me diga o que achou" usa um verbo
que não especifica tarefa nenhuma, e ainda deixa de fora formato, restrição e público.
Falta quatro dos cinco elementos.

O A tem tarefa (resumir) mas falta formato e restrição.
O B tem papel, tarefa e formato.
O D tem tarefa, formato e a regra de dúvida, que é o melhor detalhe dos quatro.
```

## Slide 38 · Onde GenAI resolve e onde atrapalha

```
⏱ 21h36 às 22h01 (25 min)  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco de julgamento crítico. É o que mais pesa na carreira deles, e o que diferencia quem
usa a ferramenta de quem escolhe a ferramenta.

ESTRUTURA:
  A escada de volta                     3 min
  Sinais de que resolve                 4 min
  Sinais de que atrapalha               5 min
  Tabela problema para ferramenta       4 min
  O erro mais comum                     5 min
  Como avaliar saída                    4 min
```

## Slide 39 · A ESCADA, DE VOLTA

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Vocês lembram desta tabela. Ela apareceu na semana 1.

Relatório responde o que aconteceu. Analytics responde por quê. Machine learning responde
o que vai acontecer. Otimização responde o que eu devo fazer. IA generativa responde como
seria isso escrito ou lido. E agentes fazem do início ao fim.

Hoje a gente passou a noite inteira no quinto degrau. E eu preciso fechar a noite lembrando
que ele é UM degrau, e não a escada inteira.

Olha a linha da IA generativa e a linha do relatório. 'Quantos clientes cancelaram no mês
passado' é uma pergunta de banco de dados. Se você mandar essa pergunta para um modelo de
linguagem com uma planilha colada, ele vai tentar contar, e vai errar. A gente vai ver isso
em detalhe daqui a pouco."
```

## Slide 40 · O TESTE RÁPIDO

```
⏱ 9 min  |  ESSENCIAL, slide-âncora do bloco  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Este é o slide que vale fotografar. Percorra os dois lados com calma.

"Seis sinais de cada lado. Este é o teste rápido que eu quero deixar com vocês.

Do lado esquerdo, sinais de que GenAI resolve bem.

O trabalho principal é ler ou escrever texto. Se o núcleo da tarefa é linguagem, é bom
candidato.

Existe variação demais para escrever regra fixa. Se você tentou escrever um 'se-então' e
apareceram trinta exceções, é sinal.

Errar de vez em quando é tolerável. Repara que eu não disse 'errar não importa'. Disse
tolerável.

Tem um humano conferindo antes de virar decisão.

O ganho é tempo, e o volume é alto. Sem volume, não compensa o esforço de construir.

E não existe uma única resposta certa. Resumo bom tem várias formas.

Agora o lado direito, sinais de que ela atrapalha.

O problema pede número exato e reproduzível. Modelo de linguagem não é calculadora.

Existe uma resposta certa e auditável. Se alguém pode processar a empresa por causa da
resposta, cuidado.

A decisão é automática, sem humano no meio. Aí o erro vira decisão direto.

O custo de errar é alto e difícil de desfazer.

Já existe regra simples que resolve. Esse é o mais comum de todos, e o mais caro de
ignorar.

E o último: você precisa explicar a decisão de forma determinística. Se o regulador
perguntar por que aquela decisão foi tomada, 'o modelo escolheu' não é resposta aceitável.

A régua está embaixo: conte quantos sinais de cada lado o seu problema tem."
```

## Slide 41 · O ERRO MAIS COMUM

```
⏱ 5 min  |  ESSENCIAL, exemplo de maior retenção  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Este é o exemplo mais prático e mais memorável do bloco. Conte devagar.

"Vou mostrar o erro mais comum que eu vejo, e ele é traiçoeiro porque falha em silêncio.

Alguém cola uma planilha na conversa e pede: 'some a coluna de vendas'. E a resposta vem,
com aparência perfeita, formatada, com o cifrão no lugar certo.

Nos primeiros testes, com poucas linhas, ele costuma acertar. E aí a pessoa confia, e passa
a usar aquilo para valer.

Com volume maior, ele erra. E não avisa. Porque ele nunca esteve somando. Ele está
compondo uma sequência de tokens que se parece com o resultado de uma soma. É a mesma
mecânica do número de processo inventado que o Edmar mostrou.

E tem uma coisa pior ainda: a mesma pergunta pode dar número diferente em duas tentativas.
Vocês entenderam por quê, no bloco da temperatura. E conta que muda de valor não serve para
nada em lugar nenhum.

A correção é simples e vale para o resto da carreira de vocês: o modelo escreve a FÓRMULA
ou o CÓDIGO. A planilha, ou o Python, executa. Você usa a IA generativa para a parte de
linguagem, que é traduzir o seu pedido em fórmula, e usa a ferramenta certa para a conta.

Cada degrau da escada fazendo o que sabe fazer."
```

## Slide 42 · ANTES DE COLOCAR EM PRODUÇÃO

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Fechando: como avaliar isso, já que na semana 1 a gente viu que GenAI não tem gabarito.

Defina o que é uma boa resposta antes de começar. Se você definir depois, a métrica vira
justificativa do que já saiu.

Monte um conjunto de vinte a cinquenta casos com a resposta esperada. Não precisa de mil.
Vinte a cinquenta já pega piora grande.

Rode esse conjunto a cada mudança de prompt ou de modelo. E aqui vai um detalhe que
surpreende quem está começando: prompt novo pode consertar um caso e quebrar cinco. Sem
conjunto de teste, você só vê o caso que consertou.

Para o que é objetivo, use regra: o formato está certo, o campo obrigatório veio, a
categoria está dentro da lista permitida. Isso dá para checar por código.

Para o que é subjetivo, use pessoa: o tom está certo, a resposta é útil, ela responde
mesmo o que foi perguntado.

E a linha final, que vale como aviso: o modelo muda de versão sozinho, do lado do
fornecedor. Sem conjunto de teste, você descobre que piorou pelo cliente reclamando."
```

## Slide 43 · Encerramento

```
⏱ 22h01 às 22h11 (10 min)  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Recapitulação        3 min
  O que vem na quinta  2 min
  Q&A                  4 min  (elástico, absorve atraso)
  Fechamento           1 min

Não passe das 22h15. A aula esticou por decisão, não por atraso.
```

## Slide 44 · RECAPITULANDO

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Leia as seis com calma. É a última chance de fixar.

"Seis ideias para levar de hoje.

A primeira: token, embedding e atenção explicam o comportamento dele, inclusive o
comportamento estranho. Quem entende essas três peças para de brigar com a ferramenta.

Segunda: ele escolhe o provável, e provável é diferente de verdadeiro. Por isso a
alucinação é comportamento esperado.

Terceira: prompt é especificação, com cinco elementos. E todo prompt ruim está sem pelo
menos três deles.

Quarta: mostrar dois exemplos vale mais que escrever três parágrafos de instrução. E dizer
o alvo funciona melhor que dizer o que evitar.

Quinta: RAG é o que faz ele falar da sua empresa citando fonte. E a qualidade do RAG
depende mais da busca do que do modelo.

E a sexta, que é a que mais vai economizar dinheiro de vocês: ela brilha em texto e falha
em conta exata. O modelo escreve a fórmula, a planilha executa."
```

## Slide 45 · PRÓXIMO ENCONTRO

```
⏱ 2 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Quinta-feira, 19h às 21h. E é a aula em que entra código pela primeira vez.

Calma para quem nunca programou: vai entrar devagar, do zero, e roda tudo no navegador.
Vocês vão usar o Google Colab, que é uma ferramenta gratuita do Google. Não precisa
instalar nada, só ter uma conta Google.

O que a gente vai fazer: rodar o primeiro código, conectar numa API gratuita de modelo de
linguagem e fazer a primeira chamada de verdade. E aí colocar em prática os cinco elementos
de prompt que vocês viram hoje, e comparar o que muda com temperatura diferente.

Ou seja: tudo que foi teoria hoje, vocês vão ver acontecendo na tela de vocês."

──────────────────────────────────────────────────────────────
LEMBRETES
PENDÊNCIA: confirmar qual API gratuita será usada e testar o notebook antes de prometer em detalhe.
```

## Slide 46 · AGORA É COM VOCÊS

```
⏱ 4 min (elástico)  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves + Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Q&A com moderação. O moderador seleciona e agrupa as repetidas.

PERGUNTAS PREVISÍVEIS DESTA AULA, com resposta pronta:

• "Qual modelo é o melhor?"
  Depende da tarefa, do custo e do idioma. Para trabalho em português vale testar mais de
  um com o SEU caso, usando aquele conjunto de 20 a 50 exemplos.

• "Preciso pagar por ChatGPT para acompanhar o curso?"
  Não. Na quinta a gente usa API gratuita, e o Colab também é gratuito.

• "IA vai substituir o meu trabalho?"
  Ela troca a tarefa de escolher pela tarefa de conferir, como no exemplo da triagem de
  chamados. Quem sabe conferir bem fica mais valorizado.

• "Dá para usar isso com dado da empresa? E a LGPD?"
  Depende do contrato com o fornecedor e da política interna. Nunca cole dado pessoal ou
  sigiloso numa ferramenta pública sem autorização. Isso é assunto da semana de governança.

• "Qual a diferença entre RAG e fine-tuning?"
  RAG serve para conhecimento que muda. Fine-tuning serve para comportamento e formato.
  Na dúvida, comece por RAG, que é mais barato e mais fácil de atualizar.

• "Esses modelos aprendem com o que eu escrevo?"
  Depende do produto e do plano contratado. Em plano corporativo costuma haver garantia de
  não treinar com o seu dado. Confira sempre antes de usar com material da empresa.
```

## Slide 47 · Obrigado!

```
⏱ 1 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

FECHAMENTO (30 segundos, com energia):

"Obrigado pela noite de hoje. Foi a aula mais técnica até agora, e vocês seguraram bem.

Entrem no Discord, o resumo com o glossário de hoje vai estar lá.

E fica com isso: hoje vocês passaram a entender por dentro uma ferramenta que a maior parte
das pessoas usa no escuro. Isso já muda a conversa que vocês conseguem ter sobre ela. Nos
vemos na quinta, com código na tela. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Postar no Discord o resumo e o glossário.
- 10 minutos de retrospectiva entre os dois: qual bloco atrasou e por quê.
```
