# Material de apoio: Aula 1

**AI Talent Academy** · Semana 1 · Panorama de Dados, IA e resolução de problemas

> Este é o material para enviar aos participantes **depois** da aula, junto com a gravação.
> Ele não substitui os slides. É a folha de consulta que a pessoa vai reabrir na semana 3
> quando esquecer o que era *overfitting*.

---

## As 6 ideias da aula de hoje

1. **IA é um guarda-chuva.** Machine Learning aprende padrões a partir de exemplos, IA
   Generativa cria conteúdo novo, e Agentes executam tarefas usando ferramentas.
2. **O que mudou nos últimos anos não foi a inteligência da máquina, foi o acesso.**
   Modelos de ponta hoje estão a uma frase de distância de qualquer pessoa.
3. **A IA não entende, não é neutra e não decide por você.** Ela reduz o caminho até a
   decisão. A responsabilidade continua sendo humana.
4. **A pergunta certa não é “como eu uso IA aqui?”** É “que decisão precisa melhorar, e o
   que esse problema realmente pede?”.
5. **Treinar modelo é a menor parte do trabalho.** Projetos vivem ou morrem na definição do
   problema, na qualidade do dado e na entrega para quem vai usar.
6. **Existe uma porta de entrada para o seu perfil.** Técnico ou não, analítico ou de
   negócio: todas são válidas.

---

## Glossário mínimo

Você não precisa decorar. Precisa reconhecer quando alguém usar.

### Conceitos gerais

| Termo | O que é |
|---|---|
| **Inteligência Artificial (IA)** | Guarda-chuva: qualquer sistema que executa tarefas que associamos à inteligência humana. |
| **Machine Learning (ML)** | O sistema descobre a regra a partir de exemplos, em vez de seguir regra escrita por uma pessoa. |
| **Deep Learning** | ML usando redes neurais profundas. É o que destravou imagem, áudio e linguagem. |
| **IA Generativa (GenAI)** | Modelos que geram conteúdo novo: texto, imagem, código, áudio. |
| **Agente de IA** | Um LLM com ferramentas, memória e objetivo. Não só responde: planeja e executa. |
| **Modelo** | O resultado do treinamento. É a “regra aprendida” que recebe uma entrada e devolve uma saída. |
| **Dataset / base** | O conjunto de dados usado para treinar ou avaliar um modelo. |

### Como a máquina aprende

| Termo | O que é |
|---|---|
| **Aprendizado supervisionado** | Aprende com exemplos rotulados (pergunta + resposta certa). É a maioria do que se faz no mercado. |
| **Aprendizado não supervisionado** | Não há resposta certa; o modelo busca estrutura escondida nos dados (ex.: agrupar clientes). |
| **Aprendizado por reforço** | Aprende por tentativa e erro, com recompensa e punição. |
| **Classificação** | Prever uma categoria (é fraude ou não? vai cancelar ou não?). |
| **Regressão** | Prever um número (preço, demanda, tempo). |
| **Clusterização** | Agrupar itens parecidos sem ter rótulo prévio. |

### GenAI

| Termo | O que é |
|---|---|
| **LLM** | *Large Language Model*. Modelo de linguagem treinado em enorme volume de texto. |
| **Token** | O pedaço de texto que o modelo processa. Aproximadamente ¾ de uma palavra. |
| **Prompt** | A instrução que você dá ao modelo. |
| **Contexto** | Tudo que “cabe” na conversa atual. Por isso o modelo parece esquecer conversas longas. |
| **Treino** | Acontece uma vez, antes de você usar. Explica a “data de corte” do conhecimento. |
| **Inferência** | O momento em que o modelo gera a resposta. Cada resposta é composta do zero. |
| **Alucinação** | Quando o modelo produz uma informação falsa com aparência de verdadeira. Comportamento esperado, não bug raro. |
| **RAG** | Técnica de dar ao modelo documentos seus para consultar antes de responder. Reduz alucinação. |

### Ciclo de vida e avaliação

