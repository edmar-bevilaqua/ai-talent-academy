# Roteiro do apresentador: Aula 12 (Semana 6, quinta-feira)

> Gerado automaticamente a partir das notas do deck.
> Não edite este arquivo à mão: edite `scripts/gerar_slides_aula12.py` e rode
> `python scripts/gerar_slides_aula12.py && python scripts/exportar_roteiro_aula12.py`.

**Como usar:** imprima ou deixe aberto num segundo monitor. O texto entre aspas é
fala sugerida. Adapte para a sua voz, não decore: o que importa é a sequência de ideias.

---

## Slide 1 · PROGRAMA DE TRAINEES EM DADOS E INTELIGÊNCIA ARTIFICIAL

```
⏱ 19h00 às 19h05 (5 min)  |  ESSENCIAL  |  Apresenta: Edmar Bevilaqua
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Abertura da noite e recepção da turma.

"Boa noite, pessoal! Sejam bem-vindos à nossa Aula 12 do AI Talent Academy.
Hoje é a nossa quinta-feira de laboratório da Semana 6, e esta noite marca um ponto
muito especial no nosso programa.

Na segunda-feira nós cobrimos toda a base conceitual de Machine Learning: o que significa
aprender, função de perda, gradiente descendente, matriz de confusão e o cardápio de
modelos. Hoje nós vamos sentar na frente do computador e treinar o primeiro modelo de
vocês, do zero, no Google Colab, usando a biblioteca scikit-learn.

Abram o Colab pelo link fixado no chat e vamos começar."

──────────────────────────────────────────────────────────────
LEMBRETES
Conferir gravação ligada e link do notebook fixado no chat do Zoom e no canal do Discord.
```

## Slide 2 · ENQUANTO TODO MUNDO ENTRA

```
⏱ 19h05 às 19h10 (5 min)  |  DESCARTÁVEL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Slide de apoio nos dez minutos iniciais para acolher quem está entrando na sala.

"Quem acabou de chegar: o link do notebook de hoje já está fixado no topo do chat e
também lá no Discord.

Abram o link no navegador. Não precisa instalar nada no computador: tudo roda nos
servidores do Google Colab. Hoje vamos usar Python, pandas e a biblioteca scikit-learn.
Aproveitem estes minutos para salvar uma cópia do notebook no Drive de vocês."
```

## Slide 3 · Bloco A · Da teoria ao código

```
⏱ 19h10 às 19h13 (3 min)  |  ESSENCIAL  |  Apresenta: Edmar Bevilaqua
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Abertura do primeiro bloco expositivo da noite.

"Começamos o Bloco A fazendo a ponte direta com o que vimos na segunda-feira.
Na segunda nós passamos mais de quatro horas discutindo conceitos, fórmulas e intuição.
Hoje a regra é outra: código executável, visualização gráfica e decisões de negócio."
```

## Slide 4 · DE VOLTA À SEGUNDA

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar Bevilaqua
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Reparem na continuidade do programa.
Na segunda a gente discutiu como a máquina aprende: ajustando parâmetros matemáticos até errar menos.
Vimos a matriz de confusão e por que acurácia engana.

Hoje nós vamos pegar esses mesmos conceitos e colocar para rodar.
E o melhor: sobre a mesma base de transações de cartão que vocês vêm acompanhando desde
a modelagem do canvas na Aula 2, as consultas em SQL na Aula 5 e o pipeline na Aula 10.
Vocês já conhecem o negócio por trás desses números."
```

## Slide 5 · A ARMADILHA DO 99%

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Provocação central do laboratório.

"Gravem esta frase antes de encostar no teclado: em dados desbalanceados, acurácia alta
é a forma mais fácil de mentir.

Se noventa e oito por cento das transações de um banco são legítimas e duas são fraude,
um modelo preguiçoso que carimba 'aprovada' em todas as compras terá noventa e oito por cento
de acurácia. A diretoria comemora a métrica e o banco quebra no final do mês porque
nenhuma fraude foi interceptada.

O nosso primeiro passo prático no Colab vai ser justamente programar esse modelo ingênuo
para ver esse número feio na tela."
```

## Slide 6 · ROTEIRO PRÁTICO

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Apresentação da trilha do aluno.

"Aqui está o mapa da nossa noite. São seis passos lógicos e bem delimitados.
Começamos preparando os dados. Em seguida, criamos o baseline ingênuo para comprovar a falha.
No passo três, fazemos a divisão em treino e teste com estratificação.
No passo quatro, treinamos nossa primeira árvore de decisão e desenhamos os ramos na tela.
No passo cinco, calculamos a matriz de confusão e convertemos erros em reais.
E fechamos no passo seis testando o overfitting ao mudar a profundidade da árvore.

