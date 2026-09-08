# Aula 9: Semana 5, segunda-feira

Pacote da nona aula do **AI Talent Academy**, no padrão visual White Cube.
Tema: **Engenharia de Dados** · 19h00 às ~22h40 · online · aula expositiva
Condução: Edmar Bevilaqua (aula inteira)

> **Esta é a versão rica, para vocês cortarem.** Por pedido explícito do usuário, o
> escopo trouxe todos os pontos do brainstorming, incluindo os complementos (nome de
> ferramenta com história, e o fechamento ponta a ponta com o caso de fraude), sem
> preocupação com caber em 3h. O resultado são 42 slides e ~3h40 de fala, contra o
> padrão de 3h. A seção "Mapa de corte sugerido", mais abaixo, indica por onde cortar
> primeiro se a aula precisar voltar para 3h.

Segue a regra das segundas: sem código ao vivo, sem mão na massa. A prática de verdade
fica para a Aula 10 (quinta), que ainda não foi produzida.

---

## O que tem aqui

| Arquivo | O que é | Para quem |
|---|---|---|
| **`AI-Talent-Academy-Aula09.pptx`** | O deck: 42 slides, com roteiro de fala nas notas | Edmar |
| [`02-roteiro-do-apresentador.md`](02-roteiro-do-apresentador.md) | Todas as notas do deck em markdown imprimível | Edmar |

---

## Estrutura da aula

| Horário | Bloco | Slides |
|---|---|---|
| 19h00 às 19h10 | Recepção | 1 e 2 |
| 19h10 às 19h35 | A pergunta que ficou em aberto (pipeline da Aula 1 revisitado) | 3 a 7 |
| 19h35 às 20h00 | De onde vêm os dados (fontes, lote x fluxo) | 8 a 12 |
| 20h00 às 20h30 | Onde os dados moram (OLTP, Data Warehouse, Data Lake, Lakehouse) | 13 a 18 |
| 20h30 às 21h00 | ETL x ELT (com a rivalidade Inmon x Kimball) | 19 a 24 |
| 21h00 às 21h15 | Intervalo | nenhum |
| 21h15 às 21h40 | Qualidade de dados | 25 a 29 |
| 21h40 às 22h10 | Pipeline de verdade (DAG, Airflow, dbt) | 30 a 35 |
| 22h10 às 22h25 | Do problema ao pipeline (caso de fraude ponta a ponta) | 36 e 37 |
| 22h25 às 22h40 | Encerramento | 38 a 42 |

Total síncrono de ~3h40, quase 40 minutos além do padrão de 3h. Diferente do ajuste
fino de outras aulas, este estouro veio de uma decisão explícita de trazer o escopo
inteiro do brainstorming, para decidir o corte depois de ver tudo montado.

---

## Mapa de corte sugerido

Se a aula precisar voltar para perto de 3h, esta é a ordem recomendada de corte, do
mais fácil ao mais custoso:

1. **Slide 18, bônus Data Lakehouse** (4 min). Já nasceu marcado como DESCARTÁVEL nas
   notas. É o corte mais barato do deck.
2. **Slides 36 e 37, fechamento com o caso de fraude** (15 min). Forte para fixação,
   mas não introduz conceito novo, só amarra o que já foi dito.
3. **Uma das duas interações do meio** (slides 12 ou 24, ~5 min cada). Reduz
   engajamento, mas não reduz conteúdo.
4. **A rivalidade Inmon x Kimball** (slide 22, 8 min). É a parte mais "história", e a
   aula sobrevive só com o conceito de ETL x ELT sem a origem.
5. **Um dos três blocos de tipo de banco** (slides 14 a 16, ~6 min cada). Só corte se
   ainda faltar tempo depois dos itens acima, porque esses três sustentam a tabela
   comparativa do slide 17.

---

## Decisões de conteúdo desta aula

| Decisão | O que foi combinado |
|---|---|
| **Escopo** | Brainstorm completo aprovado pelo usuário: fontes de dados, lote x fluxo, os três tipos de armazenamento (com Lakehouse como nota), ETL x ELT com a história Inmon x Kimball, qualidade de dados, DAG, Airflow, dbt, e um fechamento ponta a ponta |
| **Nome de ferramenta com história** | Confirmado que sim: Airflow e dbt entram nomeados, no mesmo tratamento histórico que já funcionou com NumPy, pandas, Matplotlib e Seaborn na Aula 7 |
| **Fechamento com o caso de fraude** | Confirmado que sim: os blocos 36 e 37 desenham o pipeline completo do caso que a turma já conhece desde a Aula 2, aplicando cada conceito do dia |
| **Amarração com a Aula 1** | O pipeline de 8 fases da Aula 1 volta logo na abertura (slide 5), mostrando que hoje fecha as fases 2 e 4, que ficaram em aberto |
| **Mão na massa** | Zero, mantém a regra das segundas |
| **Condução** | Edmar sozinho, aula inteira, mesmo padrão das Aulas 5 e 7 |

### Ganchos com as aulas anteriores

- O slide 5 reaproveita o layout do pipeline de 8 fases já usado nas Aulas 1 e 2
- O bloco de qualidade de dados (25 a 29) amarra direto com NULL (Aula 5) e NaN/dtype
  (Aula 7)
- O fechamento (36 e 37) reaproveita as mesmas 6 tabelas do caso de fraude das Aulas
  2, 5, 6, 7 e 8
- O bloco H aponta para a Aula 10 (quinta) e para a Aula 11 (Machine Learning,
  semana 6)

---

## Regerando o deck

```bash
python scripts/gerar_slides_aula09.py     # regera o .pptx
python scripts/exportar_roteiro_aula09.py # regera o roteiro em markdown
python scripts/auditar_vicios.py scripts/gerar_slides_aula09.py   # passo obrigatório
```

---

## Pendências antes da aula

**Decisão do usuário:**
- [ ] Decidir o corte real, usando o "Mapa de corte sugerido" acima, e regerar o
      roteiro impresso já sem os slides removidos

**Conteúdo:**
- [ ] Conferir os anos citados na linha do tempo Inmon x Kimball (slide 22) contra uma
      fonte, antes de apresentar como fato fechado
- [ ] Confirmar o escopo real da Aula 10 (quinta), para os slides 40 e 41 não
      prometerem algo que a prática não vai entregar

**Ensaio:**
- [ ] Ensaiar o bloco de ETL x ELT (19 a 24) em voz alta. É o bloco com mais nome
      próprio e mais data, o que mais exige fluência para não soar decorado
- [ ] Cronometrar a aula inteira pelo menos uma vez, mesmo já sabendo que vai passar
      de 3h, para calibrar o corte real do dia

**Operacional:**
- [ ] Criar as 2 enquetes com antecedência (slides 12 e 24)
- [ ] Instalar a fonte Roboto em quem for apresentar pelo PowerPoint
