# Material de apoio: Aula 3

**AI Talent Academy** · Semana 2 · IA Generativa

> Enviado depois da aula, junto com a gravação. É a folha de consulta para reabrir daqui
> a três semanas, quando você esquecer o que era temperatura.

---

## As 6 ideias da noite

1. **Token, embedding e atenção explicam o comportamento dele**, inclusive o comportamento
   estranho.
2. **Ele escolhe o token mais provável**, e provável é diferente de verdadeiro. Por isso a
   alucinação é esperada.
3. **Prompt é especificação**, com cinco elementos: papel, tarefa, contexto, formato e
   restrição.
4. **Mostrar dois exemplos vale mais** que escrever três parágrafos de instrução. E dizer o
   alvo funciona melhor que dizer o que evitar.
5. **RAG é o que faz ele falar da sua empresa** citando fonte. A qualidade depende mais da
   busca do que do modelo.
6. **Ela brilha em texto e falha em conta exata.** O modelo escreve a fórmula, a planilha
   executa.

---

## Os seis verbos que a GenAI faz bem

Se a sua tarefa não cabe em um destes, desconfie antes de escolher IA generativa.

| Verbo | O que é | Exemplo de trabalho |
|---|---|---|
| **Resumir** | Reduzir texto longo mantendo o que importa | Ata de reunião, thread de e-mail, relatório longo |
| **Classificar** | Ler um texto e dizer em que categoria cai | Motivo do chamado, sentimento da avaliação |
| **Extrair** | Tirar campos estruturados de texto bagunçado | Valor e vencimento de nota, partes de contrato |
| **Transformar** | Reescrever mudando formato, tom ou público | Texto técnico para linguagem de negócio |
| **Gerar** | Produzir a primeira versão de alguma coisa | Rascunho de e-mail, descrição de produto |
| **Conversar** | Responder pergunta com contexto | Busca interna, assistente de suporte |

---

## Como ele funciona por dentro

### Token

O modelo não lê letra nem palavra inteira. Ele lê pedaços de palavra, chamados **tokens**.
Em português, uma palavra costuma virar 2 ou 3 tokens. Palavra comum vira 1, palavra rara
vira vários.

**Por que importa:** preço de API e tamanho da janela de contexto são contados em token,
não em palavra. E português gasta mais token que inglês para o mesmo texto.

### Embedding

Pense em cor: toda cor vira três números (quanto de vermelho, verde e azul). Cores
parecidas têm números parecidos. Vermelho e vinho ficam perto, vermelho e azul ficam longe.

Palavra funciona igual, só que com **centenas** de coordenadas em vez de três. Palavras de
sentido próximo caem perto nesse mapa: "demitir", "desligar" e "rescindir" viram vizinhas,
mesmo sem ter uma letra em comum.

**Por que importa:** permite buscar por significado, e não por letra. É o que faz a busca
interna da empresa e o RAG funcionarem.

### Atenção

Leia: *"o prefeito negou a licença aos manifestantes porque **ele** temia violência."*
Agora: *"...porque **eles** pregavam violência."*

Uma letra muda o dono da frase inteira, e você resolveu isso sem esforço, olhando a frase
toda de uma vez. **Atenção** é o mecanismo que faz o modelo fazer o mesmo: para cada
palavra, ele pesa o quanto cada outra importa.

**Por que importa:** antes de 2017, os modelos liam em ordem e esqueciam o começo. A
arquitetura Transformer trouxe a atenção, e é ela que está por trás de tudo que você usa
hoje.

### Temperatura

Do processo sai uma **lista de candidatos com probabilidade**, e alguém precisa escolher um.
Temperatura é o botão que controla essa escolha.

| Temperatura | Efeito | Quando usar |
|---|---|---|
| Baixa | Escolhe sempre o mais provável. Resposta repetível | Extração, classificação, operação |
| Alta | Dá chance aos menos prováveis. Resposta variada | Redação, geração de ideia |

**Por que importa:** quando alguém reclama que "a IA respondeu diferente da última vez",
quase sempre é isto.

### Janela de contexto

Imagine uma mesa onde cabe uma quantidade fixa de papel. Tudo que está na mesa, ele
enxerga. Sua pergunta, o histórico da conversa e os arquivos colados disputam o mesmo
espaço. Quando enche, o começo cai da mesa e ele nunca mais vê aquilo.

