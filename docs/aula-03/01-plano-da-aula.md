# Plano da Aula 3: Semana 2, segunda-feira

**AI Talent Academy** · 19h00 às ~22h11 · online · ~190 participantes
Tema: IA Generativa
Condução: Edmar Bevilaqua (blocos 1, 2 e 3) + Felipe André Bach Alves (blocos 4, 5 e 6)

> Esta aula não estava na proposta comercial original. A ordem das semanas foi ajustada
> com as lideranças, e IA Generativa ganhou uma noite inteira pela relevância e pelo
> interesse da turma.

> ⚠️ **Esta aula esticou por decisão, não por atraso.** O bloco 3 ganhou dois assuntos
> (banco vetorial e fine-tuning) depois de validar com o usuário que a turma pede um
> aprofundamento maior que o inicialmente planejado. Isso adiciona 11 minutos, e a aula
> termina por volta de **22h11**, não 22h00. Avise a turma disso logo na abertura do
> bloco 3 (já está no roteiro), para ninguém ficar surpreso perto do fim.

---

## 1. Objetivo desta aula

Ao final dos ~191 minutos, cada participante deve conseguir:

1. **Explicar o que acontece por dentro** de um LLM, usando token, embedding e atenção.
2. **Justificar tecnicamente** por que a alucinação acontece e por que ele esquece.
3. **Escrever um prompt** que tenha papel, tarefa, contexto, formato e restrição.
4. **Distinguir técnica de folclore** entre as práticas de prompt que circulam por aí.
5. **Decidir quando não usar GenAI**, usando os seis sinais de cada lado.

> **Critério de sucesso operacional:** volume de perguntas técnicas no Discord nas 48h
> seguintes, e presença na quinta-feira (primeira aula com código).

---

## 2. Cronômetro

| Início | Fim | Duração | Bloco | Quem | Slides |
|---|---|---|---|---|---|
| 19h00 | 19h10 | 10 min | Recepção dos participantes | Edmar + moderador | 1 e 2 |
| 19h10 | 19h20 | 10 min | **Abertura, por que uma noite inteira** | Edmar | 3 a 6 |
| 19h20 | 19h55 | 35 min | **IA Generativa na prática** | Edmar | 7 a 14 |
| 19h55 | 20h30 | 35 min | **Como um LLM funciona por dentro** | Edmar | 15 a 24 |
| 20h30 | 20h45 | 15 min | Intervalo | (os dois) | 25 |
| 20h45 | 21h36 | 51 min | **Prompt, contexto e limites** | Felipe | 26 a 37 |
| 21h36 | 22h01 | 25 min | **Onde GenAI resolve e onde atrapalha** | Felipe | 38 a 42 |
| 22h01 | 22h11 | 10 min | **Recap e Q&A** | Felipe + Edmar | 43 a 47 |

O bloco 3 (Prompt, contexto e limites) ganhou dois slides novos depois do RAG original:
**banco vetorial** (35) e **RAG × fine-tuning** (36). Isso empurrou os blocos 4 e 5 em 11
minutos, e a aula termina por volta de 22h11.

### Marcos de controle (cole isso no seu monitor)

| Se às… | você não estiver em… | então corte |
|---|---|---|
| **19h22** | slide 7 (seção "IA Generativa na prática") | encurte o slide 6, leia só os títulos dos cards |
| **19h40** | slide 11 (tabela de aplicação real) | o caso aprofundado de triagem (12) |
| **19h58** | slide 16 ("De onde a gente parou") | a interação do bloco 1 (14) |
| **20h20** | slide 22 ("Como ele ficou assim") | as três fases de treino (22) |
| **21h05** | slide 32 ("O que funciona") | um dos três antes e depois, de preferência o 1 (29) |
| **21h30** | slide 35 ("Banco vetorial") | corte o exemplo do mapa, vá direto para o índice e a frase de denso × esparso |
| **21h39** | slide 39 ("A escada, de volta") | a interação do bloco 4 (37) |
| **22h03** | slide 44 ("Recapitulando") | encolha o Q&A para 2 min. **Não passe das 22h15.** |

---

## 3. Mapa essencial × descartável

### 🔴 Essencial: não corte em nenhuma hipótese

| Slide | Conteúdo | Por quê |
|---|---|---|
| 10 | Os seis verbos que ela faz bem | Slide-âncora do bloco 1, é o mais acionável da noite |
| 11 | Tabela de aplicação real | Conecta os verbos com trabalho de verdade |
| 17 a 19 | Token, embedding e atenção | O núcleo do bloco técnico. Cortar aqui esvazia a aula |
| 20 | Juntando as três peças | Sem ele, as três peças anteriores ficam soltas |
| 23 | Janela de contexto | Explica o comportamento que mais gera dúvida na prática |
| 24 | Agora dá para explicar a alucinação | Fecha o arco com a Aula 1 e paga a promessa feita lá |
| 28 | Os cinco elementos do prompt | Slide-âncora do bloco 3, vale pedir para fotografarem |
| 30 | Antes e depois de contexto | O par mais importante dos três |
| 33 | O que é folclore | Alta retenção, e desmonta crença que atrapalha o uso |
| 34 | RAG em quatro passos | Amarra o embedding do bloco 2 com aplicação real |
| 35 | Banco vetorial | Conteúdo novo, adicionado a pedido, completa o embedding |
| 36 | RAG × fine-tuning | Conteúdo novo, resolve confusão comum entre as duas técnicas |
| 40 | Os seis sinais de cada lado | Slide-âncora do bloco 4, o que mais pesa na carreira |
| 41 | O erro mais comum (pedir para calcular) | Exemplo de maior retenção do bloco final |
| 44 e 45 | Recap + o que vem na quinta | Sem isso a retenção para a quinta despenca |