Cada passo tem explicações no notebook e células marcadas com TODO para vocês preencherem."
```

## Slide 7 · Bloco B · Demonstração ao vivo

```
⏱ 19h25 às 19h27 (2 min)  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Abertura da demonstração ao vivo. Felipe assume a tela e compartilha o notebook do professor.

"Agora nós vamos para os vinte minutos de demonstração.
Ninguém precisa digitar nada agora: olhem para a minha tela.
Vou percorrer o notebook, executar célula por célula e mostrar o comportamento do código."
```

## Slide 8 · SCIKIT-LEARN NA PRÁTICA

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Explicar a simplicidade da API do scikit-learn.

"Reparem nestas quatro linhas de código. Elas resumem o coração do scikit-learn.
Primeiro você importa o modelo desejado.
Depois você instancia o estimador, definindo opções como profundidade máxima.
Em seguida você chama fit passando X e y de treino. É aqui que o computador trabalha.
E por fim você chama predict para gerar previsões no conjunto de teste.

O fascinante da biblioteca é que quando vocês forem treinar uma regressão logística ou
um random forest, o código será praticamente idêntico. O método é sempre fit e predict."
```

## Slide 9 · POR DENTRO DA ÁRVORE

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar Bevilaqua
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Explicar a leitura visual da árvore.

"Quando rodamos a função plot_tree no notebook, surge um diagrama em forma de árvore.
Cada caixa representa um nó de decisão.
No topo da caixa tem a pergunta de corte: por exemplo, valor menor ou igual a trezentos reais.
Se for sim, o dado desce para a esquerda. Se for não, desce para a direita.

Logo abaixo tem o índice de Gini, que mede a impureza. Se tiver zero, significa que todas
as transações ali são de uma classe só.
E embaixo tem a contagem exata de quantas compras legítimas e quantas fraudes caíram ali.
É por isso que equipes de auditoria adoram árvores: você consegue justificar cada decisão."
```

## Slide 10 · MATRIZ DE CONFUSÃO

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Ligação direta com finanças e negócio.

"Na segunda-feira nós aprendemos os quatro quadrantes da matriz de confusão.
Hoje nós vamos colocar preço neles.
O Verdadeiro Positivo economiza o dinheiro da fraude roubada.
O Falso Positivo custa caro: gera ligação furiosa no atendimento, retrabalho e risco de
perder o cliente para a concorrência.
O Falso Negativo é o prejuízo puro: a fraude aconteceu e o banco assume a perda.
E o Verdadeiro Negativo é o negócio funcionando em paz.

No notebook, criamos uma fórmula simples que calcula o ganho líquido em reais.
É esse número que vende o projeto internamente."
```

## Slide 11 · Bloco C · Mecânica da prática

```
⏱ 19h45 às 19h48 (3 min)  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Abertura das instruções práticas antes da mão na massa.

"Agora é a vez de vocês. Vamos explicar como a atividade vai funcionar para ninguém
ficar perdido nos próximos quarenta e cinco minutos."
```

## Slide 12 · INSTRUÇÕES DE ACESSO

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Passo a passo operacional para salvar a cópia.

"Primeiro passo operacional: abram o link do Google Colab.
Segundo passo: cliquem em Arquivo e depois em Salvar uma cópia no Drive.
Se vocês tentarem editar direto no link compartilhado, o Colab vai avisar que o arquivo
está protegido para edição.
Depois de salvar sua cópia, rodem o Passo 0."
```

## Slide 13 · REGRAS DA PRÁTICA

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar Bevilaqua
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Orientações de suporte e atitude.

"Algumas regras para o nosso laboratório render bem.
Rode sempre as células de cima para baixo. Se você pular para o Passo 3 sem ter rodado
o Passo 2, o Python vai reclamar que X_train não existe.
Onde tiver a marcação TODO, complete o código antes de rodar.
E se aparecer alguma mensagem em vermelho na tela: mantenha a calma. Leia a última linha
do erro. Se não entender, mande no chat dizendo: 'travei no Passo 4 com tal mensagem'.
Os mentores e nós dois estaremos atentos para destravar todo mundo."
```

## Slide 14 · Bloco D · Mão na massa

```
⏱ 20h00 às 20h02 (2 min)  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Liberação da turma para a prática. Cronômetro iniciado na tela.

"Valendo, pessoal! Quarenta e cinco minutos de código no Colab.
Nós vamos colocar um cronômetro na tela e acompanhar vocês pelo chat."
```

## Slide 15 · MARCOS DE PROGRESSO

```
⏱ 45 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Roteiro de acompanhamento durante os 45 minutos.

Minuto 0 a 10:  conferir se todo mundo salvou a cópia e rodou o Passo 0 sem problemas.
Minuto 10 a 20: circular nas dúvidas do chat. Focar em quem teve problema com imports.
Minuto 20 a 30: avisar no microfone: "quem já gerou a matriz de confusão, olhe o valor de recall".
Minuto 30 a 40: avisar que faltam 15 minutos e pedir para avançarem para o Passo 5 (overfitting).
Minuto 40 a 45: aviso final de 5 minutos e preparação para a interação no chat.
```

