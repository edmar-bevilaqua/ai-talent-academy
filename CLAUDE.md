# AI Talent Academy

Repositório do material didático do **AI Talent Academy**, um programa de trainees em Dados
e Inteligência Artificial da White Cube, com 8 semanas de duração.

Este arquivo é o manual de operação do repositório. Leia antes de criar ou alterar qualquer
apresentação.

---

## 1. Contexto do programa

| Item | Valor |
|---|---|
| Nome | AI Talent Academy |
| Cliente / marca | White Cube (A Think Group Company) |
| Parceiros no rodapé da capa | Bevilaqua Data Labs, BPTECH |
| Duração | 8 semanas, 80 horas (40h síncronas + 40h de preparação e avaliação) |
| Público | ~190 pessoas inscritas via LinkedIn, com pouco ou nenhum aprofundamento em IA |
| Formato | 100% online, sempre |
| Segundas, 19h às 22h | Aula principal, conceitual. 3 horas |
| Quintas, 19h às 21h | Laboratório, prática e mentoria. 2 horas |
| Etapa 1 (semanas 1 a 4) | Aberta. Nivelamento. Termina no Mini-Desafio Data & AI |
| Etapa 2 (semanas 5 a 8) | Restrita. Projeto em squad. Termina no Demo Day |

A proposta comercial completa está em
`docs/Proposta Executiva 2 - Programa de Trainees em Dados e Inteligência Artificial.pdf`.
Ela é a fonte de verdade sobre ementa, avaliação e entregáveis de cada semana.

### Pessoas

| Quem | Papel |
|---|---|
| **Edmar Bevilaqua** | Cientista de Dados Sênior. Conduz os blocos conceituais das segundas |
| **Felipe André Bach Alves** | Cientista de Dados Sênior Análogo a Marte, fotógrafo profissional. Conduz os blocos práticos |
| **Ale e Márcio** | Diretoria da White Cube. Abrem a aula 1 com 20 minutos institucionais |

Nunca use placeholders como `[NOME DO COLEGA]` em material novo. Os dois nomes acima são
definitivos.

---

## 2. Princípio central: o deck é gerado por script

**Nunca edite o `.pptx` à mão como fonte de verdade.** Cada aula tem um script Python em
`scripts/` que gera o arquivo inteiro com `python-pptx`. Alterar conteúdo significa alterar
o script e regerar.

Motivo: o deck tem dezenas de slides com roteiro de fala embutido nas notas, e o conteúdo
muda várias vezes antes da aula. Regerar leva segundos e mantém tudo consistente. Editar à
mão faz o roteiro exportado, os documentos de apoio e a numeração de slides divergirem.

### Quando o usuário edita o pptx manualmente

Acontece e é legítimo. O procedimento é:

1. O usuário salva a versão editada com outro nome (por exemplo `...-editada.pptx`).
2. Faça o diff programático do texto slide a slide entre o gerado e o editado.
3. Incorpore as edições **no script**, não no arquivo.
4. Regere e confirme que o diff zerou.

Script de diff que já funcionou (adapte conforme necessário):

```python
from pptx import Presentation
import difflib

def dump(path):
    return ["\n".join(sh.text_frame.text.strip()
                      for sh in s.shapes
                      if sh.has_text_frame and sh.text_frame.text.strip())
            for s in Presentation(path).slides]

a, b = dump("gerado.pptx"), dump("editada.pptx")
sm = difflib.SequenceMatcher(None, [x.split("\n")[0] for x in a],
                                   [x.split("\n")[0] for x in b])
# get_opcodes() revela slides removidos, inseridos e reordenados
```

> ⚠️ O console do Windows usa cp1252 e quebra ao imprimir acentos ou emoji. Escreva o
> resultado em arquivo com `encoding="utf-8"` e leia o arquivo, em vez de dar `print`.

---

## 3. As regras de estilo inegociáveis

Estas regras vieram do usuário e valem para **todo** material novo: slides, notas de
apresentador e documentos markdown. As quatro primeiras (3.1 a 3.4) são checáveis por
código e falham a geração se violadas. A quinta (3.5, vícios de escrita de IA) é editorial:
não dá para assertar por regex com segurança, então depende de revisão consciente antes de
considerar o texto pronto.

### 3.1 Roboto em 100% dos textos, sem exceção

Toda run recebe `r.font.name = "Roboto"`. É a fonte do template oficial da White Cube.
Vale para qualquer texto: título, corpo, legenda de diagrama, rodapé, nota do apresentador.
Não existe texto "pequeno demais para importar" ou "decorativo demais para contar": se é
uma run de texto no `.pptx`, é Roboto.

