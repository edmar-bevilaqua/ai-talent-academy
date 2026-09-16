# Material de apoio: Aula 12

**AI Talent Academy** · Semana 6 · Laboratório prático de Machine Learning com scikit-learn

> Este material foi elaborado para consulta pós-aula, acompanhando a gravação oficial e o notebook executado.
> Utilize esta folha como referência rápida para estruturar seus experimentos de modelagem no trabalho.

---

## As quatro conclusões centrais da prática

1. **Acurácia não mede eficácia em dados desbalanceados.**
   Um classificador que chuta a classe majoritária obtém 97,5% de acerto sem detectar nenhuma fraude.
   Em problemas de eventos raros, olhe sempre para a matriz de confusão e para a métrica alinhada ao custo do erro.

2. **A divisão entre treino e teste exige estratificação.**
   Ao repartir os dados com `train_test_split`, o parâmetro `stratify=y` garante que a proporção exata de fraudes
   seja preservada tanto no conjunto de aprendizado quanto no conjunto de validação.

3. **Árvores de decisão produzem regras claras e auditáveis.**
   Antes de recorrer a modelos complexos de caixa-preta, uma árvore com profundidade controlada (`max_depth=3`)
   permite inspecionar cada pergunta analítica feita sobre as variáveis do negócio.

4. **Desempenho perfeito no treino costuma sinalizar overfitting.**
   Quando um modelo atinge 100% de acerto nos dados de treino mas perde rendimento no teste, ele apenas memorizou
   as particularidades e o ruído da amostra, perdendo a capacidade de generalizar para novos clientes.

---

## O pipeline em seis passos (código de consulta rápida)

### Passo 1: Separação de preditores e divisão estratificada
```python
from sklearn.model_selection import train_test_split

# X contém as variáveis preditoras; y contém a variável alvo
X = df[['valor', 'score_risco_dispositivo', 'tentativas_login_falhas_24h', 'hora_transacao']]
y = df['fraude']

# Divisão 70% treino e 30% teste preservando a proporção de fraudes
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)
```

### Passo 2: Criação do baseline ingênuo
```python
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score

# Sempre prediz a classe mais frequente (não fraude)
baseline = DummyClassifier(strategy='most_frequent')
baseline.fit(X_treino, y_treino)

preds_base = baseline.predict(X_teste)
print("Acurácia ingênua:", accuracy_score(y_teste, preds_base))
```

### Passo 3: Treinamento da árvore de decisão com profundidade limitada
```python
from sklearn.tree import DecisionTreeClassifier, export_text

# Árvore controlada para evitar memorização excessiva
arvore = DecisionTreeClassifier(max_depth=3, random_state=42)
arvore.fit(X_treino, y_treino)

# Visualização das regras aprendidas pelo algoritmo
regras = export_text(arvore, feature_names=list(X.columns))
print(regras)
```

### Passo 4: Matriz de confusão e métricas da classe de interesse
```python
from sklearn.metrics import confusion_matrix, classification_report

preds_arvore = arvore.predict(X_teste)
matriz = confusion_matrix(y_teste, preds_arvore)
tn, fp, fn, tp = matriz.ravel()

print(f"Verdadeiros Negativos (Legítimas liberadas): {tn}")
print(f"Falsos Positivos (Legítimas bloqueadas): {fp}")
print(f"Falsos Negativos (Fraudes que passaram): {fn}")
print(f"Verdadeiros Positivos (Fraudes barradas): {tp}")

print("\nRelatório completo:")
print(classification_report(y_teste, preds_arvore, digits=4))
```

### Passo 5: Cálculo do custo financeiro de operação
```python
# Parâmetros de custo acordados com a área de negócios
CUSTO_FALSO_NEGATIVO = 450.0  # Fraude não detectada (prejuízo direto e chargeback)
CUSTO_FALSO_POSITIVO = 15.0   # Cliente legítimo bloqueado (custo de atendimento e atrito)

custo_total = (fn * CUSTO_FALSO_NEGATIVO) + (fp * CUSTO_FALSO_POSITIVO)
print(f"Custo total do modelo de decisão: R$ {custo_total:,.2f}")
```

### Passo 6: Diagnóstico de overfitting
```python
# Modelo sem limite de crescimento nos nós
arvore_livre = DecisionTreeClassifier(max_depth=None, random_state=42)
arvore_livre.fit(X_treino, y_treino)

acc_treino = arvore_livre.score(X_treino, y_treino)
acc_teste = arvore_livre.score(X_teste, y_teste)

print(f"Acurácia no conjunto de treino: {acc_treino:.4%}")
print(f"Acurácia no conjunto de teste:  {acc_teste:.4%}")

if acc_treino > 0.99 and acc_teste < acc_treino:
    print("Alerta: modelo decorou os dados de treino (overfitting evidente).")
```

---

## Glossário técnico da prática

| Termo | Definição operacional |
|---|---|
| **Baseline** | Ponto de partida simples e obrigatório para comparação. Se um modelo complexo não supera o baseline, ele não deve ir para produção. |
| **Estratificação (`stratify`)** | Método de amostragem que garante que as frações de cada classe nos conjuntos de treino e teste correspondam exatamente à distribuição original. |
| **Vazamento de dados (*data leakage*)** | Ocorre quando informações que não estariam disponíveis no momento da decisão em produção contaminam o treinamento do algoritmo. |
| **Matriz de confusão** | Tabela de contingência que cruza as classes reais com as classes previstas pelo modelo, discriminando acertos e naturezas de erros. |
| **Falso Positivo (FP)** | Transação legítima classificada como fraude. Gera atrito com o cliente e custo operacional de checagem. |
| **Falso Negativo (FN)** | Transação fraudulenta classificada como legítima. Gera prejuízo financeiro direto por estorno e fraude consumada. |
| **Precisão (*precision*)** | De todas as transações que o modelo apontou como fraude, qual porcentagem realmente era fraude. |
| **Revocação (*recall*)** | De todas as fraudes que realmente aconteceram na base, qual porcentagem o modelo conseguiu detectar. |
| **Hiperparâmetro** | Parâmetro configurado pelo cientista de dados antes de iniciar o treinamento, como o `max_depth` de uma árvore. |
| **Overfitting** | Situação em que o modelo aprende particularidades e ruídos do conjunto de treino, falhando ao lidar com novos dados reais. |
