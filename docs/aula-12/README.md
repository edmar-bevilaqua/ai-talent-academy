# Aula 12: Semana 6, quinta-feira

Pacote da décima segunda aula do **AI Talent Academy**, no padrão visual White Cube.
Tema: **laboratório prático de Machine Learning com scikit-learn** · 19h00 às 21h00 · online · aula inteiramente prática
Condução: Edmar Bevilaqua + Felipe André Bach Alves

Esta aula cumpre exatamente o que a Aula 11 (teórica de segunda-feira) preparou:
sair da discussão conceitual de Machine Learning e colocar as mãos no código.
No Google Colab, cada participante constrói um pipeline real de detecção de fraude
em seis passos objetivos, desde a criação de um baseline ingênuo até o diagnóstico
de overfitting em árvores de decisão e a tradução da matriz de confusão para custo
financeiro de negócio.

---

## O que tem aqui

| Arquivo | O que é | Para quem |
|---|---|---|
| **`AI-Talent-Academy-Aula12.pptx`** | O deck: 22 slides, com roteiro de fala nas notas | Edmar + Felipe |
| [`02-roteiro-do-apresentador.md`](02-roteiro-do-apresentador.md) | Todas as notas do deck em markdown imprimível | Edmar + Felipe |
| [`01-plano-da-aula.md`](01-plano-da-aula.md) | Cronograma detalhado, mapa de cortes Essencial × Descartável e checklists | Edmar + Felipe |
| [`03-material-de-apoio-participante.md`](03-material-de-apoio-participante.md) | Guia de consulta rápida pós-aula com conceitos, código e cálculo financeiro | Alunos |
| [`04-plano-de-interacao-ao-vivo.md`](04-plano-de-interacao-ao-vivo.md) | Roteiro de enquetes rápidas e dinâmica de moderação no chat para 190 pessoas | Edmar + Felipe |
| [`Aula_12_Alunos_Treinando_Primeiro_Modelo.ipynb`](Aula_12_Alunos_Treinando_Primeiro_Modelo.ipynb) | Notebook de atividades com instruções passo a passo e células `# TODO` | Alunos |
| [`Aula_12_Professor_Treinando_Primeiro_Modelo.ipynb`](Aula_12_Professor_Treinando_Primeiro_Modelo.ipynb) | Notebook gabarito executado e validado, pronto para guiar a projeção ao vivo | Edmar + Felipe |

---

## Estrutura da aula

| Horário | Bloco | Conteúdo principal | Slides |
|---|---|---|---|
| 19h00 às 19h10 | Recepção e alinhamento | Abertura da sala, objetivo da noite e link do Colab | 1 a 4 |
| 19h10 às 19h25 | Bloco A: A ponte com a teoria | O caso de negócio, as 4 colunas preditivas e o baseline ingênuo | 5 a 8 |
| 19h25 às 19h40 | Bloco B: Demonstração guiada | Demonstração ao vivo dos passos 1 e 2 no notebook do professor | 9 a 11 |
| 19h40 às 20h40 | Bloco C: Mão na massa (60 min) | Turma executa os passos 1 a 6 no Colab com apoio no chat | 12 e 13 |
| 20h40 às 20h55 | Bloco D: Discussão e custos | Comparação dos resultados, custo financeiro e overfitting | 14 a 18 |
| 20h55 às 21h00 | Bloco E: Encerramento e conexões | Síntese dos aprendizados e gancho para a Aula 13 | 19 a 22 |

Carga síncrona de 120 minutos (2 horas), sem intervalo formal, seguindo o padrão
das aulas de quinta-feira.

---

## O pipeline da atividade prática

O notebook do aluno está estruturado em seis passos encadeados:

1. **Passo 1: Carga dos dados e divisão com estratificação**
   - Carrega a base de transações e separa variáveis preditoras (`X`) do alvo (`y`).
   - Aplica `train_test_split(test_size=0.3, random_state=42, stratify=y)`.
   - Explica o risco de vazamento de dados (*data leakage*) e por que a estratificação é
     obrigatória em dados desbalanceados (2,5% de fraude).
2. **Passo 2: Construção do baseline ingênuo**
   - Cria o modelo ingênuo com `DummyClassifier(strategy='most_frequent')`.
   - Mede a acurácia (97,5%) e demonstra na prática a ilusão estatística: um modelo que
     nunca acha uma fraude sequer ainda acerta 97,5% dos casos.
3. **Passo 3: Treinamento da primeira Árvore de Decisão**
   - Treina `DecisionTreeClassifier(max_depth=3, random_state=42)`.
   - Extrai as regras de decisão em texto com `export_text()`.
   - Os alunos enxergam a árvore testando valor, horário e tentativas de senha.
4. **Passo 4: Matriz de confusão e métricas reais**
   - Calcula falsos positivos, falsos negativos, verdadeiros positivos e verdadeiros negativos.
   - Avalia precisão e recall especificamente na classe de fraude (`classe 1`).
   - Compreende por que 80% de recall resolve a operação enquanto 97,5% de acurácia ingênua falha.
5. **Passo 5: Simulação de impacto financeiro no negócio**
   - Aplica a função de custo: cada falso negativo custa R$ 450,00 de prejuízo direto,
     e cada falso positivo custa R$ 15,00 em atrito e validação de suporte.
   - Prova numericamente que o modelo de ML economiza centenas de milhares de reais
     frente ao baseline ingênuo.
6. **Passo 6: Diagnóstico prático de overfitting**
   - Treina uma árvore sem poda (`max_depth=None`).
   - Compara o treino (100% de acurácia) com o teste (desempenho inferior).
   - Demonstra a curva de generalização ao variar `max_depth` de 1 a 15.

---

## Decisões pedagógicas desta aula

| Decisão | O que foi adotado |
|---|---|
| **Base compartilhada e autossuficiente** | O notebook conecta no Google Drive oficial mas traz um gerador sintético determinístico com semente fixa no Passo 0. Nenhum aluno trava por falha de download ou falta de permissão |
| **Acurácia não é métrica de negócio** | O foco da aula é a matriz de confusão e a tradução para reais (R$). O aluno sai da aula sabendo calcular custo de erro |
| **Modelos interpretáveis primeiro** | Começamos com Árvore de Decisão porque ela permite inspecionar cada nó e cada limiar numérico antes de falar de métodos mais complexos |
| **Overfitting visível a olho nu** | O aluno vê o modelo decorar 100% dos dados de treino e falhar nos dados de teste, entendendo na prática o conceito de generalização |
| **Condução compartilhada** | Felipe conduz a explicação técnica e a demonstração no Colab; Edmar ancora a conexão de negócio, custos e media as dúvidas conceituais no chat |

---

## Como regerar este pacote

```bash
python scripts/gerar_slides_aula12.py
python scripts/exportar_roteiro_aula12.py
python scripts/gerar_notebooks_aula12.py
python scripts/auditar_vicios.py scripts/gerar_slides_aula12.py
python scripts/auditar_vicios.py docs/aula-12/
```

---

## Checklist pré-aula

- [ ] Abrir `Aula_12_Professor_Treinando_Primeiro_Modelo.ipynb` no Google Colab e executar todas as células para aquecer o ambiente.
- [ ] Confirmar que o link de compartilhamento do `Aula_12_Alunos_Treinando_Primeiro_Modelo.ipynb` está público para leitura.
- [ ] Publicar no canal de avisos do Discord o link do Colab e a instrução: "Salvar uma cópia no Drive antes das 19h00".
- [ ] Deixar aberta a janela com o slide 13 (mapa da atividade) para projeção fixa durante os 60 minutos de prática.
