# Casos coringa: para grupo que esqueceu de trazer problema

Sete casos prontos, fora dos domínios já usados hoje (fraude em cartão na demonstração,
evasão escolar e fila de pronto-socorro nas opções A e B). Use quando um grupo chegar sem
problema próprio e sem interesse nos casos A ou B.

**Como usar:** leia o "pedido vago" em voz alta para o grupo, do jeito que chegaria numa
reunião de verdade. Deixe o grupo discutir e preencher o canvas com as próprias palavras.
A tabela abaixo é gabarito seu, para orientar a conversa, e não texto para colar no
documento do grupo.

---

## Caso 1 · Varejo: reposição de estoque

**Pedido vago:** "Queremos usar IA para nunca mais faltar produto na loja."

| Campo | Resposta simplificada |
|---|---|
| 1. Contexto | Definir quanto pedir de reposição, por produto e por loja, toda semana |
| 2. Usuários | Comprador da categoria. Decide toda quarta, com poucas horas para centenas de produtos |
| 3. Dados necessários | Venda histórica por loja e produto, estoque atual, calendário de promoções, ruptura passada |
| 4. Hipóteses | Sazonalidade pesa mais que tendência recente. Promoção distorce a média das semanas seguintes |
| 5. Riscos | Fora do escopo: produto novo sem histórico. Risco de negócio: estoque parado imobiliza caixa |
| 6. Tipo de Solução | Previsão de demanda (regressão). Baseline: média das últimas 4 semanas |
| 7. Estrutura de Custos | Dado já existe no ERP. O custo real está em integrar e manter atualizado |
| 8. Métricas de Sucesso | Reduzir ruptura em X%, sem deixar o estoque parado subir acima de Y% |

---

## Caso 2 · Varejo: quando dar desconto

**Pedido vago:** "Queremos usar IA para vender tudo que encalha."

| Campo | Resposta simplificada |
|---|---|
| 1. Contexto | Decidir quando e quanto descontar um produto que parou de girar |
| 2. Usuários | Time de pricing. Revisa a coleção toda semana, pouco tempo por produto |
| 3. Dados necessários | Giro por produto, margem, estoque parado, histórico de desconto, fim de coleção |
| 4. Hipóteses | Desconto de 30% converte muito mais que 20%. Após 60 dias parado, o produto não gira mais sem corte |
| 5. Riscos | Fora do escopo: preço de lançamento. Ético: inflar preço antes da promoção fere o CDC |
| 6. Tipo de Solução | Começa descritivo (o que encalha e quando), depois otimização de desconto |
| 7. Estrutura de Custos | Dado interno. O custo escondido é aprovar mudança de preço com o comercial |
| 8. Métricas de Sucesso | Reduzir estoque de fim de coleção em X%, sem perder mais de Y pontos de margem |

---

## Caso 3 · Financeiro: priorizar cobrança

**Pedido vago:** "Queremos usar IA para cobrar melhor os inadimplentes."

| Campo | Resposta simplificada |
|---|---|
| 1. Contexto | Escolher quem entra na lista de ligações de cobrança do dia |
| 2. Usuários | Coordenador de cobrança. Monta a lista às 8h, com 15 minutos |
| 3. Dados necessários | Histórico de pagamento, dias de atraso, valor devido, contatos anteriores, canal que respondeu |
| 4. Hipóteses | Quem atrasou pela primeira vez paga mais fácil. Acima de 90 dias, a chance despenca |
| 5. Riscos | Fora do escopo: renegociação e cobrança judicial. Ético: não constranger, respeitar o CDC |
| 6. Tipo de Solução | Classificação (quem paga se for acionado). Baseline: ordenar por valor devido |
| 7. Estrutura de Custos | Dado interno, custo por ligação já é conhecido, o ROI fecha fácil |
| 8. Métricas de Sucesso | Aumentar recuperação em X% com a mesma equipe. Contra-métrica: reclamação no Procon |

---

## Caso 4 · RH: risco de saída de funcionário

**Pedido vago:** "Queremos usar IA para parar de perder gente boa."

| Campo | Resposta simplificada |
|---|---|
| 1. Contexto | Identificar quais funcionários têm risco alto de pedir demissão nos próximos meses |
| 2. Usuários | Parceiro de negócios de RH. Revisa mensalmente com cada líder |
| 3. Dados necessários | Tempo de casa, histórico de promoção, avaliação de desempenho, faltas, pesquisa de clima |
| 4. Hipóteses | Quem não é promovido em X anos tem risco maior. Queda recente na pesquisa de clima é sinal de alerta |
| 5. Riscos | Ético central: usar o score para demitir antes, em vez de reter, inverte o objetivo do projeto. Dado sensível: LGPD |
| 6. Tipo de Solução | Classificação com score de risco. Baseline: tempo de casa sozinho |
| 7. Estrutura de Custos | Dado espalhado em vários sistemas (RH, avaliação, ponto). Juntar tudo é o custo real |
| 8. Métricas de Sucesso | Reduzir saída voluntária em X%. Contra-métrica: o score nunca vira justificativa de punição |

