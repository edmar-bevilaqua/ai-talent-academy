# Aula 3: Semana 2, segunda-feira

Pacote da terceira aula do **AI Talent Academy**, no padrão visual White Cube.
Tema: **IA Generativa** · 19h00 às ~22h11 · online · ~190 participantes
Condução: Edmar Bevilaqua + Felipe André Bach Alves

> A ordem das semanas foi ajustada com as lideranças. A proposta comercial original não
> previa uma aula dedicada só a GenAI, e essa mudança já está acordada.

> ⚠️ **A aula esticou de 3h para ~3h11 por decisão deliberada.** Depois de validar com o
> usuário, dois assuntos entraram no bloco 3: banco vetorial e RAG × fine-tuning. Isso
> soma 11 minutos e empurra o encerramento para perto de 22h11, não 22h00. Ver a seção
> "Decisões de conteúdo" abaixo.

---

## O que tem aqui

| Arquivo | O que é | Para quem |
|---|---|---|
| **`AI-Talent-Academy-Aula03.pptx`** | O deck: 47 slides, com roteiro de fala nas notas | Vocês dois |
| [`01-plano-da-aula.md`](01-plano-da-aula.md) | Cronômetro, marcos de corte, cuidados desta aula, riscos | Vocês dois |
| [`02-roteiro-do-apresentador.md`](02-roteiro-do-apresentador.md) | Todas as notas do deck em markdown imprimível | Vocês dois |
| [`03-material-de-apoio-participante.md`](03-material-de-apoio-participante.md) | Resumo, glossário e tarefas até quinta | Participantes (pós-aula) |

---

## Estrutura da aula

| Horário | Bloco | Quem | Slides |
|---|---|---|---|
| 19h00 às 19h10 | Recepção | Edmar + moderador | 1 e 2 |
| 19h10 às 19h20 | Abertura, por que uma noite inteira | Edmar | 3 a 6 |
| 19h20 às 19h55 | IA Generativa na prática | Edmar | 7 a 14 |
| 19h55 às 20h30 | Como um LLM funciona por dentro | Edmar | 15 a 24 |
| 20h30 às 20h45 | Intervalo | (os dois) | 25 |
| 20h45 às 21h36 | Prompt, contexto e limites | Felipe | 26 a 37 |
| 21h36 às 22h01 | Onde GenAI resolve e onde atrapalha | Felipe | 38 a 42 |
| 22h01 às 22h11 | Recap e Q&A | Felipe + Edmar | 43 a 47 |

---

## Decisões de conteúdo desta aula

| Decisão | O que foi combinado |
|---|---|
| **Ordem dos blocos** | Prática → por dentro → prompt → onde resolve. Motiva, explica o mecanismo, ensina a operar, fecha com julgamento crítico |
| **Profundidade técnica** | Conceitual expandido: embeddings e atenção com analogia forte, sem fórmula e sem código |
| **Mão na massa** | Zero. Mantém a regra da Aula 1. Prompts aparecem como exemplo no slide, nunca ao vivo |
| **Condução** | Dividida por bloco, como na Aula 1. Edmar antes do intervalo, Felipe depois |
| **Aprofundamento extra** | Depois de validar que parte da turma pede mais profundidade, banco vetorial e RAG × fine-tuning entraram no bloco 3, esticando a aula em 11 min em vez de cortar conteúdo existente |
| **Denso × esparso** | Ficou como uma frase dentro do slide de banco vetorial (35), não virou slide próprio. É conceito mais técnico, melhor encaixado numa semana com Colab do lado |

### Por que banco vetorial entrou e denso × esparso não virou slide

O pedido original incluía três conceitos: RAG expandido, banco vetorial e denso × esparso.
Banco vetorial entrou porque é continuação direta de algo que já estava no deck: o
embedding (slide 18) já ensina "texto vira coordenada", e banco vetorial é só "onde essas
coordenadas moram e como se busca nelas rápido". Denso × esparso exige entender dois
paradigmas de busca diferentes e quando combiná-los, que é decisão de arquitetura, um
degrau acima de alfabetização em GenAI. Por isso virou uma frase dentro do slide 35, e não
um slide dedicado.

Comparação de modelos e aprofundamento em agentes de IA foram descartados de propósito:
o primeiro data rápido e favorece marca sem querer, o segundo compete com o conteúdo já
reservado para a Semana 7.

### Ganchos com as aulas anteriores

O deck amarra de propósito com o que já foi ensinado. Vale saber onde, para reforçar na fala:

- **Slide 13** retoma o caso do advogado de Londrina (alucinação, Aula 1)
- **Slide 16** recapitula os 90 segundos de LLM da Aula 1 e cumpre a promessa de aprofundar
- **Slide 24** explica tecnicamente a alucinação que a Aula 1 pediu para aceitar
- **Slide 34** (RAG) usa o embedding do slide 18 como base
- **Slide 35** (banco vetorial) também parte do embedding do slide 18
- **Slide 39** reabre a escada de ferramentas da Aula 1
- **Slide 41** usa a temperatura do slide 21 para explicar por que a conta não é reproduzível

---

## Layout novo nesta aula

Esta aula introduziu o `sl_prompt`, que compara prompt fraco e prompt bom lado a lado
(slides 29, 30 e 31). Ele é **adaptativo**: a régua divisória acompanha o prompt mais longo
dos dois lados, então dá para escrever prompts de tamanhos diferentes sem quebrar o layout.

A constante `alt_linha = 0.40"` foi medida no render, e não estimada. Se mudar `S_MIN` ou o
`line` do bloco de texto, essa constante precisa ser remedida.

---

## Regerando o deck

```bash
python scripts/gerar_slides_aula03.py     # regera o .pptx
python scripts/exportar_roteiro_aula03.py # regera o roteiro em markdown
python scripts/auditar_vicios.py scripts/gerar_slides_aula03.py   # passo obrigatório
```

Rode os três sempre que mexer no conteúdo.

---

## Pendências antes da aula

**Conteúdo:**
- [ ] Confirmar o que exatamente a quinta-feira vai ter (o slide 45 promete Colab, API
      gratuita de LLM e comparação de temperatura). **Testar o notebook antes de prometer**
- [ ] Definir qual API gratuita será usada e validar que ela responde bem com 190 pessoas

**Ensaio:**
- [ ] Ensaiar o bloco 2 em voz alta, cronometrado. É o mais denso e o mais provável de estourar
- [ ] Treinar a pausa do slide 19 (as duas frases do prefeito). O exemplo só funciona se a
      sala resolver sozinha antes de você dar a resposta
- [ ] Ensaiar o bloco 3 completo com os dois slides novos, para confirmar se os 51 minutos
      previstos batem com o ritmo real de fala de vocês

**Operacional:**
- [ ] Criar as 2 enquetes com antecedência (slides 14 e 37)
- [ ] Moderador dedicado confirmado. Esta aula gera mais pergunta técnica que as anteriores
- [ ] Instalar a fonte Roboto em quem for apresentar pelo PowerPoint
- [ ] Avisar a turma com antecedência (e-mail ou Discord) que a aula vai até por volta de
      22h11, não 22h00, para quem precisa organizar a agenda

**Conferir:**
- [ ] O deck evita número volátil de propósito (preço de token, tamanho de janela, nome de
      modelo). Se for improvisar algum número na fala, confirme antes. Esses valores mudam
      de mês para mês
