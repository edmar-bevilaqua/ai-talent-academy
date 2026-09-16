# -*- coding: utf-8 -*-
"""
Gerador dos notebooks da Aula 12 do AI Talent Academy.
Gera a versao do aluno (com TODOs) e a versao do professor (resolvida).
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST_DIR = ROOT / "docs" / "aula-12"
DEST_DIR.mkdir(parents=True, exist_ok=True)


def build_notebook(is_teacher: bool = False) -> dict:
    cells = []

    def md(text):
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [line + "\n" for line in text.strip().split("\n")]
        })

    def code(text):
        cells.append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [line + "\n" for line in text.strip().split("\n")]
        })

    # Header
    title_suffix = "Professor (Gabarito Completo)" if is_teacher else "Aluno (Atividade Prática)"
    md(f"""# Aula 12: Treinando o Primeiro Modelo de Machine Learning
**Versão:** {title_suffix}
**AI Talent Academy** · White Cube (A Think Group Company)
**Condução:** Edmar Bevilaqua e Felipe André Bach Alves

Nesta aula prática, você vai construir, avaliar e ajustar o seu primeiro modelo de Machine Learning do início ao fim usando Python e a biblioteca **scikit-learn**.
Trabalharemos com a base de transações de cartão de crédito e detecção de fraude, a mesma das aulas anteriores.

### Objetivos do laboratório:
1. Comprovar a armadilha da acurácia com um baseline ingênuo.
2. Dividir os dados em treino e teste com amostragem estratificada.
3. Treinar uma árvore de decisão (`DecisionTreeClassifier`) e visualizar seus ramos.
4. Avaliar o modelo com matriz de confusão, precisão, recall e métrica de negócio.
5. Identificar e controlar o overfitting variando o parâmetro `max_depth`.
6. Comparar a árvore com uma regressão logística (modelo linear via gradiente descendente).
""")

    # Passo 0
    md("""## Passo 0 · Preparação do ambiente e importação das bibliotecas

No Google Colab, as bibliotecas `pandas`, `numpy`, `matplotlib` e `scikit-learn` já vêm instaladas.
Importamos os módulos necessários para manipulação de dados, modelagem e avaliação visual.""")

    code("""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
    recall_score,
    precision_score,
    f1_score
)

# Configuracao visual dos graficos
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['figure.figsize'] = (10, 6)

print("Bibliotecas importadas com sucesso.")""")

    # Passo 0.1
    md("""### 0.1 Carga dos dados

Vamos carregar a base de transações e a tabela de contestações.
O código abaixo tenta baixar os dados via Google Drive (arquivos da Aula 8 e Aula 10).
Caso você esteja sem acesso externo, ele gera automaticamente uma amostra sintética com a mesma estrutura e distribuição para ninguém ficar travado.""")

    code("""# Tentativa de carregar via Google Drive ou gerador local resiliente
import os

try:
    import gdown
    files = {
        'transacoes.csv': '1OR3lgLjqVQZoajau2wrSExWPYc8xUsFS',
        'contestacoes.csv': '1lSpAe8stD3JEMDJMFbiiYrQH0jYtHzT8'
    }
    for fname, file_id in files.items():
        if not os.path.exists(fname):
            url = f'https://drive.google.com/uc?id={file_id}'
            gdown.download(url, fname, quiet=True)
            print(f"Baixado: {fname}")

    df_trans = pd.read_csv('transacoes.csv', nrows=50000)
    df_cont = pd.read_csv('contestacoes.csv')
    df_trans['data_hora'] = pd.to_datetime(df_trans['data_hora'])
    ids_fraude = set(df_cont['transacao_id'])
    df_trans['eh_fraude'] = df_trans['id'].isin(ids_fraude).astype(int)
    print(f"Dados reais carregados. Amostra: {len(df_trans):,} transacoes.")
except Exception as e:
    print(f"Aviso na carga remota ({e}). Gerando amostra sintetica equivalente...")
    np.random.seed(42)
    n = 30000
    valores = np.random.exponential(scale=120, size=n) + 5.0
    horas = np.random.randint(0, 24, size=n)
    dias = np.random.randint(0, 7, size=n)
    categorias = np.random.choice(['eletronicos', 'supermercado', 'farmacia', 'restaurante', 'viagem'], size=n)

    # Regra com sinal de fraude: madrugada + valor alto ou eletronicos
    prob_fraude = 0.015 + 0.08 * ((horas < 5) & (valores > 300)) + 0.04 * (categorias == 'eletronicos')
    eh_fraude = (np.random.rand(n) < prob_fraude).astype(int)

    df_trans = pd.DataFrame({
        'id': range(1, n + 1),
        'valor': np.round(valores, 2),
        'hora': horas,
        'dia_semana': dias,
        'categoria': categorias,
        'eh_fraude': eh_fraude
    })
    print(f"Amostra sintetica criada com sucesso: {len(df_trans):,} transacoes.")""")

    # Passo 0.2
    md("""### 0.2 Preparação das variáveis (Features)