---

## Caso 5 · Atendimento: priorizar chamados de suporte

**Pedido vago:** "Queremos usar IA para o suporte responder mais rápido."

| Campo | Resposta simplificada |
|---|---|
| 1. Contexto | Decidir qual chamado a equipe atende primeiro, dentro da fila do dia |
| 2. Usuários | Atendente e supervisor da fila. Decisão se repete a cada poucos minutos, o dia inteiro |
| 3. Dados necessários | Texto do chamado, histórico do cliente, plano contratado, tempo de espera atual |
| 4. Hipóteses | Palavras como "cancelar" e "urgente" no texto indicam prioridade real |
| 5. Riscos | Fora do escopo: automatizar a resposta em si. Ético: cliente de plano menor não pode ficar sempre por último |
| 6. Tipo de Solução | IA generativa para classificar o chamado por urgência e tema. Baseline: ordem de chegada |
| 7. Estrutura de Custos | Custo por chamada de API de classificação, multiplicado pelo volume diário |
| 8. Métricas de Sucesso | Reduzir o tempo de espera dos chamados urgentes, sem piorar a média geral |

---

## Caso 6 · Logística: priorizar entregas atrasadas

**Pedido vago:** "Queremos usar IA para nunca mais atrasar entrega."

| Campo | Resposta simplificada |
|---|---|
| 1. Contexto | Decidir quais entregas do dia recebem rota prioritária, quando não dá para atender todas no prazo |
| 2. Usuários | Coordenador de logística. Decide de manhã, antes das rotas saírem |
| 3. Dados necessários | Prazo prometido ao cliente, distância, histórico de atraso da região, capacidade do veículo |
| 4. Hipóteses | Entregas em regiões com histórico de trânsito atrasam mais, mesmo perto do centro de distribuição |
| 5. Riscos | Fora do escopo: escolha da transportadora. Risco: priorizar sempre o mesmo bairro cria desigualdade de serviço |
| 6. Tipo de Solução | Otimização de rota com prioridade por risco de atraso. Baseline: ordem de prazo mais curto |
| 7. Estrutura de Custos | Dado de trânsito histórico pode exigir fonte externa paga |
| 8. Métricas de Sucesso | Reduzir entregas atrasadas em X%, sem subir o custo de frete acima de Y% |

---

## Caso 7 · Vendas: priorizar leads

**Pedido vago:** "Queremos usar IA para o time de vendas ligar para quem realmente vai comprar."

| Campo | Resposta simplificada |
|---|---|
| 1. Contexto | Decidir a ordem em que o vendedor liga para os leads que chegaram no dia |
| 2. Usuários | Vendedor (SDR). Recebe a lista pela manhã, com capacidade para ligar só para uma parte |
| 3. Dados necessários | Origem do lead, páginas visitadas no site, porte da empresa, histórico de conversão por origem |
| 4. Hipóteses | Lead que veio de indicação converte muito mais que lead de anúncio frio |
| 5. Riscos | Fora do escopo: o discurso de vendas em si. Risco: descartar um lead bom só porque o score errou |
| 6. Tipo de Solução | Score de propensão a comprar (classificação). Baseline: ordenar por origem do lead |
| 7. Estrutura de Custos | Dado de navegação exige integração com o site, que tem custo de engenharia |
| 8. Métricas de Sucesso | Aumentar a conversão do funil, sem aumentar o tempo médio até a primeira resposta |

---

## Tabela resumo, para escolher rápido

| # | Caso | Setor | Bom para grupo que gosta de... |
|---|---|---|---|
| 1 | Reposição de estoque | Varejo | Números, previsão, operação do dia a dia |
| 2 | Desconto de produto parado | Varejo | Trade-off, precificação, margem |
| 3 | Priorizar cobrança | Financeiro | Risco, ética de cobrança, regra clara |
| 4 | Risco de saída de funcionário | RH | Discussão ética, dado sensível, pessoas |
| 5 | Priorizar chamados de suporte | Atendimento | GenAI, texto, experiência do cliente |
| 6 | Priorizar entregas atrasadas | Logística | Otimização, geografia, justiça de serviço |
| 7 | Priorizar leads | Vendas | Funil, conversão, crescimento |
