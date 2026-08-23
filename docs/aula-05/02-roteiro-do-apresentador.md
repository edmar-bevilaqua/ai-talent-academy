# Roteiro do apresentador: Aula 5 (Semana 3, segunda-feira)

> Gerado automaticamente a partir das notas do deck.
> Não edite este arquivo à mão: edite `scripts/gerar_slides_aula05.py` e rode
> `python scripts/gerar_slides_aula05.py && python scripts/exportar_roteiro_aula05.py`.

**Como usar:** imprima ou deixe aberto num segundo monitor. O texto entre aspas é
fala sugerida. Adapte para a sua voz, não decore: o que importa é a sequência de ideias.

---

## Slide 1 · PROGRAMA DE TRAINEES EM DADOS E INTELIGÊNCIA ARTIFICIAL

```
⏱ 19h00 às 19h10 (slide de espera)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Slide projetado desde 18h55. Fale a cada 2 ou 3 minutos enquanto a sala enche.

"Boa noite! Terceira semana, e hoje é a primeira aula técnica de verdade do programa:
SQL. Enquanto todo mundo entra, escreve no chat: hoje você já usa filtro ou tabela
dinâmica numa planilha? É a mesma lógica de hoje, só que com outro nome."

Não comece antes de 19h08.

──────────────────────────────────────────────────────────────
LEMBRETES
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- Moderador com o link do Discord pronto para colar.
- Sem código ao vivo hoje. As consultas aparecem como slide, a prática é na quinta.
```

## Slide 2 · ENQUANTO TODO MUNDO ENTRA

```
⏱ 19h00 às 19h10  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Leia os itens uma vez, por volta de 19h05. Insista no quarto item: tem gente que vai
ficar tensa por achar que hoje é dia de escrever código na frente de todo mundo, e não é.
```

## Slide 3 · Por que SQL, e por que agora

```
⏱ 19h10 às 19h25 (15 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco curto de contextualização. Situar a turma no programa e justificar por que SQL
vem antes de Python. Ritmo rápido, 3 slides.
```

## Slide 4 · ONDE ESTAMOS

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Onde vocês estão. Semana 1 foi panorama. Semana 2 foi IA generativa, de propósito antes
de qualquer coisa técnica, porque é a porta de entrada mais acessível da área.

Hoje, semana 3, começa a parte estrutural: SQL primeiro, Python na semana 4, engenharia
de dados na 5, machine learning na 6, agentes na 7. Faz sentido nessa ordem: você precisa
saber consultar e limpar dado antes de modelar qualquer coisa."
```

## Slide 5 · POR QUE SQL

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Quatro razões para dedicar uma noite inteira a SQL.

Primeira: é a habilidade mais pedida em vaga de dados, sem exceção de nível.

Segunda: funciona em praticamente qualquer banco. Aprende uma vez, usa a vida inteira.

Terceira: SQL existe desde os anos 1970 e continua sendo a base. Python se conecta nela,
não substitui ela.

E a quarta, a mais prática: sem SQL, todo pedido de dado vira um pedido para outra
pessoa. Com SQL, você mesmo busca a resposta, sem depender de fila de outro time."
```

## Slide 6 · O PLANO DE HOJE

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Quatro blocos, com intervalo no meio.

Primeiro, a anatomia de uma consulta: as cinco palavras que resolvem a maioria das
perguntas do dia a dia.

Segundo, filtros mais finos: comparação, faixa, texto e o cuidado com valor vazio.

Terceiro, depois do intervalo, agregação: como resumir milhares de linhas numa resposta
só.

E quarto, o mais esperado: juntar tabelas. Porque dado nunca mora numa tabela só.