Para alimentar os modelos matemáticos, precisamos de variáveis numéricas.
Criamos variáveis temporais e transformamos categorias em colunas numéricas (One-Hot Encoding).""")

    if is_teacher:
        code("""# Extracao de caracteristicas temporais caso tenhamos data_hora
if 'data_hora' in df_trans.columns:
    df_trans['hora'] = df_trans['data_hora'].dt.hour
    df_trans['dia_semana'] = df_trans['data_hora'].dt.dayofweek

# Selecao de colunas explicativas (X) e variavel alvo (y)
features_base = ['valor', 'hora', 'dia_semana']
X = df_trans[features_base].copy()
y = df_trans['eh_fraude'].copy()

# Se houver coluna de categoria ou status, podemos aplicar get_dummies
if 'categoria' in df_trans.columns:
    dummies = pd.get_dummies(df_trans['categoria'], prefix='cat', drop_first=True)
    X = pd.concat([X, dummies], axis=1)

print("Formato da matriz de entrada X:", X.shape)
print("Distribuição da variável alvo y:")
print(y.value_counts(normalize=True).rename({0: 'Legítima', 1: 'Fraude'}).map('{:.2%}'.format))""")
    else:
        code("""# Extracao de caracteristicas temporais caso tenhamos data_hora
if 'data_hora' in df_trans.columns:
    df_trans['hora'] = df_trans['data_hora'].dt.hour
    df_trans['dia_semana'] = df_trans['data_hora'].dt.dayofweek

# TODO: Selecione as features numericas basicas ('valor', 'hora', 'dia_semana')
features_base = ['valor', 'hora', 'dia_semana']
X = df_trans[features_base].copy()

# TODO: Defina a variavel alvo y (coluna 'eh_fraude')
y = df_trans['eh_fraude'].copy()

# Se houver categoria, criamos dummies
if 'categoria' in df_trans.columns:
    dummies = pd.get_dummies(df_trans['categoria'], prefix='cat', drop_first=True)
    X = pd.concat([X, dummies], axis=1)

print("Formato da matriz de entrada X:", X.shape)
print("Distribuicao da variavel alvo:")
print(y.value_counts(normalize=True))""")

    # Passo 1
    md("""## Passo 1 · A armadilha da acurácia (Baseline Ingênuo)

Na Aula 11 vimos o exemplo do modelo ingênuo: em um cenário onde 98% das transações são legítimas e 2% são fraudes, um modelo que simplesmente responde "não é fraude" para todo mundo terá 98% de acurácia.
Vamos provar isso em código usando o `DummyClassifier` do scikit-learn.""")

    if is_teacher:
        code("""# Criamos um classificador que sempre repete a classe mais frequente (0 = legitima)
dummy = DummyClassifier(strategy='most_frequent')
dummy.fit(X, y)
y_pred_dummy = dummy.predict(X)

acc_dummy = accuracy_score(y, y_pred_dummy)
rec_dummy = recall_score(y, y_pred_dummy, zero_division=0)

print(f"Acurácia do modelo ingênuo: {acc_dummy:.2%}")
print(f"Recall do modelo ingênuo (taxa de detecção de fraude): {rec_dummy:.2%}")
print("\\nMatriz de confusão do modelo ingênuo:")
print(confusion_matrix(y, y_pred_dummy))""")
    else:
        code("""# TODO: Instancie o DummyClassifier com strategy='most_frequent'
dummy = DummyClassifier(strategy='most_frequent')

# TODO: Ajuste o modelo aos dados com .fit(X, y)
dummy.fit(X, y)

# TODO: Faca predicoes para toda a base com .predict(X)
y_pred_dummy = dummy.predict(X)

acc_dummy = accuracy_score(y, y_pred_dummy)
rec_dummy = recall_score(y, y_pred_dummy, zero_division=0)

