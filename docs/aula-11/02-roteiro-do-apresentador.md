# Roteiro do apresentador: Aula 11 (Semana 6, segunda-feira)

> Gerado automaticamente a partir das notas do deck.
> Não edite este arquivo à mão: edite `scripts/gerar_slides_aula11.py` e rode
> `python scripts/gerar_slides_aula11.py && python scripts/exportar_roteiro_aula11.py`.

**Como usar:** imprima ou deixe aberto num segundo monitor. O texto entre aspas é
fala sugerida. Adapte para a sua voz, não decore: o que importa é a sequência de ideias.

---

## Slide 1 · PROGRAMA DE TRAINEES EM DADOS E INTELIGÊNCIA ARTIFICIAL

```
⏱ 19h00 às 19h10 (slide de espera)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Slide projetado desde 18h55. Fale a cada 2 ou 3 minutos enquanto a sala enche.

"Boa noite! Semana 6, Machine Learning. Enquanto a sala enche, uma pergunta: você já
recebeu uma recomendação de filme, série ou produto que pareceu ler sua mente? Hoje a
gente desmonta como isso funciona por dentro."

Não comece antes de 19h08.

──────────────────────────────────────────────────────────────
LEMBRETES
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- Moderador com o link do Discord pronto para colar.
- Sem código ao vivo hoje. A prática de treinar um modelo de verdade é na Aula 12.
```

## Slide 2 · ENQUANTO TODO MUNDO ENTRA

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Bem-vindos à Aula 11. Rapidinho: microfone no mudo, câmera à vontade, dúvida no chat
a qualquer momento, aula gravada com link em até 24h.

Hoje é só teoria, igual toda segunda. A prática de treinar um modelo de verdade fica
para quinta-feira.