**Por que importa:** explica por que ele esquece o início de conversa longa, e por que
repetir a informação resolve. E ele **não tem memória entre conversas**: cada conversa nova
começa com a mesa vazia.

---

## Os cinco elementos de um prompt

Nenhum prompt precisa dos cinco. Mas todo prompt ruim está sem pelo menos três.

| Elemento | O que é | Exemplo |
|---|---|---|
| **Papel** | Quem o modelo deve ser | "Você é um analista de dados explicando para um gerente comercial." |
| **Tarefa** | O verbo, específico | "Classifique cada chamado abaixo." Melhor que "analise". |
| **Contexto** | O material que ele precisa ter | O texto da política, os dados, o histórico. Cole junto. |
| **Formato** | Como você quer receber | "Uma linha de tabela por item, com estas três colunas." |
| **Restrição** | Tamanho, tom, e o que fazer na dúvida | "Máximo 3 frases. Se faltar informação, escreva NÃO SEI." |

### O padrão que evita alucinação

```
[cole aqui o documento]

Com base APENAS no texto acima, responda: [sua pergunta]
Se o texto não disser, responda NÃO CONSTA.
```

As três partes importam: o texto vem antes da pergunta, a fonte fica restrita, e ele ganha
uma saída honesta para quando não souber.

---

## O que funciona e o que é folclore

### Funciona

- **Dar exemplos.** Mostre 2 ou 3 exemplos com entrada e saída. Vale mais que descrever o
  formato em três parágrafos.
- **Pedir o raciocínio.** "Explique seu raciocínio antes da resposta final." Ajuda em
  tarefa com etapas. Custa mais token, então evite em tarefa simples.
- **Definir papel e público.** Muda vocabulário e profundidade de uma vez só.

### Folclore

- Dizer "por favor" e "obrigado" (sem efeito confiável na qualidade)
- Prometer gorjeta ou ameaçar o modelo
- Escrever em CAIXA ALTA para enfatizar (gasta mais token e não obriga nada)
- Repetir a mesma instrução três vezes
- Achar que prompt gigante é sempre melhor (instrução contraditória piora o resultado)
- Dizer só o que **não** fazer, em vez de dizer o alvo

---

## RAG, em quatro passos

O modelo não sabe nada da sua empresa. Mas você não vai colar dez mil documentos a cada
pergunta.

1. **A pergunta chega**
2. **O sistema busca** os trechos mais próximos em significado nos documentos da empresa
3. **Os trechos são colados** no prompt, junto com a pergunta
4. **O modelo responde** com base no que foi colado, citando a fonte

**Duas consequências:** a resposta vem com fonte, e fonte é o que faz o usuário confiar. E
se a busca do passo 2 trouxer o trecho errado, o modelo responde errado com total
confiança. A qualidade do RAG depende mais da busca do que do modelo.

---

## Banco vetorial

O embedding transforma texto em coordenada. O **banco vetorial** é onde essas coordenadas
moram, e é o que faz o passo 2 do RAG funcionar em escala.

Cada pedaço de documento vira uma linha: o texto original, mais a coordenada dele. Quando
a pergunta chega, ela também vira coordenada, e o banco busca os vizinhos mais próximos,
usando um índice especializado que permite buscar entre milhões de coordenadas em
milissegundos.

É como um aplicativo de mapa achando o restaurante mais perto de você: ele não compara a
distância até cada restaurante do país, um por um. Sem esse tipo de índice, RAG funciona
numa pasta de vinte documentos e trava numa base de verdade.

**Um cuidado técnico:** busca por coordenada (chamada de **densa**) acha sentido parecido,
mas pode perder uma palavra-chave exata, como um código de produto ou número de lei. Um
sistema de busca bem feito costuma combinar busca densa com busca por palavra exata
(chamada de **esparsa**).

---

## RAG × fine-tuning

Duas formas diferentes de adaptar um modelo para o seu contexto, e é comum confundir as
duas.

