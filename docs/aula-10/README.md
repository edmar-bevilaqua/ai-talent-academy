# Aula 10: Semana 5, quinta-feira

Pacote da décima aula do **AI Talent Academy**, no padrão visual White Cube.
Tema: **aplicação de Engenharia de Dados** · 19h00 às 21h00 · online · aula quase
inteiramente prática
Condução: Edmar Bevilaqua + Felipe André Bach Alves

Dois cenários combinados, exatamente como a Aula 9 prometeu no fechamento: uma
demonstração curta de Apache Airflow (só o instrutor, ninguém mais instala nada), e
uma prática completa de PySpark no Google Colab (toda a turma, pipeline de seis
passos, do extract até a reconciliação final).

---

## O que tem aqui

| Arquivo | O que é | Para quem |
|---|---|---|
| **`AI-Talent-Academy-Aula10.pptx`** | O deck: 21 slides, com roteiro de fala nas notas | Edmar + Felipe |
| [`02-roteiro-do-apresentador.md`](02-roteiro-do-apresentador.md) | Todas as notas do deck em markdown imprimível | Edmar + Felipe |
| [`00-guia-de-preparacao.md`](00-guia-de-preparacao.md) | Guia operacional: instalação do Airflow, setup do PySpark, roteiro de demonstração | Edmar |
| [`dag_fraude_aula10.py`](dag_fraude_aula10.py) | A DAG de demonstração do Airflow (extract, transform, load) | Edmar |
| [`Aula_10_Alunos_Engenharia_de_Dados_com_PySpark.ipynb`](Aula_10_Alunos_Engenharia_de_Dados_com_PySpark.ipynb) | O notebook da atividade prática, com `# TODO` para completar | Alunos |
| [`Aula_10_Professor_Engenharia_de_Dados_com_PySpark.ipynb`](Aula_10_Professor_Engenharia_de_Dados_com_PySpark.ipynb) | O mesmo notebook, resolvido, para demonstrar ao vivo e usar como gabarito | Edmar + Felipe |

---

## Estrutura da aula

| Horário | Bloco | Slides |
|---|---|---|
| 19h00 às 19h10 | Recepção | 1 e 2 |
| 19h10 às 19h25 | Bloco A: De volta à segunda (recap da Aula 9, os dois cenários, mecânica) | 3 a 6 |
| 19h25 às 19h45 | Bloco B: Apache Airflow, demonstração ao vivo | 7 a 10 |
| 19h45 às 20h00 | Bloco C: PySpark no Colab, mecânica da prática | 11 a 14 |
| 20h00 às 20h50 | Bloco D: Mão na massa, 50 minutos | 15 e 16 |
| 20h50 às 21h00 | Bloco E: Encerramento | 17 a 21 |

Total síncrono de 2h, o padrão das quintas. Sem intervalo, mesmo padrão das Aulas 2,
4, 6 e 8.

---

## O pipeline da atividade

O notebook do aluno tem seis passos, não quatro. As duas primeiras versões deste
pacote paravam em extract, transform, unify e load. Depois de revisar, ficou claro
que isso deixava pouco trabalho de verdade para o aluno fazer, então o pipeline
cresceu para cobrir o que um pipeline de produção realmente precisa:

1. **Extract**: lê as seis tabelas do caso de fraude (a mesma base de 1 milhão de
   transações da Aula 8).
2. **Transform, com quarentena**: em vez de só descartar linha ruim, separa
   `transacoes_validas` de `transacoes_rejeitadas`, com o motivo de cada rejeição.
   Na base atual a quarentena fica vazia (a base já chega limpa nesses três
   critérios), e o notebook explica por que isso não torna o passo inútil.
3. **Unify**: junta as seis tabelas, resolvendo a colisão de nome de coluna
   (`nome`, presente em `clientes`, `lojistas` e `categorias` com significados
   diferentes) com `.alias()`. Uma célula deliberadamente dá erro de referência
   ambígua antes da correção, mesmo padrão didático das versões anteriores.
4. **Bifurcação por regra de negócio**: separa `trilha_normal` (transações
   aprovadas) de `trilha_atencao` (recusadas ou contestadas), enriquecendo a
   segunda com o detalhe de `contestacoes` via `LEFT JOIN`.
5. **Load, em múltiplos destinos**: a trilha normal vai para Parquet particionado
   por estado, a trilha de atenção vira um CSV único, e ainda sai um resumo
   agregado por lojista.
