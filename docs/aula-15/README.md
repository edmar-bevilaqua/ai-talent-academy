# Aula 15: Semana 8, segunda-feira

Pacote da última aula do **AI Talent Academy**, no padrão visual White Cube.
Tema: **Demo Day e encerramento do programa** · 19h00 · online
Condução: Edmar Bevilaqua + Felipe André Bach Alves

> **Este deck é deliberadamente curto**, a pedido explícito do usuário: "slides
> super sucintos e curtos". Não é uma aula de conteúdo novo. É o esqueleto que
> cerca a apresentação das squads para a banca, que acontece ao vivo e não tem
> slide nenhum neste `.pptx`.

---

## O que tem aqui

| Arquivo | O que é | Para quem |
|---|---|---|
| **`AI-Talent-Academy-Aula15.pptx`** | O deck: 13 slides, com roteiro de fala nas notas | Edmar + Felipe |
| [`02-roteiro-do-apresentador.md`](02-roteiro-do-apresentador.md) | Todas as notas do deck em markdown imprimível | Edmar + Felipe |

---

## ⚠️ O Bloco A precisa da sua edição antes da aula

Os slides 4 e 5 (seção "Antes de começar") foram deixados **de propósito** como
esqueleto, com a marcação visível "★ A PREENCHER PELO USUÁRIO ★" no lugar de
qualquer conteúdo real. O usuário pediu explicitamente para preencher essa parte
manualmente, com os detalhes reais de:

- Ordem de apresentação das squads
- Tempo disponível por squad, e o que fazer se alguém passar do tempo
- O que a banca vai avaliar
- Como funciona a devolutiva, e quando os aprovados são avisados

Não apresente esses dois slides sem editar antes: eles não têm informação real,
só a estrutura de onde ela deveria entrar.

---

## Estrutura da aula

| Bloco | O que é | Slides |
|---|---|---|
| Recepção | Abertura curta, mecânica do dia | 1 e 2 |
| Bloco A: Antes de começar | **Esqueleto a preencher.** Orientação sobre a apresentação | 3 a 5 |
| Bloco B: Oito semanas, um caminho só | O pedido principal desta rodada: recap rápido do curso inteiro | 6 a 9 |
| *(fora do deck)* | Apresentação das squads para a banca, ao vivo, sem slide | nenhum |
| Bloco C: Encerramento | Mensagem final, agradecimento, fechamento | 10 a 13 |

Este deck cobre só os bookends do dia. A apresentação das squads em si, que é o
grosso do tempo real do Demo Day, acontece ao vivo e não tem slide de instrutor.

---

## O recap do curso (Bloco B), o pedido principal desta rodada

Reaproveita o pipeline de 8 fases da Aula 1 como gancho ("lembram desse mapa? hoje
todas as oito fases já passaram pela mão de vocês"), depois resume as duas etapas
do programa em duas tabelas compactas:

- **Etapa 1, semanas 1 a 4**: panorama de dados e IA, IA Generativa, SQL, Python
  (NumPy, pandas, Matplotlib, Seaborn), fechando com a investigação de fraude em 1
  milhão de transações.
- **Etapa 2, semanas 5 a 8**: Engenharia de Dados com Airflow e PySpark, Machine
  Learning até o primeiro modelo treinado, Agentes de IA até o primeiro agente
  construído com MCP de verdade, e hoje.

Os temas de cada semana foram conferidos contra o `README.md` real de cada aula já
produzida (Aulas 1, 3 a 13), não vieram de memória solta. Aula 2, 4 e 6 não têm
`README.md` próprio (são pacotes mais simples, sem deck dedicado), então os temas
delas vieram do que já está documentado no `CLAUDE.md` e no histórico de produção.

---

## Regerando o deck

```bash
python scripts/gerar_slides_aula15.py       # regera o .pptx
python scripts/exportar_roteiro_aula15.py   # regera o roteiro em markdown
python scripts/auditar_vicios.py scripts/gerar_slides_aula15.py   # passo obrigatório
```

---

## Pendências antes da aula

**Conteúdo, prioridade máxima:**
- [ ] Preencher o Bloco A (slides 4 e 5) com a orientação real da apresentação
- [ ] Confirmar se Ale e Márcio, da diretoria da White Cube, participam do
      encerramento. Se sim, o slide de agradecimento (slide 11) tem uma nota
      sugerindo o momento natural para a fala institucional deles, no mesmo
      espírito de como abriram a Aula 1

**Operacional:**
- [ ] Confirmar a banca de avaliação e a ordem real das squads antes de editar o
      Bloco A
- [ ] Combinar com a organização o processo de certificado e os próximos passos
      dos aprovados para a Etapa 2, fora deste deck
- [ ] Instalar a fonte Roboto em quem for apresentar pelo PowerPoint
