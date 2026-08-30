# Gabarito: Aula 6, exercícios de SQL

Respostas de referência para as 18 perguntas de `exercicios_aluno.sql`. Uso do
instrutor, para testar no FreeSQL antes da aula e para conferir a resposta de um
aluno rapidamente durante a mentoria.

Cada pergunta traz a contagem real, obtida rodando contra os dados gerados com os
parâmetros padrão (`--seed 42`, 1.500 clientes, 300 lojistas, 50.000 transações). Se
você regerar com outro `--seed`, os números mudam, mas a lógica da consulta continua
valendo.

O arquivo `gabarito_respostas.sql`, na mesma pasta, tem as mesmas 18 consultas prontas
para colar direto no worksheet.

---

## Bloco 1: Anatomia da consulta

### Pergunta 1

Liste o nome e a cidade de todos os clientes de Curitiba.

```sql
SELECT nome, cidade
FROM clientes
WHERE cidade = 'Curitiba';
```

**Esperado:** 69 linhas. Técnica: `WHERE` simples, igualdade de texto.

### Pergunta 2

Liste as 10 transações de maior valor, da maior para a menor.

```sql
SELECT id_transacao, valor
FROM transacoes
ORDER BY valor DESC
FETCH FIRST 10 ROWS ONLY;
```

**Esperado:** 10 linhas. Técnica: `ORDER BY DESC` com `FETCH FIRST`, o equivalente
Oracle do `LIMIT`.

### Pergunta 3

Liste os cartões com status 'bloqueado', mostrando id_cartao, id_cliente e bandeira.

```sql
SELECT id_cartao, id_cliente, bandeira
FROM cartoes
WHERE status = 'bloqueado';
```

**Esperado:** 126 linhas.

---

## Bloco 2: Filtros e condições

### Pergunta 4

Liste as transações com valor entre R$1.000 e R$5.000.

```sql
SELECT id_transacao, valor
FROM transacoes
WHERE valor BETWEEN 1000 AND 5000;
```

**Esperado:** 235 linhas. `WHERE valor >= 1000 AND valor <= 5000` também é aceito,
é a mesma coisa escrita de outro jeito.

### Pergunta 5

Liste os lojistas da cidade de São Paulo.

```sql
SELECT nome, cidade
FROM lojistas
WHERE cidade = 'São Paulo';
```

**Esperado:** 16 linhas.

### Pergunta 6

Liste os clientes cujo nome começa com a letra A.

```sql
SELECT nome
FROM clientes
WHERE nome LIKE 'A%';
```

**Esperado:** 183 linhas.

### Pergunta 7

Liste os clientes sem telefone cadastrado.

```sql
SELECT nome
FROM clientes
WHERE telefone IS NULL;
```

**Esperado:** 251 linhas. Repare no `IS NULL`, nunca `= NULL`.

---

## Bloco 3: Agregações

### Pergunta 8

Quantas transações existem, qual o valor total e qual o valor médio?

```sql
SELECT COUNT(*) AS total_transacoes,
       SUM(valor) AS valor_total,
       AVG(valor) AS valor_medio
FROM transacoes;
```

**Esperado:** 50.000 transações no total, com o valor total e a média variando
conforme o seed usado na geração.

### Pergunta 9

Para cada lojista, quantas transações e qual o valor total?

```sql
SELECT id_lojista, COUNT(*) AS total,
       SUM(valor) AS valor_total
FROM transacoes
GROUP BY id_lojista
ORDER BY valor_total DESC;
```

**Esperado:** 294 linhas, uma por lojista que teve pelo menos uma transação. São 300
lojistas no total, menos os 6 que nunca venderam nada: esses não aparecem aqui, porque
`GROUP BY` só agrupa linha que existe, e eles não têm nenhuma.

### Pergunta 10

Quais lojistas somaram mais de R$25.000 em transações?

```sql
SELECT id_lojista, SUM(valor) AS valor_total
FROM transacoes
GROUP BY id_lojista
HAVING SUM(valor) > 25000
ORDER BY valor_total DESC;
```

**Esperado:** 14 lojistas. Técnica: `HAVING` filtra depois de agrupar, diferente do
`WHERE`.

### Pergunta 11

Quantos cartões cada cliente tem? Liste só quem tem mais de um.

```sql
SELECT id_cliente, COUNT(*) AS total_cartoes
FROM cartoes
GROUP BY id_cliente
HAVING COUNT(*) > 1
ORDER BY total_cartoes DESC;
```

**Esperado:** 452 clientes.

### Pergunta 12

Para cada motivo de contestação, quantas existem, e qual o mais comum?

```sql
SELECT motivo, COUNT(*) AS total
FROM contestacoes
GROUP BY motivo
ORDER BY total DESC;
```

