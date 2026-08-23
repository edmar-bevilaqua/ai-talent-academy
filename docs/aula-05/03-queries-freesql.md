# Queries para a demonstração ao vivo no Oracle FreeSQL

> Base própria, criada na hora da demonstração, com o mesmo caso de fraude em cartão
> usado na Aula 5. Não depende do schema pré-carregado do FreeSQL, porque os nomes
> exatos de tabela e coluna daquele schema não foram confirmados. Cole os blocos abaixo
> na ordem, todos rodam em [freesql.com](https://freesql.com/).

**Um cuidado de sintaxe antes de começar:** o slide da Aula 5 usa `LIMIT 10`, que é
sintaxe de MySQL e PostgreSQL. Oracle não tem `LIMIT`. O equivalente é
`FETCH FIRST n ROWS ONLY`, depois do `ORDER BY`. As queries abaixo já usam a forma
correta para o FreeSQL. Se copiar direto do slide, vai dar erro de sintaxe.

---

## 1. Criar as tabelas (DDL)

Três tabelas, o mesmo caso da Aula 5: quem compra, onde compra, e a transação em si.

```sql
-- Isso aqui é DDL (Data Definition Language): cria a estrutura, ainda sem dado dentro.

CREATE TABLE clientes (
    id_cliente     NUMBER PRIMARY KEY,
    nome           VARCHAR2(60),
    cidade         VARCHAR2(40),
    telefone       VARCHAR2(20),
    data_cadastro  DATE
);

CREATE TABLE lojistas (
    id_lojista NUMBER PRIMARY KEY,
    nome       VARCHAR2(60),
    categoria  VARCHAR2(30),
    cidade     VARCHAR2(40)
);

CREATE TABLE transacoes (
    id_transacao NUMBER PRIMARY KEY,
    id_cliente   NUMBER,
    id_lojista   NUMBER,
    valor        NUMBER(10,2),
    data_hora    DATE,
    canal        VARCHAR2(20),
    status       VARCHAR2(20),
    CONSTRAINT fk_transacoes_cliente FOREIGN KEY (id_cliente)
        REFERENCES clientes (id_cliente),
    CONSTRAINT fk_transacoes_lojista FOREIGN KEY (id_lojista)
        REFERENCES lojistas (id_lojista)
);
```

As duas linhas de `CONSTRAINT` são a chave estrangeira. Elas dizem ao banco que todo
`id_cliente` dentro de `transacoes` precisa existir antes em `clientes`, e todo
`id_lojista` precisa existir antes em `lojistas`. É a mesma ideia da tabela de chave
primária e chave estrangeira da seção 6, agora aplicada na criação da tabela, não só
explicada.

Por causa disso, a ordem de criação passa a importar: `clientes` e `lojistas` precisam
existir antes de `transacoes`, senão o `REFERENCES` não encontra o que apontar. A ordem
acima já está correta.

Um efeito prático de ter a chave estrangeira: se alguém tentar inserir uma transação
com um `id_cliente` que não existe, o banco recusa a inserção, em vez de aceitar um dado
quebrado. Dá para mostrar isso ao vivo, se sobrar tempo:

```sql
INSERT INTO transacoes VALUES (99, 999, 1, 100.00, DATE '2026-03-15', 'online', 'aprovada');
-- Erro esperado: ORA-02291, violação de chave estrangeira. O cliente 999 não existe.
```

Se precisar refazer a demonstração outro dia, rode antes:

```sql
DROP TABLE transacoes;
DROP TABLE clientes;
DROP TABLE lojistas;
```

A ordem do `DROP` também importa agora, e por sorte já está certa: `transacoes` precisa
sair primeiro, porque é ela que tem a chave estrangeira apontando para as outras duas.
Tentar apagar `clientes` ou `lojistas` antes dá erro, porque ainda existe uma tabela
dependendo delas.

---

## 2. Popular as tabelas (DML)

### 2.1 Clientes

Repare nos três clientes sem telefone cadastrado (`NULL`), e no cliente 8, que nunca fez
nenhuma compra. Os dois casos servem de exemplo mais à frente.

```sql
INSERT INTO clientes VALUES (1, 'Ana Souza', 'Curitiba', '11999990001', DATE '2023-03-10');
INSERT INTO clientes VALUES (2, 'Bruno Lima', 'São Paulo', '11999990002', DATE '2022-11-05');
INSERT INTO clientes VALUES (3, 'Carla Mendes', 'São Paulo', NULL, DATE '2024-01-20');
INSERT INTO clientes VALUES (4, 'Diego Alves', 'Curitiba', '41999990004', DATE '2023-07-15');
INSERT INTO clientes VALUES (5, 'Elisa Rocha', 'Belo Horizonte', NULL, DATE '2021-09-01');
INSERT INTO clientes VALUES (6, 'Fabio Nunes', 'Rio de Janeiro', '21999990006', DATE '2024-05-12');
INSERT INTO clientes VALUES (7, 'Gabriela Dias', 'São Paulo', '11999990007', DATE '2022-02-28');
INSERT INTO clientes VALUES (8, 'Hugo Castro', 'Curitiba', NULL, DATE '2023-12-01');
COMMIT;
```

### 2.2 Lojistas

O lojista 5 nunca recebeu nenhuma transação. É a mesma pergunta da enquete da Aula 5:
qual JOIN revela isso.

```sql
INSERT INTO lojistas VALUES (1, 'TechPoint Eletronicos', 'Eletronicos', 'São Paulo');
INSERT INTO lojistas VALUES (2, 'Joalheria Aurora', 'Joalheria', 'Curitiba');
INSERT INTO lojistas VALUES (3, 'Mercado Bom Preco', 'Supermercado', 'São Paulo');
INSERT INTO lojistas VALUES (4, 'Posto Estrada Norte', 'Combustivel', 'Belo Horizonte');
INSERT INTO lojistas VALUES (5, 'Livraria Pagina Certa', 'Livraria', 'Rio de Janeiro');
COMMIT;
```

### 2.3 Transações

24 transações, espalhadas entre os 7 clientes que compram e os 4 lojistas que vendem.
Duas estão com status `contestada`, o gatilho de fraude do caso.

```sql
INSERT INTO transacoes VALUES (1, 1, 1, 350.00, DATE '2026-01-05', 'online', 'aprovada');
INSERT INTO transacoes VALUES (2, 1, 2, 1200.00, DATE '2026-01-10', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (3, 2, 1, 89.90, DATE '2026-01-12', 'online', 'aprovada');
INSERT INTO transacoes VALUES (4, 2, 3, 245.30, DATE '2026-01-15', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (5, 3, 1, 4500.00, DATE '2026-01-18', 'online', 'contestada');
INSERT INTO transacoes VALUES (6, 3, 4, 180.00, DATE '2026-01-20', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (7, 4, 2, 2300.00, DATE '2026-01-22', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (8, 4, 3, 67.50, DATE '2026-01-25', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (9, 5, 1, 999.00, DATE '2026-02-01', 'online', 'recusada');
INSERT INTO transacoes VALUES (10, 5, 4, 210.00, DATE '2026-02-03', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (11, 6, 3, 55.00, DATE '2026-02-05', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (12, 6, 1, 3200.00, DATE '2026-02-08', 'online', 'aprovada');
INSERT INTO transacoes VALUES (13, 7, 2, 890.00, DATE '2026-02-10', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (14, 7, 4, 130.00, DATE '2026-02-12', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (15, 1, 3, 42.00, DATE '2026-02-15', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (16, 2, 2, 1750.00, DATE '2026-02-18', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (17, 3, 3, 88.90, DATE '2026-02-20', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (18, 4, 1, 5600.00, DATE '2026-02-22', 'online', 'contestada');
INSERT INTO transacoes VALUES (19, 5, 2, 430.00, DATE '2026-02-25', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (20, 6, 4, 199.90, DATE '2026-03-01', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (21, 7, 1, 76.00, DATE '2026-03-03', 'online', 'aprovada');
INSERT INTO transacoes VALUES (22, 1, 4, 310.00, DATE '2026-03-05', 'presencial', 'aprovada');
INSERT INTO transacoes VALUES (23, 3, 1, 12000.00, DATE '2026-03-08', 'online', 'recusada');
INSERT INTO transacoes VALUES (24, 6, 2, 670.00, DATE '2026-03-10', 'presencial', 'aprovada');
COMMIT;
```

---

## 3. Anatomia de uma consulta

```sql
-- SELECT e FROM
SELECT nome, cidade
FROM clientes;

-- WHERE
SELECT nome, cidade
FROM clientes
WHERE cidade = 'Curitiba';

-- ORDER BY e FETCH FIRST (o equivalente Oracle do LIMIT)
SELECT id_transacao, valor
FROM transacoes
ORDER BY valor DESC
FETCH FIRST 10 ROWS ONLY;
```

---

## 4. Filtrando e refinando

```sql
-- Comparação e faixa, duas formas de escrever a mesma coisa
SELECT id_transacao, valor
FROM transacoes
WHERE valor > 500 AND valor <= 2000;

SELECT id_transacao, valor
FROM transacoes
WHERE valor BETWEEN 500 AND 2000;

-- OR e IN, também duas formas da mesma pergunta
SELECT nome, categoria
FROM lojistas
WHERE categoria = 'Eletronicos' OR categoria = 'Joalheria';

SELECT nome, categoria
FROM lojistas
WHERE categoria IN ('Eletronicos', 'Joalheria');

-- LIKE, buscando por padrão de texto
SELECT nome
FROM clientes
WHERE nome LIKE 'A%';

-- NULL, os três clientes sem telefone cadastrado
SELECT nome
FROM clientes
WHERE telefone IS NULL;

-- E o oposto, quem tem telefone
SELECT nome
FROM clientes
WHERE telefone IS NOT NULL;
```

---

## 5. Agregações

```sql
-- Funções agregadas gerais
SELECT COUNT(*) AS total_transacoes,
       SUM(valor) AS valor_total,
       AVG(valor) AS valor_medio
FROM transacoes;
-- Resultado esperado: 24 transações, total 35.583,50, média 1.482,65

-- GROUP BY, uma linha por lojista
SELECT id_lojista, COUNT(*) AS total,
       SUM(valor) AS valor_total
FROM transacoes
GROUP BY id_lojista
ORDER BY valor_total DESC;
-- O lojista 5 não aparece aqui: sem transação, não tem grupo. Guarde esse detalhe
-- para o bloco de JOIN, ele volta a aparecer lá.

-- HAVING, filtrando por valor total
SELECT id_lojista, SUM(valor) AS valor_total
FROM transacoes
GROUP BY id_lojista
HAVING SUM(valor) > 5000
ORDER BY valor_total DESC;
-- Só os lojistas 1 e 2 passam no filtro

-- HAVING, filtrando por quantidade de transações
SELECT id_lojista, COUNT(*) AS total
FROM transacoes
GROUP BY id_lojista
HAVING COUNT(*) > 5
ORDER BY total DESC;
-- Só os lojistas 1 e 2 passam neste também, mas por um critério diferente do anterior
```

---

## 6. Juntando tabelas

```sql
-- JOIN simples: nome do cliente ao lado da transação
SELECT t.id_transacao, c.nome, t.valor
FROM transacoes t
JOIN clientes c
  ON t.id_cliente = c.id_cliente
ORDER BY t.valor DESC
FETCH FIRST 10 ROWS ONLY;

-- LEFT JOIN: quais clientes nunca compraram
SELECT c.nome
FROM clientes c
LEFT JOIN transacoes t
  ON c.id_cliente = t.id_cliente
WHERE t.id_transacao IS NULL;
-- Resposta: só Hugo Castro

-- LEFT JOIN: quais lojistas nunca receberam nenhuma transação
-- (a mesma pergunta da enquete do bloco de JOIN, agora rodando de verdade)
SELECT l.nome
FROM lojistas l
LEFT JOIN transacoes t
  ON l.id_lojista = t.id_lojista
WHERE t.id_transacao IS NULL;
-- Resposta: só Livraria Pagina Certa
```

### 6.1 Revelação da enquete: as três opções rodando de verdade

A pergunta do slide 29 é: "Você quer saber quais lojistas nunca receberam nenhuma
transação. Qual caminho resolve isso?" Rode as três opções na sequência, para a turma
ver por que só uma funciona.

**Opção A: INNER JOIN partindo de transacoes**

```sql
SELECT DISTINCT l.nome
FROM transacoes t
JOIN lojistas l
  ON t.id_lojista = l.id_lojista
ORDER BY l.nome;
```

Resultado: 4 lojistas, sem a Livraria Pagina Certa. E aqui está o problema desta opção:
ela não erra o resultado, ela simplesmente nunca mostra a resposta. Quem não aparece
numa lista de 4 fica invisível, ninguém percebe que falta um lojista sem comparar à mão
com a lista completa.

**Opção B: LEFT JOIN partindo de lojistas, procurando transacoes**

```sql
SELECT l.nome
FROM lojistas l
LEFT JOIN transacoes t
  ON l.id_lojista = t.id_lojista
WHERE t.id_transacao IS NULL;
```

Resultado: Livraria Pagina Certa, sozinha. Esta é a resposta certa da enquete: o LEFT
JOIN mantém todo lojista na lista, mesmo sem transação, e o filtro por `IS NULL` isola
exatamente quem ficou sem correspondência.

**Opção C: WHERE sozinho, sem nenhum JOIN**

Com as ferramentas de hoje, não dá. WHERE filtra linhas de UMA tabela, ele não tem como
cruzar com outra sem algum tipo de JOIN. Esta opção está errada na enquete.

Se alguém da turma insistir que existe um jeito, tem razão, mas usa uma ferramenta que a
aula ainda não deu, a subconsulta:

```sql
SELECT nome
FROM lojistas
WHERE id_lojista NOT IN (SELECT id_lojista FROM transacoes);
```

Isso funciona e chega no mesmo resultado, sem a palavra JOIN aparecer na consulta. Vale
como gancho para semanas futuras: existe mais de um caminho até a mesma resposta, e a
aula de hoje ensinou só um deles.

```sql
-- JOIN com WHERE: quais clientes têm transação contestada
SELECT DISTINCT c.nome, t.valor, t.data_hora
FROM transacoes t
JOIN clientes c
  ON t.id_cliente = c.id_cliente
WHERE t.status = 'contestada';
```

---

## 7. Extra, para quem quiser ir além

Estes não fazem parte do roteiro da Aula 5, mas usam só o que já foi ensinado, mais uma
combinação nova. Bons para responder pergunta de quem quer ver mais.

```sql
-- Quantos clientes DIFERENTES compraram em cada lojista, não quantas transações
SELECT id_lojista, COUNT(DISTINCT id_cliente) AS clientes_distintos
FROM transacoes
GROUP BY id_lojista
ORDER BY clientes_distintos DESC;

-- Juntando as três tabelas de uma vez: cliente, lojista e valor, lado a lado
SELECT c.nome AS cliente, l.nome AS lojista, t.valor, t.status
FROM transacoes t
JOIN clientes c ON t.id_cliente = c.id_cliente
JOIN lojistas l ON t.id_lojista = l.id_lojista
WHERE t.status = 'contestada'
ORDER BY t.valor DESC;

-- Ordenando por mais de uma coluna: cidade do lojista, depois valor
SELECT l.cidade, l.nome, t.valor
FROM transacoes t
JOIN lojistas l ON t.id_lojista = l.id_lojista
ORDER BY l.cidade, t.valor DESC;
```

---

## 8. Referência rápida de sintaxe Oracle

| No slide da aula (SQL genérico) | No FreeSQL (Oracle) |
|---|---|
| `LIMIT 10` | `FETCH FIRST 10 ROWS ONLY`, depois do `ORDER BY` |
| Texto entre aspas simples | Igual, sem mudança |
| `IS NULL` / `IS NOT NULL` | Igual, sem mudança |
| Data como texto | `DATE 'AAAA-MM-DD'`, sem aspas extras |
