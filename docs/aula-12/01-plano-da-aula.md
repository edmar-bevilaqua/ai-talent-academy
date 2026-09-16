# Plano da Aula 12: Semana 6, quinta-feira

**AI Talent Academy** · 19h00 às 21h00 · online · ~190 participantes
Condução: Edmar Bevilaqua (blocos A, D, E) + Felipe André Bach Alves (blocos B, C)

---

## 1. Objetivos da aula

Ao final dos 120 minutos, cada participante deve ser capaz de:

1. **Estruturar um pipeline básico de Machine Learning** com scikit-learn, separando preditores e alvo.
2. **Dividir dados com estratificação**, evitando vazamento de dados e preservando a proporção de fraudes no teste.
3. **Construir um baseline ingênuo** e provar por que acurácia de 97,5% é insuficiente em problemas desbalanceados.
4. **Treinar e inspecionar uma Árvore de Decisão**, interpretando as regras nos nós e folhas.
5. **Calcular o custo financeiro da matriz de confusão**, pesando falsos positivos e falsos negativos em reais.
6. **Diagnosticar overfitting na prática**, comparando o desempenho da árvore no conjunto de treino e no conjunto de teste.

---

## 2. Cronômetro operacional

| Início | Fim | Duração | Bloco | Quem | Slides |
|---|---|---|---|---|---|
| 19h00 | 19h10 | 10 min | Recepção e alinhamento do ambiente | Edmar + Felipe | 1 a 4 |
| 19h10 | 19h25 | 15 min | **Bloco A: A ponte com a teoria** | Edmar | 5 a 8 |
| 19h25 | 19h40 | 15 min | **Bloco B: Demonstração guiada no Colab** | Felipe | 9 a 11 |
| 19h40 | 20h40 | 60 min | **Bloco C: Mão na massa (atividade prática)** | Felipe e Edmar circulando | 12 e 13 |
| 20h40 | 20h55 | 15 min | **Bloco D: Discussão dos resultados e custos** | Edmar | 14 a 18 |
| 20h55 | 21h00 | 5 min | **Bloco E: Encerramento e conexões** | Edmar + Felipe | 19 a 22 |

### Marcos de controle

| Se às… | você não estiver em… | então adote esta ação |
|---|---|---|
| **19h26** | Slide 9 (início da demonstração) | Reduza o slide 8 e abra imediatamente o notebook do professor. |
| **19h42** | Slide 13 (projeção fixa da atividade) | Encurte a demonstração dos passos 3 e 4; mostre apenas o código já executado. |
| **20h20** | Metade da turma no Passo 4 | Avise no chat: "Quem concluiu o passo 3, pule direto para o cálculo financeiro do passo 5". |
| **20h42** | Slide 14 (abertura do debate) | Traga as respostas dos alunos no chat para a tela e analise o custo financeiro direto no slide 16. |
| **20h56** | Slide 19 (recapitulação) | Pule comentários adicionais do chat e foque nos 4 aprendizados definitivos do slide 20. |

> **Regra de ouro das quintas-feiras:** os 60 minutos de prática autônoma (Bloco C) são sagrados.
> Não consuma o tempo dos alunos com preleções longas. A demonstração inicial serve apenas para
> destravar a navegação no Colab.

---

## 3. Mapa essencial × descartável

### 🔴 Essencial (não cortar em hipótese alguma)

| Slide | Conteúdo | Motivo pedagógico |
|---|---|---|
| 3 | Objetivo prático da aula | Alinha o foco dos 190 participantes desde o início |
| 6 | As quatro colunas preditivas | Contextualiza a base de dados usada no laboratório |
| 8 | O paradoxo dos 97,5% | Demonstra o perigo de avaliar modelo desbalanceado por acurácia |
| 10 | Os seis passos do pipeline | Mapa mental de toda a atividade do aluno |
| 13 | Slide de projeção da atividade | Fica fixado na tela durante os 60 minutos com orientações claras |
| 15 | A matriz de confusão em quatro quadrantes | Conecta predição matemática ao impacto operacional |
| 16 | O cálculo financeiro em reais | Prova o valor de negócio do modelo de Machine Learning |
| 18 | O teste do overfitting | Mostra visualmente a diferença entre aprender regras e decorar dados |
| 20 | As quatro ideias consolidadas | Resumo memorável para o aluno levar para o trabalho |

