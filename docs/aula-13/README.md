# Aula 13: Semana 7, segunda-feira

Pacote da décima terceira aula do **AI Talent Academy**, no padrão visual White Cube.
Tema: **Agentes de IA** · 19h00 às 23h05 · online · aula expositiva **e prática**
Condução: Edmar Bevilaqua + Felipe André Bach Alves

> **Segunda versão: a prática entrou para dentro da segunda.** A primeira versão
> seguia a regra padrão das segundas (sem código ao vivo, prática só na Aula 14). O
> usuário decidiu quebrar essa regra de propósito: construir o agente já hoje, para a
> quinta-feira (Aula 14) ficar **inteira livre para mentoria de squad**, com a
> Semana 8 e o Demo Day se aproximando. Isso mudou a estrutura, o tempo total e o
> plano da Aula 14, que deixou de ser um laboratório guiado.

---

## Escopo, exatamente como pedido

O usuário definiu as seis perguntas que a aula precisa responder, e cada uma virou
um bloco. Depois, pediu para acrescentar uma sétima coisa, que não é pergunta, é
ação: construir um agente de verdade, com pelo menos uma ferramenta.

1. Quando agentes de IA surgiram
2. O que é um agente, de verdade
3. **Construir um, com a própria mão** (acrescentado na segunda rodada)
4. Como um agente se diferencia de uma chamada única de LLM
5. Como se controla um agente
6. Quais são as principais soluções do mercado para criar um
7. Qual é o estado da arte hoje, em uso e em ferramenta

---

## A prática: um agente, uma ferramenta, um servidor MCP de verdade

O pedido original do usuário foi "uma tool super genérica e simples", com a
sugestão explícita de usar um servidor MCP. Isso definiu a arquitetura:

- **Servidor MCP**: construído com `fastmcp` (biblioteca que hoje serve a maioria
  dos servidores MCP do mercado), com uma única ferramenta, `consultar_lojista`, que
  devolve o total de transações e a taxa de contestação de um lojista da base de
  fraude já conhecida.
- **Conexão em memória**: o cliente MCP conecta ao servidor **dentro do mesmo
  notebook**, sem subprocesso nem rede (`Client(mcp)` do próprio `fastmcp`). É o
  jeito mais simples de rodar um servidor MCP real sem infraestrutura extra, ideal
  para uma turma de 190 pessoas com pouco tempo.
- **O "cérebro"**: a API da NVIDIA (build.nvidia.com), gratuita e compatível com o
  formato da OpenAI, então o cliente Python é literalmente `from openai import
  OpenAI`, só trocando a URL base. Modelo usado: `nvidia/nemotron-3.5-lightning-30b-a3b`,
  o mesmo já usado em outra aula do curso, com chamada de ferramenta confirmada por
  teste real (ver seção seguinte). **Não** force `enable_thinking: False` nesse
  modelo: testado ao vivo, isso faz o modelo pular a ferramenta e inventar uma
  resposta em vez de chamar `consultar_lojista`. Chamada simples, sem esse
  parâmetro, funciona corretamente.
- **O loop**: escrito à mão, célula por célula, replicando exatamente o loop pensa,
  age, observa, responde do Bloco 02, sobre a mesma pergunta já usada como exemplo
  nos slides ("o lojista 141 tem uma taxa de contestação alta?").

### O que foi validado de verdade, e o que ainda precisa de atenção

| Parte | Status |
|---|---|
| Setup, download dos dados, servidor MCP, cliente em memória, chamada da ferramenta | **Validado de ponta a ponta**, com os dados reais baixados do Drive. Os outputs no notebook do professor são reais, não inventados |
| Chamada de ferramenta do `nvidia/nemotron-3.5-lightning-30b-a3b`, isolada | **Validada com chave real**, em 4 chamadas de teste. Funcionou em 3 delas; numa quarta, forçando `enable_thinking: False`, o modelo pulou a ferramenta e respondeu um número inventado |
| O loop completo do notebook (Passo 5 em diante), de ponta a ponta | **Testado, e travou**: a execução automatizada bateu no limite de 180 segundos por célula, na primeira pergunta real. Ver o alerta de latência abaixo antes de assumir que vai rodar liso ao vivo |