6. **Reconciliação**: confere, com `assert`, que a soma de válidas e rejeitadas
   bate com o total extraído, e que a soma das duas trilhas bate com a base
   unificada.

Todos os números usados nos slides e nas notas (1.000.090 transações extraídas,
938.859 na trilha normal, 61.231 na trilha de atenção, quarentena vazia) foram
conferidos contra o CSV real da Aula 8 antes de escrever o conteúdo, não são
placeholder.

---

## Decisões de conteúdo desta aula

| Decisão | O que foi combinado |
|---|---|
| **Dois cenários, um só instala** | Airflow roda só na máquina do instrutor, para demonstração. PySpark roda no Colab de cada aluno, sem instalar nada local |
| **Correção de premissa registrada nos slides** | O plano original presumia que o Colab já vinha com PySpark pronto. Não vem: falta Java. O bloco C abre corrigindo isso, em vez de deixar o aluno descobrir sozinho no meio da prática |
| **Pipeline de seis passos, não quatro** | Pedido explícito do usuário: a versão de quatro passos (extract, transform, unify, load) estava rasa demais, os alunos mal precisavam decidir alguma coisa. Quarentena, bifurcação e reconciliação foram acrescentadas para dar peso de engenharia real ao exercício |
| **Bifurcação usa dado real, não sintético** | A coluna `status` (aprovada, recusada, contestada) já existe na base e já tem massa suficiente nas três categorias. Não foi necessário inventar um padrão de fraude novo para justificar a bifurcação |
| **Erro proposital mantido** | A colisão de coluna `nome` entre `clientes`, `lojistas` e `categorias` continua sendo usada de propósito, para o aluno bater num erro real do Spark antes de aprender `.alias()` |
| **Condução** | Dupla, como nas outras quintas: Felipe assume o bloco C (mecânica do PySpark), Edmar assume a demonstração do Airflow, os dois circulam durante a prática |

### Ganchos com as aulas anteriores

- O bloco A reabre com os três nomes que a Aula 9 só descreveu (DAG, Airflow,
  Spark), e promete que hoje eles rodam de verdade
- A DAG de demonstração usa a mesma base de fraude da Aula 6, e o pipeline do aluno
  usa a base de 1 milhão de transações da Aula 8
- O passo de unify reaproveita a mesma lição de consistência de dados ensinada no
  bloco de qualidade de dados da Aula 9
- O bloco de encerramento aponta para a Aula 11 (Machine Learning, semana 6), que
  volta ao formato conceitual das segundas

---

## Regerando o material

```bash
python scripts/gerar_slides_aula10.py       # regera o .pptx
python scripts/exportar_roteiro_aula10.py   # regera o roteiro em markdown
python scripts/auditar_vicios.py scripts/gerar_slides_aula10.py   # passo obrigatório
```

Os dois notebooks (`Aula_10_Alunos_...` e `Aula_10_Professor_...`) não têm gerador
de script: foram escritos e são editados diretamente como `.ipynb`, no mesmo padrão
já usado nos notebooks da Aula 8.

---

## Pendências antes da aula

**Ambiente (ver `00-guia-de-preparacao.md`):**
- [ ] Confirmar que os containers do Airflow ainda estão de pé na tarde do dia da
      aula (`docker compose ps`), e subir de novo se o computador reiniciou
- [ ] Confirmar que `aula10_pipeline_fraude` importa sem erro
      (`airflow dags list-import-errors`)
- [ ] Rodar o `Aula_10_Professor_...ipynb` do início ao fim, num Colab novo, no dia
      anterior à aula, para conferir que o setup de Java e PySpark ainda funciona
      igual

**Conteúdo:**
- [ ] Decidir se a atividade vira avaliação com Google Forms (padrão da Aula 8) ou
      entrega livre em notebook, sem nota
- [ ] Ensaiar o roteiro da demonstração do Airflow (bloco B) em voz alta pelo menos
      uma vez, cronometrando os 20 minutos

**Operacional:**
- [ ] Fixar, no Discord, o link do `Aula_10_Alunos_...ipynb` antes das 19h10
- [ ] Combinar com os mentores que vão circular durante os 50 minutos de prática:
      o erro de referência ambígua no passo 3 é esperado, não travar tentando
      "corrigir" antes de o aluno ler a explicação
- [ ] Gravar o vídeo de backup da demonstração do Airflow, para o caso de falha ao
      vivo (seção 2.7 do guia)