print(f"Acuracia do modelo ingenuo: {acc_dummy:.2%}")
print(f"Recall de fraude capturada: {rec_dummy:.2%}")""")

    md("""**Reflexão:** O modelo teve acurácia superior a 95%, mas o recall de fraude foi exatamente 0%.
Ou seja: se a diretoria olhar apenas a acurácia, vai achar o modelo excelente, enquanto a empresa continua perdendo 100% do dinheiro com fraudes.
Por isso acurácia nunca deve ser usada isoladamente em problemas desbalanceados.""")

    # Passo 2
    md("""## Passo 2 · Separação correta de Treino e Teste

Nunca avaliamos um modelo nos mesmos dados em que ele aprendeu.
Usamos `train_test_split` separando 70% para treino e 30% para teste.
Com classes raras, o parâmetro `stratify=y` é obrigatório para garantir que a proporção de fraudes seja idêntica nos dois conjuntos.""")

    if is_teacher:
        code("""X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

print(f"Conjunto de Treino: {X_train.shape[0]:,} linhas ({y_train.mean():.2%} de fraude)")
print(f"Conjunto de Teste:  {X_test.shape[0]:,} linhas ({y_test.mean():.2%} de fraude)")""")
    else:
        code("""# TODO: Divida X e y em treino (70%) e teste (30%) com stratify=y e random_state=42
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

print(f"Treino: {len(X_train)} | Teste: {len(X_test)}")
print(f"Taxa de fraude no treino: {y_train.mean():.2%}")
print(f"Taxa de fraude no teste:  {y_test.mean():.2%}")""")

    # Passo 3
    md("""## Passo 3 · Treinando a primeira Árvore de Decisão

A Árvore de Decisão cria regras lógicas baseadas em perguntas com respostas 'sim' ou 'não'.
Começamos com `max_depth=3` para manter a árvore compacta, legível e interpretável para humanos.""")

    if is_teacher:
        code("""# Instanciamos a arvore com profundidade maxima limitada
arvore = DecisionTreeClassifier(max_depth=3, random_state=42)

# Treinamos com os dados de treino
arvore.fit(X_train, y_train)

print("Árvore de decisão treinada com sucesso.")
print(f"Variáveis utilizadas: {list(X_train.columns)}")""")
    else:
        code("""# TODO: Instancie o DecisionTreeClassifier com max_depth=3 e random_state=42
arvore = DecisionTreeClassifier(max_depth=3, random_state=42)

# TODO: Treine a arvore com X_train e y_train
arvore.fit(X_train, y_train)

print("Arvore treinada!")""")

    md("""### 3.1 Visualizando os ramos e as regras da árvore

Uma das grandes vantagens da árvore de decisão é a explicabilidade.
Podemos desenhar a árvore completa ou imprimir as regras em formato de texto.""")

    code("""# Visualizacao grafica da arvore