### ⚠️ Alerta real: a latência deste modelo varia muito

Medido com a mesma pergunta, repetida: **3,9 segundos numa chamada, 68 e 77
segundos em outras duas**, sem relação clara com `max_tokens` ou com o modo de
raciocínio. O loop do agente faz pelo menos duas chamadas em sequência por
pergunta (uma para decidir chamar a ferramenta, outra para responder com o
resultado em mãos), então duas respostas lentas empilhadas ultrapassam fácil o que
uma demonstração ao vivo tolera, e foi exatamente isso que causou o timeout do
teste automatizado.

Isso não é motivo para trocar de modelo: é o mesmo já usado em outra aula do curso,
e a chamada de ferramenta em si funciona. Mas é motivo real para **testar de novo
perto da data da aula**, com calma, cronometrando, e ter o vídeo de backup pronto
(mesma prática já usada nas Aulas 9, 10 e 11 para demonstração ao vivo).

### Arquivos

| Arquivo | O que é | Para quem |
|---|---|---|
| [`Aula_13_Alunos_Construindo_Primeiro_Agente.ipynb`](Aula_13_Alunos_Construindo_Primeiro_Agente.ipynb) | O notebook da prática, leitura guiada (código já pronto, sem lacuna) | Alunos |
| [`Aula_13_Professor_Construindo_Primeiro_Agente.ipynb`](Aula_13_Professor_Construindo_Primeiro_Agente.ipynb) | O mesmo notebook, com os outputs reais já validados nas células que não dependem de chave de API | Edmar + Felipe |

**Por que leitura guiada, sem lacuna:** mesma decisão já tomada na Aula 12. Hoje a
turma encontra de uma vez só MCP, código assíncrono e chamada de ferramenta, tudo
novo. Pedir para também preencher lacuna de sintaxe teria custo alto de fricção para
um ganho pedagógico pequeno perto do que já é pedido: ver o loop rodando de verdade.

---

## Uma decisão de conteúdo importante

Antes de escrever, conferi os scripts das Aulas 1 e 3 e encontrei uma base já
plantada, que este deck não repete:

- **A Aula 1** já definiu agente numa frase: "uma GenAI que não só responde: planeja,
  usa ferramentas e executa tarefas", e colocou "agentes" como o marco mais recente da
  linha do tempo histórica, logo depois do ChatGPT.
- **A Aula 3** prometeu este dia explicitamente no próprio roteiro do curso: o slide
  do roadmap da Semana 2 já dizia "Semana 7: Agentes de IA, da resposta à ação". A
  Aula 3 também já cobriu Transformer, janela de contexto, prompt engineering e RAG
  em profundidade, tudo isso reaproveitado aqui como base técnica já conhecida.

O Bloco 01 recapitula essa base numa frase por conceito e segue direto para o que
ainda não tinha sido dito.

---

## O que tem aqui

| Arquivo | O que é | Para quem |
|---|---|---|
| **`AI-Talent-Academy-Aula13.pptx`** | O deck: 40 slides, com roteiro de fala nas notas | Edmar + Felipe |
| [`02-roteiro-do-apresentador.md`](02-roteiro-do-apresentador.md) | Todas as notas do deck em markdown imprimível | Edmar + Felipe |
| `Aula_13_Alunos_...ipynb` / `Aula_13_Professor_...ipynb` | A prática (ver seção acima) | Todos |

---

## Estrutura da aula

