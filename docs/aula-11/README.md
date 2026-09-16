# Aula 11: Semana 6, segunda-feira

Pacote da décima primeira aula do **AI Talent Academy**, no padrão visual White Cube.
Tema: **Machine Learning** · 19h00 às 00h15 · online · aula expositiva
Condução: Edmar Bevilaqua (aula inteira)

Segue a regra das segundas: sem código ao vivo, sem mão na massa. A prática de
treinar um modelo de verdade fica para a Aula 12 (quinta), que ainda não foi
produzida.

> **Quinta versão deste deck.** Histórico rápido:
> 1. Primeira versão: ficou rasa demais em fundamentos.
> 2. Segunda versão: acrescentado o Bloco 03 (o que significa aprendizado, função
>    de perda, otimização, gradiente descendente, treino, inferência), e trocada a
>    numeração dos blocos de letras para números de dois dígitos.
> 3. Terceira versão: pedido urgente do usuário para não ficar só em métrica e
>    árvore de decisão. Acrescentado o Bloco 06, um cardápio cobrindo Regressão
>    Linear, Regressão Logística, Naive Bayes, SVM, Random Forest, XGBoost e
>    Stacking em duas tabelas de resumo.
> 4. Quarta versão: o usuário achou o Bloco 06 raso demais ainda ("só esses 4
>    slides? Podemos ter 60 slides sem problema"). Cada um dos sete modelos ganhou
>    tratamento próprio, história verificada incluída, em vez de uma linha de
>    tabela. O Bloco 06 foi de 4 para 19 slides, o deck foi de 50 para 65.
> 5. Quinta versão (esta): pedido específico por Redes Neurais, "o que é, conceito,
>    e como aprende". Vira o oitavo modelo do cardápio, com história (McCulloch e
>    Pitts 1943 até o backpropagation de 1986), conceito (um neurônio é o mesmo "a
>    vezes x mais b" do Bloco 03, com uma função de ativação), arquitetura (camadas)
>    e mecanismo (forward pass, função de perda, backpropagation, gradiente
>    descendente), fechando com a ponte para os LLMs da Aula 3. O deck foi de 65
>    para 70 slides. Duração segue deliberadamente não otimizada, a pedido do
>    usuário, e já passa da meia-noite.

---

## Uma decisão de conteúdo importante

Antes de escrever a primeira versão deste deck, conferi o script da Aula 1 e
descobri que ela já cobre, na Fase 5 e na Fase 6 do pipeline de 8 fases, boa parte
do que um brainstorm de "Machine Learning para iniciantes" proporia do zero:
baseline, treino e teste, overfitting (com a metáfora do aluno que decorou a
prova), e a própria armadilha da acurácia, com o exemplo de detectar fraude onde
sempre responder "não é fraude" acerta 99% e não pega nenhuma.

Este deck **não repete essa explicação**. Ele abre com um recap de uma frase por
conceito (slide 4) e vai direto para o que a Aula 1 não teve tempo de fazer:

- Como um modelo aprende por dentro: parâmetro, função de perda, otimização e
  gradiente descendente (a Aula 1 nunca chegou perto disso, ela ficou na avaliação,
  não no mecanismo de aprendizado).
- A matriz de confusão formal, com números de verdade (a Aula 1 só deu os nomes
  precisão, recall e F1, sem fazer a conta).
- Um algoritmo nomeado e explicado, com história real (a Aula 1 nunca nomeou um
  algoritmo específico), incluindo a diferença entre um modelo que aprende por
  gradiente descendente e um que aprende por escolha gulosa.
- Métricas de regressão, MAE, RMSE e R quadrado (a Aula 1 não cobriu nenhuma).
- Uma releitura do caso de viés da Aula 1 pela lente de "isto é um classificador".

Se uma futura revisão deste deck achar sobreposição com a Aula 1, o critério é
sempre este: a Aula 1 fica com a visão geral em uma frase, a Aula 11 fica com a
profundidade.

---

## O que tem aqui

| Arquivo | O que é | Para quem |
|---|---|---|
| **`AI-Talent-Academy-Aula11.pptx`** | O deck: 70 slides, com roteiro de fala nas notas | Edmar |
| [`02-roteiro-do-apresentador.md`](02-roteiro-do-apresentador.md) | Todas as notas do deck em markdown imprimível | Edmar |

---

## Estrutura da aula

| Horário | Bloco | Slides |
|---|---|---|
| 19h00 às 19h10 | Recepção | 1 e 2 |
| 19h10 às 19h20 | Bloco 01: Duas fases, de novo, agora a fundo (recap de uma frase por conceito) | 3 a 5 |
| 19h20 às 19h35 | Bloco 02: Que tipo de problema é esse (classificação, regressão, clusterização) | 6 a 9 |
| 19h35 às 20h10 | Bloco 03: Como uma máquina aprende de verdade (perda, otimização, gradiente descendente, treino, inferência) | 10 a 19 |
| 20h10 às 20h40 | Bloco 04: A matemática por trás da armadilha (matriz de confusão, precisão, recall, F1) | 20 a 26 |
| 20h40 às 21h10 | Bloco 05: Seu primeiro modelo (árvore de decisão, história e feature engineering) | 27 a 31 |
| 21h10 às 22h30 | Bloco 06: O cardápio de modelos de hoje (oito modelos, cada um com história, mecanismo e exemplo) | 32 a 55 |
| 22h30 às 22h45 | Intervalo | 56 |
| 22h45 às 23h15 | Bloco 07: Quando a resposta é um número (MAE, RMSE, R², Netflix Prize) | 57 a 62 |
| 23h15 às 23h35 | Bloco 08: Quando o modelo aprende o preconceito (releitura do caso de viés da Aula 1) | 63 a 65 |
| 23h35 às 00h15 | Bloco 09: Encerramento | 66 a 70 |

Total síncrono de 5h15, mais que o dobro do padrão de 3h, terminando depois da
meia-noite. Duração deliberadamente não otimizada nesta versão: o usuário pediu,
agora três vezes seguidas, para acrescentar conteúdo "sem se apegar ao tempo", e vai
decidir o corte real por conta própria. Vale um alerta direto, mesmo sem ação
automática: uma aula até 00h15 numa segunda-feira é pesado para uma turma que
trabalha no dia seguinte, e o corte deixou de ser só uma questão de ritmo de aula.
O Bloco 06 (cardápio de modelos) é agora o bloco mais longo do deck, 80 minutos
sozinho.

---

## Bloco 03: o que foi acrescentado

Nove slides novos, entre o recap de tipos de problema e a matriz de confusão:

1. **O que significa aprender, para uma máquina**: não é entender, é ajustar
   números até errar menos.
2. **Um exemplo mínimo**: uma reta, `valor_previsto = a × variável + b`, para
   apresentar o conceito de parâmetro sem esconder atrás de um algoritmo complexo.
3. **Função de perda**: como medir o erro, com MSE explicado passo a passo,
   plantando o gancho para o RMSE que aparece depois no Bloco 07.
4. **Otimização**: o problema de busca que o treino resolve.
5. **Gradiente descendente**: a metáfora da montanha na neblina, sentindo a
   inclinação do chão com os pés.
6. **Gradiente descendente, sem neblina**: o mecanismo real, passo a passo, com
   taxa de aprendizado como o tamanho de cada passo.
7. **Treinamento e inferência**: duas fases muito diferentes, e por que todo modelo
   em produção vive fazendo inferência, não treino.
8. **Parâmetro e hiperparâmetro**: a distinção que o resto do programa vai
   pressupor.
9. **A ponte honesta para a árvore de decisão**: a árvore de hoje NÃO usa gradiente
   descendente, ela decide por escolha gulosa. Gradiente descendente é o mecanismo
   de regressão, redes neurais e dos LLMs da Aula 3.

O item 9 é o mais importante do bloco do ponto de vista de rigor: sem ele, a aula
passaria a impressão de que todo modelo aprende do mesmo jeito, o que não é
verdade, e a árvore de decisão do Bloco 05 contradiria em silêncio tudo que acabou
de ser ensinado.

---

## Bloco 06: o que foi acrescentado (pedido urgente, duas rodadas)

Primeira rodada: quatro slides, duas tabelas resumindo sete modelos numa linha
cada, mais a ponte de volta ao Bloco 03. O usuário achou raso ("só esses 4 slides?
Podemos ter 60 slides sem problema"). Segunda rodada, o formato atual: cada um dos
sete modelos ganhou tratamento individual, no mesmo padrão de "ferramenta com
história" já usado em Airflow, dbt, Hadoop, Spark, Databricks (Aula 9) e CART
(Bloco 05 desta aula):

1. **Antes de começar**: por que a área tem tantos nomes de modelo, nenhum vence em
   tudo.
2. **Regressão Linear**: história (Legendre 1805, Gauss 1809, a disputa de
   prioridade, Galton 1886 batizando "regressão") + mecanismo e exemplo no caso de
   fraude.
3. **Regressão Logística**: história (a curva de Verhulst, 1838, criada para
   crescimento populacional, emprestada pela estatística do século 20) + mecanismo
   e exemplo.
4. **Naive Bayes**: história (o teorema de Bayes, publicado postumamente em 1763)
   + mecanismo e exemplo.
5. **SVM**: história (Vapnik na União Soviética dos anos 1960, kernel trick em
   1992, margem suave com Cortes em 1995) + mecanismo e limitação (não é a escolha
   óbvia para 1 milhão de linhas).
6. **Árvore de Decisão**: um slide de recap, apontando de volta para o Bloco 05.
7. **Random Forest**: história (o mesmo Breiman do CART, 2001) + mecanismo
   (bagging, votação) e por que reduz overfitting.
8. **XGBoost**: história (Chen e Guestrin, 2016, KDD) + mecanismo (boosting
   sequencial) e por que domina competição de dados em tabela.
9. **Stacking**: história (Wolpert, 1992, "stacked generalization") + mecanismo
   (meta-modelo) e o trade-off de complexidade, tudo num slide só, por ser o mais
   simples de resumir.
10. **Redes Neurais**: pedido à parte, na quinta versão ("o que é, conceito, e como
    aprende"). História em linha do tempo de 4 pontos (McCulloch e Pitts 1943,
    Rosenblatt 1958, o "inverno da IA" de Minsky e Papert 1969, o backpropagation
    de Rumelhart, Hinton e Williams 1986) + conceito (um neurônio artificial é o
    mesmo "a vezes x mais b" do Bloco 03, com uma função de ativação) + arquitetura
    (camada de entrada, oculta, saída, com o caso de fraude) + mecanismo (forward
    pass, função de perda, backpropagation calculando o gradiente de trás para
    frente) + quando usar e a ponte para os LLMs da Aula 3.
11. **Duas tabelas de resumo**, mantidas do formato anterior, agora como cola de
    revisão depois do aprofundamento, não como primeira exposição. A tabela de
    modelos individuais ganhou uma sexta linha, Redes Neurais.
12. **De volta à pergunta do Bloco 03**: mantido, fecha o bloco amarrando tudo à
    distinção gradiente descendente x escolha gulosa, agora citando Redes Neurais
    explicitamente entre os modelos que usam gradiente.

Todos os fatos históricos (datas, nomes, publicações) foram verificados via busca
antes de escrever, mesmo padrão de rigor das Aulas 9 e 10. Ver a tabela de fontes
na seção "Decisões de conteúdo" abaixo.

---

## Mapa de corte sugerido

Se a aula precisar voltar para perto de 3h, o corte é decisão do usuário desta vez,
e agora é um corte grande. Como referência:

1. **Os nove slides de história dentro do Bloco 06** (~28 min). Marcados
   `DESCARTÁVEL` nas notas do próprio deck (oito modelos individuais, mais a linha
   do tempo de Redes Neurais). Cortar todos preserva mecanismo, exemplo e quando
   usar de cada modelo, só perde a origem.
2. **Interação de trade-off de negócio, no Bloco 04** (5 min). Forte para
   engajamento, mas não introduz conceito novo.
3. **Bloco 08 inteiro, quando o modelo aprende o preconceito** (20 min). É uma
   releitura de um caso já visto na Aula 1, não conteúdo inédito. Se cortar, ajuste
   a recapitulação do encerramento para remover a última ideia.
4. **Interação do Bloco 02** (5 min). Reduz engajamento, não reduz conteúdo.
5. **O slide de parâmetro x hiperparâmetro, no Bloco 03** (3 min). Importante, mas
   é o único ponto do bloco de fundamentos que pode virar uma frase dentro de outro
   slide, se o tempo apertar.

Cortar só o item 1 (os nove slides de história) já devolve quase 30 minutos sem
perder nenhum mecanismo, exemplo ou critério de "quando usar". Combinado com os
itens 2 a 5, chega perto de 1h de corte, ainda deixando a aula bem acima de 3h: com
5h15 de partida, mesmo um corte generoso não devolve uma segunda-feira de duração
normal.

O Bloco 03 (fundamentos) e o núcleo mecanismo/exemplo de cada modelo no Bloco 06
não devem ser cortados: foram os motivos diretos das revisões deste deck. História
é o que sobra, de propósito, para ser a primeira coisa cortada.

---

## Decisões de conteúdo desta aula

| Decisão | O que foi combinado |
|---|---|
| **Numeração dos blocos** | Números de dois dígitos (01, 02, 03...), não letras. A primeira versão usou letras, por engano, divergindo do padrão já estabelecido na Aula 9 |
| **Fundamentos de verdade** | Bloco 03 inteiro, acrescentado a pedido do usuário: aprendizado, parâmetro, função de perda, otimização, gradiente descendente, treino, inferência, hiperparâmetro |
| **Cardápio de modelos, aprofundado duas vezes** | Bloco 06 inteiro: Regressão Linear, Regressão Logística, Naive Bayes, SVM, Random Forest, XGBoost, Stacking e Redes Neurais, cada um com história própria, além da Árvore de Decisão já vista. Redes Neurais entrou por pedido específico ("o que é, conceito, e como aprende"), depois do cardápio já existir |
| **Algoritmo âncora** | Árvore de decisão, escolhida por ser visual (fluxograma de perguntas sim ou não), auditável, e por ser a base de Random Forest e XGBoost. Agora explicitamente contrastada com gradiente descendente |
| **Zero código ao vivo** | Mantém a regra das segundas. Toda a prática de treinar um modelo de verdade é na Aula 12 |
| **Dataset do exemplo** | O caso de fraude em cartão, usado desde a Aula 2, agora tratado como classificação, e também como pano de fundo do exemplo mínimo de regressão do Bloco 03 e da arquitetura de rede neural do Bloco 06 |
| **Não duplicar a Aula 1** | Ver a seção "Uma decisão de conteúdo importante" acima. A rede neural também evita duplicar o marco "deep learning 2012" já fixado na Aula 1, e constrói a história em cima dele (1943 a 1986), não por cima |
| **Fatos históricos conferidos** | CART (Breiman e colegas, 1984), ID3 (Quinlan, 1986), Netflix Prize (2006 a 2009, RMSE, BellKor's Pragmatic Chaos), mínimos quadrados (Legendre 1805, Gauss 1809), "regressão" (Galton 1886), curva logística (Verhulst 1838), teorema de Bayes (publicado 1763), SVM (Vapnik anos 1960, Cortes e Vapnik 1995), Random Forest (Breiman 2001), XGBoost (Chen e Guestrin 2016), Stacking (Wolpert 1992), redes neurais (McCulloch e Pitts 1943, Rosenblatt 1958, Minsky e Papert 1969, Rumelhart/Hinton/Williams 1986). Todos verificados via busca antes de escrever |
| **Duração não otimizada** | O usuário pediu, três vezes seguidas, para não cortar por causa do tempo ("eu cuido disso", "podemos ter 60 slides sem problema", e o próprio pedido de Redes Neurais sem ressalva de tempo). O deck ficou com 5h15, terminando depois da meia-noite, e o corte fica para uma decisão futura do usuário |
| **Marcação de corte embutida** | Os nove slides de história dentro do Bloco 06 já nasceram marcados `DESCARTÁVEL` nas notas, para o corte futuro ser rápido de identificar |
| **Condução** | Edmar sozinho, aula inteira, mesmo padrão da Aula 9 |

### Ganchos com as aulas anteriores

- O Bloco 01 reabre o pipeline de 8 fases e o diagrama de círculos concêntricos da
  Aula 1, sem repetir a explicação, só o nome
- O Bloco 02, o Bloco 03, o Bloco 04 e o Bloco 06 usam o mesmo caso de fraude das
  Aulas 2, 5, 6, 7, 8, 9 e 10
- O Bloco 03 (gradiente descendente) planta um gancho explícito para os LLMs da
  Aula 3, que aprendem pelo mesmo mecanismo, e o Bloco 06 retoma esse gancho ao
  classificar cada modelo do cardápio, incluindo a ressalva sobre o XGBoost e o
  fechamento com Redes Neurais
- O Bloco 05 (feature engineering) reaproveita diretamente a técnica de
  transformação de coluna já ensinada em pandas na Aula 7, e o Bloco 05 volta a
  aparecer dentro do Bloco 06 como o modelo "Árvore de Decisão" do cardápio
- O bloco de Redes Neurais amarra direto com a Aula 1 (o marco "deep learning
  2012") e com a Aula 3 (os LLMs são redes neurais treinadas do mesmo jeito, em
  escala maior)
- O Bloco 08 releitura o caso de viés (reconhecimento facial, Aracaju) já
  apresentado na Aula 1
- O encerramento aponta para a Aula 12 (quinta), que vai treinar de verdade uma
  árvore de decisão sobre a base de fraude

---

## Regerando o deck

```bash
python scripts/gerar_slides_aula11.py       # regera o .pptx
python scripts/exportar_roteiro_aula11.py   # regera o roteiro em markdown
python scripts/auditar_vicios.py scripts/gerar_slides_aula11.py   # passo obrigatório
```

---

## Pendências antes da aula

**Conteúdo:**
- [ ] Decidir o corte real usando o "Mapa de corte sugerido" acima. 5h15 é mais do
      dobro do padrão de 3h e termina depois da meia-noite. O usuário pediu três
      vezes seguidas para não cortar por tempo, mas em algum ponto essa decisão
      precisa ser tomada antes do dia da aula, não durante
- [ ] Ensaiar o Bloco 03 (como uma máquina aprende) em voz alta pelo menos duas
      vezes. É o bloco tecnicamente mais denso do programa até agora, gradiente
      descendente precisa sair fluido, não lido
- [ ] Ensaiar o Bloco 06 (cardápio de modelos) em voz alta, é o bloco mais longo do
      deck, 80 minutos sozinho, com oito histórias e oito mecanismos para não
      misturar. O trecho de backpropagation merece um ensaio à parte
- [ ] Ensaiar o Bloco 04 (a matemática da armadilha) em voz alta, é o outro bloco
      mais denso, com mais número de cabeça

**Produção da Aula 12:**
- [ ] Confirmar o escopo real da Aula 12 (quinta): treinar uma árvore de decisão de
      verdade com scikit-learn, no Colab, sobre a base de fraude, para os slides de
      "próximos encontros" não prometerem algo que a prática não vai entregar
- [ ] Decidir se a Aula 12 reaproveita a mesma base de 1 milhão de transações da
      Aula 8 e 10, ou uma amostra menor para treinar mais rápido
- [ ] Decidir se a Aula 12 formaliza gradiente descendente em código (por exemplo,
      treinando também uma regressão logística, não só a árvore), já que o Bloco 03
      de hoje deixou o terreno preparado para isso

**Operacional:**
- [ ] Criar a enquete ou preparar a leitura do chat para as duas interações
      (Bloco 02 e Bloco 04)
- [ ] Instalar a fonte Roboto em quem for apresentar pelo PowerPoint
