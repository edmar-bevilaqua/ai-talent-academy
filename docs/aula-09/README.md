# Aula 9: Semana 5, segunda-feira

Pacote da nona aula do **AI Talent Academy**, no padrão visual White Cube.
Tema: **Engenharia de Dados** · 19h00 às ~23h20 · online · aula expositiva
Condução: Edmar Bevilaqua (aula inteira)

> **Esta é a versão rica, para vocês cortarem.** Por pedido explícito do usuário, em
> duas rodadas, o escopo cresceu para cobrir tudo do brainstorming original mais um
> aprofundamento posterior em processamento distribuído (Spark, Databricks), sem
> preocupação com caber em 3h. O resultado são 50 slides e ~4h20 de fala, contra o
> padrão de 3h. A seção "Mapa de corte sugerido", mais abaixo, indica por onde cortar
> primeiro se a aula precisar voltar para perto de 3h.

Segue a regra das segundas: sem código ao vivo, sem mão na massa. A prática de verdade
fica para a Aula 10 (quinta), que ainda não foi produzida.

---

## O que tem aqui

| Arquivo | O que é | Para quem |
|---|---|---|
| **`AI-Talent-Academy-Aula09.pptx`** | O deck: 50 slides, com roteiro de fala nas notas | Edmar |
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
| 22h10 às 22h50 | Processamento distribuído (MapReduce, Hadoop, Spark, Databricks) | 36 a 43 |
| 22h50 às 23h05 | Do problema ao pipeline (caso de fraude ponta a ponta) | 44 e 45 |
| 23h05 às 23h20 | Encerramento | 46 a 50 |

Total síncrono de ~4h20, quase uma hora e meia além do padrão de 3h. Diferente do
ajuste fino de outras aulas, este estouro veio de duas decisões explícitas e
sucessivas de trazer mais escopo, para decidir o corte só depois de ver tudo montado.

---

## Mapa de corte sugerido

Se a aula precisar voltar para perto de 3h, esta é a ordem recomendada de corte, do
mais fácil ao mais custoso:

1. **Slide 18, bônus Data Lakehouse** (4 min). Já nasceu marcado como DESCARTÁVEL nas
   notas. Se cortar, ajuste a fala do slide 18 para não prometer mais "a história
   completa vem mais à frente", já que o bloco de processamento distribuído continua
   valendo mesmo sem esse gancho.
2. **Slides 44 e 45, fechamento com o caso de fraude** (15 min). Forte para fixação,
   mas não introduz conceito novo, só amarra o que já foi dito.
3. **Uma das três interações do meio** (slides 12, 24 ou 43, ~5 min cada). Reduz
   engajamento, mas não reduz conteúdo.
4. **A rivalidade Inmon x Kimball** (slide 22, 8 min). É a parte mais história, e a
   aula sobrevive só com o conceito de ETL x ELT sem a origem.
5. **O bloco de processamento distribuído inteiro** (slides 36 a 43, 40 min). É o
   corte mais custoso do deck, porque foi pedido explicitamente numa segunda rodada.
   Considere primeiro reduzir a MapReduce e Hadoop (36 a 38) como história rápida, sem
   cortar Spark e Databricks, que são os nomes mais citados hoje no mercado.
6. **Um dos três blocos de tipo de banco** (slides 14 a 16, ~6 min cada). Só corte se
   ainda faltar tempo depois de tudo acima, porque esses três sustentam a tabela
   comparativa do slide 17.

---

## Decisões de conteúdo desta aula

| Decisão | O que foi combinado |
|---|---|
| **Escopo original** | Brainstorm completo aprovado pelo usuário: fontes de dados, lote x fluxo, os três tipos de armazenamento (com Lakehouse como nota), ETL x ELT com a história Inmon x Kimball, qualidade de dados, DAG, Airflow, dbt, e um fechamento ponta a ponta |
| **Aprofundamento posterior** | Depois de revisar a primeira versão, o usuário pediu mais profundidade especificamente em Spark, Databricks e processamento distribuído, que a v1 não cobria |
| **Nome de ferramenta com história** | Airflow, dbt, e agora também Hadoop, Spark e Databricks entram nomeados, no mesmo tratamento histórico que já funcionou com NumPy, pandas, Matplotlib e Seaborn na Aula 7 |
| **Fechamento com o caso de fraude** | Os blocos 44 e 45 desenham o pipeline completo do caso que a turma já conhece desde a Aula 2, aplicando cada conceito do dia |
| **Amarração com a Aula 1** | O pipeline de 8 fases da Aula 1 volta logo na abertura (slide 5), mostrando que hoje fecha as fases 2 e 4, que ficaram em aberto |
| **Ponte pandas → Spark** | O bloco de processamento distribuído usa um exemplo de código comparando pandas com PySpark lado a lado (slide 40), mostrando que a sintaxe é quase igual de propósito |
| **Mão na massa** | Zero, mantém a regra das segundas |
| **Condução** | Edmar sozinho, aula inteira, mesmo padrão das Aulas 5 e 7 |

### Ganchos com as aulas anteriores

- O slide 5 reaproveita o layout do pipeline de 8 fases já usado nas Aulas 1 e 2
- O bloco de qualidade de dados (25 a 29) amarra direto com NULL (Aula 5) e NaN/dtype
  (Aula 7)
- O bloco de processamento distribuído (36 a 43) amarra direto com o `groupby` de
  pandas ensinado na Aula 7
- O bônus de Data Lakehouse (slide 18) planta o nome Databricks, que só recebe a
  história completa mais à frente, no slide 41
- O fechamento (44 e 45) reaproveita as mesmas 6 tabelas do caso de fraude das Aulas
  2, 5, 6, 7 e 8
- O bloco final aponta para a Aula 10 (quinta) e para a Aula 11 (Machine Learning,
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
      roteiro impresso já sem os slides removidos. Com quase 1h30 de excesso sobre o
      padrão de 3h, algum corte é praticamente obrigatório

**Conteúdo:**
- [ ] Conferir os anos citados na linha do tempo Inmon x Kimball (slide 22) contra uma
      fonte, antes de apresentar como fato fechado
- [ ] Conferir os anos e nomes citados no bloco de processamento distribuído (slides
      38, 39 e 41: paper do Google 2004, Hadoop, Spark 2009, Databricks 2013) contra
      uma fonte, pelo mesmo motivo
- [ ] Confirmar o escopo real da Aula 10 (quinta), para os slides de "próximos
      encontros" não prometerem algo que a prática não vai entregar

**Ensaio:**
- [ ] Ensaiar o bloco de ETL x ELT (19 a 24) em voz alta. É o bloco com mais nome
      próprio e mais data do primeiro escopo, o que mais exige fluência para não soar
      decorado
- [ ] Ensaiar o bloco de processamento distribuído (36 a 43) em voz alta, pelo mesmo
      motivo, agora sendo o bloco com mais nome próprio e mais data do deck inteiro
- [ ] Cronometrar a aula inteira pelo menos uma vez, mesmo já sabendo que vai passar
      de 3h, para calibrar o corte real do dia

**Operacional:**
- [ ] Criar as 3 enquetes com antecedência (slides 12, 24 e 43)
- [ ] Instalar a fonte Roboto em quem for apresentar pelo PowerPoint