| Horário | Bloco | Slides |
|---|---|---|
| 19h00 às 19h10 | Recepção | 1 e 2 |
| 19h10 às 19h25 | Bloco 01: De volta à promessa da Semana 2 | 3 a 5 |
| 19h25 às 19h50 | Bloco 02: Quando isso surgiu (história, ReAct a MCP) | 6 a 10 |
| 19h50 às 20h15 | Bloco 03: O que é um agente, de verdade (definição, loop ReAct, ferramenta) | 11 a 14 |
| **20h15 às 20h45** | **Bloco 04: Mão na massa, seu primeiro agente** | **15 a 17** |
| 20h45 às 21h05 | Bloco 05: O que muda em relação a uma chamada única | 18 a 21 |
| 21h05 às 21h20 | Intervalo | 22 |
| 21h20 às 21h50 | Bloco 06: Como controlamos um agente | 23 a 27 |
| 21h50 às 22h20 | Bloco 07: Principais soluções para criar um agente | 28 a 31 |
| 22h20 às 22h45 | Bloco 08: O estado da arte hoje | 32 a 35 |
| 22h45 às 23h05 | Bloco 09: Encerramento | 36 a 40 |

Total síncrono de 4h05. Cresceu quase meia hora em relação à versão anterior
(3h35), por causa do Bloco 04. Foi uma troca consciente: o usuário decidiu que valia
a pena esticar a segunda para esvaziar a quinta por completo.

---

## Os fatos verificados

Todo fato histórico e todo número de adoção de mercado foi conferido via busca antes
de entrar no script, no mesmo padrão já usado nas Aulas 9 e 11:

| Fato | Fonte / verificação |
|---|---|
| ReAct, o paper que junta raciocínio e ação num loop, outubro de 2022, Google Research e Princeton | Conferido via busca |
| ChatGPT, novembro de 2022 | Já estabelecido na Aula 1 |
| Toolformer, Meta, fevereiro de 2023 | Conferido via busca |
| AutoGPT, Toran Bruce Richards, repositório criado em 16 de março de 2023, mais de 185 mil estrelas no GitHub | Conferido via busca |
| Function calling da OpenAI, meados de 2023 | Conferido via busca |
| MCP (Model Context Protocol), Anthropic, novembro de 2024, mais de 16 mil servidores publicados hoje | Conferido via busca |
| LangGraph à frente do CrewAI em adoção empresarial, com clientes como Uber, LinkedIn, JPMorgan, Klarna, Cisco | Conferido via busca |
| CrewAI, mais de 2 bilhões de execuções de agente em 12 meses, presente em quase metade da Fortune 500 | Conferido via busca |
| Claude Agent SDK, lançado em 2025, adoção concentrada em ferramenta de desenvolvedor | Conferido via busca |
| NVIDIA NIM, API gratuita compatível com OpenAI. `nvidia/nemotron-3.5-lightning-30b-a3b` suporta chamada de ferramenta, mas só sem forçar `enable_thinking: False` | **Testado com chamada real**, não só documentação |
| `fastmcp`, cliente em memória (`Client(servidor)`) roda servidor e cliente MCP no mesmo processo, sem subprocesso nem rede | Conferido via busca e testado de verdade |

---

## Decisões de conteúdo desta aula

| Decisão | O que foi combinado |
|---|---|
| **A prática entrou na segunda, quebrando a regra padrão** | Pedido explícito do usuário, para esvaziar a quinta inteira para mentoria |
| **Um agente, uma ferramenta, um MCP server de verdade** | Não é simulação: `fastmcp` real, cliente em memória, ferramenta consultando a base de fraude de verdade |
| **NVIDIA como provedor de LLM** | Escolhido pelo usuário entre NVIDIA, Gemini e Groq. Era também o plano original cogitado no início do curso |
| **Leitura guiada, sem lacuna, no notebook** | Mesma decisão da Aula 12: dado tudo que é novo hoje (MCP, async, tool calling), preencher lacuna de sintaxe custaria fricção demais |
| **A prática reaproveita o exemplo exato do Bloco 03** | "O lojista 141 tem taxa de contestação alta?" é literalmente o exemplo do slide do loop ReAct, agora rodando de verdade |
| **Seis blocos de pergunta, mais um bloco de prática** | Estrutura direta: o usuário deu a ordem das perguntas, o deck seguiu essa ordem, e a prática entrou logo depois do bloco que a fundamenta |
| **AutoGPT como o "gancho dramático" do bloco de história** | Febre viral seguida de decepção prática, prepara terreno emocional para o bloco de controle |
| **O próprio material como exemplo de estado da arte** | O Bloco 08 usa a produção deste curso, feita com apoio de um agente de codificação, como exemplo mais próximo da turma |
| **Condução** | Dupla: Edmar assume história, conceito e controle; Felipe assume a mecânica da prática, a diferença prática, as soluções de mercado e parte do estado da arte |