> Os slides 35 e 36 são a expansão pedida depois do desenho original. Eles esticaram a
> aula em 11 minutos por decisão deliberada, não por acidente. Se precisar recuperar
> tempo em cenário de atraso grave (algo além do que os cortes abaixo já resolvem), esses
> dois são os primeiros candidatos, porque foram adição posterior, não parte do núcleo.

### 🟡 Descartável: ordem de corte

1. **Slide 22:** As três fases de treino. Interessante, mas não sustenta nada depois
2. **Slide 14:** Interação do bloco 1
3. **Slide 37:** Interação do bloco 3
4. **Slide 12:** Caso aprofundado de triagem (a tabela do 11 já entrega a ideia)
5. **Slide 29:** Antes e depois 1 (o 30 e o 31 são mais fortes)
6. **Slide 9:** As quatro famílias (dá para resumir em uma frase falada)
7. **Slide 42:** Como avaliar saída (importante, mas cabe no material de apoio)
8. **Slides 35 e 36:** Banco vetorial e RAG × fine-tuning, só em cenário de atraso grave
   (ver nota acima). Prefira cortar tudo o mais antes de chegar nestes dois

> **Plano B se o bloco 2 estourar:** ele é o mais provável de estourar, porque é o mais
> denso. Se às 20h25 você ainda estiver no slide 21, pule direto para o 23 e depois o 24.
> O slide 22 é o único do bloco que dá para perder sem prejuízo.

---

## 4. Divisão de responsabilidades

| Papel | Quem | O que faz |
|---|---|---|
| Apresentador | quem está no bloco | Fala, controla o slide, olha para a câmera |
| Apoio | o outro | Lê o chat, responde por escrito, avisa sobre o tempo |
| Moderação | 1 pessoa dedicada | Modera chat, posta links, agrupa perguntas do Q&A |

**Combinado de tempo:** quem está de apoio manda mensagem privada com "faltam 10",
"faltam 5", "estouro", sem interromper em voz alta.

---

## 5. Cuidados específicos desta aula

Esta é a aula mais técnica até agora, e isso muda alguns riscos.

| Cuidado | Por quê | O que fazer |
|---|---|---|
| **Nenhuma fórmula na tela** | Mesmo com parte da turma pedindo mais profundidade, fórmula ainda esvazia a sala | O bloco 2 usa só analogia. Se sentir vontade de escrever matriz, respire |
| **Analogia antes do termo** | Cor antes de embedding, mesa antes de janela de contexto | Sempre apresente a analogia primeiro e o nome técnico depois |
| **Pausa nas duas frases da atenção** | O exemplo do prefeito só funciona se a sala resolver sozinha | Leia, pause de verdade, e só então dê a resposta |
| **Não prometer o que a quinta terá** | O notebook e a API ainda não estão testados | Fale em termos gerais até confirmar. Ver pendências no README |
| **Cuidado com número volátil** | Preço de API e limite de contexto mudam toda hora | O deck evita número específico de propósito. Não improvise um |

---

## 6. Restrições de conteúdo (valem para todas as aulas)

| ⛔ Não dizer | ✅ Dizer no lugar |
|---|---|
| O número de vagas de trainee | "Vai depender do desempenho da turma" |
| Nota de corte específica | "Os critérios completos apresentamos com antecedência" |
| Recomendação de fornecedor como "o melhor" | "Depende da tarefa, do custo e do idioma. Teste com o seu caso" |
| Que dado da empresa pode ser colado em ferramenta pública | "Depende do contrato e da política interna. Confira antes" |

---

## 7. Riscos e planos B

| Risco | Probabilidade | Plano B |
|---|---|---|
| O bloco 2 (técnico) estoura o tempo | **Alta** | É o mais denso. Corte o slide 22 e siga |
| A sala trava no embedding | Média | Volte para a analogia da cor e repita. Confirme pelo chat antes de seguir |
| Perguntas técnicas demais no chat | **Alta** | Moderador agrupa. O que não couber vai para o Discord |
| Alguém pede demonstração ao vivo | Média | A aula é expositiva por decisão. Prometa para a quinta, que é a aula de código |
| Queda de internet de um apresentador | Média | O outro assume com o roteiro em markdown |
| Estouro além de 22h15 | Média | O Q&A é o amortecedor. A nova régua desta aula passou de 22h15 |