plt.figure(figsize=(18, 8))
plot_tree(
    arvore,
    feature_names=list(X_train.columns),
    class_names=['Legítima', 'Fraude'],
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("Árvore de Decisão · AI Talent Academy (max_depth=3)", fontsize=14, fontweight='bold')
plt.show()

# Regras em texto puro
print("\\n--- Regras lógicas extraídas da árvore ---")
print(export_text(arvore, feature_names=list(X_train.columns)))""")

    # Passo 4
    md("""## Passo 4 · Avaliação com Matriz de Confusão e Métricas Reais

Agora geramos previsões para o conjunto de teste e calculamos as métricas ensinadas na Aula 11:
- **Verdadeiros Positivos (VP)**: Fraudes corretamente detectadas.
- **Falsos Positivos (FP)**: Clientes legítimos bloqueados indevidamente (custo operacional de SAC e atrito).
- **Verdadeiros Negativos (VN)**: Transações legítimas aprovadas sem fricção.
- **Falsos Negativos (FN)**: Fraudes que passaram despercebidas (perda financeira direta).""")

    if is_teacher:
        code("""y_pred_arvore = arvore.predict(X_test)

cm = confusion_matrix(y_test, y_pred_arvore)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Legítima', 'Fraude'])

fig, ax = plt.subplots(figsize=(6, 5))
disp.plot(cmap='Blues', ax=ax, values_format='d')
plt.title("Matriz de Confusão · Conjunto de Teste", fontsize=12, fontweight='bold')
plt.grid(False)
plt.show()

print("\\nRelatório Detalhado de Métricas:")
print(classification_report(y_test, y_pred_arvore, target_names=['Legítima', 'Fraude'], digits=4))""")
    else:
        code("""# TODO: Gere as previsoes no conjunto de teste X_test
y_pred_arvore = arvore.predict(X_test)

# TODO: Calcule e exiba a matriz de confusao com ConfusionMatrixDisplay
cm = confusion_matrix(y_test, y_pred_arvore)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Legitima', 'Fraude'])
disp.plot(cmap='Blues')
plt.title("Matriz de Confusao")
plt.grid(False)
plt.show()

# TODO: Exiba o relatorio com classification_report
print(classification_report(y_test, y_pred_arvore, target_names=['Legitima', 'Fraude']))""")

    md("""### 4.1 Tradução para métricas de negócio (Impacto Financeiro)

No mundo real, a pergunta do comitê executivo nunca é "qual o seu F1-score?", mas sim: "quanto dinheiro economizamos e quanto incomodamos nossos bons clientes?".
Vamos simular o cálculo financeiro real.""")

    code("""# Parametros de negocio hipoteticos
CUSTO_FALSO_POSITIVO = 35.0   # Custo medio de ligacao no SAC + atrito do cliente legitimo
PERDA_MEDIA_FRAUDE = 450.0    # Valor medio de uma transacao fraudulenta nao capturada

vn, fp, fn, vp = cm.ravel()

fraude_evitada_reais = vp * PERDA_MEDIA_FRAUDE
custo_falsos_bloqueios = fp * CUSTO_FALSO_POSITIVO
resultado_liquido = fraude_evitada_reais - custo_falsos_bloqueios

print("--- IMPACTO FINANCEIRO ESTIMADO (CONJUNTO DE TESTE) ---")
print(f"Fraudes reais detectadas (VP): {vp} transações -> R$ {fraude_evitada_reais:,.2f} economizados")
print(f"Clientes legítimos bloqueados (FP): {fp} transações -> R$ {custo_falsos_bloqueios:,.2f} em custos de atrito")
print(f"Fraudes não detectadas (FN): {fn} transações perdidas")
print(f"Resultado líquido gerado pelo modelo: R$ {resultado_liquido:,.2f}")""")

    # Passo 5
    md("""## Passo 5 · O dilema do Overfitting (Ajustando a Profundidade)

O que acontece se deixarmos a árvore crescer livremente sem limitar `max_depth`?
Ela criará uma folha para cada transação específica do conjunto de treino.
No treino o acerto será quase 100%, mas no conjunto de teste o desempenho cai drasticamente porque o modelo memorizou o ruído.
Vamos testar diferentes profundidades de 1 a 15 e observar a curva.""")

    if is_teacher:
        code("""profundidades = list(range(1, 16)) + [None]
scores_treino = []
scores_teste = []
recalls_teste = []

for prof in profundidades:
    clf = DecisionTreeClassifier(max_depth=prof, random_state=42)
    clf.fit(X_train, y_train)

    pred_tr = clf.predict(X_train)
    pred_te = clf.predict(X_test)

    scores_treino.append(f1_score(y_train, pred_tr, zero_division=0))
    scores_teste.append(f1_score(y_test, pred_te, zero_division=0))
    recalls_teste.append(recall_score(y_test, pred_te, zero_division=0))

labels_x = [str(p) if p is not None else 'Livre' for p in profundidades]

plt.figure(figsize=(12, 5))
plt.plot(labels_x, scores_treino, marker='o', label='F1 no Treino (decorando)', color='#28347B', linewidth=2)
plt.plot(labels_x, scores_teste, marker='s', label='F1 no Teste (generalizando)', color='#E23635', linewidth=2)
plt.xlabel('Profundidade Máxima (max_depth)')
plt.ylabel('F1-Score')
plt.title('Curva de Overfitting · Árvore de Decisão', fontsize=13, fontweight='bold')
plt.legend()
plt.show()

melhor_idx = np.argmax(scores_teste)
print(f"Melhor profundidade para generalização: max_depth = {labels_x[melhor_idx]} (F1 no Teste: {scores_teste[melhor_idx]:.4f})")""")
    else:
        code("""profundidades = list(range(1, 16)) + [None]
scores_treino = []
scores_teste = []

for prof in profundidades:
    # TODO: Instancie o classificador com max_depth=prof
    clf = DecisionTreeClassifier(max_depth=prof, random_state=42)
    clf.fit(X_train, y_train)

    pred_tr = clf.predict(X_train)
    pred_te = clf.predict(X_test)

    scores_treino.append(f1_score(y_train, pred_tr, zero_division=0))
    scores_teste.append(f1_score(y_test, pred_te, zero_division=0))

labels_x = [str(p) if p is not None else 'Livre' for p in profundidades]

plt.figure(figsize=(12, 5))
plt.plot(labels_x, scores_treino, marker='o', label='Treino', color='blue')
plt.plot(labels_x, scores_teste, marker='s', label='Teste', color='red')
plt.xlabel('Profundidade')
plt.ylabel('F1-Score')
plt.title('Identificando o Overfitting')
plt.legend()
plt.show()""")

    # Passo 6
    md("""## Passo 6 (Bônus) · Comparando com Regressão Logística (Gradiente Descendente)

Na Aula 11 aprendemos a distinção entre dois mecanismos de aprendizado:
- A **Árvore de Decisão** aprende por divisão gulosa (calcula o ganho de informação em cada nó sem calcular gradiente).
- A **Regressão Logística** aprende ajustando pesos via função de perda e **gradiente descendente**.

Vamos treinar a regressão logística na mesma base e comparar os resultados.""")

    if is_teacher:
        code("""from sklearn.preprocessing import StandardScaler

# Modelos lineares exigem normalizacao das escalas das variaveis
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

reg_log = LogisticRegression(max_iter=1000, random_state=42)
reg_log.fit(X_train_scaled, y_train)

y_pred_log = reg_log.predict(X_test_scaled)

print("--- Comparação de Desempenho no Conjunto de Teste ---")
print(f"Árvore (max_depth=3)  -> Recall: {recall_score(y_test, y_pred_arvore):.2%} | F1: {f1_score(y_test, y_pred_arvore):.2%}")
print(f"Regressão Logística   -> Recall: {recall_score(y_test, y_pred_log):.2%} | F1: {f1_score(y_test, y_pred_log):.2%}")

# Coeficientes da regressao logistica (pesos aprendidos pelo gradiente)
pesos = pd.Series(reg_log.coef_[0], index=X_train.columns).sort_values(ascending=False)
print("\\nPesos atribuídos pelo modelo linear (Gradiente Descendente):")
print(pesos)""")
    else:
        code("""from sklearn.preprocessing import StandardScaler

# Normalizacao das escalas para o gradiente descendente convergir bem
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# TODO: Instancie e treine a LogisticRegression
reg_log = LogisticRegression(max_iter=1000, random_state=42)
reg_log.fit(X_train_scaled, y_train)

# TODO: Faca a predicao no teste normalizado
y_pred_log = reg_log.predict(X_test_scaled)

print(f"Recall da Arvore: {recall_score(y_test, y_pred_arvore):.2%}")
print(f"Recall da Regressao Logistica: {recall_score(y_test, y_pred_log):.2%}")""")

    # Síntese
    md("""## Síntese do Laboratório

Parabéns! Você construiu seu primeiro fluxo profissional de Machine Learning:
1. Comprovou na prática que **acurácia alta é uma ilusão** em dados desbalanceados.
2. Criou um split de dados estratificado para treinar sem vazamento de informação.
3. Treinou uma **árvore de decisão**, desenhou seus nós e extraiu regras claras de negócio.
4. Converteu erros de modelo em **perda e ganho financeiro em reais**.
5. Controlou o **overfitting** podando a árvore no ponto ideal de generalização.
6. Comparou uma árvore gulosa com um modelo treinado por **gradiente descendente**.

Este mesmo fluxo forma a espinha dorsal de qualquer projeto de Machine Learning corporativo.""")

    return {
        "cells": cells,
        "metadata": {
            "language_info": {
                "name": "python",
                "version": "3.10"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }


def main():
    student_nb = build_notebook(is_teacher=False)
    teacher_nb = build_notebook(is_teacher=True)

    p_student = DEST_DIR / "Aula_12_Alunos_Treinando_Primeiro_Modelo.ipynb"
    p_teacher = DEST_DIR / "Aula_12_Professor_Treinando_Primeiro_Modelo.ipynb"

    p_student.write_text(json.dumps(student_nb, indent=1, ensure_ascii=False), encoding="utf-8")
    p_teacher.write_text(json.dumps(teacher_nb, indent=1, ensure_ascii=False), encoding="utf-8")

    print(f"OK: Notebook do aluno gerado em {p_student}")
    print(f"OK: Notebook do professor gerado em {p_teacher}")


if __name__ == "__main__":
    main()
