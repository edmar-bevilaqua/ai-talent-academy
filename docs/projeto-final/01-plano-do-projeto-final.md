# Plano do projeto final: AI Talent Academy

> **Anunciado na semana 2.** Este documento adapta o projeto final já descrito na
> proposta comercial (seção 6.2, "Proposta de atividade seletiva da Etapa 2") para
> começar agora, com squads fixos de 6 pessoas desde já, em vez de squads formados só
> na semana 5. Os pesos, os critérios, os entregáveis finais e os momentos de avaliação
> continuam os mesmos já definidos na proposta. O que muda é o cronograma: mais tempo de
> preparo, do início ao fim do curso.
>
> O Mini-Desafio Data & AI (semana 4) continua existindo exatamente como já estava
> previsto, como instrumento individual de avaliação da Etapa 1. Ele roda em paralelo ao
> projeto em grupo. Um não substitui o outro.
>
> Base de participantes: aproximadamente 190 inscritos, organizados em cerca de 32
> grupos de 6 pessoas. Ajuste esse número conforme a lista real de inscritos confirmados,
> mantendo cada grupo entre 4 e 7 pessoas.

---

## 1. O desafio

**Enunciado oficial** (já definido na proposta comercial): construir uma solução de
Dados e IA que melhore uma decisão de negócio ou uma experiência de usuário, e que
possa, em tese, ser incorporada a uma das plataformas de IA da White Cube: White
Conductor, White Field ou White Pulse.

Isso significa que o projeto não precisa resolver um problema abstrato de dados. Ele
precisa resolver uma decisão real, ou pelo menos verossímil, de alguém que usaria a
solução no dia a dia.

### 1.1 Trilhas temáticas

Cada grupo escolhe uma trilha principal para orientar o tipo de solução. Como o grupo
tem 6 pessoas com perfis variados, é comum o tema final combinar mais de uma trilha, por
exemplo um pipeline de dados que alimenta um modelo de Machine Learning, ou um copiloto
de GenAI que consulta um banco estruturado.

| Trilha | Indicada para | Exemplo de entrega |
|---|---|---|
| Analytics / Dados | Perfis analíticos, storytelling com dados | Análise exploratória, dashboard, relatório executivo |
| Programação / Engenharia | Perfis técnicos, automação | Pipeline de dados, API, automação de processo |
| Machine Learning | Perfis com interesse em modelagem | Modelo preditivo, de classificação ou de clusterização, com métricas |
| GenAI | Perfis interessados em IA generativa | Copiloto, assistente com RAG, automação com LLM |

### 1.2 Banco de temas modelo

Estes seis temas já estão validados na proposta comercial. Qualquer grupo pode adotar
um deles diretamente:

| Tema | Ideia de solução |
|---|---|
| Score de potencial produtivo, para predição de IMA | Modelo preditivo a partir de variáveis como material genético, idade do plantio, solo, clima, manejo e histórico silvicultural |
| Avaliação de índices foliares automatizada | Solução baseada em imagens de satélite, drone ou sensoriamento remoto, calculando índices como NDVI, NDRE, EVI ou SAVI |
| Score de risco de fraude em saúde, focando em hiperutilizadores | Detecção de padrões atípicos de uso em bases de saúde |
| Avaliação automática de radiografias | Protótipo de visão computacional para apoio à triagem, identificando sinais sugestivos de determinadas condições clínicas |
| Criação automática de queries usando LLMs | Copiloto que transforma pergunta em linguagem natural em consulta SQL, agnóstico ao banco de destino |
| Assessment automatizado de governança de dados e IA | Solução que avalia maturidade de governança a partir de questionários, documentos e políticas internas |

### 1.3 Temas livres

Como são só seis exemplos para cerca de 32 grupos, a maioria vai propor um tema
próprio. Um tema livre precisa cumprir três regras:

1. Resolve uma decisão de negócio real ou verossímil, não é só uma exploração de dados
   sem pergunta por trás.
2. Usa dados que o grupo consegue obter e compartilhar legalmente.
3. Se encaixa em pelo menos uma das quatro trilhas da seção 1.1.

---

## 2. Base de dados: como cada grupo propõe a sua

Cada grupo tem três caminhos possíveis para a base de dados:

| Caminho | Como funciona |
|---|---|
| Tema modelo | Usa um dos seis temas da seção 1.2, com a base pública equivalente disponibilizada pela coordenação |
| Base pública própria | O grupo encontra e propõe uma base de um portal de dados abertos (governo federal, estadual ou municipal, IBGE, DATASUS, ANEEL, Kaggle, entre outros) |
| Base do próprio contexto | Algum integrante do grupo traz um dado do próprio trabalho, estudo ou nicho, desde que anonimizado e compartilhável sem violar confidencialidade |

**Critérios mínimos para a base ser aprovada:**
- Volume suficiente para sustentar uma análise não trivial.
- Ao menos parcialmente estruturado (planilha, tabela, banco ou API).
- Sem dado sensível de terceiros sem anonimização.
- Sem informação confidencial de empresa sem autorização explícita de quem autoriza.

**Prazo:** até o fim da semana 3, cada grupo registra tema e base propostos no canal
indicado (formulário ou Discord) para validação da coordenação. Grupos que usarem os
temas modelo da seção 1.2 já entram com a base pré-aprovada.

---

## 3. Estrutura do projeto

### 3.1 Escopo recomendado

O projeto não precisa de uma solução perfeita nem pronta para produção. O que o projeto
avalia é:

- Como o participante pensa diante de um problema aberto.
- Como aprende ao longo das semanas.
- Como prioriza entre o que é possível fazer e o tempo disponível.
- Como colabora dentro do grupo.
- Como transforma dados e IA em algo de valor prático para a decisão proposta.
- Como reconhece limitações da própria solução e propõe próximos passos.

### 3.2 Entregáveis finais (semana 8)

Cada grupo entrega, ao final da semana 8:

1. Apresentação executiva, com problema, solução, impacto e próximos passos.
2. Protótipo funcional: notebook, dashboard, fluxo de GenAI ou demo navegável.
3. Documentação técnica, explicando dados, abordagem, decisões e limitações.
4. Métricas de avaliação, técnicas e de negócio.
5. Análise de riscos, incluindo viés, privacidade, segurança e limitações.
6. Reflexão individual de cada integrante, com aprendizados e contribuição pessoal.

---

## 4. Critérios de avaliação

### 4.1 Componentes avaliativos

| Componente | Peso |
|---|---|
| Projeto final em squad | 35% |
| Contribuição individual no projeto | 20% |
| Desempenho técnico | 15% |
| Comunicação e apresentação final | 10% |
| Colaboração e postura profissional | 10% |
| Evolução ao longo do projeto | 10% |

### 4.2 Momentos de avaliação

| Momento | Semana | Finalidade |
|---|---|---|
| Anúncio e formação dos squads | 2 | Grupos fechados, tema e base propostos |
| Registro da proposta de projeto | 4 | Documento com problema, público-alvo, dados, abordagem, entregáveis e cronograma próprio |
| Checkpoint de planejamento | 5 | Avaliar entendimento do problema e desenho da solução |
| Checkpoint técnico 1 | 6 | Avaliar execução, organização e primeiras evidências do MVP |
| Checkpoint técnico 2 | 7 | Avaliar evolução, qualidade da solução e resposta a feedback |
| Demo Day | 8 | Avaliar solução final, narrativa, defesa técnica e maturidade |
| Entrevista final | 8 | Avaliar fit, motivação, repertório, colaboração e potencial |

### 4.3 Avaliação individual dentro do grupo

Para a nota não ficar só coletiva, a avaliação combina:

- Registro de contribuições individuais ao longo das semanas.
- Autoavaliação.
- Avaliação por pares, dentro do próprio grupo.
- Perguntas individuais na banca do Demo Day.
- Entrevista final.

### 4.4 Competências técnicas avaliadas

| Competência | Evidência esperada |
|---|---|
| Raciocínio analítico | Formula hipóteses, interpreta dados, identifica padrões e justifica resultados |
| Manipulação de dados | Trabalha com bases, identifica problemas de qualidade e realiza transformações básicas |
| Programação ou automação | Usa Python, SQL, notebooks, scripts, APIs ou ferramentas equivalentes |
| Visualização e comunicação com dados | Cria gráficos claros, escolhe métricas adequadas e comunica achados |
| Fundamentos de Machine Learning | Entende treino e teste, métricas, baseline, validação e limitações de modelos |
| Uso responsável de GenAI | Constrói prompts, avalia respostas, reconhece riscos e evita uso acrítico da IA |
| Experimentação | Compara abordagens, testa hipóteses e usa evidências para decidir |
| Documentação | Explica decisões, estrutura entregas e facilita reprodução da solução |
| Visão de produto e negócio | Conecta a solução técnica a valor, usuário, viabilidade e impacto |