### 3.2 Tamanho mínimo de 17pt em todo texto de leitura

Piso de legibilidade: **nada abaixo de 17pt**, com duas exceções documentadas e só essas
duas. A régua veio de comparar a versão final que o usuário efetivamente apresentou em aula
(`docs/AI-Talent-Academy-Aula01-editada.pptx` e o PDF irmão) contra o que o gerador produzia
antes: corpo de card a 15,5pt, célula de tabela a 15pt e texto de card do pipeline a 14pt
estavam pequenos demais para uma sala de 190 pessoas assistindo por streaming compartilhado.

As constantes do gerador refletem isso: `S_SUB`, `S_BULLET`, `S_CARD_T`, `S_CARD_B`,
`S_TABLE_H`, `S_TABLE_C`, `S_BIG`, `S_SRC`, `S_TIMELINE`, `S_PIPELINE_B` e
`S_NESTED_LEGEND` são todas ≥ `S_MIN` (17), e há um `assert` logo abaixo das constantes que
quebra a geração se alguma cair abaixo disso.

**As duas exceções documentadas**, ambas confirmadas na própria versão final aprovada pelo
usuário:

1. **`S_FOOT` (13pt), o rodapé.** `whitecube.com.br` e o número do slide são mobília da
   página, não conteúdo de leitura. Na versão final o usuário manteve o rodapé em 13pt em
   todos os 64 slides. Não force para 17.
2. **Os rótulos internos dos três anéis externos do `sl_nested`** (o diagrama de círculos
   concêntricos IA → ML → Deep Learning → GenAI). O espaço físico dentro dos anéis mais
   finos não comporta 17pt sem quebrar o desenho ou estourar o anel seguinte. Na versão
   final do usuário esses rótulos ficam em 13, 14 e 15pt (o anel mais interno, GenAI, já
   nasce maior e fica em 17). Aumente até o ponto em que o desenho aguenta, mas não force
   a igualdade com o piso geral.

Qualquer outro texto abaixo de 17pt que aparecer numa aula nova é bug, não exceção nova.
Se um layout genuinamente precisar de uma terceira exceção, pare e pergunte ao usuário
antes de adicionar. Não decida sozinho que "esse caso também é especial".

### 3.3 Um único tamanho de fonte por caixa de texto

Nunca alterne tamanho dentro do mesmo bloco de texto. Consequência prática de arquitetura:
título e corpo de um card ficam em **caixas de texto separadas**. O mesmo vale para célula
de tabela, legenda de diagrama e qualquer par título/descrição.

Negrito e cor podem variar dentro do bloco. Só o **tamanho** é que não pode.

### 3.4 Zero travessões

Proibidos `—` (em dash, U+2014) e `–` (en dash, U+2013). Substitua preservando a semântica:

| Em vez de | Use |
|---|---|
| `A palavra — explicação` | `A palavra: explicação` |
| `X — e isso importa` | `X, e isso importa` |
| `19h30 – 19h45` | `19h30 às 19h45` |
| `Slide 12 — Interação` | `Slide 12: Interação` ou `Slide 12 · Interação` |
| `frase — outra frase` | `frase. Outra frase` |

> Os travessões dentro das crases acima são as **únicas** ocorrências legítimas em todo o
> repositório: uma regra precisa mostrar o que proíbe. Se uma checagem automática apontar
> travessão neste arquivo, confira se é apenas esta tabela antes de mexer.

Permitidos e usados livremente: hífen em palavra composta (`segunda-feira`), interponto
`·`, seta `→`, multiplicação `×`, e o traço de caixa `─` (U+2500) usado como separador
dentro das notas do apresentador.

### 3.5 Vícios de escrita que soam a IA

O usuário mandou o artigo "9 vícios de escrita que dão aquele cheirinho de IA" (comunidade
O Novo Mercado, copywriting) e pediu para internalizar os padrões e **nunca reproduzi-los**
em nada que este repositório gerar: slides, roteiro, e-mails, planos, glossário. A lista
completa, adaptada:

| # | Vício | Exemplo do artigo | Como evitar aqui |
|---|---|---|---|
| 1 | Título Com Todas As Palavras Maiúsculas | "Como Aumentar Suas Vendas Em 2024" | Use frase normal: só a primeira palavra e nomes próprios em maiúscula. Sigla legítima (IA, SQL, LGPD) não conta como violação |
| 2 | Pergunta retórica em série | "A verdade? Investir cedo muda tudo." | Uma vez no texto todo tudo bem; várias vezes no mesmo bloco, não |
| 3 | Título com dois-pontos como fórmula fixa | "Renda variável: o que os investidores não te contam" | Prefira título direto ou pergunta. Nota: `"Fase 1: Tradução"` **não** é este vício, é rótulo estrutural numerado, não manchete persuasiva |
| 4 | Maiúscula depois de dois-pontos no meio da frase | "Ela tinha um objetivo claro: Conquistar novos clientes" | Em português, a frase continua em minúscula. Exceção real: fala, citação, enumeração ou nome próprio |
| 5 | Vocabulário genérico de robô | insight, crucial, fundamental, essencial, mergulhar, navegar, revolucionário, inspirador, valioso, significativo, "em um mundo", "não apenas... como também", otimizar, contínuo, vital | Troque por linguagem concreta, específica do domínio. `ESSENCIAL`/`DESCARTÁVEL` como marcação de corte no roteiro não é este vício: é rótulo operacional, não adjetivo decorativo |
| 6 | Contraste raso "Não é X. É Y." | "Não é só investir. É construir patrimônio." | Vale uma vez no deck inteiro, no máximo. Prefira fundir numa frase só, ou inverter a ordem |
| 7 | Repetição em escadinha | "Você não precisa de outro simulador. Você não precisa de outra planilha. Você só precisa..." | Ok como recurso de fala pontual (o roteiro é falado em voz alta), mas nunca em prosa escrita nem mais de uma vez por bloco |
| 8 | Adjetivo que enfeita sem explicar | "retorno incrível", "estratégia sólida", "crescimento extraordinário" | Troque por dado concreto: risco baixo, prazo curto, taxa travada, número específico |
| 9 | "Sem X. Sem Y. Só Z." | "Sem dicas milagrosas. Sem enrolação. Só estratégia." | Evite a fórmula. Se quiser o efeito de lista, use bullets de verdade |

**Isso já rendeu correção real neste repositório**, não é regra só teórica: uma varredura
em `scripts/gerar_slides_aula01.py` achou e corrigiu "fundamental" (vício 5), quatro usos de
"valioso/valiosa" (vício 5 e 8) e cinco ocorrências do contraste "não é X. É Y." (vício 6),
incluindo o "solução de dados não é obra pronta. É jardim" que virou "solução de dados é
jardim, não obra pronta: precisa de manutenção", preservando a metáfora mas quebrando o
esqueleto de frase repetido.

**Como aplicar ao escrever conteúdo novo:** antes de considerar um bloco de texto pronto,
releia contra esta tabela. Não existe assert de código para isso (linguagem natural não dá
pra regex com segurança sem gerar falsos positivos), então é revisão manual mesmo. Um
bullet com "cabeça em negrito + explicação" (o padrão `rich_block` usado no deck inteiro)
não é o vício 6: é a estrutura de bullet do projeto, consistente e repetida de propósito.

### 3.6 A validação é automática (regras 3.1 a 3.4)

O fim de `scripts/gerar_slides_aula01.py` tem um bloco que percorre todos os slides e
**levanta erro antes de salvar** se encontrar: travessão em texto ou nota, mais de um
tamanho de fonte na mesma caixa, ou fonte diferente de Roboto. Um segundo `assert`, logo
após a definição das constantes de tamanho, garante que nenhuma delas caiu abaixo de
`S_MIN`.

Copie os dois blocos para qualquer gerador novo. Se o script salvar, as quatro regras
mecânicas foram cumpridas. A regra 3.5 (vícios de IA) ainda precisa de leitura humana.

---

## 4. Identidade visual White Cube

Extraída do template oficial `docs/Apresentação_Template_WhiteCube.pptx`. Os fundos e
logos usados são os **arquivos PNG reais** do template, não recriações.

### 4.1 Grid e formato

| Item | Valor |
|---|---|
| Tamanho do slide | 20 × 11,25 pol (16:9, medida exata do template) |
| Margem esquerda e direita | 1,059 pol |
| Largura útil (`CW`) | 17,882 pol |
| Topo do bloco de título | 1,19 pol |
| Limite inferior do conteúdo (`BOTTOM`) | 9,55 pol |
| Linha do rodapé (`FOOT_Y`) | 9,829 pol |
| Logo | left 16,328 · top 0,586 · 3,066 × 0,795 pol |

### 4.2 Paleta

| Constante | Hex | Uso |
|---|---|---|
| `NAVY` | `#28347B` | Azul institucional. Títulos de card, fundos de seção, cabeçalho de tabela |
| `NAVY_SOFT` | `#3C5DAA` | Azul do logo. Acento secundário |
| `RED` | `#E23635` | Vermelho do logo. Réguas de acento e destaques pontuais |
| `INK` | `#404148` | Texto de corpo e títulos de slide |
| `MUTED` | `#767880` | Subtítulos e texto secundário |
| `LIGHT` | `#EAEBEB` | Fundo claro e faixas alternadas de tabela |
| `LINE` | `#D2D5D5` | Bordas de card |
| `NAVY_TXT_SOFT` | `#B8C0DE` | Texto secundário sobre fundo azul |