### Ganchos com as aulas anteriores

- O Bloco 01 reabre a definição de agente da Aula 1 e a promessa explícita da Aula 3
- O Bloco 03 e o Bloco 04 usam o caso de fraude em cartão das Aulas 2, 5, 6, 7, 8, 9, 10
- O Bloco 06 (controle) resolve diretamente o risco que a Fase 5 da Aula 1 já
  apontou: "perder controle e rastreabilidade"
- O Bloco 07 (soluções) cita o RAG da Aula 3 como um exemplo concreto de ferramenta
  que um agente pode ter
- O encerramento aponta para a Aula 14 (quinta), agora reformulada como mentoria
  aberta, e para a Semana 8, reta final da Etapa 1

---

## Regerando o material

```bash
python scripts/gerar_slides_aula13.py       # regera o .pptx
python scripts/exportar_roteiro_aula13.py   # regera o roteiro em markdown
python scripts/auditar_vicios.py scripts/gerar_slides_aula13.py   # passo obrigatório
```

Os dois notebooks não têm gerador de script: foram escritos e são editados
diretamente como `.ipynb`, no mesmo padrão das Aulas 8, 10 e 12.

---

## Pendências antes da aula

**Crítico, teste real:**
- [ ] Rodar o loop completo (Passo 5 em diante) perto da data da aula, cronometrando
      cada pergunta. Já foi testado com chave real e a ferramenta é chamada
      corretamente, mas a latência variou de 4 a 77 segundos por chamada nos testes
      feitos, e o loop faz pelo menos duas chamadas por pergunta. Ver o alerta de
      latência acima
- [ ] Gravar um vídeo de backup do agente respondendo, para o caso de a API estar
      lenta ou instável no dia
- [ ] **Revogar a chave de API usada nos testes** (foi colada em texto puro numa
      conversa) e gerar uma nova antes de distribuir instruções para a turma
- [ ] Decidir se avisa a turma que a resposta pode demorar (às vezes bem mais que
      alguns segundos), para não parecer que travou

**Conteúdo:**
- [ ] Ensaiar o Bloco 02 (história) em voz alta, é o bloco com mais nome próprio e
      mais data do deck
- [ ] Combinar entre Edmar e Felipe os pontos exatos de corte ao vivo, já que o
      próprio usuário pediu para controlar o tempo "de acordo com o que sentirem que
      precisa ser demonstrado"

**Produção da Aula 14:**
- [ ] Definir a dinâmica real da mentoria aberta de quinta (squads se inscrevem por
      horário? Fila livre no chat? Salas separadas?), já que deixou de ser um
      laboratório guiado e os slides de "próximos encontros" já prometem esse formato

**Operacional:**
- [ ] Fixar, no Discord, o link do `Aula_13_Alunos_Construindo_Primeiro_Agente.ipynb`
      antes das 20h15
- [ ] Avisar a turma, com antecedência (e-mail ou Discord), para criar a conta em
      build.nvidia.com **antes** da aula, não durante os 30 minutos da prática
- [ ] Preparar a leitura do chat para a interação do Bloco 05 (comparação de
      cenários)
- [ ] Instalar a fonte Roboto em quem for apresentar pelo PowerPoint
