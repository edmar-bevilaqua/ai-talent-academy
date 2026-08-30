# Roteiro do apresentador: Aula 7 (Semana 4, segunda-feira)

> Gerado automaticamente a partir das notas do deck.
> Não edite este arquivo à mão: edite `scripts/gerar_slides_aula07.py` e rode
> `python scripts/gerar_slides_aula07.py && python scripts/exportar_roteiro_aula07.py`.

**Como usar:** imprima ou deixe aberto num segundo monitor. O texto entre aspas é
fala sugerida. Adapte para a sua voz, não decore: o que importa é a sequência de ideias.

---

## Slide 1 · PROGRAMA DE TRAINEES EM DADOS E INTELIGÊNCIA ARTIFICIAL

```
⏱ 19h00 às 19h10 (slide de espera)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Slide projetado desde 18h55. Fale a cada 2 ou 3 minutos enquanto a sala enche.

"Boa noite! Semana 4, e hoje é a origem das ferramentas que a maioria de vocês já usa
sem saber de onde veio. Enquanto todo mundo entra, escreve no chat: você já ouviu falar
em pandas ou NumPy antes de hoje?"

Não comece antes de 19h08.

──────────────────────────────────────────────────────────────
LEMBRETES
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- Moderador com o link do Discord pronto para colar.
- Sem código ao vivo hoje. Os exemplos aparecem no slide, a prática é na quinta.
```

## Slide 2 · ENQUANTO TODO MUNDO ENTRA

```
⏱ 19h00 às 19h10  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Leia os itens uma vez, por volta de 19h05. As respostas do chat servem de termômetro:
se quase ninguém conhece os nomes, vale desacelerar o bloco 2. Se boa parte já ouviu
falar, dá para andar mais rápido nos exemplos e sobrar tempo para perguntas.
```

## Slide 3 · De onde vêm as ferramentas que você já usa

```
⏱ 19h10 às 19h25 (15 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco curto de contextualização. Situar a turma no programa e no porquê de uma aula
inteira de história antes de qualquer código. Ritmo rápido, 3 slides.
```

## Slide 4 · ONDE ESTAMOS

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Onde vocês estão. Semana 3 foi SQL: consultar e extrair dado direto do banco. Hoje é
Python: pegar esse dado e manipular, cruzar, visualizar, contar uma história com ele.

É a mesma pergunta de sempre, só que com outra ferramenta na mão."
```

## Slide 5 · POR QUE PYTHON

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Antes de qualquer exemplo, uma pergunta: por que Python? Ele nem foi criado para
análise de dados. Nasceu como linguagem de propósito geral, em 1989, para outra coisa
inteiramente.

A comunidade científica adotou ele nos anos 2000, e construiu bibliotecas em cima da
linguagem, sem precisar mudar a linguagem em si. É por isso que hoje SQL busca o dado, e
Python manipula, cruza e visualiza. Um não substitui o outro.

E reparem numa coisa que vai aparecer o tempo todo hoje: nenhuma das quatro ferramentas
que a gente vai ver veio de dentro de uma universidade de ciência da computação ou de
uma grande empresa de tecnologia. Vieram de gente com um problema real no próprio
trabalho, que resolveu compartilhar a solução."
```

## Slide 6 · O PLANO DE HOJE

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Quatro blocos, com intervalo no meio.

Primeiro, a história do Python: de onde vem a linguagem, e por que o nome não tem nada
a ver com cobra, apesar do símbolo.

Segundo, NumPy: a base numérica por trás de tudo o que vem depois, inclusive do pandas.

Terceiro, depois do intervalo, pandas: a ferramenta que vocês vão mais usar no dia a
dia. E aqui vai um aviso de agenda: esse bloco cresceu bastante, porque pandas é o
verdadeiro foco desta noite. Isso significa que hoje vamos até por volta de 23h05, uns
60 minutos além do normal. Avisando já de cara para ninguém se programar errado.

E quarto, Matplotlib e Seaborn: transformar tabela em gráfico.