E um aviso: todo exemplo de hoje usa o mesmo caso que vocês já conhecem, fraude em
cartão, da Aula 2. Vocês não vão gastar energia entendendo um cenário novo, só a
ferramenta."
```

## Slide 7 · Anatomia de uma consulta

```
⏱ 19h25 às 20h00 (35 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco central da primeira metade. Objetivo: sair daqui lendo e escrevendo uma consulta
simples sozinho.

ESTRUTURA:
  O caso de hoje                    4 min
  O que é SQL                       4 min
  SELECT e FROM                     6 min
  WHERE                             6 min
  ORDER BY e LIMIT                  6 min
  A ordem real de execução          6 min
  Interação                         3 min
```

## Slide 8 · O CASO DE HOJE

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Antes de qualquer consulta, as três tabelas que vamos usar a noite inteira.

Transações: cada compra no cartão, com valor, data, canal e status.

Clientes: quem é o dono do cartão.

Lojistas: onde a compra aconteceu.

Repara que o dado não está tudo numa tabela só. A gente vai voltar nisso no bloco de
JOIN, mas já fica o aviso: isso é proposital. A razão aparece mais à frente."
```

## Slide 9 · O QUE É SQL

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"SQL significa Structured Query Language, mas o nome ajuda pouco. O que importa é isto:
SQL é uma linguagem declarativa. Você descreve O QUE quer, não escreve o passo a passo de
como buscar. Quem decide o caminho mais rápido é o banco, por trás, com um otimizador.

E a base de tudo, para o que vocês vão precisar no dia a dia, são cinco palavras: SELECT,
FROM, WHERE, ORDER BY e LIMIT. Vamos ver as cinco agora."
```

## Slide 10 · ANATOMIA DE UMA CONSULTA

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"A consulta mais simples possível. SELECT nome, cidade, FROM clientes.

SELECT escolhe as colunas, só o que você pede aparece. FROM escolhe a tabela, de onde
essas colunas são lidas.

Repara que a ordem das colunas no resultado segue o SELECT, não a ordem que elas estão
guardadas na tabela.

E um atalho comum: SELECT asterisco traz todas as colunas de uma vez. Prático para
explorar uma tabela nova, mas evite deixar isso num relatório final. É mais lento e traz
coluna que ninguém vai usar."

──────────────────────────────────────────────────────────────
LEMBRETES
Deixe este slide um pouco mais de tempo na tela. É o primeiro contato de muita gente com uma consulta de verdade.
```

## Slide 11 · ANATOMIA DE UMA CONSULTA

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Agora um filtro. WHERE cidade igual Curitiba.

WHERE decide quais LINHAS entram no resultado, diferente do SELECT, que decide quais
COLUNAS aparecem. Aqui, só os clientes de Curitiba passam pelo filtro.

Detalhe de sintaxe: texto vai entre aspas simples. Número não precisa.

E um aviso de segurança: sem WHERE, a consulta traz a tabela inteira. Numa tabela com
milhões de linhas, isso pode travar o banco para todo mundo, não só para você."
```

## Slide 12 · ANATOMIA DE UMA CONSULTA

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"ORDER BY valor DESC, LIMIT 10. Duas palavras que resolvem um pedido clássico: quais são
as dez maiores transações.

ORDER BY organiza o resultado. ASC é do menor para o maior, DESC é do maior para o menor.
LIMIT corta o tamanho do que volta.

Juntos, esses dois respondem 'quais são os maiores' ou 'quais são os menores', um dos
pedidos mais comuns em qualquer análise de negócio."
```

## Slide 13 · A ORDEM REAL

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Este é o slide para fotografar. A ordem que você ESCREVE uma consulta não é a ordem que
o banco EXECUTA ela.

Primeiro o banco decide de qual tabela ler, o FROM. Depois filtra linha por linha, o
WHERE. Se existir agrupamento, agrupa, o GROUP BY, e filtra os grupos, o HAVING. Só
então escolhe as colunas do resultado, o SELECT. Organiza o que sobrou, o ORDER BY. E
corta o tamanho por último, o LIMIT.

GROUP BY e HAVING a gente ainda não usou, eles vêm no bloco de agregação, depois do
intervalo. Mas guardem esta ordem agora, porque ela explica um erro clássico de
iniciante que a gente vai ver lá na frente."
```

## Slide 14 · INTERAÇÃO

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Testando o que a gente acabou de ver. Você quer transações entre R$100 e R$300, feitas
em São Paulo ou Curitiba. Qual opção resolve isso de um jeito só?"

[aguarde 30 segundos]

Resposta: B. BETWEEN resolve a faixa de valor numa linha só, e IN resolve a lista de
cidades sem precisar escrever OR duas vezes. A é incompleto, falta o limite superior do
valor. C está errado nos dois pedidos.
```

## Slide 15 · Filtrando e refinando

```
⏱ 20h00 às 20h25 (25 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco de aprofundamento do WHERE. Menos conceito novo, mais repertório de sintaxe.

ESTRUTURA:
  Comparação e faixa      7 min
  OR e IN                 7 min
  Texto e valor vazio      8 min
  Transição                3 min
```

## Slide 16 · FILTRANDO E REFINANDO

```
⏱ 7 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Além do igual, os operadores de comparação: maior que, menor que, maior ou igual, menor
ou igual, diferente.

AND exige que as duas condições sejam verdadeiras ao mesmo tempo. Aqui, valor acima de
500 E até 2000.

E existe um atalho para faixa: BETWEEN escreve a mesma coisa numa linha só. Os dois
jeitos funcionam, BETWEEN só é mais direto de ler."
```

## Slide 17 · FILTRANDO E REFINANDO

```
⏱ 7 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"OR é diferente de AND: exige só que UMA das condições seja verdadeira, não as duas.
Aqui, categoria eletrônicos OU joalheria.

Quando o OR se repete várias vezes na mesma coluna, existe um atalho: IN. Faz a mesma
coisa, com menos linha de código.

E um aviso importante: quando você mistura AND e OR na mesma consulta, sem parênteses o
banco pode agrupar as condições de um jeito que não é o que você pensou. Na dúvida, use
parênteses para deixar explícito."
```

## Slide 18 · FILTRANDO E REFINANDO

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"LIKE busca por padrão de texto. 'Ana%' encontra qualquer nome que começa com Ana. O
símbolo % substitui qualquer sequência de caracteres.

E agora o ponto que mais confunde quem está começando: valor vazio no banco tem nome
próprio, NULL, um estado que significa 'sem valor definido', diferente de zero e
diferente de texto vazio.

Por causa disso, NULL não se compara com igual. Um erro comum de iniciante é escrever
WHERE cidade = NULL, e isso simplesmente não retorna nada, mesmo quando existe linha com
cidade vazia. O jeito certo é IS NULL, ou IS NOT NULL para o contrário."

──────────────────────────────────────────────────────────────
LEMBRETES
Este é o erro mais comum de quem está aprendendo. Vale repetir em voz alta: NULL nunca usa igual.
```

## Slide 19 · Agregações

```
⏱ 20h40 às 21h15 (35 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco da segunda metade, logo após o intervalo. É onde SQL passa de listar linha para
responder pergunta de negócio de verdade.

ESTRUTURA:
  Por que agregar        5 min
  Funções agregadas       8 min
  GROUP BY               10 min
  HAVING                 10 min
  Transição               2 min
```

## Slide 20 · AGREGAÇÕES

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Até agora, toda consulta devolveu uma lista de linhas. Cada linha, uma transação.

Mas boa parte das perguntas de negócio quer um número, não uma lista fila por fila.
'Quanto São Paulo faturou no total' resume as transações numa resposta só.

E cinco funções resolvem a maior parte desses casos: COUNT, SUM, AVG, MIN e MAX."
```

## Slide 21 · AGREGAÇÕES

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"COUNT conta linhas. SUM soma um valor numérico. AVG calcula a média. E MIN e MAX trazem
o menor e o maior valor de uma coluna, que não estão nesta consulta mas funcionam igual.

Repara no AS: ele dá um nome ao resultado de cada função. Sem isso, a coluna sai do
banco com um nome esquisito, tipo o texto inteiro da função. AS deixa o resultado
legível para quem for ler depois."
```

## Slide 22 · AGREGAÇÕES

```
⏱ 10 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"GROUP BY é o que transforma a pergunta de 'no total' para 'por lojista'. Ele separa as
linhas em grupos, um grupo para cada valor de id_lojista.

E aqui está o pulo do gato: a função agregada roda DENTRO de cada grupo. COUNT e SUM não
calculam mais pela tabela inteira, calculam por lojista.

Regra que trava muita gente no início: toda coluna que aparece no SELECT precisa estar
no GROUP BY, ou estar dentro de uma função como COUNT ou SUM. Senão o banco fica sem
saber qual linha específica do grupo deveria mostrar naquela coluna, e dá erro."
```

## Slide 23 · AGREGAÇÕES

```
⏱ 10 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Última peça do bloco: HAVING. E aqui a gente volta no slide da ordem real de execução,
lá do primeiro bloco.

WHERE filtra ANTES de agrupar, linha por linha. HAVING filtra DEPOIS de agrupar, grupo
por grupo. São dois momentos diferentes da mesma consulta, e por isso existem os dois.

Aqui, HAVING SUM(valor) maior que 10 mil deixa só os lojistas que somaram mais de dez mil
reais em transações.

E o erro clássico: tentar escrever WHERE SUM(valor) maior que 10 mil. Isso dá erro,
porque na ordem de execução, quando o WHERE roda, a soma ainda nem existe. Ela só existe
depois do GROUP BY. Por isso o SUM precisa estar no HAVING, não no WHERE."
```

## Slide 24 · Juntando tabelas

```
⏱ 21h15 às 21h45 (30 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco mais esperado da noite. É onde as três tabelas do início finalmente se encontram.

ESTRUTURA:
  Por que os dados vivem separados    5 min
  Chave primária e estrangeira        5 min
  JOIN                                8 min
  INNER x LEFT                        8 min
  Interação                           4 min
```

## Slide 25 · JUNTANDO TABELAS

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Lá no começo eu falei que o dado não estava tudo numa tabela só, e prometi voltar
nisso. Chegou a hora.

Guardar tudo numa tabela só parece mais simples à primeira vista. Mas isso repete o
nome e a cidade do cliente em TODA transação dele. Se o cliente tiver mil compras, o
nome dele aparece escrito mil vezes.

Separar em tabelas evita essa repetição. O nome do cliente mora uma vez só, na tabela
clientes. E a ligação entre as tabelas é feita por uma chave, um identificador que
aparece nas duas."
```

## Slide 26 · JUNTANDO TABELAS

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Dois termos que aparecem sempre que se fala de banco relacional.

Chave primária identifica cada linha de forma única, dentro da própria tabela. Em
clientes, é o id_cliente.

Chave estrangeira aponta para a chave primária de outra tabela. Em transações, o
id_cliente que aparece ali não identifica a transação, ele aponta de volta para o
cliente dono dela.

É esse par, chave primária de um lado, chave estrangeira do outro, que o JOIN usa para
juntar as tabelas. Vamos ver isso agora."
```

## Slide 27 · JUNTANDO TABELAS

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"JOIN junta linhas de duas tabelas, usando a chave que elas têm em comum.

ON diz exatamente qual coluna de cada lado combina. Aqui, o id_cliente de transações com
o id_cliente de clientes.

Repara nos apelidos, t e c. Eles encurtam o nome da tabela e evitam ambiguidade quando a
mesma coluna existe nas duas tabelas, como id_cliente.

E o motivo de tudo isso existir: sem JOIN, esse cruzamento teria que ser feito
manualmente, fora do banco, numa planilha, linha por linha. Com milhares de transações,
isso não é viável."
```

## Slide 28 · JUNTANDO TABELAS

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Existe mais de um tipo de JOIN, e a escolha muda o resultado.

INNER JOIN, o que a gente viu no slide anterior, só traz quem existe nas DUAS tabelas.
Cliente sem nenhuma transação simplesmente some do resultado.

LEFT JOIN mantém tudo da tabela da esquerda, mesmo sem correspondência do outro lado.
Aqui, todo cliente aparece, e quem não tem transação vem com valor vazio.

E por que isso importa: a pergunta 'quantos clientes nunca compraram' só é respondível
com LEFT JOIN. Com INNER JOIN, esses clientes já teriam sumido antes de você poder
contar."
```

## Slide 29 · INTERAÇÃO

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Última pergunta antes do fechamento. Você quer saber quais lojistas nunca receberam
nenhuma transação. Qual caminho resolve isso?"

[aguarde 30 segundos]

Resposta: B. LEFT JOIN partindo de lojistas mantém todo lojista no resultado, e quem não
tem transação correspondente aparece com valor vazio, é só filtrar por isso depois. A
elimina justamente quem você quer encontrar. C não tem como cruzar as duas tabelas sem
JOIN.
```

## Slide 30 · Da pergunta à query

```
⏱ 21h45 às 22h05 (20 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Recapitulação            5 min
  O que vem pela frente    4 min
  Q&A                      9 min  (elástico, absorve atraso)
  Fechamento               2 min
```

## Slide 31 · ENCERRAMENTO

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Cinco ideias para levar de hoje.

SQL descreve o que você quer, não o passo a passo de como buscar.

A ordem de execução não é a ordem que você escreve: FROM, WHERE, GROUP BY, HAVING,
SELECT, ORDER BY, LIMIT.

Agregação muda o formato da resposta, de uma lista de linhas para um resumo.

JOIN existe porque os dados vivem separados de propósito, e o tipo de JOIN muda a
resposta.

E a mais importante: toda consulta boa começa numa pergunta de negócio clara, não numa
tabela aberta sem destino."
```

## Slide 32 · PRÓXIMOS ENCONTROS

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O que vem pela frente.

Na quinta desta semana, SQL sai do slide e vai para a tela de vocês, num banco real, com
o mesmo caso de fraude que vocês já conhecem. Vale revisar estes slides antes.

E na segunda da semana 4, análise de dados com Python. Mesma lógica de hoje, filtrar,
agrupar, cruzar, agora com pandas. O que vocês aprenderam hoje não fica para trás, ele
volta."
```

## Slide 33 · ANTES DE IR

```
⏱ 9 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

PERGUNTAS PREVISÍVEIS DE HOJE:

- "Preciso decorar a ordem de execução?"
  Não. Com prática ela fica automática. O que importa hoje é saber que ela existe.

- "SQL funciona igual em todo banco?"
  A base é a mesma em qualquer banco. Pequenos detalhes de sintaxe mudam entre
  PostgreSQL, MySQL e outros, mas SELECT, WHERE, GROUP BY e JOIN funcionam em todos.

- "Isso ajuda no projeto final?"
  Ajuda direto. É exatamente o que cada grupo vai usar para explorar a própria base a
  partir desta semana.

- "Perdi a aula, consigo acompanhar a quinta?"
  Sim. A gravação e o roteiro ficam no Discord antes da quinta.
```

## Slide 34 · Obrigado!

```
⏱ 2 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. SQL parece árido no slide, mas é a ferramenta que mais
volta a aparecer no trabalho de vocês, semana após semana.

Revisem os slides antes da quinta, principalmente a ordem real de execução. Nos vemos
lá, com um banco de verdade na tela. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Confirmar com quem conduz a quinta que o caso de fraude e as três tabelas de hoje são
  exatamente o que vai aparecer no banco real da prática.
```
