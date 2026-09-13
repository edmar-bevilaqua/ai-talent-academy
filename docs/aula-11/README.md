# Aula 11: Semana 6, segunda-feira

Pacote da décima primeira aula do **AI Talent Academy**, no padrão visual White Cube.
Tema: **Machine Learning** · 19h00 às 22h55 · online · aula expositiva
Condução: Edmar Bevilaqua (aula inteira)

Segue a regra das segundas: sem código ao vivo, sem mão na massa. A prática de
treinar um modelo de verdade fica para a Aula 12 (quinta), que ainda não foi
produzida.

> **Segunda versão deste deck.** A primeira ficou rasa demais em fundamentos: o
> usuário pediu para resgatar o que significa aprendizado, função de perda,
> otimização, treinamento, inferência e gradiente descendente, e para trocar a
> numeração dos blocos de letras (A, B, C...) para números de dois dígitos (01, 02,
> 03...), no padrão já usado desde a Aula 9. As duas mudanças estão feitas: ver a
> seção "Bloco 03" abaixo para o conteúdo novo.

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
| **`AI-Talent-Academy-Aula11.pptx`** | O deck: 46 slides, com roteiro de fala nas notas | Edmar |
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
| 21h10 às 21h25 | Intervalo | 32 |
| 21h25 às 21h55 | Bloco 06: Quando a resposta é um número (MAE, RMSE, R², Netflix Prize) | 33 a 38 |
| 21h55 às 22h15 | Bloco 07: Quando o modelo aprende o preconceito (releitura do caso de viés da Aula 1) | 39 a 41 |
| 22h15 às 22h55 | Bloco 08: Encerramento | 42 a 46 |

Total síncrono de 3h55, quase uma hora além do padrão de 3h. O Bloco 03 (como uma
máquina aprende) é o coração técnico do deck, acrescentado inteiro na segunda
versão. O Bloco 04 (a matemática da armadilha) continua sendo o segundo mais denso.

---

## Bloco 03: o que foi acrescentado

Nove slides novos, entre o recap de tipos de problema e a matriz de confusão:

1. **O que significa aprender, para uma máquina**: não é entender, é ajustar
   números até errar menos.
2. **Um exemplo mínimo**: uma reta, `valor_previsto = a × variável + b`, para
   apresentar o conceito de parâmetro sem esconder atrás de um algoritmo complexo.
3. **Função de perda**: como medir o erro, com MSE explicado passo a passo,
   plantando o gancho para o RMSE que aparece depois no Bloco 06.
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

## Mapa de corte sugerido

Se a aula precisar voltar para perto de 3h:

1. **Interação de trade-off de negócio, no Bloco 04** (5 min). Forte para
   engajamento, mas não introduz conceito novo.
2. **O detalhe dos 20 minutos do Netflix Prize, no Bloco 06** (5 min). Memorável,
   mas é uma curiosidade histórica, não um conceito que a Aula 12 vai cobrar.
3. **Bloco 07 inteiro, quando o modelo aprende o preconceito** (20 min). É uma
   releitura de um caso já visto na Aula 1, não conteúdo inédito. Se cortar, ajuste
   a recapitulação do encerramento para remover a sétima ideia.
4. **Interação do Bloco 02** (5 min). Reduz engajamento, não reduz conteúdo.
5. **O slide de parâmetro x hiperparâmetro, no Bloco 03** (3 min). Importante, mas
   é o único ponto do bloco novo que pode virar uma frase dentro de outro slide, em
   vez de slide próprio, se o tempo apertar.

Cortando os itens 1, 2 e 4 (15 min) chega perto de 3h40. Cortar o item 3 também
aproxima bastante de 3h padrão, mas o Bloco 03 (fundamentos) não deve ser cortado:
foi o motivo direto da segunda versão deste deck.

---

## Decisões de conteúdo desta aula

| Decisão | O que foi combinado |
|---|---|
| **Numeração dos blocos** | Números de dois dígitos (01, 02, 03...), não letras. A primeira versão usou letras, por engano, divergindo do padrão já estabelecido na Aula 9 |
| **Fundamentos de verdade** | Bloco 03 inteiro, acrescentado a pedido do usuário: aprendizado, parâmetro, função de perda, otimização, gradiente descendente, treino, inferência, hiperparâmetro |
| **Algoritmo âncora** | Árvore de decisão, escolhida por ser visual (fluxograma de perguntas sim ou não), auditável, e por ser a base de Random Forest e XGBoost. Agora explicitamente contrastada com gradiente descendente |
| **Zero código ao vivo** | Mantém a regra das segundas. Toda a prática de treinar um modelo de verdade é na Aula 12 |
| **Dataset do exemplo** | O caso de fraude em cartão, usado desde a Aula 2, agora tratado como classificação, e também como pano de fundo do exemplo mínimo de regressão do Bloco 03 |
| **Não duplicar a Aula 1** | Ver a seção "Uma decisão de conteúdo importante" acima |
| **Fatos históricos conferidos** | CART (Breiman e colegas, 1984), ID3 (Quinlan, 1986) e o Netflix Prize (2006 a 2009, meta de 10% de RMSE, vencedor BellKor's Pragmatic Chaos) foram verificados via busca antes de escrever |
| **Condução** | Edmar sozinho, aula inteira, mesmo padrão da Aula 9 |

### Ganchos com as aulas anteriores

- O Bloco 01 reabre o pipeline de 8 fases e o diagrama de círculos concêntricos da
  Aula 1, sem repetir a explicação, só o nome
- O Bloco 02, o Bloco 03 e o Bloco 04 usam o mesmo caso de fraude das Aulas 2, 5, 6,
  7, 8, 9 e 10
- O Bloco 03 (gradiente descendente) planta um gancho explícito para os LLMs da
  Aula 3, que aprendem pelo mesmo mecanismo
- O Bloco 05 (feature engineering) reaproveita diretamente a técnica de
  transformação de coluna já ensinada em pandas na Aula 7
- O Bloco 07 releitura o caso de viés (reconhecimento facial, Aracaju) já
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
- [ ] Decidir o corte real usando o "Mapa de corte sugerido" acima. Quase uma hora
      de excesso sobre o padrão de 3h é significativo, mesmo com o Bloco 03 sendo
      inegociável
- [ ] Ensaiar o Bloco 03 (como uma máquina aprende) em voz alta pelo menos duas
      vezes. É o bloco tecnicamente mais denso do programa até agora, gradiente
      descendente precisa sair fluido, não lido
- [ ] Ensaiar o Bloco 04 (a matemática da armadilha) em voz alta, é o segundo mais
      denso, com mais número de cabeça

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