Sempre que der, os exemplos usam o mesmo caso de fraude em cartão que vocês já
conhecem das Aulas 2, 5 e 6. Vocês não vão gastar energia entendendo um cenário novo."
```

## Slide 7 · A história do Python

```
⏱ 19h25 às 20h00 (35 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco de contexto histórico. Objetivo: a turma sair sabendo de onde vem a linguagem, e
por que ela virou o padrão da área de dados sem ter sido desenhada para isso.

ESTRUTURA:
  Linha do tempo              8 min
  Por que o nome              6 min
  O Zen do Python             6 min
  Por que dominou dados       8 min
  Interação                   4 min
```

## Slide 8 · A HISTÓRIA DO PYTHON

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"1989. Guido van Rossum, um programador holandês, começa Python como projeto de fim de
ano, durante o feriado de Natal, trabalhando no CWI, um instituto de pesquisa na
Holanda. Não era encomenda de empresa nenhuma, era hobby de fim de ano.

1991, sai a primeira versão pública. Ano 2000, Python 2. E em 2008, um ano que vai
aparecer de novo daqui a pouco, sai o Python 3, e no mesmo ano nascem o pandas e a
versão madura do NumPy. Não é coincidência: 2008 é o ano em que Python vira, de fato,
uma linguagem de dados.

2018, Guido van Rossum deixa o papel que ele mesmo tinha, de dirigente vitalício da
linguagem, o apelido era literalmente esse.

E hoje, quase quatro décadas depois daquele Natal, Python é uma das linguagens mais
usadas do mundo, puxada em boa parte pela área de dados e inteligência artificial."
```

## Slide 9 · A HISTÓRIA DO PYTHON

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Pergunta clássica: por que Python? Todo mundo assume que é por causa da cobra. Não é.

O nome vem de um programa de comédia britânico, Monty Python's Flying Circus, que era o
programa de televisão favorito do Guido van Rossum na época. A cobra no símbolo veio
depois, por associação visual com o nome, não foi a inspiração original.

E essa origem não é só curiosidade: a filosofia da linguagem carrega bom humor e
simplicidade desde o início, e isso aparece até hoje na documentação oficial e nas
mensagens de erro."
```

## Slide 10 · A HISTÓRIA DO PYTHON

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Existe um documento não oficial, mas que todo mundo trata como oficial, chamado o Zen
do Python. Dezenove frases curtas sobre como escrever código nessa linguagem. Separei
quatro.

Bonito é melhor que feio: código também se lê, não só executa. Explícito é melhor que
implícito: prefira ficar claro a ser esperto. Simples é melhor que complexo, e complexo
ainda é melhor que complicado. E a que mais importa para quem está começando:
legibilidade conta, porque código é escrito uma vez e lido muitas.

Quem quiser ler as dezenove, é só abrir o Python e digitar import this. O texto inteiro
aparece na tela, é uma piada interna da comunidade que virou parte da linguagem."
```

## Slide 11 · A HISTÓRIA DO PYTHON

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Última peça antes da interação: por que Python, especificamente, dominou a área de
dados, e não outra linguagem qualquer.

Primeiro, a sintaxe é próxima da leitura comum, o que baixa a barreira para quem não vem
de programação, e boa parte de quem trabalha com dados não vem.

Segundo, a comunidade científica adotou cedo. Físicos, estatísticos, gente que só
queria resolver o próprio problema preferiu Python a linguagens mais fechadas.

Terceiro, o ecossistema cresceu em cima da linguagem, não trancado dentro dela. Qualquer
pessoa podia publicar uma biblioteca nova, sem pedir licença para ninguém.

E a prova disso são as quatro ferramentas de hoje. Nenhuma delas foi criada pela equipe
oficial do Python. Vamos conhecer a primeira agora."
```

## Slide 12 · INTERAÇÃO

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Testando o que a gente acabou de ver, e adiantando o próximo bloco. Qual dessas
ferramentas tem um nome que descreve literalmente o que ela faz?"

[aguarde 30 segundos]

Resposta: C. NumPy vem de "Numerical Python", nome direto ao ponto. Python vem de um
programa de comédia, sem relação com programação. pandas vem de um termo de
econometria, "panel data". A gente vai ver os dois de perto no resto da aula.
```

## Slide 13 · NumPy

```
⏱ 20h00 às 20h25 (25 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Primeira biblioteca de verdade da noite. Objetivo: entender que NumPy existe para fazer
conta em massa rápido, e que tudo o que vem depois herda essa base.

ESTRUTURA:
  A origem do NumPy       6 min
  Criando um array          8 min
  Operação vetorizada       8 min
  Transição                 3 min
```

## Slide 14 · NUMPY

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Nos anos 1990, existiam duas bibliotecas numéricas concorrentes em Python, a Numeric e
a Numarray, cada uma melhor em uma coisa e pior em outra. Isso dividia esforço e
confundia quem estava escolhendo qual usar.

Em 2005, Travis Oliphant uniu as duas, e o resultado se chamou NumPy.

A peça central é o array: uma estrutura que guarda números do mesmo tipo, em bloco, na
memória, de um jeito bem mais compacto que uma lista comum de Python.

E aqui vai a frase mais importante do bloco: todo o resto do ecossistema de dados roda
em cima do array do NumPy, incluindo o pandas, que a gente vê depois do intervalo."
```

## Slide 15 · NUMPY

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Primeiro exemplo de código da noite. np.array pega uma lista comum, com três valores de
transação, e transforma num array. Por fora parece uma lista, por dentro é uma estrutura
bem mais compacta.

E já aparece a vantagem: .mean() calcula a média direto, sem escrever um laço somando
item por item e dividindo pelo total. Uma lista comum de Python não tem esse tipo de
operação pronta. É exatamente para isso que o array existe."
```

## Slide 16 · NUMPY

```
⏱ 8 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Segundo exemplo: multiplicar o array inteiro por 1,1, simulando um reajuste de 10% em
todas as transações de uma vez.

Repara que não tem laço nenhum. A operação se aplica em cada posição do array ao mesmo
tempo. Isso se chama vetorização, e é a razão do NumPy ser tão mais rápido que Python
puro quando a conta é em massa, com milhares ou milhões de números.

E fica a ponte para o próximo bloco: o pandas herda exatamente essa ideia. Cada coluna
de uma tabela pandas é, por dentro, um array do NumPy. Vocês vão sentir essa mesma
rapidez lá."
```

## Slide 17 · pandas

```
⏱ 20h40 às 22h20 (100 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Bloco principal da noite, logo após o intervalo, e o motivo de a aula ter esticado.
pandas é a ferramenta que a turma mais vai usar no dia a dia, e a que mais amarra com
o SQL das Aulas 5 e 6. Vale um aviso de agenda no início: este bloco é bem mais longo
que os outros, sozinho quase do tamanho do resto da aula somado.

ESTRUTURA (parte 1, os fundamentos):
  A origem do pandas          6 min
  DataFrame e Series           5 min
  O índice                      5 min
  Lendo um arquivo                5 min
  Tipos de dado                    6 min
  Um primeiro raio-x                6 min
  Contando valores únicos            5 min
  Filtrando linhas                     5 min
  loc e iloc                            7 min
  Interação                              4 min

ESTRUTURA (parte 2, o dia a dia de quem analisa):
  Valores ausentes             6 min
  Criando uma coluna nova       5 min
  Agrupando e somando            5 min
  Mais de uma agregação            5 min
  Tabela dinâmica: conceito          4 min
  Tabela dinâmica: exemplo             6 min
  Juntando tabelas                       5 min
  Glossário rápido                         5 min
  Interação final                            4 min
```

## Slide 18 · PANDAS

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"pandas. A ferramenta que vocês vão mais usar a partir de hoje, e por isso este bloco
é bem mais longo que os outros.

Wes McKinney criou o pandas em 2008, trabalhando na AQR Capital Management, um fundo de
investimento quantitativo. Ele precisava analisar dado financeiro no dia a dia, e
Python, na época, não tinha nada parecido com o que a linguagem R já oferecia para isso.

O nome vem de "panel data", um termo de econometria para dado que combina tempo e
categoria na mesma tabela, exatamente o tipo de dado que ele analisava no fundo.

Em 2009 o projeto virou open source, e hoje é a ferramenta mais usada para manipular
tabela em Python, dentro e fora do mercado financeiro."
```

## Slide 19 · PANDAS

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Duas estruturas resolvem quase tudo em pandas. Series é uma coluna só, uma sequência de
valores, cada um com um rótulo. DataFrame é a tabela inteira, várias Series lado a lado,
com linhas e colunas nomeadas.

E se você já usou planilha, já entendeu o essencial: DataFrame é a versão programável de
uma aba de Excel ou Google Sheets. A diferença é que aqui cada passo fica escrito em
código, então dá para repetir, revisar e automatizar."
```

## Slide 20 · PANDAS

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Antes do primeiro exemplo de código, uma peça que ninguém vê de cara: o índice. Toda
tabela pandas tem um índice, além das colunas de verdade. Por padrão, é só um número
sequencial, 0, 1, 2, e por aí vai.

O índice não é uma coluna comum, ele identifica cada linha, e várias operações que
vocês vão ver hoje usam ele por trás dos panos, mesmo sem vocês pedirem diretamente.

Dá para trocar esse índice padrão por uma coluna que faça mais sentido, como
id_transacao, usando set_index. E reset_index desfaz essa troca, volta para o número
sequencial. Guardem esse nome, ele vai voltar no bloco de loc e iloc."
```

## Slide 21 · PANDAS

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Primeiro exemplo de pandas. read_csv lê o arquivo inteiro e já monta um DataFrame, numa
linha de código. head() mostra só as cinco primeiras linhas, bom para conferir se
carregou certo sem imprimir a tabela inteira na tela.

E olha a continuidade: esse é o mesmo transacoes.csv que vocês carregaram no FreeSQL na
Aula 6. O caminho do arquivo muda, o dado é exatamente o mesmo."
```

## Slide 22 · PANDAS

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Cada coluna de um DataFrame tem um tipo por trás, o dtype. int64 e float64 para número,
object para texto, datetime64 para data.

E aqui mora um erro clássico de quem está começando: número que chega como texto. Isso
acontece quando o arquivo original tem alguma célula fora do padrão, uma vírgula, um
espaço, um texto onde devia ter número, e a coluna inteira vira object. Nesse estado,
soma e média simplesmente não funcionam, mesmo a coluna parecendo cheia de número.

astype converte o tipo à força, quando vocês já sabem que está tudo certo por trás. E
data quase sempre precisa de conversão manual: pd.to_datetime transforma um texto em
data de verdade, com todas as operações de data e hora liberadas depois disso."
```

## Slide 23 · PANDAS

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Com o dtype na cabeça, o primeiro raio-x de qualquer tabela nova. info() mostra o tipo
de cada coluna e quantos valores não vazios existem em cada uma, o primeiro lugar para
conferir se algo veio errado do arquivo.

describe() resume as colunas numéricas de uma vez: contagem, média, desvio padrão,
mínimo, máximo e os quartis. Onde vocês usariam COUNT, AVG, MIN e MAX separados em SQL,
aqui sai tudo junto, numa linha de código.

Os dois juntos respondem a primeira pergunta de qualquer análise: o que eu tenho na
mão, antes de fazer qualquer conta de verdade."
```

## Slide 24 · PANDAS

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Duas funções pequenas que vocês vão usar toda hora. value_counts conta quantas vezes
cada valor aparece numa coluna, aqui quantas transações são presenciais e quantas são
online.

nunique conta quantos valores DIFERENTES existem, aqui quantos lojistas distintos
aparecem na tabela inteira, sem repetir.

Os dois são o primeiro passo para entender uma coluna de categoria, antes de decidir
como filtrar ou agrupar por ela."
```

## Slide 25 · PANDAS

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Filtro. Dentro dos colchetes vai uma condição, e o pandas devolve só as linhas que
passam nela. Aqui, só transações acima de 1000 reais.

É a mesma ideia do WHERE que vocês praticaram na Aula 5. Muda a sintaxe, não muda o
raciocínio: definir uma condição, e deixar a ferramenta filtrar.

len() conta quantas linhas sobraram depois do filtro, o equivalente ao COUNT(*) que
vocês já usaram em SQL."
```

## Slide 26 · PANDAS

```
⏱ 7 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Este é o slide para fotografar do bloco. loc seleciona pelo rótulo: o nome do índice e
o nome da coluna. iloc seleciona pela posição: a posição numérica da linha e da coluna,
sempre começando em zero.

Quando o índice ainda é o número padrão, os dois parecem fazer a mesma coisa, e é
exatamente aí que mora a confusão. A diferença aparece de verdade quando o índice vira
outra coisa, como id_transacao, do jeito que vimos no slide do índice. Nesse momento,
loc[1050] busca a linha cujo RÓTULO é 1050, e iloc[1050] busca a linha na POSIÇÃO 1050,
que pode ser uma transação completamente diferente.

Guardem a regra, ela evita o erro mais comum de quem está começando: loc é nome, iloc é
posição."
```

## Slide 27 · INTERAÇÃO

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Testando loc e iloc. A tabela tem o índice trocado para id_transacao. Você quer a linha
cujo id_transacao é 500. Qual comando resolve isso?"

[aguarde 30 segundos]

Resposta: A. loc busca pelo rótulo, e o rótulo aqui é o próprio id_transacao. iloc
buscaria a linha na posição 500 da tabela, que só por acaso seria a transação 500. C
está errado: os dois só coincidem quando o índice é o número sequencial padrão.
```

## Slide 28 · PANDAS

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Começando a segunda metade do bloco. No pandas, valor ausente se chama NaN, o
equivalente exato ao NULL que vocês já usaram em SQL, com o mesmo cuidado: NaN também
não se compara com igual.

isna() marca onde está vazio, célula por célula, e sum() em cima disso conta quantos
valores ausentes existem em cada coluna. É o primeiro raio-x de qualidade de dado antes
de qualquer análise séria.

fillna substitui o vazio por um valor combinado, aqui um texto padrão no lugar do
telefone que falta. E dropna faz o oposto, descarta a linha inteira que tem valor
ausente. Qual dos dois usar depende do que a análise está pedindo: às vezes preencher é
seguro, às vezes é melhor jogar fora a linha incompleta."
```

## Slide 29 · PANDAS

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Criar uma coluna nova é só atribuir a um nome que ainda não existe na tabela. Sem
comando especial, sem declarar nada antes.

E a conta roda em todas as linhas de uma vez, a mesma vetorização que vocês viram no
bloco do NumPy. Aqui, aplicando uma taxa de 3% em cima do valor de cada transação.

É assim que se calcula qualquer métrica derivada: taxa, margem, faixa de valor, o que a
análise pedir. Vocês vão fazer isso o tempo todo a partir de agora."
```

## Slide 30 · PANDAS

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"groupby separa as linhas em grupos, um grupo para cada id_lojista, exatamente como o
GROUP BY da Aula 5. sum() soma o valor dentro de cada grupo, a mesma agregação, só
escrita diferente.

E sort_values ordena o resultado, a versão pandas do ORDER BY. Reparem que em três
linhas de código a gente respondeu a mesma pergunta que levava um GROUP BY inteiro em
SQL: quanto cada lojista faturou, do maior para o menor."
```

## Slide 31 · PANDAS

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O groupby do slide anterior calculou uma agregação só. Na prática, quase sempre vocês
vão querer mais de uma ao mesmo tempo, e é para isso que existe o agg.

agg aceita uma lista de funções de uma vez, aqui contagem, soma e média, numa linha só.
Sem ele, seria preciso repetir o groupby inteiro uma vez para cada conta, um jeito bem
mais longo de chegar no mesmo lugar.

O resultado já sai como uma tabela, uma coluna por função pedida, pronta para virar
relatório ou gráfico, que é exatamente o assunto do próximo bloco."
```

## Slide 32 · PANDAS

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Última ferramenta nova antes do merge: pivot_table, a versão programável da tabela
dinâmica do Excel ou Google Sheets. Quem já montou uma reconhece a lógica na hora.

Ela cruza duas colunas de categoria, com uma agregação no meio. Por exemplo, um lojista
por linha, um canal por coluna, e o valor somado em cada cruzamento.

É a ferramenta certa quando o groupby de uma coluna só não é suficiente, quando a
pergunta de negócio envolve duas dimensões ao mesmo tempo, não uma."
```

## Slide 33 · PANDAS

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"index define as linhas da tabela final, aqui um lojista por linha. columns define as
colunas, aqui uma coluna para presencial, outra para online.

values e aggfunc dizem o que calcular em cada cruzamento, aqui a soma do valor. O
resultado é uma tabela nova: cada lojista, quanto vendeu presencial, quanto vendeu
online, lado a lado. Essa pergunta não sairia de um groupby de uma coluna só."
```

## Slide 34 · PANDAS

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"merge, a versão pandas do JOIN. Junta duas tabelas por uma coluna em comum, aqui
id_cartao, a mesma chave que vocês usaram na Aula 6.

Por padrão, merge se comporta como INNER JOIN: só entra quem existe nas duas tabelas.
Para o equivalente de LEFT JOIN, existe o parâmetro how, e how igual a "left" muda esse
comportamento.

Se você entendeu JOIN na Aula 5 e 6, você já entendeu merge. É a mesma lógica, com
outro nome."
```

## Slide 35 · PANDAS

```
⏱ 5 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Antes de fechar o bloco, um glossário rápido. Estes oito termos aparecem toda hora em
documentação e em vaga de emprego, e vale reconhecer todos.

DataFrame, a tabela inteira. Series, uma coluna só. Índice, o rótulo de cada linha.
dtype, o tipo por trás de uma coluna. NaN, valor ausente, o NULL do pandas. Vetorização,
aplicar uma conta em todas as linhas de uma vez. axis, a direção de uma operação, 0 por
linha, 1 por coluna. E inplace, quando uma operação altera a própria tabela, em vez de
devolver uma cópia nova.

Não precisa decorar agora. Precisa reconhecer quando aparecer de novo, e vai aparecer."
```

## Slide 36 · INTERAÇÃO

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Testando o bloco inteiro numa pergunta só. Você quer o valor médio de transação por
canal. Qual sequência resolve isso?"

[aguarde 30 segundos]

Resposta: A. groupby separa por canal, e mean() calcula a média do valor dentro de cada
grupo. B tenta calcular média de uma coluna de texto, não funciona. C tenta um merge sem
sentido, canal não é uma tabela para juntar.
```

## Slide 37 · Matplotlib e Seaborn

```
⏱ 22h20 às 22h50 (30 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

Último bloco de conteúdo. Objetivo: sair sabendo que as duas ferramentas se completam,
uma desenha, a outra deixa bonito por padrão.

ESTRUTURA:
  A origem do Matplotlib     6 min
  Um gráfico de barras         7 min
  A origem do Seaborn           6 min
  Um histograma                  7 min
  Transição                       4 min
```

## Slide 38 · MATPLOTLIB

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Matplotlib. John Hunter criou a partir de 2002. Ele era neurocientista, analisava sinal
de eletroencefalograma, e usava o MATLAB para gerar os gráficos da pesquisa.

O objetivo inicial era simples: ter no Python o mesmo tipo de gráfico que ele já fazia
no MATLAB, sem precisar trocar de ferramenta no meio do trabalho.

Hoje o Matplotlib é a base de quase todo gráfico feito em Python. Inclusive o Seaborn,
que vem a seguir, usa o Matplotlib por baixo, em vez de ser uma ferramenta separada."
```

## Slide 39 · MATPLOTLIB

```
⏱ 7 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"bar() desenha uma barra para cada posição, aqui uma barra por lojista. resumo.index
vira o eixo horizontal, resumo.values a altura de cada barra. É o mesmo resumo que saiu
do groupby no bloco anterior, agora virando desenho.

E não esqueçam do show(): é o que efetivamente exibe o gráfico na tela. Sem ele, o
gráfico fica montado por dentro do programa, mas invisível para quem está olhando."
```

## Slide 40 · SEABORN

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Seaborn. Michael Waskom criou a partir de 2012, com um objetivo diferente do
Matplotlib: deixar gráfico estatístico bonito por padrão, sem precisar configurar cor,
proporção e estilo à mão toda vez.

Uma curiosidade: o nome é uma referência a um personagem de série de TV, Sam Seaborn,
de The West Wing.

E o ponto técnico mais importante: Seaborn não substitui o Matplotlib, ele se apoia
nele. Por baixo, quem desenha continua sendo o Matplotlib. Seaborn só decide as cores,
proporções e ajustes por vocês."
```

## Slide 41 · SEABORN

```
⏱ 7 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Último exemplo de código da noite. histplot desenha um histograma: quantas transações
caem em cada faixa de valor.

Em uma linha só, já sai com eixo, cor e proporção ajustados. No Matplotlib puro, chegar
nesse mesmo resultado levaria várias linhas de configuração manual.

E reparem que a função recebeu a coluna de um DataFrame direto, sem conversão nenhuma.
Seaborn entende pandas nativamente. É por isso que NumPy, pandas, Matplotlib e Seaborn
trabalham tão bem juntos: cada um foi construído sabendo que o anterior já existia."
```

## Slide 42 · Encerramento

```
⏱ 22h50 às 23h05 (15 min)  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

DISTRIBUIÇÃO:
  Recapitulação            4 min
  O que vem pela frente    3 min
  Q&A                      6 min  (elástico, absorve atraso)
  Fechamento               2 min
```

## Slide 43 · ENCERRAMENTO

```
⏱ 4 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"Cinco ideias para levar de hoje.

Python nasceu como hobby, não como ferramenta de dados. O ecossistema foi construído em
cima dele depois.

NumPy existe para fazer conta em massa rápido, com array e operação vetorizada, sem
escrever laço.

pandas faz em Python o que vocês já sabem fazer em SQL: filtrar, agrupar e juntar, só
que com outra sintaxe.

Matplotlib desenha, Seaborn deixa bonito por padrão. Um se apoia no outro, não competem.

E a mais importante: nenhuma das quatro ferramentas veio de dentro do time oficial do
Python. Vieram de gente resolvendo o próprio problema, e publicando depois."
```

## Slide 44 · PRÓXIMOS ENCONTROS

```
⏱ 3 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

"O que vem pela frente.

Na quinta desta semana, Python sai do slide e vai para o Colab de vocês, com o mesmo
caso de fraude. Vale revisar estes slides antes.

E na segunda da semana 5, engenharia de dados: como construir os pipelines que entregam
dado limpo, no lugar certo. Ainda conceitual, como toda segunda."
```

## Slide 45 · ANTES DE IR

```
⏱ 6 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

PERGUNTAS PREVISÍVEIS DE HOJE:

- "Preciso saber tudo isso de cor?"
  Não. O que importa hoje é reconhecer o nome e saber para que serve. A sintaxe fica
  automática com prática, a partir da quinta.

- "R não fazia tudo isso antes do pandas existir?"
  Fazia, e foi justamente a referência que faltava em Python até 2008. Hoje as duas
  linguagens têm ferramentas fortes para dados, cada uma com sua comunidade.

- "Isso ajuda no projeto final?"
  Ajuda direto. pandas é o que a maioria dos grupos vai usar para explorar e preparar a
  própria base, junto com o SQL que vocês já praticaram.

- "Perdi a aula de SQL, consigo acompanhar Python?"
  Sim, mas vale revisar o material da Aula 5 antes da quinta. Os exemplos de hoje
  assumem que os termos WHERE, GROUP BY e JOIN já são familiares.
```

## Slide 46 · Obrigado!

```
⏱ 2 min  |  ESSENCIAL  |  Apresenta: Edmar
──────────────────────────────────────────────────────────────
ROTEIRO DE FALA

FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. Da próxima vez que vocês rodarem um .groupby() ou virem um
gráfico do Seaborn, vão saber de onde isso veio, e por que existe.

Revisem os slides antes da quinta, principalmente os exemplos de pandas. Nos vemos lá,
com código de verdade na tela. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Confirmar com quem conduz a Aula 8 que o caso de fraude e os quatro exemplos de hoje
  (read_csv, filtro, groupby, merge) são exatamente o que vai aparecer no Colab da
  prática.
```
