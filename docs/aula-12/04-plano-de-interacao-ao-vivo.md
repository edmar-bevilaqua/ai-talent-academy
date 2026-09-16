# Plano de interação ao vivo: 190 participantes

Conduzir uma aula prática para cerca de 190 participantes conectados à noite, com câmeras desligadas,
exige dinâmicas rápidas e objetivas. Ninguém deve ser solicitado a abrir microfone. Toda interação
ocorre via chat de texto ou ferramenta de enquete nativa da plataforma de transmissão.

---

## 1. Ferramenta recomendada

| Ferramenta | Limite de público | Custo | Adequação para hoje |
|---|---|---|---|
| **Enquete nativa da plataforma (Zoom/Teams/Meet)** | Sem limite prático | Grátis | ✅ **Primeira opção para as 3 enquetes** |
| **Chat de texto da transmissão** | Sem limite | Grátis | ✅ **Canal oficial para dúvidas e envio de códigos** |
| **Mentimeter / Slido** | Depende de licença paga | Variável | ⚠️ Desnecessário para este formato |

---

## 2. As três enquetes da aula

### Enquete 1: O paradoxo da acurácia (Slide 8 · ~19h20)

**Pergunta projetada:**
> Um classificador que diz sempre "não é fraude" atinge 97,5% de acurácia na base histórica.
> Você autoriza a subida desse modelo para produção?
>
> **A)** Sim: 97,5% de acurácia é uma meta excelente para qualquer sistema inicial.  
> **B)** Depende: precisamos apenas confirmar se o tempo de resposta em milissegundos é baixo.  
> **C)** Não: esse modelo deixa passar 100% dos golpes e gera prejuízo total nas fraudes.  
> **D)** Não sei avaliar sem olhar a linguagem de programação utilizada.

- **Duração:** 90 segundos para votação.
- **Gabarito e condução:** Opção **C**.
- **Comentário de fechamento (Edmar):**
  *"Mais de 90% da turma marcou C. Esse é o paradoxo da classe rara: em uma base com 2,5% de fraude,
  a preguiça estatística parece competência quando olhamos apenas para a acurácia global. É por isso
  que nosso primeiro passo prático é construir o baseline ingênuo para desmascarar essa métrica."*

---

### Enquete 2: O peso relativo dos erros (Slide 15 · ~20h42)

**Pergunta projetada:**
> No modelo de negócio da nossa empresa de pagamentos, qual situação provoca maior dano operacional?
>
> **A)** Falso Positivo: bloquear compra legítima e gerar fricção com cliente fiel.  
> **B)** Falso Negativo: liberar transação fraudulenta e arcar com o estorno direto de R$ 450,00.  
> **C)** Os dois erros possuem exatamente o mesmo impacto financeiro para o lojista.  
> **D)** Nenhum dos dois: o risco financeiro é absorvido integralmente pela bandeira do cartão.

- **Duração:** 60 segundos para votação.
- **Gabarito e condução:** Opção **B**.
- **Comentário de fechamento (Edmar):**
  *"O falso positivo irrita e custa R$ 15,00 em suporte e atrito. Mas o falso negativo custa R$ 450,00
  líquidos de prejuízo em dinheiro que sai da conta. Cada erro tem um preço diferente. Modelagem
  responsável começa traduzindo matriz de confusão para a moeda do negócio."*

---

### Enquete 3: O diagnóstico do modelo livre (Slide 18 · ~20h50)

**Pergunta projetada:**
> Uma árvore treinada sem limite de profundidade cravou 100% de acurácia no treino e 94,8% no teste.
> Qual é o diagnóstico técnico do modelo?
>
> **A)** O algoritmo convergiu para uma solução ótima e deve ser congelado para produção.  
> **B)** Ocorreu overfitting: a árvore decorou particularidades do treino e perdeu capacidade preditiva no teste.  
> **C)** Ocorreu underfitting: a árvore é simples demais e precisa de mais variáveis preditoras.  
> **D)** Há erro na divisão dos dados, pois nenhum algoritmo real consegue atingir 100% no treino.

- **Duração:** 60 segundos para votação.
- **Gabarito e condução:** Opção **B**.
- **Comentário de fechamento (Felipe):**
  *"Opção B com ampla maioria. Decorar não é aprender. Se deixarmos a árvore crescer sem controle,
  ela cria uma folha exclusiva para cada transação individual do treino. Quando entra uma compra nova,
  a regra específica falha. Poda e controle de profundidade são defesas contra a ilusão do treino perfeito."*

---

## 3. Dinâmica de moderação no chat durante o Bloco C (19h40 às 20h40)

Durante os 60 minutos de execução autônoma, Felipe e Edmar revezam na leitura e resposta rápida
às mensagens no chat. Para evitar digitação repetitiva, utilize os modelos de resposta padronizados:

### Respostas rápidas para copiar e colar no chat

1. **Quando o participante reportar que não consegue editar células:**
   > *"Atenção: o notebook compartilhado está em modo somente leitura. Vá no menu superior:
   > Arquivo → Salvar uma cópia no Drive. A nova aba aberta será sua cópia pessoal e executável."*

2. **Quando houver dúvida sobre lentidão ou erro de biblioteca:**
   > *"Como estamos no Google Colab, todo o ambiente com scikit-learn e pandas já vem pré-instalado.
   > Se alguma célula falhar por variável não definida, vá em Ambiente de execução → Reiniciar e executar tudo."*

3. **Quando o participante perguntar se deve alterar o `random_state`:**
   > *"Mantenha `random_state=42` em todas as funções (`train_test_split`, `DummyClassifier` e
   > `DecisionTreeClassifier`). Isso garante que os seus números batam exatamente com o gabarito que
   > analisaremos juntos às 20h40."*

4. **Quando perguntarem se haverá entrega com nota:**
   > *"Esta atividade é um laboratório de nivelamento e prática guiada. O objetivo é que cada um execute
   > no próprio ambiente e compreenda os resultados. O gabarito oficial completo será disponibilizado
   > no canal do Discord logo após o encerramento da aula."*

---

## 4. Cronograma de intervenções proativas no chat

| Horário | Mensagem proativa dos instrutores no chat |
|---|---|
| **19h40** | *"Iniciamos a prática autônoma. O Slide 13 projeta os 6 passos. Qualquer dúvida de sintaxe ou conceito, mande aqui no chat."* |
| **20h00** | *"20 minutos decorridos. A maioria da turma deve estar concluindo o Passo 2 (baseline ingênuo) e iniciando o Passo 3 (árvore de decisão)."* |
| **20h20** | *"Faltam 20 minutos para a nossa discussão coletiva. Quem já concluiu o Passo 4, concentre-se no cálculo de custo financeiro do Passo 5."* |
| **20h35** | *"Últimos 5 minutos de mão na massa. Quem terminou o Passo 5, compartilhe no chat: quanto deu o custo total do baseline versus o custo da árvore?"* |
| **20h40** | *"Tempo de prática concluído. Retomamos a apresentação para analisar os números consolidados e debater os impactos."* |
