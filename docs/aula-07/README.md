# Aula 7: Semana 4, segunda-feira

Pacote da sétima aula do **AI Talent Academy**, no padrão visual White Cube.
Tema: **Análise de Dados com Python, com foco em pandas** · 19h00 às ~23h05 · online ·
aula expositiva
Condução: Edmar Bevilaqua (aula inteira)

> **Esta aula esticou de propósito**, de ~3h05 para ~4h05, por pedido explícito do
> usuário. O bloco de pandas estava raso demais para o peso que essa ferramenta tem no
> dia a dia de quem analisa dados, e o pedido foi claro: aprofundar, não resumir. O
> bloco de pandas sozinho passou de 8 para 20 slides. Ver a seção "Decisões de
> conteúdo" abaixo.

Segue a regra das segundas: sem código ao vivo obrigatório, sem mão na massa da turma.
Todo exemplo aparece como slide, com o código num bloco destacado e a explicação em
bullets logo abaixo, igual ao padrão de consulta SQL da Aula 5. A prática de verdade,
com cada aluno escrevendo o próprio código, fica para a Aula 8 (quinta), que ainda não
foi produzida.

A exceção é `demonstracao_pandas.ipynb`: um notebook que o instrutor pode rodar ao
vivo, célula por célula, se quiser mostrar o código de verdade funcionando durante a
aula, sem quebrar a regra de que os alunos não escrevem nada. Ver a seção
"Demonstração ao vivo" abaixo.

---

## O que tem aqui

| Arquivo | O que é | Para quem |
|---|---|---|
| **`AI-Talent-Academy-Aula07.pptx`** | O deck: 46 slides, com roteiro de fala nas notas | Edmar |
| [`02-roteiro-do-apresentador.md`](02-roteiro-do-apresentador.md) | Todas as notas do deck em markdown imprimível | Edmar |
| [`demonstracao_pandas.ipynb`](demonstracao_pandas.ipynb) | Material de apoio: NumPy, pandas, Matplotlib e Seaborn, código de verdade | Edmar |

---

## Estrutura da aula

| Horário | Bloco | Slides |
|---|---|---|
| 19h00 às 19h10 | Recepção | 1 e 2 |
| 19h10 às 19h25 | De onde vêm as ferramentas que você já usa | 3 a 6 |
| 19h25 às 20h00 | A história do Python (linha do tempo, nome, Zen, por que dominou dados) | 7 a 12 |
| 20h00 às 20h25 | NumPy (origem, array, operação vetorizada) | 13 a 16 |
| 20h25 às 20h40 | Intervalo | nenhum |
| 20h40 às 22h20 | pandas, 100 minutos (ver detalhamento abaixo) | 17 a 36 |
| 22h20 às 22h50 | Matplotlib e Seaborn (origem de cada um, um gráfico de cada) | 37 a 41 |
| 22h50 às 23h05 | Encerramento | 42 a 46 |

Total síncrono de ~4h05, quase uma hora além do padrão de 3h. Diferente do ajuste fino
de 5 ou 11 minutos das Aulas 3 e 5, este é um estouro grande e deliberado, avisado à
turma logo no início da aula (slide 6, e de novo em voz alta na transição para o bloco
de pandas).

### O bloco de pandas, por dentro (slides 17 a 36)

| Sub-bloco | Conteúdo | Slides |
|---|---|---|
| Fundamentos | Origem, DataFrame e Series, o índice, ler CSV, tipos de dado, `info()`/`describe()`, `value_counts`/`nunique`, filtro, `loc`/`iloc`, interação | 17 a 27 |
| O dia a dia de quem analisa | Valores ausentes (NaN), coluna derivada, `groupby`, `agg` com várias funções, `pivot_table` (conceito e exemplo), `merge`, glossário, interação final | 28 a 36 |

---

## Decisões de conteúdo desta aula

| Decisão | O que foi combinado |
|---|---|
| **Escopo original** | História da linguagem Python, origem de cada uma das quatro bibliotecas (NumPy, pandas, Matplotlib, Seaborn), e exemplo de código de cada uma |
| **Ajuste de foco** | Depois de revisar a primeira versão, o usuário pediu para aprofundar especificamente pandas: mais operações comuns, e um glossário dos termos da área. NumPy, Matplotlib e Seaborn ficaram do jeito que já estavam |
| **Orçamento de tempo** | Entre esticar a aula, encolher NumPy/Matplotlib/Seaborn, ou encolher também a história do Python, o usuário escolheu esticar. Mesma lógica da Aula 3, numa escala bem maior |
| **Continuidade** | Todo exemplo de código usa o mesmo caso de fraude em cartão das Aulas 2, 5 e 6, incluindo os nomes reais de coluna (`id_lojista`, `id_cartao`, `valor`) |
| **Ponte com SQL** | Cada exemplo de pandas é apresentado como "a versão pandas de" um comando SQL já visto: filtro é WHERE, `groupby` é GROUP BY, `merge` é JOIN, valor ausente é NULL |
| **Mão na massa** | Zero, mantém a regra das segundas |
| **Condução** | Edmar sozinho, aula inteira, mesmo padrão da Aula 5 |