| | RAG | Fine-tuning |
|---|---|---|
| Como funciona | Entrega os documentos certos na hora da pergunta | Retreina o modelo com exemplos do seu padrão de resposta |
| Resolve | Conhecimento que muda: política, preço, estoque | Comportamento: tom, formato, jargão do setor |
| Atualizar | Troca o documento, pronto | Exige treinar de novo, processo mais lento |
| Efeito | Mantém o jeito de responder do modelo igual | Ensina jeito de responder, não fato confiável |
| Custo | Mais barato e mais rápido de montar | Mais caro e mais lento de montar |

**Na dúvida, comece por RAG.** Ele resolve a maior parte dos casos reais de conhecimento
desatualizado. Fine-tuning entra quando o alvo do ajuste é o comportamento do modelo.

---

## Quando usar e quando evitar

| ✅ GenAI resolve quando | ❌ GenAI atrapalha quando |
|---|---|
| O trabalho principal é ler ou escrever texto | O problema pede número exato e reproduzível |
| Existe variação demais para escrever regra fixa | Existe uma resposta certa e auditável |
| Errar de vez em quando é tolerável | A decisão é automática, sem humano no meio |
| Tem humano conferindo antes de virar decisão | O custo de errar é alto e difícil de desfazer |
| O ganho é tempo, e o volume é alto | Já existe regra simples que resolve |
| Não existe uma única resposta certa | Você precisa explicar a decisão de forma determinística |

Conte quantos sinais de cada lado o seu problema tem. O lado com mais sinais decide.

### O erro mais comum

Pedir para o modelo **calcular**. Alguém cola uma planilha e pede a soma de uma coluna. A
resposta vem com aparência perfeita. Com poucas linhas costuma acertar, e a pessoa confia.
Com volume maior ele erra e não avisa, porque ele nunca esteve somando: ele estava
compondo texto plausível.

**A correção:** o modelo escreve a **fórmula** ou o **código**. A planilha, ou o Python,
executa.

---

## Glossário da noite

| Termo | O que é |
|---|---|
| **Token** | O pedaço de palavra que o modelo processa. Unidade de preço e de limite |
| **Embedding** | A representação de um texto como coordenadas num mapa de significados |
| **Atenção** | Mecanismo que pesa, para cada palavra, o quanto cada outra importa |
| **Transformer** | Arquitetura de 2017 que trouxe a atenção. Base de todos os LLMs atuais |
| **Temperatura** | Controle de aleatoriedade na escolha do próximo token |
| **Janela de contexto** | Quanto texto cabe de uma vez. A mesa de trabalho do modelo |
| **Pré-treino** | Fase em que ele leu texto em escala e aprendeu a completar frase |
| **Ajuste por instrução** | Fase em que ele aprendeu a atender pedido, e não só completar |
| **Alinhamento (RLHF)** | Fase em que pessoas indicaram qual resposta preferiam |
| **RAG** | Buscar trechos relevantes e colar no prompt antes de responder |
| **Banco vetorial** | Onde as coordenadas do embedding ficam guardadas para busca em escala |
| **Busca densa** | Busca por coordenada, por significado. É o que o embedding permite |
| **Busca esparsa** | Busca por palavra exata, como uma busca tradicional |
| **Fine-tuning** | Retreinar um modelo pronto com exemplos do seu padrão de resposta |
| **Alucinação** | Produzir informação falsa com aparência de verdadeira |
| **Few-shot** | Dar exemplos de entrada e saída dentro do próprio prompt |

---

## Para fazer até quinta

**Obrigatório (2 minutos)**
- [ ] Garanta que você tem uma **conta Google** ativa. Vamos usar o Google Colab.

**Recomendado (15 minutos), vale muito a pena**
- [ ] Pegue um pedido que você já fez para uma IA e que deu resposta ruim. Reescreva usando
      os cinco elementos. Compare as duas respostas.

**Opcional**
- [ ] Teste o padrão de contexto (colar documento + "com base APENAS no texto acima" +
      "se não disser, responda NÃO CONSTA") com algum documento seu.

Nada para instalar. Tudo roda no navegador.

---

## Próximo encontro

**Quinta-feira, 19h00 às 21h00.** Primeira aula com código. Google Colab, primeira chamada
a uma API de LLM, e os cinco elementos de prompt na prática.

Quem nunca programou: vai entrar devagar, do zero.

Dúvidas até lá: canal `#duvidas` do Discord.