### 4.5 Competências comportamentais avaliadas

| Competência | Evidência esperada |
|---|---|
| Aprendizado rápido | Evolui com feedback, busca soluções e demonstra curiosidade |
| Comunicação | Explica ideias complexas com clareza para públicos técnicos e não técnicos |
| Colaboração | Trabalha bem no squad, compartilha conhecimento e escuta os colegas |
| Autonomia com responsabilidade | Avança nas entregas, pede ajuda quando necessário e cumpre combinados |
| Pensamento crítico | Questiona dados, métricas, respostas de IA e conclusões fáceis |
| Organização | Gerencia tempo, prioriza atividades e estrutura entregáveis |
| Resiliência | Lida com ambiguidade, erros e limitações técnicas |
| Ética e responsabilidade | Considera viés, privacidade, segurança e impactos da solução |
| Postura profissional | Demonstra comprometimento, abertura a feedback e maturidade |

---

## 5. Divisão de responsabilidades no grupo (6 integrantes)

Papéis sugeridos, não obrigatórios. Cada grupo pode ajustar conforme o perfil de quem
está dentro dele. A tabela serve só como ponto de partida para a divisão do trabalho.

| Papel | Foco principal | Trilha relacionada |
|---|---|---|
| Liderança de dados e analytics | Exploração de dados, qualidade, indicadores e visualização | Analytics / Dados |
| Liderança de engenharia | Estrutura do pipeline, automação, organização do repositório | Programação / Engenharia |
| Liderança de modelagem | Construção e avaliação de modelos preditivos ou de GenAI | Machine Learning ou GenAI |
| Liderança de produto e negócio | Conecta a solução ao problema de negócio, prioriza o backlog | Perfil diverso, visão de negócio |
| Coordenação do squad | Organiza prazos, reuniões, divisão de tarefas e ponte com a mentoria | Todas |
| Comunicação e apresentação | Narrativa do Demo Day, documentação final, storytelling com dados | Todas |

Três avisos práticos:

- Ninguém fica só no próprio papel. O trabalho técnico é compartilhado, o papel só
  define quem puxa a frente em cada frente.
- Grupos com menos de 6 pessoas acumulam papéis. Grupos com mais de 6 dividem um papel
  em dois.
- A contribuição individual continua sendo avaliada à parte (seção 4.3), então um papel
  de coordenação não substitui a produção técnica de quem está nele.

---

## 6. Cronograma sugerido (semana 2 à semana 8)

| Semana | Foco do curso | O que acontece no projeto final |
|---|---|---|
| 1 (já ocorrida) | Fundamentos | Sem atividade de projeto. Referência de contexto |
| 2 | IA Generativa | Anúncio do projeto, formação dos squads de 6, publicação do desafio e das trilhas |
| 3 | SQL | Cada grupo registra tema e base de dados propostos, e começa a explorar a qualidade dos dados com SQL |
| 4 | Python | Grupo aprofunda a exploração com Python. Entrega o documento de proposta do projeto (problema, público-alvo, dados, abordagem, entregáveis, cronograma próprio). Em paralelo, ocorre o Mini-Desafio Data & AI individual |
| 5 | Engenharia de Dados | Checkpoint de planejamento: desenho da solução, arquitetura simples, definição do MVP |
| 6 | Machine Learning | Checkpoint técnico 1: construção do MVP, com dados, modelo e protótipo |
| 7 | Agentes de IA | Checkpoint técnico 2: avaliação, melhoria e preparação da apresentação final |
| 8 | Apresentação final | Demo Day, entrevista final e entrega dos itens da seção 3.2 |

---

## 7. Próximos passos para a coordenação

- [ ] Definir e divulgar a lista de grupos de 6, com base nos inscritos confirmados até
      a semana 2.
- [ ] Disponibilizar as bases públicas equivalentes aos seis temas modelo antes do fim
      da semana 3.
- [ ] Definir o canal e o formato de registro da proposta de tema e base (formulário ou
      Discord).
- [ ] Confirmar com cada mentor qual squad acompanha, para o checkpoint da semana 5 já
      começar com responsável definido.
- [ ] Alinhar com quem conduz o Mini-Desafio da semana 4 que ele continua rodando em
      paralelo ao projeto em grupo, sem sobreposição de agenda.