### Ganchos com as aulas anteriores

- Os exemplos de pandas reaproveitam literalmente `transacoes.csv` e `cartoes.csv` da
  Aula 6
- Cada exemplo de filtro, valor ausente, agrupamento e junção é apresentado como
  equivalente direto de um comando já ensinado na Aula 5 (WHERE, NULL, GROUP BY, JOIN)
- O bloco F aponta direto para a Aula 8 (quinta) e para a Aula 9 (Engenharia de Dados,
  semana 5)

---

## Material de apoio: notebook das quatro bibliotecas

`demonstracao_pandas.ipynb` cobre as quatro bibliotecas apresentadas na aula, não só
pandas, sem preocupação de caber num tempo de apresentação. É material de apoio para
ler, rodar e revisitar com calma, não um roteiro cronometrado.

| Seção | Conteúdo |
|---|---|
| 0. Preparação | Lê as 6 tabelas da Aula 6, converte `data_hora` para data de verdade |
| 1. NumPy | `to_numpy()`, funções estatísticas, operação vetorizada, indexação booleana, array 2D |
| 2. pandas | Índice, tipos de dado, raio-x (`info`/`describe`), valores únicos, filtro, `loc`/`iloc`, valores ausentes, coluna nova, `groupby`, `agg`, `pivot_table`, `merge` em cadeia |
| 3. Matplotlib | Gráfico de barras, gráfico de linha por mês, histograma |
| 4. Seaborn | Histograma, boxplot por canal, barras com agregação embutida |

Todas as 34 células de código executáveis (35 no total, descontando a célula que só
funciona dentro do Colab) foram rodadas em sequência contra os dados reais da Aula 6
antes de este notebook ser considerado pronto, sem nenhum erro.

**Como usar:** o notebook espera os CSVs na mesma pasta do pacote da Aula 6. Se ele
estiver na mesma pasta do Drive que `docs/aula-06/dados/csv/`, só ajuste
`PASTA_DADOS` na célula 2 para apontar para lá. Este notebook não conecta no FreeSQL,
não precisa de `oracledb` nem de credencial nenhuma: só lê os CSVs direto com pandas.

Use como preferir: como demonstração projetada ao vivo durante a aula, se sobrar
tempo e vontade, como leitura complementar para os alunos revisarem depois, ou os
dois. Os alunos não escrevem nada nele durante a aula, isso continua reservado para a
Aula 8.

---

## Layout novo nesta aula

Reaproveitou o `sl_query` da Aula 5, renomeado para `sl_code` por ser genérico o
suficiente para qualquer linguagem, não só SQL. Mesmo bloco destacado (fundo cinza
claro, borda azul, texto em negrito), agora mostrando Python em vez de consulta.

---

## Regerando o deck

```bash
python scripts/gerar_slides_aula07.py     # regera o .pptx
python scripts/exportar_roteiro_aula07.py # regera o roteiro em markdown
python scripts/auditar_vicios.py scripts/gerar_slides_aula07.py   # passo obrigatório
```

---

## Pendências antes da aula

**Conteúdo:**
- [ ] Confirmar se a Aula 8 (quinta desta semana) vai usar exatamente os exemplos de
      pandas prometidos aqui (`read_csv`, `info`/`describe`, filtro, `loc`/`iloc`,
      valores ausentes, `groupby`, `agg`, `pivot_table`, `merge`)
- [ ] Validar todos os exemplos de código rodando de verdade num notebook, contra o
      `transacoes.csv` e o `cartoes.csv` reais da Aula 6, antes de prometer o resultado
      em voz alta na aula
- [ ] Confirmar com a turma, com antecedência, que a aula desta semana vai até por
      volta de 23h05, para quem precisa se planejar

**Ensaio:**
- [ ] Ensaiar o bloco da história do Python em voz alta. É o bloco com mais fato e
      data, o que mais exige fluência para não soar decorado
- [ ] Ensaiar o bloco de pandas inteiro, cronometrado. Com 20 slides, é o mais fácil de
      estourar o tempo previsto de 100 minutos
- [ ] Praticar a transição de cada exemplo de pandas para o comando SQL equivalente,
      porque é o gancho que sustenta a lógica do bloco inteiro
- [ ] Praticar a explicação de `loc` versus `iloc` em voz alta. É o ponto do bloco com
      maior risco de confundir a turma, segundo o próprio roteiro

**Operacional:**
- [ ] Criar as 3 enquetes com antecedência (slides 12, 27 e 36)
- [ ] Instalar a fonte Roboto em quem for apresentar pelo PowerPoint