### 4.3 Fundos (em `assets/whitecube/`)

| Constante | Arquivo | Quando usar |
|---|---|---|
| `BG_COVER` | `image1.png` | Só a capa. Foto de cubos |
| `BG_LIGHT` | `image3.png` | Cinza `#EAEBEB` com marca d'água. Padrão para cards e diagramas |
| `BG_WHITE` | `image5.png` | Branco com régua azul no rodapé. Padrão para bullets e tabelas |
| `BG_NAVY` | `image6.png` | Azul institucional. Seções, declarações, intervalo, encerramento |
| `LOGO_COLOR` | `image4.png` | Logo colorido, para fundos claros |
| `LOGO_WHITE` | `image7.png` | Logo branco, aplicado automaticamente quando `bg == BG_NAVY` |

Alternar `BG_LIGHT` e `BG_WHITE` ao longo do deck cria ritmo visual. `BG_NAVY` marca
mudança de bloco e vira pausa para os olhos.

### 4.4 Tamanhos de fonte

Definidos como constantes no topo do gerador. Não invente tamanhos novos sem necessidade.
Todas, exceto `S_FOOT`, são ≥ `S_MIN` (17), por causa da regra 3.2. Isso é verificado por
`assert` logo depois da definição das constantes.

| Constante | pt | Papel |
|---|---|---|
| `S_KICKER` | 20 | Linha de apoio em caixa alta, azul, acima do título |
| `S_TITLE` | 40 | Título do slide |
| `S_MIN` | 17 | Piso de legibilidade. Referência, não usada direto em texto |
| `S_SUB` | 17 | Subtítulo |
| `S_BULLET` | 21 | Itens de lista |
| `S_CARD_T` | 20 | Título de card |
| `S_CARD_B` | 17 | Corpo de card |
| `S_TABLE_H` | 18 | Cabeçalho de tabela |
| `S_TABLE_C` | 17 | Célula de tabela |
| `S_BIG` | 36 | Frase de declaração |
| `S_SRC` | 18 | Fonte ou complemento da declaração |
| `S_TIMELINE` | 17 | Texto de cada marco da linha do tempo |
| `S_PIPELINE_B` | 17 | Descrição de cada card do pipeline |
| `S_NESTED_LEGEND` | 17 | Texto da legenda ao lado do diagrama de círculos |
| `S_FOOT` | 13 | Rodapé. **Única exceção** ao piso de 17pt (regra 3.2) |

### 4.5 Assinatura de cabeçalho

O template White Cube tem um título de duas linhas: uma em **negrito, caixa alta, azul** e
outra em regular cinza. Nosso `chrome()` reproduz isso com kicker (azul, caixa alta,
negrito) acima do título (cinza, regular).

### 4.6 Rodapé

`whitecube.com.br` à esquerda, número do slide à direita, ambos em `S_FOOT`. O contador é
global (`_n["i"]`), incrementado por `footer()`, então **todo slide precisa chamar
`footer()` exatamente uma vez** ou a numeração sai errada.

### 4.7 Disposição de objetos: lições da versão final

O usuário pediu atenção a "disposição de objetos na tela" depois de comparar o gerador
contra a versão que ele efetivamente editou e apresentou. Três aprendizados concretos:

1. **Conector de virada de linha em grades de card.** Num `sl_pipeline` com mais de uma
   linha (8 passos em 2 linhas de 4, por exemplo), sem um conector visual entre o último
   card de uma linha e o primeiro da próxima, o olho para no fim da linha e não continua a
   leitura. O `sl_pipeline` já resolve isso: quando `c == per_row - 1` (última coluna) e
   ainda há próximo item, desenha um chevron na margem verdadeira (à esquerda de `ML`),
   alinhado ao centro vertical da linha **seguinte**, não da atual. Reaproveite esse padrão
   em qualquer grade nova que quebre linha.