Enquanto isso, escreve no chat: que serviço já te recomendou um filme, uma música ou
um produto de um jeito que pareceu ler sua mente? Vou usar algumas respostas daqui a
pouco."
```

## Slide 3 · Duas fases, de novo, agora a fundo

```
⏱ 19h10 às 19h20 (10 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Recap de uma frase por conceito    5 min
  Panorama de hoje                   5 min

Este bloco é deliberadamente curto. Baseline, treino e teste, overfitting e a
armadilha da acurácia já foram ensinados na Aula 1, Fase 5 e Fase 6, com o exemplo do
cancelamento de cliente. Não repita a explicação inteira, só toque o nome e siga.
```

## Slide 4 · LEMBRANDO DA AULA 1

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Rapidíssimo, cinco coisas que vocês já ouviram na Aula 1.

Baseline: a solução mais simples que funciona.

Treino e teste: o modelo é avaliado numa parte dos dados que nunca viu.

Overfitting: o aluno que decorou a prova, vai bem no que já viu e mal no que é novo.

A armadilha da acurácia: o exemplo de detectar fraude, sempre dizer "não é fraude" e
acertar 99% sem pegar nenhuma.

E os nomes precisão, recall e F1, que resolvem essa armadilha.

Hoje a gente não reexplica nada disso. A gente vai direto para o que a Aula 1 não
teve tempo de fazer: a conta de verdade, um algoritmo de verdade, e as métricas para
quando a resposta vira um número em vez de uma categoria."
```

## Slide 5 · O PANORAMA DE HOJE

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O panorama de hoje, em cinco blocos: como uma máquina aprende de verdade por
dentro, a matemática por trás da armadilha da acurácia, o primeiro algoritmo de
verdade, o que muda quando a resposta é um número, e o que acontece quando o modelo
aprende o preconceito dos dados.

Tudo usando o caso de fraude em cartão que vocês já conhecem desde a Aula 2. Nada de
exemplo hipotético novo."
```

## Slide 6 · Que tipo de problema é esse

```
⏱ 19h20 às 19h35 (15 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Recap rápido dos três tipos    4 min
  Mapeando no caso de fraude     6 min
  Interação                      5 min
```

## Slide 7 · RECAP RÁPIDO

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"A Fase 5 da Aula 1 já deu os três nomes. Classificação: resposta é categoria.
Regressão: resposta é número. Clusterização: não tem rótulo, é achar grupo sozinho.

Hoje a gente não fica na definição. A gente aplica isso no caso de fraude."
```

## Slide 8 · APLICANDO NO CASO DE FRAUDE

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"A mesma base de fraude serve para os três tipos, dependendo da pergunta.

Classificação: esta transação vai ser contestada? O rótulo já existe na coluna
status.

Regressão: quanto este cliente vai gastar no próximo mês? Aqui a resposta é um
número.

Clusterização: que grupos de cliente existem, sem eu ter definido antes? Aqui
ninguém rotulou nada, o algoritmo tem que achar sozinho.

Hoje a gente fica principalmente em classificação, porque é o problema do caso de
fraude, mas os três merecem estar no seu vocabulário."
```

## Slide 9 · INTERAÇÃO RÁPIDA

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"No chat: para cada cenário que eu vou ler, escreva C de classificação, R de
regressão ou CL de clusterização.

Gato ou cachorro? Classificação.
Quantos graus vai fazer amanhã? Regressão.
Quais clientes se parecem, sem eu saber por quê? Clusterização.
Este e-mail é spam? Classificação.

Reparem: "gato ou cachorro" e "spam ou não" são o mesmo tipo de problema, mesmo
sendo de áreas completamente diferentes. Isso é o poder de pensar em tipos de
problema, não em domínios."
```

## Slide 10 · Como uma máquina aprende de verdade

```
⏱ 19h35 às 20h10 (35 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  O que significa aprender, e o exemplo mínimo    6 min
  Função de perda                                 6 min
  Otimização e gradiente descendente             12 min
  Treino, inferência, parâmetro e hiperparâmetro   7 min
  Ponte para a árvore de decisão de hoje           4 min

Este é o bloco que a turma pediu de volta: sem ele, "Machine Learning" vira um nome
para "escolher a métrica certa", sem explicar o mecanismo por trás do aprendizado.
Vá devagar aqui, é o bloco mais denso tecnicamente da aula inteira.
```

## Slide 11 · O QUE SIGNIFICA APRENDER, PARA UMA MÁQUINA

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Até agora falamos de classificação, regressão, precisão, recall. Mas ninguém
explicou o que significa, por dentro, uma máquina "aprender". É isso que fecha
hoje.

Para uma máquina, aprender significa só uma coisa: ajustar um conjunto de números
repetidamente, até o modelo errar menos nos exemplos que ele já viu. Nenhuma
compreensão envolvida. Vamos ver com um exemplo mínimo."
```

## Slide 12 · UM EXEMPLO MÍNIMO

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Exemplo mínimo, de propósito simples demais para a base de fraude real, só para
mostrar o mecanismo.

Quero prever o valor de uma transação a partir do horário. A fórmula é uma reta:
valor previsto igual a "a" vezes horário, mais "b".

"a" e "b" são os parâmetros. São os únicos números que o treino vai mexer. Antes de
treinar, eles começam em qualquer valor, geralmente aleatório, o modelo começa
"burro" de propósito. Depois do treino, "a" e "b" ficam fixos, e essa reta vira o
modelo inteiro."
```

## Slide 13 · COMO MEDIR O ERRO

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Como saber se "a" e "b" estão bons? Precisa de um número que resuma o quão errado
o modelo está. Isso é a função de perda.

Para cada exemplo, compare o valor previsto com o valor real, isso dá o erro daquele
exemplo. Eleve ao quadrado, de propósito: um erro de 100 pesa muito mais que dez
erros de 10 cada. Tire a média de todos os exemplos. Isso tem nome, MSE, erro
quadrático médio.

Quanto menor a perda, melhor o modelo. E aqui está a ideia central do bloco inteiro:
treinar um modelo é, do início ao fim, só isso: encontrar os parâmetros que deixam
essa perda a mais baixa possível.

E reparem no nome: a raiz quadrada do MSE é exatamente o RMSE que vocês vão ver daqui
a pouco. Mesma conta, dois nomes diferentes."
```

## Slide 14 · DA PERGUNTA AO PROCESSO

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Encontrar os melhores "a" e "b" é um problema de busca. E não dá para tentar ao
acaso, são infinitas combinações possíveis.

A boa notícia: a função de perda não é só um número, ela também aponta uma direção.
Para cada parâmetro, dá para calcular "se eu aumentar um pouquinho, a perda sobe ou
desce?". Isso guia a busca. Esse processo tem nome: gradiente descendente."
```

## Slide 15 · O ALGORITMO POR TRÁS DO AJUSTE

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"A metáfora que fica: você está numa montanha coberta de neblina. Não enxerga o
vale lá embaixo. A única informação que você tem é o chão debaixo dos seus pés: para
que lado ele desce mais rápido agora.

Você dá um passo nessa direção. Sente de novo. Dá outro passo. Repete isso centenas,
milhares de vezes, até chegar a um ponto onde qualquer passo te faz subir, não
descer mais. Você chegou perto do fundo do vale.

Gradiente descendente é exatamente isso, só que o "vale" é a função de perda, e os
"seus pés" são a derivada dela em cada parâmetro."
```

## Slide 16 · GRADIENTE DESCENDENTE, SEM NEBLINA

```
⏱ 6 min  |  ESSENCIAL, o coração técnico do bloco  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Vá devagar aqui, é o ponto mais denso da aula inteira.

"Passo a passo, sem neblina agora.

A cada passo, o algoritmo calcula, para cada parâmetro, em que direção mudá-lo
reduz a perda. Isso é o gradiente.

Ajusta cada parâmetro um pouquinho nessa direção. Não tudo de uma vez, um passo
pequeno.

Repete isso milhares de vezes, recalculando a cada rodada, até a perda parar de cair
de um jeito que valha a pena continuar.

E o tamanho de cada passo tem nome: taxa de aprendizado. Se o passo é grande demais,
o modelo pula o fundo do vale e fica oscilando, nunca estabiliza. Se o passo é
pequeno demais, o treino converge, mas demora uma eternidade, às vezes mais tempo do
que alguém tem paciência de esperar."
```

## Slide 17 · DUAS FASES MUITO DIFERENTES

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Duas fases bem diferentes, e é comum confundir os nomes.

Treinamento é repetir o gradiente descendente sobre os dados que o modelo tem
disponível, ajustando os parâmetros a cada passo. É lento e caro, pode levar de
minutos a dias, dependendo do modelo. E não acontece toda hora: acontece uma vez, ou
de tempos em tempos, quando alguém decide retreinar.

Inferência é usar o modelo já treinado, com os parâmetros já fixos, para prever um
caso novo. Nenhum parâmetro muda nesse momento, é só aplicar a fórmula pronta. É
rápido, e acontece toda vez que alguém usa o modelo.

Quando vocês usam qualquer app com IA no dia a dia, é inferência que está
acontecendo. O treinamento já aconteceu bem antes, em algum servidor, uma vez."
```

## Slide 18 · DUAS CATEGORIAS DE NÚMERO, FÁCEIS DE CONFUNDIR

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Uma distinção que vocês vão ouvir o resto do programa: parâmetro e hiperparâmetro.

Parâmetro é o que o modelo aprende sozinho, durante o treino. "a" e "b" do nosso
exemplo, ou os pesos de uma rede neural.

Hiperparâmetro é escolha humana, feita antes do treino começar. Taxa de
aprendizado é um hiperparâmetro. Quantos passos dar é outro. Profundidade máxima de
uma árvore, que vocês vão ver daqui a pouco, também é.

Ninguém treina um modelo sem escolher hiperparâmetro primeiro. E escolher mal pode
fazer o treino nunca convergir, ou convergir devagar demais para ser útil."
```

## Slide 19 · E A ÁRVORE DE DECISÃO DE HOJE?

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Um aviso importante antes de ver a árvore de decisão: tudo que vimos agora, função
de perda, gradiente descendente, taxa de aprendizado, NÃO é como uma árvore de
decisão aprende.

A árvore decide de outro jeito, chamado escolha gulosa: a cada pergunta, ela testa
várias divisões possíveis dos dados e escolhe a que separa melhor fraude de não
fraude, sem calcular gradiente nenhum, sem função de perda contínua.

Gradiente descendente é o mecanismo por trás de outra família de modelo: regressão
linear, regressão logística, e redes neurais, incluindo os LLMs que vocês viram na
Aula 3.

Vocês acabaram de conhecer os dois grandes jeitos de uma máquina aprender. A árvore
de hoje usa um. O resto do programa vai reencontrar o outro."
```

## Slide 20 · A matemática por trás da armadilha

```
⏱ 20h10 às 20h40 (30 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Recap de uma frase                 2 min
  Matriz de confusão                 8 min
  Precisão e recall, com a conta    10 min
  F1                                  5 min
  Interação                          5 min

Este é o bloco mais denso da aula. Reserve o tempo e não deixe a interação do final
ser cortada, ela é o gancho para o trade-off de negócio.
```

## Slide 21 · LEMBRANDO

```
⏱ 2 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Vocês já ouviram isso na Aula 1. Hoje a gente vê a máquina por trás desse número."
```

## Slide 22 · A MATRIZ DE CONFUSÃO

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Isto aqui é a matriz de confusão. Quatro números, não um só.

Verdadeiro positivo: era fraude, o modelo disse fraude. Acertou.

Falso negativo: era fraude, o modelo disse que não era. Errou, e esse erro é caro:
uma fraude passou.

Falso positivo: não era fraude, o modelo disse que era. Errou, e esse erro incomoda
um cliente honesto.

Verdadeiro negativo: não era fraude, o modelo disse que não era. Acertou.

Acurácia junta os quatro números numa conta só, e é exatamente por isso que ela
engana: ela não separa qual tipo de erro está acontecendo."
```

## Slide 23 · UM EXEMPLO COM NÚMEROS

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Exemplo ilustrativo, com números redondos, não é resultado real, isso vocês vão
medir de verdade na quinta.

1.000 transações, 20 são fraude de verdade. O modelo pegou 12 (verdadeiro positivo),
deixou passar 8 (falso negativo), assustou 30 clientes honestos (falso positivo), e
acertou 950 transações normais (verdadeiro negativo).

Acurácia: 962 dividido por 1.000, 96,2%. Parece ótimo. Vamos ver o que precisão e
recall dizem sobre o mesmo modelo."
```

## Slide 24 · PRECISÃO E RECALL, COM A CONTA

```
⏱ 10 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Precisão: das vezes que o modelo gritou fraude, quantas eram mesmo? 12 acertos
dividido por 42 alarmes totais (12 verdadeiros mais 30 falsos), 28,6%. Ou seja, mais
de 7 em cada 10 alarmes deste modelo são falsos.

Recall: das 20 fraudes que existiam de verdade, quantas o modelo pegou? 12 dividido
por 20, 60%. Ou seja, 4 em cada 10 fraudes passam batido.

Reparem: acurácia de 96,2% escondeu os dois problemas. Um modelo que parecia ótimo
tem quase três quartos de alarme falso, e ainda deixa passar 40% das fraudes."
```

## Slide 25 · F1, O EQUILÍBRIO ENTRE OS DOIS

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"F1 junta precisão e recall numa métrica só, mas não pela média simples. É a média
harmônica dos dois, que pune mais forte quando um deles está muito baixo.

Neste exemplo, F1 fica perto de 38,7%. Muito mais honesto que os 96,2% de acurácia
sobre o mesmo modelo.

F1 é útil quando você precisa de um número só para comparar modelos. Mas ele não
decide sozinho o que importa mais para o seu negócio, precisão ou recall. Isso é a
próxima pergunta."
```

## Slide 26 · TRADE-OFF DE NEGÓCIO

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Pergunta para o chat: o que dói mais para um banco, bloquear uma compra honesta por
engano, ou deixar passar uma fraude de verdade?

Não existe resposta certa universal. Um banco de cartão pré-pago, com cliente
sensível a fricção, pode preferir menos bloqueio (mais recall, menos precisão). Uma
operação de empréstimo, com prejuízo alto por fraude confirmada, pode preferir o
contrário.

Essa decisão nunca é só técnica. É decisão de negócio, e quem escolhe a métrica
está, na prática, escolhendo essa resposta."
```

## Slide 27 · Seu primeiro modelo

```
⏱ 20h40 às 21h10 (30 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  História, CART e ID3       6 min
  Como ela decide            10 min
  Por que é fácil de explicar 6 min
  Feature engineering         8 min
```

## Slide 28 · UMA FERRAMENTA COM HISTÓRIA

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"A árvore de decisão tem quatro décadas. Em 1984, o estatístico Leo Breiman e
colegas publicaram o livro que formalizou o CART, Classification And Regression
Trees, o nome já entrega os dois usos: classificação e regressão.

Em 1986, Ross Quinlan publicou o ID3, outra família de árvore, de uma linha de
pesquisa diferente.

E hoje, os algoritmos mais fortes do mercado, Random Forest e XGBoost, não abandonam
a árvore: eles juntam centenas delas para decidir em conjunto. Entender uma árvore
sozinha é a porta de entrada para entender os dois."
```

## Slide 29 · COMO ELA DECIDE

```
⏱ 10 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Uma árvore de decisão é uma sequência de perguntas sim ou não, aprendidas a partir
dos dados, não escritas por uma pessoa.

Valor passa de R$500? Se não, aprovada. Se sim, próxima pergunta.

Horário de madrugada, entre 1h e 5h? Se não, aprovada. Se sim, próxima.

País diferente do Brasil? Se sim, marca como suspeita.

Importante: isto é só UM caminho, para dar a intuição. Uma árvore de verdade tem
várias perguntas em cada ponto, e vários caminhos possíveis, formando de fato uma
árvore que se ramifica. O algoritmo escolhe sozinho quais perguntas fazer, e em qual
ordem, testando qual pergunta separa melhor fraude de não fraude nos dados de
treino."
```

## Slide 30 · POR QUE É FÁCIL DE EXPLICAR

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"A grande vantagem da árvore: cada decisão é auditável. Dá para mostrar exatamente
qual sequência de perguntas levou a uma transação ser marcada como suspeita. Não é
caixa preta.

Isso não é só elegância técnica. Em crédito, seguro e saúde, decisão automatizada que
afeta uma pessoa muitas vezes precisa ser explicável, às vezes por exigência legal.

O custo: uma árvore sozinha erra mais do que os modelos mais sofisticados de hoje.
Por isso o mercado combina centenas delas, Random Forest, XGBoost, trocando um pouco
de explicabilidade por mais acerto."
```

## Slide 31 · FEATURE ENGINEERING

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Feature engineering é transformar a coluna bruta numa pergunta que o modelo
consegue usar bem.

Data e hora inteira não ajuda muito. "É madrugada?" ajuda demais.

Valor contínuo funciona, mas faixas (até R$50, R$50 a R$500, acima de R$500) às
vezes revelam um padrão mais claro para a árvore encontrar.

País com cinco valores possíveis vira uma pergunta binária, "é Brasil?", que é
exatamente o tipo de pergunta que uma árvore faz.

Reparem: isso é a mesma técnica de transformação de coluna que a Aula 7 já ensinou
em pandas. O que muda agora é só o destino: essa coluna vai alimentar um modelo."
```

## Slide 32 · INTERVALO

```
⏱ 15 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Intervalo. Sem apresentação.
```

## Slide 33 · Quando a resposta é um número

```
⏱ 21h25 às 21h55 (30 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  MAE, RMSE, R2               10 min
  O caso do Netflix Prize     15 min
  Por que RMSE fazia sentido   5 min

Este bloco reaproveita o MSE que acabou de aparecer no Bloco 03: RMSE é a raiz do
MSE. A Aula 1 nunca cobriu nenhuma métrica de regressão, então o resto é inédito.
```

## Slide 34 · TRÊS MÉTRICAS PARA QUANDO A RESPOSTA É UM NÚMERO

```
⏱ 10 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Em classificação a gente tem acurácia, precisão, recall. Em regressão, o jogo é
outro, porque não existe "acertou ou errou", existe "errou por quanto".

MAE: erro médio absoluto. Some a diferença entre previsto e real de cada exemplo, em
valor absoluto, e tire a média. Se o MAE é R$50, o modelo erra em média R$50 pra mais
ou pra menos.

RMSE: é a raiz daquele MSE do Bloco 03, a mesma função de perda que o gradiente
descendente tenta minimizar. Eleva cada erro ao quadrado antes de tirar a média, e
depois tira a raiz. Consequência prática: um erro de R$500 pesa muito mais que dez
erros de R$50 cada. RMSE pune erro grande com mais força que MAE.

R quadrado: de 0 a 1, quanto da variação dos dados o modelo explica. Perto de 1 é
bom, perto de 0 significa que o modelo não está capturando quase nada."
```

## Slide 35 · UMA FERRAMENTA COM HISTÓRIA

```
⏱ 2 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Vocês já ouviram falar do Netflix Prize na Aula 1, só como uma data. Hoje, a
história completa, porque ela é literalmente sobre a métrica que a gente acabou de
ver."
```

## Slide 36 · O DESAFIO

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O desafio era prever, para cada usuário, que nota de 1 a 5 estrelas ele daria para
um filme que ainda não tinha visto. E o critério de vitória era literalmente o RMSE
que vocês acabaram de aprender.

O sistema que a Netflix já usava, Cinematch, tinha RMSE de 0,9525. A meta era baixar
isso em 10%. Prêmio: um milhão de dólares para a primeira equipe a conseguir.

A equipe BellKor's Pragmatic Chaos venceu em 2009, com RMSE de 0,8567, uma melhora de
10,06% sobre o Cinematch."
```

## Slide 37 · O DETALHE QUE NINGUÉM ESQUECE

```
⏱ 5 min  |  ESSENCIAL, o mais memorável do bloco  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Conte devagar, é o tipo de detalhe que fica na cabeça da turma.

"Um detalhe real do Netflix Prize que vale a pena guardar: outra equipe, chamada The
Ensemble, também bateu a meta de 10%, com um resultado empatado ou levemente melhor
que o time vencedor.

Só que enviou a resposta 20 minutos depois. E a regra do desafio dizia: em caso de
empate, vence quem enviou primeiro.

BellKor's Pragmatic Chaos levou o milhão de dólares inteiro. Não só por ter o modelo
mais forte, mas por ter cronometrado o envio. Lição real: a métrica decide o
resultado técnico, mas a regra do jogo decide quem ganha."
```

## Slide 38 · POR QUE RMSE FAZIA SENTIDO PARA A NETFLIX

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Por que RMSE, e não MAE? Porque, para a Netflix, o erro grave é recomendar com
confiança um filme que a pessoa vai odiar, bem mais grave que errar por pouco. RMSE pune erro
grande desproporcionalmente mais que erro pequeno, exatamente o comportamento que a
Netflix queria incentivar nos competidores.

Isso fecha a ideia do bloco: escolher métrica nunca é neutro. É sempre uma escolha
sobre o que você mais quer evitar errar."
```

## Slide 39 · Quando o modelo aprende o preconceito dos dados

```
⏱ 21h55 às 22h15 (20 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Releitura do caso de viés    8 min
  De onde vem o viés          12 min
```

## Slide 40 · RELEITURA

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Lembram do caso de viés da Aula 1? Reconhecimento facial, Aracaju, o estudo da DPU
com o CESeC mapeando 24 casos entre 2019 e abril de 2025, mais da metade das
abordagens resultando em identificação equivocada.

Na Aula 1 isso foi apresentado como um caso de IA dando errado. Hoje, com o
vocabulário de hoje: aquilo é um classificador. Ele recebe uma imagem, e decide
"esta pessoa é quem o sistema busca, sim ou não". É exatamente a mesma estrutura da
árvore de decisão que vimos hoje, só que rodando dentro de uma rede neural, não numa
árvore.

E o problema real está em outro lugar: ele decidiu errado com muito mais frequência
para um grupo específico de pessoas."
```

## Slide 41 · DE ONDE VEM O VIÉS

```
⏱ 12 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"De onde vem o viés? Três origens, e nenhuma delas é o algoritmo em si.

Dado de treino não representativo: se um grupo aparece pouco nos dados de treino, o
modelo simplesmente aprende menos sobre esse grupo, e erra mais nele.

Rótulo enviesado: se o "gabarito" usado para treinar já vem de uma decisão humana
historicamente enviesada, o modelo aprende a repetir esse padrão com uma confiança
matemática que parece objetiva, mas não é.

Variável usada como proxy: um campo que parece neutro, como CEP ou nome, pode
carregar, na prática, informação que correlaciona fortemente com um grupo sensível.

A saída nunca é "não usar dado". É auditar quem está representado nos dados, e medir
o erro do modelo SEPARADO por grupo, não só no total. Um modelo com 95% de acurácia
geral pode estar errando 40% do tempo só para um grupo específico, e a métrica geral
esconde isso completamente."
```

## Slide 42 · Encerramento

```
⏱ 22h15 às 22h55 (40 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Recapitulação             6 min
  O que vem pela frente     4 min
  Q&A                      25 min  (elástico, absorve atraso)
  Fechamento                5 min
```

## Slide 43 · ENCERRAMENTO

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Sete ideias para levar de hoje.

Aprender é ajustar números até errar menos: função de perda, otimização, gradiente
descendente.

Treino é lento e raro, inferência é rápida e constante.

Nem todo modelo aprende do mesmo jeito: árvore escolhe gulosamente, sem gradiente.

Acurácia sozinha não basta, e agora vocês sabem a conta: matriz de confusão,
precisão, recall, F1.

Regressão tem métricas próprias: MAE, RMSE, R quadrado.

Escolher métrica é escolher prioridade de negócio, o Netflix Prize é a prova disso.

E viés de modelo nasce do dado que treinou o modelo, quase nunca do algoritmo em si.

Vocês saem hoje sabendo o suficiente para treinar o primeiro modelo de verdade. Isso
acontece quinta-feira."
```

## Slide 44 · PRÓXIMOS ENCONTROS

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Na quinta, primeiro modelo de verdade: árvore de decisão, no Colab, sobre a base de
fraude que vocês já conhecem. Mesmo formato de sempre, demonstração curta e o resto é
prática.

Isso fecha um ciclo bonito: vocês exploraram o dado com SQL e pandas, construíram um
pipeline de engenharia de dados, e agora vão treinar um modelo em cima do mesmo caso.
Tudo conectado."
```

## Slide 45 · ANTES DE IR

```
⏱ 25 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

PERGUNTAS PREVISÍVEIS DE HOJE:

- "Preciso saber calcular gradiente descendente na mão?"
  Não. O que importa é entender o mecanismo (ajustar parâmetro na direção que reduz
  a perda, passo a passo) e reconhecer quando um modelo usa isso e quando não usa.
  A conta, na prática, quem faz é a biblioteca.

- "Preciso saber a fórmula de F1 de cabeça?"
  Não. O que importa é saber que ela existe, o que ela resume, e quando pedir para
  alguém calcular ou usar uma biblioteca que calcula sozinha.

- "Toda árvore de decisão é fácil de explicar?"
  Uma árvore sozinha, sim. Quando o mercado junta centenas delas (Random Forest,
  XGBoost), a explicabilidade cai bastante, mesmo a base ainda sendo árvore.

- "Por que não aprendemos redes neurais hoje?"
  Redes neurais entram melhor depois de já entender treino, teste, overfitting e
  métrica com um modelo simples. Árvore de decisão é a porta de entrada mais didática.

- "Isso cai no projeto final?"
  Cai direto, para quem escolher a trilha de Machine Learning na Etapa 2.
```

## Slide 46 · Obrigado!

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. Vocês saem daqui sabendo fazer a conta que a maioria
das pessoas que fala de IA no dia a dia não sabe fazer. Revisem os slides antes de
quinta, principalmente a matriz de confusão. Nos vemos lá. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Anotar quais dos seis blocos geraram mais pergunta no chat, para calibrar onde
  cortar se a Aula 11 precisar ficar mais curta numa próxima turma.
```