## Slide 16 · INTERAÇÃO AO VIVO

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Condução da interação no chat após a prática.

"Vamos ver o que as máquinas de vocês descobriram.
Olhem para o diagrama da árvore no Passo 3. Qual foi a variável que o algoritmo escolheu
no primeiro retângulo, lá no topo?
Escrevam no chat: foi valor ou foi hora? E qual foi o número de corte?"

LER 3 OU 4 RESPOSTAS DO CHAT:
"O algoritmo do Lucas cortou em valor menor que trezentos. A da Mariana também.
Isso mostra que mesmo rodando em máquinas separadas, o critério matemático do ganho
de informação convergiu para a mesma regra de negócio."
```

## Slide 17 · O TESTE DO OVERFITTING

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar Bevilaqua
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Conclusão do experimento de overfitting do Passo 5.

"Olhem para o gráfico de overfitting que vocês acabaram de gerar no Passo 5.
A linha azul do treino sobe até encostar em cem por cento quando a árvore é livre.
Mas a linha vermelha do teste atinge um pico na profundidade três ou quatro e depois
começa a cair.

Isso é a prova visual do que discutimos na segunda-feira: se você deixa a árvore livre,
ela decora o ruído do treino. O estudante que decora as questões da prova anterior tira
dez no simulado e zera a prova oficial quando trocam as perguntas.
Por isso a poda é obrigatória em árvores de decisão."
```

## Slide 18 · Bloco E · Síntese e encerramento

```
⏱ 20h45 às 20h48 (3 min)  |  ESSENCIAL  |  Apresenta: Edmar Bevilaqua
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Abertura da síntese final da noite.

"Chegamos ao Bloco E. Vamos amarrar as principais conclusões desta noite e falar sobre
o que vem na reta final do nosso programa."
```

## Slide 19 · O QUE A GENTE VIU HOJE

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar Bevilaqua
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Recapitulação numerada em voz alta.

"Cinco ideias para levar da nossa noite de hoje.
A primeira: nunca avaliem problemas de fraude ou evento raro olhando apenas a acurácia.
Segunda: usem sempre amostragem estratificada para dividir treino e teste.
Terceira: a árvore de decisão é a melhor porta de entrada para Machine Learning porque
ela gera regras que qualquer pessoa de negócio consegue auditar.
Quarta: traduzam métricas em dinheiro: falsos positivos e falsos negativos têm impactos
comerciais completamente diferentes.
E quinta: controlem a profundidade para o modelo aprender a pensar, e não apenas a decorar."
```

## Slide 20 · O ARCO DO PROGRAMA

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar Bevilaqua
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Ponte institucional e motivação da turma.

"Olhem para a coluna da esquerda. Vocês começaram na Semana 1 aprendendo a estruturar
um problema de negócio sem abrir código.
Passaram por SQL, pandas, pipelines de dados e hoje treinaram o primeiro modelo preditivo.
Vocês percorreram todo o ciclo de vida de uma solução de Inteligência Artificial.

Nas próximas duas semanas, na Etapa 2, vocês vão aplicar esse conjunto de ferramentas
em squads para resolver desafios reais que serão apresentados no Demo Day."
```

## Slide 21 · PERGUNTAS FREQUENTES

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar Bevilaqua e Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Perguntas previsíveis da noite de hoje:

• "Por que a árvore escolheu 'valor' e não 'hora' no nó raiz?"
  Porque matematicamente a divisão por valor gerou uma redução maior de impureza
  (maior ganho de informação) do que a divisão por hora naquele ponto específico.

• "Posso usar essa mesma lógica para prever cancelamento de clientes (churn)?"
  Exatamente a mesma. Churn também é um problema de classificação com classes desbalanceadas.

• "Como escolher o melhor max_depth na prática corporativa?"
  Geralmente usamos validação cruzada (GridSearchCV) para testar várias profundidades
  automaticamente e escolher a que obtém o melhor F1 ou recall no conjunto de validação.

• "Os notebooks resolvidos ficarão disponíveis?"
  Sim, o notebook do professor com todos os gabaritos comentados será enviado logo após a aula.
```

## Slide 22 · Obrigado!

```
⏱ 1 min  |  ESSENCIAL  |  Apresenta: Felipe André Bach Alves
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Fechamento da aula (30 segundos).

"Parabéns pelo trabalho de hoje! Treinar o primeiro modelo de Machine Learning é um marco
na carreira de qualquer profissional de dados.
Salvem seus notebooks, continuem praticando e nos vemos na segunda-feira.
Boa noite a todos!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Enviar o link do notebook do professor no canal do Discord.
- Realizar retrospectiva de 10 minutos entre Edmar e Felipe sobre onde os alunos mais travaram.
```