### 🟡 Descartável (ordem de corte prioritária se o tempo apertar)

| Prioridade de corte | Slide | Conteúdo | Como proceder o corte |
|---|---|---|---|
| **1º a cortar** | 17 | Tabela comparativa detalhada dos três modelos | Mencione verbalmente apenas a coluna de custo financeiro final e passe ao próximo |
| **2º a cortar** | 7 | As três perguntas do Cientista de Dados | Resuma em uma única frase: "Testamos hipóteses antes de treinar qualquer algoritmo" |
| **3º a cortar** | 11 | Checklist de preparação antes de rodar | Peça apenas para confirmarem se o notebook foi copiado para o Drive pessoal |
| **4º a cortar** | 21 | Detalhes do laboratório da próxima semana | Mencione apenas a data da Aula 13 no fechamento |

---

## 4. Riscos operacionais e planos de contingência

| Risco | Probabilidade | Impacto | Ação de contingência |
|---|---|---|---|
| Aluno tenta editar o notebook sem fazer cópia | Alta | Médio | Mensagem padrão fixada no chat: "Menu Arquivo → Salvar uma cópia no Drive". Felipe reforça isso nos primeiros 2 minutos. |
| Erro de download ou restrição de rede corporativa | Média | Alto | O Passo 0 do notebook já traz gerador sintético determinístico com semente fixa. O aluno executa a célula e prossegue sem travar. |
| Dúvidas sobre nomes de colunas no `train_test_split` | Alta | Baixo | Felipe projeta a estrutura exata do dicionário de dados no slide 6 e o gabarito no Passo 1. |
| Aluno altera parâmetros e obtém números diferentes | Média | Baixo | Esclarecer que a semente `random_state=42` foi padronizada para manter reprodutibilidade em toda a turma. |
| Colab desconecta por inatividade | Baixa | Médio | Orientar o aluno a usar "Ambiente de execução → Reiniciar e executar tudo". Como o dataset tem 20 mil linhas, a execução leva 3 segundos. |

---

## 5. Checklists operacionais

### Antes da aula (18h00 às 18h50)
- [ ] Abrir o link do Colab do aluno em aba anônima para testar permissão pública de leitura.
- [ ] Rodar todas as células do notebook do professor no Google Colab, validando que nenhuma biblioteca quebrou.
- [ ] Abrir o deck de slides em tela cheia no aplicativo de apresentação.
- [ ] Colocar `02-roteiro-do-apresentador.md` na tela secundária.
- [ ] Testar microfone, compartilhamento de tela e permissões de chat no ambiente de transmissão.

### Durante a aula (19h00 às 21h00)
- [ ] 19h02: Colar no chat o link oficial do Colab com a instrução de salvar cópia no Drive.
- [ ] 19h40: Projetar o Slide 13 em tela cheia e desativar compartilhamento de som ambiente.
- [ ] 19h40 às 20h40: Felipe e Edmar revezam no atendimento às dúvidas dos alunos no chat do evento.
- [ ] 20h10: Enviar aviso no chat informando o tempo restante de atividade (30 minutos).
- [ ] 20h35: Pedir no chat que os alunos postem os valores de custo financeiro que encontraram no Passo 5.
- [ ] 20h40: Retomar a projeção do deck no Slide 14 e conduzir o debate de encerramento.

### Pós-aula (21h00 às 21h30)
- [ ] Disponibilizar no canal do Discord o link do notebook do professor (gabarito).
- [ ] Enviar o material de apoio (`03-material-de-apoio-participante.md`) junto à gravação oficial da aula.
- [ ] Registrar principais dúvidas dos participantes para alimentar a abertura da Aula 13.