**Esperado:** 4 linhas, uma por motivo. Qual motivo fica em primeiro pode variar um
pouco entre seeds diferentes, porque a distribuição é sorteada com pesos parecidos.

---

## Bloco 4: Juntando tabelas

Diferença importante em relação à Aula 5: ali, `transacoes` tinha `id_cliente` direto.
Aqui não. `transacoes` aponta para `id_cartao`, e é `cartoes` que aponta para
`id_cliente`. Chegar do cliente até a transação dele exige dois `JOIN` em sequência.

### Pergunta 13

Liste as 10 transações de maior valor, com o número final do cartão usado.

```sql
SELECT t.id_transacao, t.valor, c.final_cartao
FROM transacoes t
JOIN cartoes c
  ON t.id_cartao = c.id_cartao
ORDER BY t.valor DESC
FETCH FIRST 10 ROWS ONLY;
```

**Esperado:** 10 linhas. Um `JOIN` só, entre `transacoes` e `cartoes`.

### Pergunta 14

Liste as 10 transações de maior valor com o nome do cliente.

```sql
SELECT t.id_transacao, t.valor, cli.nome
FROM transacoes t
JOIN cartoes car
  ON t.id_cartao = car.id_cartao
JOIN clientes cli
  ON car.id_cliente = cli.id_cliente
ORDER BY t.valor DESC
FETCH FIRST 10 ROWS ONLY;
```

**Esperado:** 10 linhas. Dois `JOIN` em sequência: `transacoes` a `cartoes`, e
`cartoes` a `clientes`.

### Pergunta 15

Liste os lojistas que nunca receberam nenhuma transação.

```sql
SELECT l.id_lojista, l.nome
FROM lojistas l
LEFT JOIN transacoes t
  ON l.id_lojista = t.id_lojista
WHERE t.id_transacao IS NULL;
```

**Esperado:** 6 linhas. São 6 lojistas reservados de propósito no gerador de dados,
para este exercício ter uma resposta real.

### Pergunta 16

Liste os clientes que nunca fizeram nenhuma transação em nenhum cartão.

```sql
SELECT cli.id_cliente, cli.nome
FROM clientes cli
LEFT JOIN cartoes car
  ON cli.id_cliente = car.id_cliente
LEFT JOIN transacoes t
  ON car.id_cartao = t.id_cartao
GROUP BY cli.id_cliente, cli.nome
HAVING COUNT(t.id_transacao) = 0;
```

**Esperado:** 15 linhas, os mesmos 15 clientes que o gerador deixou sem cartão
nenhum.

Esta é a mais delicada das 18. Um `WHERE t.id_transacao IS NULL` sozinho, sem o
`GROUP BY` e o `HAVING`, funcionaria neste conjunto de dados específico, porque aqui
todo cliente sem transação também é um cliente sem nenhum cartão. Mas isso é um
detalhe deste dataset, não uma garantia geral: um cliente com dois cartões, um usado
e outro parado, apareceria errado numa versão mais simples da consulta. O `GROUP BY`
com `HAVING COUNT(...) = 0` confirma que **nenhum** cartão do cliente tem transação,
não só que um deles não tem.

---

## Desafio: combinando tudo

### Pergunta 17

Para cada categoria de lojista, qual o valor total de transações contestadas?

```sql
SELECT cat.nome AS categoria, SUM(t.valor) AS valor_contestado
FROM transacoes t
JOIN lojistas l
  ON t.id_lojista = l.id_lojista
JOIN categorias cat
  ON l.id_categoria = cat.id_categoria
WHERE t.status = 'contestada'
GROUP BY cat.nome
ORDER BY valor_contestado DESC;
```

**Esperado:** 12 linhas, uma por categoria. Três tabelas juntas (`transacoes`,
`lojistas`, `categorias`), com filtro e agregação por cima.

### Pergunta 18

Liste os clientes com pelo menos uma transação contestada, com motivo e resultado.

```sql
SELECT cli.nome AS cliente, con.motivo, con.resultado
FROM contestacoes con
JOIN transacoes t
  ON con.id_transacao = t.id_transacao
JOIN cartoes car
  ON t.id_cartao = car.id_cartao
JOIN clientes cli
  ON car.id_cliente = cli.id_cliente
ORDER BY cli.nome;
```

**Esperado:** 1.013 linhas, uma por contestação (o mesmo total de linhas de
`contestacoes`). Alguns clientes aparecem mais de uma vez, se tiveram mais de uma
transação contestada. Quatro tabelas encadeadas: `contestacoes` a `transacoes`,
`transacoes` a `cartoes`, `cartoes` a `clientes`.