2. **Slides de declaração (`sl_statement`) sobram muito espaço à direita quando o texto é
   curto.** O fundo `BG_NAVY` deixa a metade direita do slide vazia por padrão. Na versão
   final o usuário preencheu isso, quando fazia sentido, com uma ilustração pequena e
   relacionada ao conceito (por exemplo, uma navalha ao lado da frase sobre a "regra do
   baseline", fazendo o trocadilho visual com a Navalha de Ockham), com legenda em
   `S_SRC` avisando "(Imagem meramente ilustrativa)". O gerador **não** faz isso
   automaticamente, porque não existe hoje uma biblioteca de ícones/ilustrações no
   `assets/`. Se o usuário fornecer uma imagem relevante para um `sl_statement` específico,
   é legítimo posicioná-la na metade direita; não crie isso especulativamente sem uma
   imagem real para usar.

3. **Slides "hero" (bio dos professores, capa) recebem polimento manual fora do gerador.**
   O slide "Os professores" na versão final tem foto circular, ícones de GitHub/LinkedIn,
   link clicável e QR code por pessoa. Isso é montado à mão no Canva/PowerPoint depois da
   importação, não no `python-pptx`: gerar QR code e recortar foto em círculo por código
   é engenharia cara para um conteúdo curado manualmente (fotos e bios reais). O gerador
   entrega a versão de texto (`sl_cards` com nome, cargo, formação), e a curadoria visual
   final acontece depois. Isso é divergência aceita entre o `.pptx` gerado e o `.pptx`
   apresentado; não tente replicar no script.

---

## 5. Catálogo de layouts

Assinaturas de `scripts/gerar_slides_aula01.py`. Todas já aplicam as regras de estilo.

```python
sl_cover()
sl_section(numero, titulo, subtitulo, horario)
sl_bullets(kicker, title, items, subtitle=None, bg=BG_WHITE, numbered=False)
sl_cards(kicker, title, cards, subtitle=None, cols=3, bg=BG_LIGHT, card_h=None)
sl_two_col(kicker, title, left_title, left_items, right_title, right_items,
           subtitle=None, lcolor=NAVY, rcolor=NAVY_SOFT, bg=BG_LIGHT)
sl_statement(kicker, big, source=None)
sl_timeline(kicker, title, steps, subtitle=None)
sl_pipeline(kicker, title, steps, subtitle=None, per_row=4)
sl_nested(kicker, title, subtitle=None)
sl_table(kicker, title, headers, rows, subtitle=None, widths=None, bg=BG_WHITE)
sl_interaction(kicker, title, pergunta, instrucoes)
sl_break()
sl_closing()
```

Formato dos argumentos compostos:

| Layout | Formato |
|---|---|
| `sl_bullets` | `items`: lista de `str` ou de tuplas `(destaque, complemento)`. O destaque sai em negrito e o complemento em cinza, no mesmo tamanho |
| `sl_cards` | `cards`: lista de `(titulo, corpo)`. `\n` no corpo vira parágrafo. `card_h` limita a altura quando o conteúdo é curto |
| `sl_timeline` | `steps`: lista de `(rótulo, texto)`. `\n` no texto quebra linha |
| `sl_pipeline` | `steps`: lista de `(numero, titulo, descricao)`. Renderiza com chevrons entre os cards |
| `sl_table` | `widths`: lista de frações que soma 1.0. A primeira coluna sai em negrito azul |

### Primitivas

```python
new_slide(bg=BG_LIGHT, logo=True)                  # aplica fundo e logo
chrome(slide, kicker, title, subtitle=None,        # cabeçalho; devolve o y do conteúdo
       dark=False)
block(slide, l, t, w, h, lines, size, color=INK,   # caixa de UM tamanho de fonte
      bold=False, align, space=8, line=1.18)
rich_block(slide, l, t, w, h, items, size, ...)    # bullets destaque + complemento
shape(slide, l, t, w, h, fill=None, border=None,   # retângulo, oval, chevron
      kind=MSO_SHAPE.RECTANGLE, border_w=1.0)
footer(slide, dark=False)                          # rodapé + numeração
notes(slide, tempo, marcacao, quem, roteiro,       # notas do apresentador
      lembrete=None)
```

`block()` existe precisamente para tornar difícil violar a regra do tamanho único: ela
recebe **um** `size` e o aplica a todas as linhas.

---

## 6. As notas do apresentador

Cada slide recebe `notes()` com quatro informações obrigatórias:

1. **Tempo** previsto do slide (`"3 min"`, `"19h45 às 20h30 (45 min)"`).
2. **Marcação** `ESSENCIAL` ou `DESCARTÁVEL`, com a ordem de corte quando aplicável.
3. **Quem** apresenta.
4. **Roteiro de fala** em primeira pessoa, quase verbatim, entre aspas.

Um quinto campo opcional, `lembrete`, guarda avisos operacionais: ação do moderador,
fatos a conferir, armadilhas.

O roteiro deve ser falável em voz alta, não um resumo do slide. Ele existe para que a
pessoa consiga apresentar sem ter memorizado o conteúdo. Ninguém decora: adapta.

`scripts/exportar_roteiro.py` transforma essas notas em markdown imprimível. **As notas
não sobrevivem à importação no Canva**, então o markdown é o que vai para o segundo
monitor.

---

## 7. Fluxo de trabalho

```bash
python scripts/gerar_slides_aula01.py     # regera o .pptx (valida estilo antes de salvar)
python scripts/exportar_roteiro.py        # regera docs/aula-01/02-roteiro-do-apresentador.md
```

**Rode sempre os dois em sequência.** Se rodar só o primeiro, o roteiro fica defasado.

### Validação visual obrigatória

O `python-pptx` não renderiza, então overflow de texto passa despercebido. Antes de
entregar, exporte para PNG via COM do PowerPoint e **olhe as imagens**:

```powershell
$out = "<pasta do scratchpad>\preview"
New-Item -ItemType Directory -Force $out | Out-Null
$app = New-Object -ComObject PowerPoint.Application
$pres = $app.Presentations.Open("<caminho absoluto do pptx>", $true, $false, $false)
$pres.Export($out, "PNG", 1600, 900)
$pres.Close(); $app.Quit()
```

Confira pelo menos: capa, um slide de seção, o card mais denso, a tabela mais longa, cada
diagrama e cada slide de declaração.

### Checagem de geometria

Complementa a inspeção visual, detectando formas que saíram da página:

```python
from pptx import Presentation
p = Presentation("docs/aula-01/AI-Talent-Academy-Aula01.pptx")
W, H = p.slide_width, p.slide_height
for i, s in enumerate(p.slides, 1):
    for sh in s.shapes:
        if sh.left is None: continue
        if (sh.left < -2000 or sh.top < -2000
                or sh.left + sh.width > W + 2000 or sh.top + sh.height > H + 2000):
            print("fora dos limites:", i)
```

### Entrega final

O deck é montado no Canva pelo usuário. O `.pptx` é construído com formas e caixas
posicionadas manualmente (sem placeholders de layout) exatamente para sobreviver ao
import. O tamanho 20 × 11,25 já bate com o template, então não há reescala.

---

## 8. Regras de conteúdo e tom

### Público

190 pessoas leigas, à noite, com câmera desligada. Isso determina tudo:

- **Nunca peça para alguém abrir o microfone.** A latência social mata o ritmo. Toda
  interação é por chat ou enquete de múltipla escolha da própria plataforma.
- **Dinâmicas em grupo não escalam.** A proposta comercial prevê squads e apresentações de
  5 a 7 minutos: isso vale para a Etapa 2, não para uma sala de 190 pessoas.
- **Tom lúdico e direto.** Analogias do cotidiano, casos reais contados como história,
  zero jargão sem tradução.
- **Calibrar expectativa é conteúdo.** O bloco "o que a IA não faz" é tão importante
  quanto o "o que a IA faz".

### Exemplos e casos

Use **apenas casos públicos e verificáveis**. Nada de dados, clientes ou cases internos.

**Prefira o caso brasileiro ao equivalente estrangeiro.** Numa sala de 190 brasileiros, um
caso local pega muito mais. Quando o caso estrangeiro for o mais conhecido, cite-o em uma
linha dentro do caso brasileiro, para mostrar que o fenômeno é sistêmico e não uma
peculiaridade local.

Casos já usados e validados no deck da aula 1:

| Caso | Fato |
|---|---|
| Netflix Prize | US$ 1 milhão, concluído em 2009 |
| Alucinação | 2ª Vara Federal de Londrina (PR), 1º/jul/2025. A IA inventou artigos de lei, jurisprudência e números de processo. Multa de 20 salários mínimos e ofício à OAB/PR |
| Viés (principal) | Reconhecimento facial, Aracaju, abr/2024. Sustentado pelo estudo DPU + CESeC de 7/mai/2025: 24 casos mapeados de 2019 a abr/2025, e mais da metade das abordagens resultou em identificação equivocada |
| Viés (secundário) | Ferramenta de triagem de currículos da Amazon, descontinuada em 2018 |
| Marcos históricos | Dartmouth 1956, Deep Blue 1997, deep learning 2012, Transformer 2017, ChatGPT 2022 |

Estatísticas voláteis (por exemplo "X% dos projetos de IA falham") exigem fonte conferida
na data da aula. Sem fonte, mantenha a afirmação qualitativa.

### Restrição de conteúdo em vigor

> 🚫 **Não mencionar o número de vagas de trainee.** São até 10, e os participantes não
> devem saber. Resposta padrão para o Q&A: *"Vai depender do desempenho da turma. Nosso
> interesse é levar o máximo de gente engajada para a Etapa 2."*

Também fora de limite: número de aprovados na Etapa 2, nota de corte específica e qualquer
promessa de contratação.

### Slides de transição

Não escreva "Conduzido por [pessoa]" nos slides de seção. A divisão entre apresentadores é
decisão interna, combinada na hora, e vive nas notas do apresentador.

---

## 9. Armadilhas conhecidas

Problemas reais que já custaram retrabalho. Confira todos ao criar uma aula nova.

| Armadilha | Sintoma | Solução |
|---|---|---|
| **Texto grande estoura a linha** | Frase de declaração quebra em lugar feio | `S_BIG` limitado a 36 pt e `MAX_LINHA_BIG = 62` caracteres, com `assert` no `sl_statement` |
| **Régua atropela o texto** | Elemento em posição fixa colide quando o texto tem mais linhas | Calcule a posição a partir do número de linhas, nunca fixe |
| **Card com metade vazia** | Poucos cards curtos esticam até o rodapé | Use `card_h` para limitar a altura |
| **Diagrama estoura o slide** | Círculos concêntricos passam do rodapé | Dimensione a partir do espaço disponível (`BOTTOM - y`), nunca com valores absolutos |
| **Rótulo na borda da forma** | Texto encosta na linha do círculo | Deslocamento mínimo de 0,3 pol para dentro |
| **Contagem no título não bate** | Título diz "cinco" e há seis cards | Confira número escrito por extenso contra `len(cards)` |
| **Numeração de slide errada** | Números pulam ou repetem | Todo slide chama `footer()` uma vez, e só uma |
| **Roboto não instalada** | Preview do PowerPoint mostra outra fonte | O `.pptx` está correto. Instale Roboto (fonts.google.com) para conferir localmente. O Canva já tem |
| **Console quebra com acento** | `UnicodeEncodeError: cp1252` | Grave em arquivo com `encoding="utf-8"` e leia o arquivo |
| **Linha de tabela com duas linhas** | Texto vaza da faixa alternada | Encurte a célula até caber em uma linha, ou aumente a largura da coluna. Nunca reduza `S_TABLE_C` abaixo de `S_MIN` |
| **Texto pequeno demais numa sala de 190 pessoas** | Corpo de card ou célula de tabela em 14 a 15,5pt, ilegível em tela compartilhada | Piso de 17pt (regra 3.2). Só `S_FOOT` e os rótulos internos do `sl_nested` são exceção documentada |
| **Grade de cards quebra linha sem aviso visual** | Card 4 termina numa borda, card 5 começa do nada na linha de baixo | Conector de virada de linha na margem verdadeira, ver seção 4.7 |
| **Texto soa gerado por IA** | Palavra da lista de vícios (insight, crucial, fundamental...), contraste raso "não é X. É Y.", pergunta retórica em série | Releia contra a tabela da regra 3.5 antes de considerar o texto pronto. Não é checável por código |

---

## 10. Estrutura do repositório

```
ai-talent-academy/
├── CLAUDE.md                      Este arquivo
├── assets/whitecube/              Fundos e logos extraídos do template oficial
│   ├── image1.png                 capa (cubos)
│   ├── image3.png                 fundo cinza claro
│   ├── image4.png                 logo colorido
│   ├── image5.png                 fundo branco com régua azul
│   ├── image6.png                 fundo azul institucional
│   └── image7.png                 logo branco
├── docs/
│   ├── Proposta Executiva 2 ...pdf        Fonte de verdade do programa
│   ├── Apresentação_Template_WhiteCube.pptx   Template oficial de marca
│   ├── AI Talent Academy - Aula 01.pdf        Registro do que foi de fato apresentado
│   ├── AI-Talent-Academy-Aula01-editada.pptx  Idem, em pptx. Ver nota abaixo
│   └── aula-01/
│       ├── README.md                          Índice do pacote da aula
│       ├── AI-Talent-Academy-Aula01.pptx      Deck gerado (64 slides)
│       ├── 01-plano-da-aula.md                Cronômetro, cortes, checklists, riscos
│       ├── 02-roteiro-do-apresentador.md      Gerado a partir das notas do deck
│       ├── 03-material-de-apoio-participante.md   Glossário, enviado pós-aula
│       ├── 04-plano-de-interacao-ao-vivo.md   Enquetes e moderação do chat
│       └── 05-emails-convite-e-lembrete.md    4 e-mails prontos
└── scripts/
    ├── gerar_slides_aula01.py     Gerador do deck
    └── exportar_roteiro.py        Notas do deck para markdown
```

### ⚠️ `assets/` e `*.pptx` estão no `.gitignore`

Consequência: quem clonar o repositório **não consegue rodar o gerador**, porque
`assets/whitecube/` não vem junto e `new_slide()` falha ao abrir os PNGs.

Se isso for indesejado, a correção é adicionar ao final do `.gitignore`:

```gitignore
!assets/whitecube/
!docs/Apresentação_Template_WhiteCube.pptx
```

Decisão pendente do usuário. Não altere sem perguntar.

### Sobre `AI Talent Academy - Aula 01.pdf` e `AI-Talent-Academy-Aula01-editada.pptx`

São o registro do que o usuário **efetivamente editou e apresentou em sala**, entregues em
2026-08-12. Não são a fonte de verdade do conteúdo (essa continua sendo o script, regra 2)
mas são a referência mais confiável para três coisas: (a) o piso de 17pt de fonte descrito
na regra 3.2, (b) as lições de disposição de objetos da seção 4.7, e (c) confirmação de que
o texto ali não usa os vícios de escrita da regra 3.5. Se um comparativo futuro achar
divergência de CONTEÚDO (não de estilo/layout) entre o gerado e esses arquivos, siga o
procedimento da seção 2: diff programático, incorporar no script, regerar.

---

## 11. Receita para uma aula nova

1. **Leia a proposta comercial** e localize a semana. Ela define tema, objetivos de
   aprendizagem, conteúdos, atividades e entregáveis.
2. **Levante o cronograma real** com o usuário: horário de cada bloco, quem apresenta o
   quê, onde entra o intervalo. Não presuma.
3. **Copie `scripts/gerar_slides_aula01.py`** para `gerar_slides_aulaNN.py`. Todo o bloco
   de identidade visual, primitivas, layouts e validação vem junto e não deve mudar.
4. **Escreva o conteúdo**, incluindo as notas de apresentador de cada slide. O roteiro de
   fala é parte do trabalho, não um extra.
5. **Rode o gerador.** Se ele reclamar de estilo, corrija o conteúdo. Não relaxe a
   validação.
6. **Exporte para PNG e olhe.** Corrija overflow e slides com espaço morto.
7. **Rode o exportador de roteiro.**
8. **Escreva os documentos de apoio** no padrão de `docs/aula-01/`: plano com cronômetro e
   mapa de cortes, material do participante, plano de interação, e-mails.
9. **Confira a numeração de slides** citada nos documentos contra o deck real. Ela muda
   sempre que um slide entra ou sai, e é a fonte mais comum de erro nesses arquivos.
10. **Liste as pendências** de preenchimento no README da aula.

### Padrão de arquitetura de uma aula

O deck da aula 1 segue uma estrutura que funcionou bem e vale reaproveitar:

- Capa e slide de espera (loop enquanto a sala enche)
- Slide de seção por bloco, com número, título, subtítulo e horário
- Dentro de cada bloco: alterna declaração (fundo azul), conceito (cards ou tabela),
  exemplo concreto e caso real
- Interação a cada 20 ou 25 minutos
- Slide de intervalo com horário de retorno explícito
- Recapitulação numerada no encerramento, com as ideias que a pessoa deve levar
- Q&A com respostas prontas nas notas para as perguntas previsíveis

---

## 12. Estado atual

**Aula 1 (Semana 1, segunda-feira): já apresentada em sala**, em 2026-08-12. 64 slides,
todos com roteiro de fala. Identidade White Cube aplicada. As quatro regras mecânicas de
estilo (3.1 a 3.4) validadas por `assert`; a quinta (3.5, vícios de IA) revisada à mão
nesta sessão, com correções reais aplicadas no script.

O gerador ficou **atrás** da versão que o usuário efetivamente apresentou num ponto
conhecido e aceito: o slide 5 ("Quem conduz") na versão final tem foto circular, bio
completa, GitHub, LinkedIn e QR code por pessoa, feitos à mão no Canva. O script ainda
produz a versão placeholder (`[1 linha sobre o que você faz no dia a dia]`). Isso é a
divergência documentada na seção 4.7, item 3: não é bug, é o ponto em que o fluxo passa do
gerador para curadoria manual. Só sincronize se o usuário pedir explicitamente.

**Próximo material a produzir:** aula de quinta-feira da semana 1, o primeiro laboratório.
Já está prometido nos slides 60 e 61 e no e-mail de pós-aula, com este escopo:

- Transformar um problema de negócio vago em pergunta analítica, na prática
- Apresentar o **Canvas do Problema**, primeira ferramenta de trabalho do programa
- Um caso real estruturado junto com a turma
- Ainda sem código. O Google Colab entra a partir da semana 2
- Os participantes foram convidados a levar um problema real do próprio dia a dia
- APIs gratuitas da NVIDIA serão a base das aulas práticas com LLM
