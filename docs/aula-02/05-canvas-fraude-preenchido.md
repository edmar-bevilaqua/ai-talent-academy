# Canvas preenchido ao vivo: fraude em cartão de crédito

Guia de apoio para a demonstração dos slides 10 a 19. Para cada campo: o **texto pronto**
para digitar no canvas compartilhado enquanto você fala, e um lembrete curto do que **não
pode faltar** na fala. A ordem é a mesma da tela, então dá para seguir slide a slide.

---

## Antes de abrir o campo 1: o pedido vago

Leia em voz alta, com entonação de quem recebeu isso numa reunião:

> "Queremos usar IA para reduzir as perdas com fraude no cartão."

Lembrete: é o mesmo problema que apareceu duas vezes na Aula 1 (compra bloqueada pelo
banco, e o modelo de 99% de acurácia que não pegava fraude nenhuma). Diga isso antes de
abrir o campo 1, cria continuidade.

---

## Campo 1 · Contexto

**Texto para o canvas**
- Decisão: a cada transação, em milissegundos, aprovar, pedir confirmação ou recusar
- Hoje quem decide: regras fixas (valor acima de X, país estrangeiro, categoria de risco)
- Problema da regra fixa: não se adapta, o fraudador testa até achar o limite
- Custo de errar para menos: perda que o banco absorve
- Custo de errar para mais: cliente legítimo recusado na frente da fila
- Fora do desejo vago: "reduzir fraude" não é decisão. Vamos fechar em fraude de cartão
  clonado (não fraude interna, não conta invadida)

**Não esquecer de falar**
- "Reduzir fraude" é vontade da diretoria. A decisão real, específica, é o que escrevemos aqui.
- A decisão já é tomada hoje, só que por um sistema de regras, não por uma pessoa.

---

## Campo 2 · Usuários

**Texto para o canvas**
- Usuário direto: o sistema de autorização, consome a resposta em menos de 100 ms
- Usuário humano: o analista de prevenção a fraude, calibra o limiar e revisa a fila
- A fila do analista tem capacidade limitada por dia
- Terceiro afetado: o cliente que teve a compra recusada, reclama no SAC
- Requisito: se o analista não entender por que o modelo marcou, a fila trava

**Não esquecer de falar**
- Usuário nem sempre é uma pessoa só. Aqui são três, com necessidades diferentes.
- O prazo de 100 ms virou requisito técnico a partir de uma pergunta sobre gente, não de arquitetura.

---

## Campo 3 · Dados necessários

**Texto para o canvas**
- Histórico do cliente: valor, horário, categoria e local das compras habituais
- Dados da transação atual: valor, lojista, país, presencial ou online
- Sessão online: dispositivo, tempo de preenchimento, geolocalização
- Rótulo de fraude confirmada vem do chargeback, com atraso de 30 a 90 dias
- Cuidado com vazamento: "transação estornada" só existe depois. Não pode entrar no modelo

**Não esquecer de falar**
- O rótulo chega atrasado: o modelo aprende com o mundo de três meses atrás, e o fraudador já mudou de tática.
- Isso vai aparecer de novo no campo 7, na frequência de retreino.

---

## Campo 4 · Hipóteses

**Texto para o canvas**
- O fraudador testa valor baixo antes do valor alto
- Compra fora do padrão geográfico do cliente pesa muito (padrão varia por cliente)
- Cartão não presente (compra online) arrisca mais que presencial
- Sequência rápida em lojistas diferentes é sinal forte
- Hipótese a derrubar: "fraude concentra na madrugada", pode ser só viés de proporção

**Não esquecer de falar**
- Hipótese boa é a que pode ser derrubada pelo dado. Escreva antes de olhar.
- Destaque a hipótese que você espera derrubar, isso mostra que hipótese não é certeza.

---

## Campo 5 · Riscos

**Texto para o canvas**
- Fora do escopo: fraude interna e fraude de estabelecimento (outra lógica, outros dados)
- Fora do escopo: recuperar o valor depois do chargeback (outro time)
- Risco ético: bloquear mais numa região ou faixa de renda é discriminação, mesmo sem ninguém programar isso
- O modelo pode aprender CEP como substituto de renda
- Quem é prejudicado: o cliente legítimo constrangido no caixa
- Exigência: o SAC precisa conseguir explicar o bloqueio ao cliente

**Não esquecer de falar**
- Puxe o gancho com o caso da Amazon da Aula 1: ninguém programou discriminação, o modelo aprendeu sozinho.
- Se o SAC não explica o bloqueio, o cliente cancela o cartão. Isso já vira requisito de negócio, além de ético.

---

## Campo 6 · Tipo de Solução

**Texto para o canvas**
- Não é IA generativa: não tem texto para gerar nem para entender
- Classificação, devolvendo SCORE em vez de sim ou não
- Score permite três ações: aprovar, pedir confirmação, recusar
- Baseline obrigatório: as regras fixas que já existem hoje
- Restrição dura: responder em menos de 100 ms

**Não esquecer de falar**
- Este é o único dos oito campos que fala de tecnologia, e ele vem só em sexto lugar.
- Score em vez de sim/não é decisão de produto: a faixa do meio salva o cliente legítimo do constrangimento.
- Se o modelo não vencer as regras atuais, mantém as regras e economiza o projeto inteiro.

---

## Campo 7 · Estrutura de Custos

**Texto para o canvas**
- Maior custo: infraestrutura de baixa latência (100 ms, milhões de transações por dia)
- Desenvolvimento: time de 2 a 3 pessoas, por alguns meses
- Retreino em semanas, não em trimestres (fraude se adapta rápido, rótulo já chega atrasado)
- Custo da fila de revisão manual: tempo do analista
- Custo escondido: falso bloqueio (ligação no SAC, cliente irritado, às vezes cancelamento)
- Comparar sempre com a perda atual em reais por mês

**Não esquecer de falar**
- Este é o campo que quase ninguém preenche, e é o que mais derruba projeto depois de aprovado.
- Sem comparar com a perda atual, ninguém aprova orçamento.

---

## Campo 8 · Métricas de Sucesso

**Texto para o canvas**
- De negócio: reduzir 25% da perda financeira com fraude, medida em reais
- De modelo: priorizar recall, com teto de falso positivo
- Contra-métrica: falso bloqueio abaixo de 1%
- De operação: a fila de revisão cabe na equipe atual
- Prazo: 3 meses rodando, com grupo de controle

**Não esquecer de falar**
- Feche relembrando o caso da Aula 1: modelo que acerta 99% respondendo sempre "não é fraude" e não pega fraude nenhuma. É por isso que acurácia não entra nesta lista.
- Sem contra-métrica, existe uma solução trivial que bate a meta: recusar tudo.

---

## Fechamento: o contraste final

Depois de preencher os 8 campos, mostre lado a lado:

| Antes | Depois |
|---|---|
| "Queremos usar IA para reduzir as perdas com fraude no cartão." | Decisão específica, 3 usuários, dado com rótulo atrasado, hipóteses testáveis, riscos éticos escritos, solução com justificativa, custo real mapeado, meta em reais com contra-métrica e prazo |

Pergunta de fechamento, para ler devagar:

> "Se você fosse o diretor que fez o pedido original, qual dos dois você aprovaria? A
> frase ou este canvas?"

Depois: "Quinze minutos. Sem abrir um dado, sem escrever uma linha de código. Agora é a
vez de vocês."