| Termo | O que é |
|---|---|
| **Baseline** | A solução mais simples que funciona. Serve de régua honesta para o modelo. |
| **Treino e teste** | Separar os dados: o modelo aprende com uma parte e é avaliado em outra que nunca viu. |
| **Overfitting** | O modelo “decorou” em vez de aprender: vai bem no que já viu, mal no que é novo. |
| **Vazamento de dados** | Usar no modelo uma informação que só existe *depois* do fato a prever. Gera resultado ótimo e inútil. |
| **Acurácia** | % de acertos. Enganosa quando as classes são desbalanceadas. |
| **Recall** | De tudo que existia, quanto o modelo encontrou. |
| **Precisão** | De tudo que o modelo apontou, quanto estava certo. |
| **Feature engineering** | Criar variáveis novas a partir das que existem (ex.: “tempo de casa” a partir da data de cadastro). |
| **EDA** | *Exploratory Data Analysis*. A primeira conversa com o dado. |
| **Drift** | Quando os dados novos deixam de se parecer com os dados do treino e o modelo piora silenciosamente. |
| **MVP** | A menor versão da solução que já entrega valor real para alguém. |
| **Produção** | Quando a solução roda sozinha, com dado novo, monitorada, com alguém responsável. |

---

## As 8 fases de uma solução de dados e IA

| # | Fase | A pergunta central |
|---|---|---|
| 1 | Entender o problema | Qual decisão precisa melhorar, e como medimos sucesso? |
| 2 | Conseguir os dados | O dado existe, é acessível e eu posso usá-lo? |
| 3 | Explorar | O que os dados realmente dizem? Qual a qualidade? |
| 4 | Preparar | Como limpar, padronizar e criar boas variáveis? |
| 5 | Construir | Regra, ML, GenAI ou agente: o que este problema pede? |
| 6 | Avaliar | Funciona melhor do que a alternativa mais simples? |
| 7 | Colocar no ar | Alguém consegue usar isso de verdade, no dia a dia? |
| 8 | Monitorar | Continua funcionando daqui a três meses? |

> **Não é uma linha reta.** Voltar de uma fase para a anterior não é fracasso, é o trabalho.

---

## As 4 perguntas de uso responsável

Faça em todo projeto, desde o primeiro dia:

1. **De onde veio esse dado?** Tenho autorização? A LGPD se aplica? Há dado pessoal aqui?
2. **Quem esse dado representa, e quem ele deixa de fora?**
3. **Quem é prejudicado se o modelo errar?**
4. **Eu consigo explicar essa decisão para a pessoa afetada?**

---

## Os papéis da área

| Papel | A pergunta que ele responde | Boa porta de entrada para |
|---|---|---|
| **Analista de Dados** | O que os dados dizem sobre o negócio? | Quem vem de áreas não técnicas |
| **Analytics Engineer** | Como transformo dado bruto em base confiável? | Quem gosta de SQL e organização |
| **Engenheiro de Dados** | Como o dado chega aqui, limpo e no horário? | Perfis técnicos e de infraestrutura |
| **Cientista de Dados** | O que vai acontecer, e por quê? | Quem gosta de investigar e testar hipótese |
| **ML Engineer / MLOps** | Como isso funciona em produção todo dia? | Quem vem de desenvolvimento de software |
| **AI / LLM Engineer** | Como construo um produto sobre modelos de IA? | Quem quer entrar pela fronteira mais nova |
| **Governança / Data Steward** | Esse dado é confiável, seguro e legal de usar? | Quem vem de auditoria, jurídico, processos |

---

## Para fazer até quinta-feira

**Obrigatório (5 minutos):**
- [ ] Entrar no Discord do AI Talent Academy e se apresentar no canal `#apresente-se`.

**Recomendado (10 minutos), vamos usar isso na aula:**
- [ ] Pense em **um problema real** do seu trabalho, faculdade ou dia a dia que você acredita
      que dados poderiam ajudar a resolver. Escreva em 2 ou 3 frases. Não precisa ser
      sofisticado. “Por que a fila do meu setor sempre trava na sexta” já é um ótimo começo.

**Opcional:**
- [ ] Anote as 3 palavras da aula de hoje que você não conhecia e procure no glossário acima.
- [ ] Reveja a gravação nos trechos que passaram rápido.

**Nada para instalar.** A aula de quinta ainda é sem código. A partir da semana 2 usaremos o
**Google Colab**, que é gratuito e roda no navegador. Basta ter uma conta Google.

---

## Próximo encontro

**Quinta-feira, 19h00 às 21h00.** Laboratório 1: transformando um problema de negócio em
problema analítico. Apresentaremos o **Canvas do Problema**, a primeira ferramenta de
trabalho do programa.

Dúvidas até lá: canal `#duvidas` do Discord.
