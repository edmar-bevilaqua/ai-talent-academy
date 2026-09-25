# -*- coding: utf-8 -*-
"""
Gerador do deck da Aula 15 (Semana 8, segunda-feira) do AI Talent Academy.

Tema: Demo Day e encerramento do programa. A ultima aula, pedida explicitamente pelo
usuario como "super sucinta e curta", ao contrario de toda a serie de decks longos
que vieram antes. Nao e uma aula de conteudo novo: e o dia em que as squads
apresentam o projeto final para uma banca. Este deck cobre so os dois blocos que
cercam essa apresentacao, que nao faz parte do .pptx (acontece ao vivo, sem slide):

  1. Um bloco de ORIENTACAO PLACEHOLDER (Bloco A), deixado de proposito vazio: o
     usuario disse que vai editar essa parte a mao, com os detalhes reais de ordem
     de apresentacao, tempo por squad e criterio de avaliacao. Os slides aqui tem
     marcacao visivel "A PREENCHER", para nao passar a impressao de conteudo pronto.
  2. Um recap rapido do curso inteiro (Bloco B), o pedido principal desta rodada:
     "demonstrar rapidamente tudo que passamos ao longo do curso". Reaproveita o
     pipeline de 8 fases da Aula 1 como gancho, depois resume as duas etapas do
     programa (semanas 1 a 4, semanas 5 a 8) em duas tabelas.
  3. Encerramento com agradecimento, sem apontar para a proxima aula (nao existe).

Identidade visual: padrao White Cube (Roboto, azul 28347B, fundos e logo do template
oficial em assets/whitecube/).

Uso:  python scripts/gerar_slides_aula15.py
Saida: docs/aula-15/AI-Talent-Academy-Aula15.pptx

Regras de estilo aplicadas em todo o deck:
  1. Fonte Roboto em 100% dos textos.
  2. Um unico tamanho de fonte por caixa de texto (nunca alterna tamanho no mesmo bloco).
  3. Zero travessoes (nem "em dash" nem "en dash"). Ha assert no final que garante isso.
"""

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "whitecube"

# --------------------------------------------------------------------------
# Identidade visual White Cube
# --------------------------------------------------------------------------
NAVY = RGBColor(0x28, 0x34, 0x7B)      # azul institucional
NAVY_SOFT = RGBColor(0x3C, 0x5D, 0xAA)  # azul do logo
RED = RGBColor(0xE2, 0x36, 0x35)        # vermelho do logo
INK = RGBColor(0x40, 0x41, 0x48)        # texto padrao
MUTED = RGBColor(0x76, 0x78, 0x80)      # texto secundario
LIGHT = RGBColor(0xEA, 0xEB, 0xEB)      # fundo claro
LINE = RGBColor(0xD2, 0xD5, 0xD5)       # bordas
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
NAVY_TXT_SOFT = RGBColor(0xB8, 0xC0, 0xDE)  # texto secundario sobre fundo azul

BG_COVER = ASSETS / "image1.png"   # capa: cubos
BG_LIGHT = ASSETS / "image3.png"   # cinza claro + marca d'agua
BG_WHITE = ASSETS / "image5.png"   # branco + regua azul + cubo
BG_NAVY = ASSETS / "image6.png"    # azul institucional + marca d'agua
LOGO_COLOR = ASSETS / "image4.png"
LOGO_WHITE = ASSETS / "image7.png"

FONT = "Roboto"

SW = Inches(20)
SH = Inches(11.25)
ML = Inches(1.059)                       # margem esquerda do template
CW = SW - 2 * ML                         # largura util
FOOT_Y = Inches(9.829)                   # linha do rodape do template
BOTTOM = Inches(9.55)                    # limite inferior do conteudo
LOGO = (Inches(16.328), Inches(0.586), Inches(3.066), Inches(0.795))

# tamanhos (um por papel; nunca combinados numa mesma caixa)
S_MIN = 17
S_KICKER = 20
S_TITLE = 40
S_SUB = 17
S_BULLET = 21
S_CARD_T = 20
S_CARD_B = 17
S_TABLE_H = 18
S_TABLE_C = 17
S_BIG = 36
S_SRC = 18
MAX_LINHA_BIG = 62   # caracteres por linha em S_BIG antes de quebrar sozinho
S_FOOT = 13          # excecao documentada: rodape, nao e texto de leitura

assert min(S_SUB, S_BULLET, S_CARD_T, S_CARD_B, S_TABLE_H, S_TABLE_C, S_BIG,
           S_SRC) >= S_MIN, f"Tamanho de fonte de leitura abaixo do minimo de {S_MIN}pt"

ACCENTS = [NAVY, NAVY_SOFT, RED, NAVY, NAVY_SOFT, RED]

prs = Presentation()
prs.slide_width = SW
prs.slide_height = SH
_n = {"i": 0}


# --------------------------------------------------------------------------
# Primitivas
# --------------------------------------------------------------------------
def new_slide(bg=BG_LIGHT, logo=True):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    s.shapes.add_picture(str(bg), 0, 0, SW, SH)
    if logo:
        s.shapes.add_picture(str(LOGO_WHITE if bg == BG_NAVY else LOGO_COLOR), *LOGO)
    return s


def txt(slide, left, top, width, height, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    tf.paragraphs[0].alignment = align
    return tf


def block(slide, left, top, width, height, lines, size, color=INK, bold=False,
          align=PP_ALIGN.LEFT, space=8, line=1.18, anchor=MSO_ANCHOR.TOP,
          italic=False):
    """Uma caixa de texto com UM unico tamanho de fonte para todas as linhas."""
    tf = txt(slide, left, top, width, height, align=align, anchor=anchor)
    if isinstance(lines, str):
        lines = [lines]
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(space)
        p.space_before = Pt(0)
        p.line_spacing = line
        if isinstance(ln, tuple):          # (texto, negrito)
            content, is_bold = ln
        else:
            content, is_bold = ln, bold
        r = p.add_run()
        r.text = content
        r.font.size = Pt(size)
        r.font.bold = is_bold
        r.font.italic = italic
        r.font.color.rgb = color
        r.font.name = FONT
    return tf


def rich_block(slide, left, top, width, height, items, size, space=13, line=1.2,
               bullet_color=NAVY, head_color=INK, tail_color=MUTED, marker="•   "):
    """Bullets com destaque + complemento, TODOS no mesmo tamanho de fonte."""
    tf = txt(slide, left, top, width, height)
    for i, it in enumerate(items):
        head, tail = it if isinstance(it, tuple) else (it, None)
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(space)
        p.line_spacing = line
        mk = f"{i+1}.   " if marker == "#" else marker
        r = p.add_run(); r.text = mk
        r.font.size = Pt(size); r.font.bold = True
        r.font.color.rgb = bullet_color; r.font.name = FONT
        r = p.add_run(); r.text = head
        r.font.size = Pt(size); r.font.bold = tail is not None
        r.font.color.rgb = head_color; r.font.name = FONT
        if tail:
            r = p.add_run(); r.text = "  " + tail
            r.font.size = Pt(size); r.font.bold = False
            r.font.color.rgb = tail_color; r.font.name = FONT
    return tf


def shape(slide, left, top, width, height, fill=None, border=None,
          kind=MSO_SHAPE.RECTANGLE, radius=None, border_w=1.0):
    sp = slide.shapes.add_shape(kind, left, top, width, height)
    sp.shadow.inherit = False
    if fill is None:
        sp.fill.background()
    else:
        sp.fill.solid()
        sp.fill.fore_color.rgb = fill
    if border is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = border
        sp.line.width = Pt(border_w)
    if radius is not None and kind == MSO_SHAPE.ROUNDED_RECTANGLE:
        try:
            sp.adjustments[0] = radius
        except Exception:
            pass
    sp.text_frame.word_wrap = True
    return sp


def chrome(slide, kicker, title, subtitle=None, dark=False):
    """Cabecalho no padrao White Cube: linha de apoio em caixa alta + titulo."""
    k_color = WHITE if dark else NAVY
    t_color = WHITE if dark else INK
    s_color = NAVY_TXT_SOFT if dark else MUTED
    y = Inches(1.19)
    if kicker:
        block(slide, ML, y, CW, Inches(0.42), kicker.upper(), S_KICKER, k_color,
              bold=True, space=0, line=1.0)
        y += Inches(0.52)
    block(slide, ML, y, CW, Inches(0.85), title, S_TITLE, t_color, space=0, line=1.02)
    y += Inches(0.82)
    if subtitle:
        block(slide, ML, y + Inches(0.1), CW, Inches(0.5), subtitle, S_SUB, s_color,
              space=0, line=1.15)
        y += Inches(0.6)
    return y + Inches(0.42)


def footer(slide, dark=False):
    """Rodape do template. SEM numero de slide: a numeracao e feita no Canva, que
    renumera sozinho quando um slide entra ou sai. O contador `_n` continua existindo
    so para o relatorio final da geracao."""
    _n["i"] += 1
    c = NAVY_TXT_SOFT if dark else MUTED
    block(slide, ML, FOOT_Y, Inches(6), Inches(0.4), "whitecube.com.br", S_FOOT, c, space=0)


def notes(slide, tempo, marcacao, quem, roteiro, lembrete=None):
    body = f"⏱ {tempo}  |  {marcacao}  |  Apresenta: {quem}\n"
    body += "─" * 62 + "\nROTEIRO DE FALA\n\n" + roteiro.strip() + "\n"
    if lembrete:
        body += "\n" + "─" * 62 + "\nLEMBRETES\n" + lembrete.strip() + "\n"
    slide.notes_slide.notes_text_frame.text = body


# --------------------------------------------------------------------------
# Layouts
# --------------------------------------------------------------------------
def sl_cover():
    s = new_slide(BG_COVER, logo=False)
    s.shapes.add_picture(str(LOGO_COLOR), ML, Inches(6.55), Inches(4.4), Inches(1.142))
    block(s, ML, Inches(2.05), Inches(13), Inches(0.45),
          "PROGRAMA DE TRAINEES EM DADOS E INTELIGÊNCIA ARTIFICIAL", 17, NAVY, bold=True, space=0)
    block(s, ML, Inches(2.85), Inches(14), Inches(1.5), "AI Talent Academy", 66, NAVY,
          bold=True, space=0, line=1.0)
    block(s, ML, Inches(4.55), Inches(14), Inches(0.9),
          "Semana 8  ·  Demo Day e Encerramento", 25, INK, space=0)
    shape(s, ML, Inches(5.75), Inches(2.4), Pt(5), fill=RED)
    block(s, ML, Inches(8.15), Inches(13), Inches(1.0),
          ["Aula 15  ·  Segunda-feira, 19h00  ·  Online",
           "White Cube  ·  Bevilaqua Data Labs  ·  BPTECH"], S_MIN, INK, space=5)
    footer(s)
    return s


def sl_section(numero, titulo, subtitulo, horario):
    s = new_slide(BG_NAVY)
    y = Inches(3.0)
    if numero:
        block(s, ML, y, Inches(4), Inches(1.6), numero, 96, RGBColor(0x40, 0x4E, 0x9B),
              bold=True, space=0, line=1.0)
    y = Inches(4.55)
    block(s, ML, y, Inches(15), Inches(1.9), titulo, 52, WHITE, bold=True, space=6, line=1.06)
    nlines = titulo.count("\n") + 1
    y += Inches(0.95) * nlines + Inches(0.28)
    block(s, ML, y, Inches(15), Inches(0.7), subtitulo, 24, NAVY_TXT_SOFT, space=0)
    y += Inches(0.95)
    shape(s, ML, y, Inches(2.4), Pt(5), fill=RED)
    block(s, ML, y + Inches(0.4), Inches(14), Inches(0.5), horario, 17, NAVY_TXT_SOFT, space=0)
    footer(s, dark=True)
    return s


def sl_bullets(kicker, title, items, subtitle=None, bg=BG_WHITE, numbered=False):
    s = new_slide(bg)
    y = chrome(s, kicker, title, subtitle)
    rich_block(s, ML, y, CW, BOTTOM - y, items, S_BULLET,
               marker="#" if numbered else "•   ")
    footer(s)
    return s


def sl_cards(kicker, title, cards, subtitle=None, cols=3, bg=BG_LIGHT, card_h=None):
    """cards: lista de (titulo, corpo). Titulo e corpo em caixas separadas."""
    s = new_slide(bg)
    y = chrome(s, kicker, title, subtitle)
    n = len(cards)
    rows = (n + cols - 1) // cols
    gap = Inches(0.38)
    cw = int((CW - gap * (cols - 1)) / cols)
    ch = int((BOTTOM - y - gap * (rows - 1)) / rows)
    if card_h:
        ch = min(ch, Inches(card_h))
    for i, (ct, cb) in enumerate(cards):
        r, c = divmod(i, cols)
        x = ML + c * (cw + gap)
        yy = y + r * (ch + gap)
        acc = ACCENTS[i % len(ACCENTS)]
        shape(s, x, yy, cw, ch, fill=WHITE if bg != BG_WHITE else LIGHT, border=LINE)
        shape(s, x, yy, Pt(6), ch, fill=acc)
        block(s, x + Inches(0.36), yy + Inches(0.28), cw - Inches(0.62), Inches(1.0),
              ct, S_CARD_T, NAVY, bold=True, space=0, line=1.06)
        if cb:
            block(s, x + Inches(0.36), yy + Inches(1.05), cw - Inches(0.62),
                  ch - Inches(1.25), cb.split("\n"), S_CARD_B, INK, space=7, line=1.2)
    footer(s)
    return s


def sl_statement(kicker, big, source=None):
    """Bloco de declaração. A régua e a fonte acompanham o número de linhas."""
    s = new_slide(BG_NAVY)
    linhas = big.split("\n")
    for ln in linhas:
        assert len(ln) <= MAX_LINHA_BIG, f"linha longa demais no statement: {ln!r}"
    top = Inches(3.85)
    lh = Inches(0.62)                      # altura de linha a S_BIG
    block(s, ML, top - Inches(0.78), Inches(16), Inches(0.45), kicker.upper(), S_KICKER,
          WHITE, bold=True, space=0)
    block(s, ML, top, CW, lh * len(linhas) + Inches(0.3), linhas, S_BIG, WHITE,
          bold=True, space=2, line=1.14)
    y = top + lh * len(linhas) + Inches(0.32)
    shape(s, ML, y, Inches(2.4), Pt(5), fill=RED)
    if source:
        block(s, ML, y + Inches(0.45), CW, Inches(1.0), source.split("\n"), S_SRC,
              NAVY_TXT_SOFT, space=4)
    footer(s, dark=True)
    return s


def sl_table(kicker, title, headers, rows, subtitle=None, widths=None, bg=BG_WHITE):
    s = new_slide(bg)
    y = chrome(s, kicker, title, subtitle)
    ncol = len(headers)
    widths = widths or [1.0 / ncol] * ncol
    colw = [int(CW * w) for w in widths]
    hh = Inches(0.66)
    rowh = min(Inches(0.86), int((BOTTOM - y - hh) / len(rows)))
    shape(s, ML, y, CW, hh, fill=NAVY)
    x = ML
    for i, h in enumerate(headers):
        block(s, x + Inches(0.26), y + Inches(0.17), colw[i] - Inches(0.45), Inches(0.4),
              h, S_TABLE_H, WHITE, bold=True, space=0)
        x += colw[i]
    yy = y + hh
    for r, row in enumerate(rows):
        if r % 2 == 0:
            shape(s, ML, yy, CW, rowh, fill=LIGHT if bg == BG_WHITE else WHITE)
        x = ML
        for i, cell in enumerate(row):
            block(s, x + Inches(0.26), yy + Inches(0.13), colw[i] - Inches(0.45),
                  rowh - Inches(0.1), cell, S_TABLE_C, NAVY if i == 0 else INK,
                  bold=(i == 0), space=0, line=1.1)
            x += colw[i]
        yy += rowh
    footer(s)
    return s


def sl_two_col(kicker, title, left_title, left_items, right_title, right_items,
               subtitle=None, lcolor=NAVY, rcolor=NAVY_SOFT, bg=BG_LIGHT):
    s = new_slide(bg)
    y = chrome(s, kicker, title, subtitle)
    gap = Inches(0.5)
    cw = int((CW - gap) / 2)
    h = BOTTOM - y
    for idx, (ct, items, col) in enumerate([(left_title, left_items, lcolor),
                                            (right_title, right_items, rcolor)]):
        x = ML + idx * (cw + gap)
        shape(s, x, y, cw, h, fill=WHITE if bg != BG_WHITE else LIGHT, border=LINE)
        shape(s, x, y, cw, Inches(0.78), fill=col)
        block(s, x + Inches(0.36), y + Inches(0.2), cw - Inches(0.6), Inches(0.5),
              ct, S_CARD_T, WHITE, bold=True, space=0)
        block(s, x + Inches(0.36), y + Inches(1.12), cw - Inches(0.7), h - Inches(1.35),
              ["•  " + it for it in items], 17, INK, space=12, line=1.18)
    footer(s)
    return s


# ==========================================================================
# CONTEÚDO
# ==========================================================================
EU = "Edmar"
FELIPE = "Felipe André Bach Alves"
PREENCHER = "★ A PREENCHER PELO USUÁRIO ★"

# --------------------------------------------------------------------------
# RECEPÇÃO (19h00 às 19h10)
# --------------------------------------------------------------------------
s = sl_cover()
notes(s, "19h00 às 19h10 (slide de espera)", "ESSENCIAL", EU,
      """
Slide projetado desde 18h55.

"Boa noite! Hoje é diferente de todas as outras noites: é o Demo Day, o
encerramento do AI Talent Academy. Enquanto a sala enche, deixem no chat: qual
foi a aula que mais marcou vocês, nessas oito semanas?"

Não comece antes de 19h08.
""",
      """
- Este deck é deliberadamente curto, a pedido explícito do usuário: não é uma aula
  de conteúdo novo, é o bloco que cerca a apresentação das squads.
- O Bloco A (orientação sobre a apresentação) foi deixado como esqueleto de
  propósito, com marcação "A PREENCHER". O usuário vai editar essa parte à mão
  antes da aula, com ordem de apresentação, tempo por squad e critério de avaliação
  reais.
- Confirmar com antecedência: banca de avaliação presente, ordem das squads
  definida, tempo por apresentação combinado.
""")

s = sl_bullets("Hoje é diferente", "O dia em que o trabalho de vocês fala mais alto que o slide",
               [("Áudio e câmera", "microfone no mudo até sua vez, câmera à vontade"),
                ("A pauta de hoje", "orientação rápida, apresentação das squads, e um fechamento com vocês"),
                ("Gravação", "a aula é gravada e o link chega em até 24h"),
                ("A partir daqui, o protagonismo é de vocês", "cada squad vai apresentar o que construiu nas últimas semanas")],
               subtitle="Semana 8: Demo Day e encerramento do AI Talent Academy.")
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Hoje a estrutura é diferente. Rapidinho: microfone no mudo até chegar sua vez,
câmera à vontade, aula gravada com link em até 24h.

A pauta: uma orientação rápida sobre como vai funcionar a apresentação de vocês,
depois as squads apresentam, e a gente fecha o programa juntos.

A partir de agora, o protagonismo é de vocês."
""")

# --------------------------------------------------------------------------
# BLOCO A: Orientação sobre a apresentação (PLACEHOLDER, a preencher)
# --------------------------------------------------------------------------
s = sl_section("A", "Antes de começar",
               "Como vai funcionar a apresentação de vocês",
               PREENCHER)
notes(s, PREENCHER, "A PREENCHER", EU,
      f"""
{PREENCHER}

Este bloco foi deixado como esqueleto de propósito. O usuário pediu para montar
essa parte manualmente, com os detalhes reais de ordem de apresentação, tempo por
squad e critério de avaliação.
""")

s = sl_bullets("Como vai funcionar", PREENCHER,
               [(PREENCHER, "ordem de apresentação das squads"),
                (PREENCHER, "tempo disponível por squad, e o que fazer se passar do tempo"),
                (PREENCHER, "o que a banca vai avaliar"),
                (PREENCHER, "como funciona a devolutiva, e quando os aprovados são avisados")],
               subtitle="Slide esqueleto. Edite cada linha antes de apresentar.")
notes(s, PREENCHER, "A PREENCHER", EU,
      f"""
{PREENCHER}

Sugestão de estrutura para preencher: ordem das squads, tempo por apresentação,
critério de avaliação da banca, e como funciona a devolutiva.
""")

# --------------------------------------------------------------------------
# BLOCO B: Oito semanas, um caminho só (recap do curso)
# --------------------------------------------------------------------------
s = sl_section("B", "Oito semanas, um caminho só",
               "Tudo que vocês passaram, do primeiro slide até hoje",
               "Recapitulação rápida")
notes(s, "12 min", "ESSENCIAL", FELIPE,
      """
DISTRIBUIÇÃO:
  O mapa da Aula 1, revisitado    3 min
  Etapa 1: fundamentos            4 min
  Etapa 2: imersão prática        4 min
  Números do programa             1 min

Bloco pedido explicitamente pelo usuário como o foco principal desta aula: "demonstrar
rapidamente tudo que passamos ao longo do curso". Vá rápido, é recapitulação, não
ensino novo.
""")

s = sl_statement("Lembram desse mapa?",
                 "Oito fases, no slide 4 da Aula 1.\nHoje, todas elas já passaram\npela mão de vocês.",
                 "Entender o problema, conseguir o dado, explorar, preparar, modelar, avaliar, publicar, monitorar.")
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Lembram desse mapa? Oito fases de uma solução de dados e IA, mostradas no
primeiro dia de aula, quando a maioria de vocês ainda nem sabia diferenciar SQL de
Python.

Entender o problema, conseguir o dado, explorar, preparar, modelar, avaliar,
publicar, monitorar. Naquele dia, era teoria. Hoje, cada uma dessas oito fases já
passou pela mão de vocês, pelo menos uma vez."
""")

s = sl_table("Etapa 1 · Semanas 1 a 4", "Fundamentos: da primeira aula ao primeiro desafio",
             ["Semana", "Segunda (conceito)", "Quinta (prática)"],
             [["1", "Panorama de Dados e IA, o pipeline de 8 fases", "Canvas do Problema, primeiro laboratório"],
              ["2", "IA Generativa: Transformer, prompt, RAG", "GenAI na prática, segundo laboratório"],
              ["3", "Análise de Dados com SQL", "SQL na prática, banco de fraude em cartão"],
              ["4", "Análise de Dados com Python: NumPy, pandas, Matplotlib, Seaborn", "Investigação de fraude, 1 milhão de transações"]],
             widths=[0.10, 0.48, 0.42])
notes(s, "4 min", "ESSENCIAL", FELIPE,
      """
"As primeiras quatro semanas, a Etapa 1, foram sobre nivelar a base.

Semana 1: o panorama de dados e IA, e o Canvas do Problema.
Semana 2: IA Generativa, Transformer, prompt, RAG, e a prática logo em seguida.
Semana 3: SQL, direto no banco de fraude em cartão que acompanhou vocês o curso
inteiro.
Semana 4: Python, NumPy, pandas, Matplotlib, Seaborn, fechando com uma investigação
de verdade em cima de 1 milhão de transações.

Essa etapa terminou com o Mini-Desafio Data & AI, a primeira seleção do programa."
""")

s = sl_table("Etapa 2 · Semanas 5 a 8", "Imersão prática: de engenharia de dados ao Demo Day",
             ["Semana", "Segunda (conceito)", "Quinta (prática)"],
             [["5", "Engenharia de Dados: fontes, ETL, qualidade, orquestração", "Airflow e PySpark, pipeline de verdade"],
              ["6", "Machine Learning: do baseline à árvore de decisão", "Treinando o primeiro modelo, com scikit-learn"],
              ["7", "Agentes de IA: história, controle, ferramentas", "Construindo o primeiro agente, com MCP de verdade"],
              ["8", "Demo Day e encerramento", "Hoje"]],
             widths=[0.10, 0.48, 0.42])
notes(s, "4 min", "ESSENCIAL", FELIPE,
      """
"E as últimas quatro semanas, a Etapa 2, foram sobre colocar a mão na massa de
verdade.

Semana 5: Engenharia de Dados, com Airflow e PySpark rodando de verdade.
Semana 6: Machine Learning, terminando com vocês treinando o primeiro modelo de
verdade, com scikit-learn.
Semana 7: Agentes de IA, terminando com vocês construindo um agente de verdade, com
uma ferramenta MCP de verdade.

E semana 8: hoje. Demo Day, e o encerramento do programa."
""")

s = sl_cards("Alguns números", "Oito semanas, de um jeito só",
             [("8", "semanas de programa,\nde ponta a ponta"),
              ("13", "aulas com conteúdo\nnovo até aqui"),
              ("~190", "pessoas que começaram\nessa jornada com vocês")],
             cols=3, card_h=2.8)
notes(s, "1 min", "ESSENCIAL", FELIPE,
      """
"Alguns números, rápido: oito semanas, treze aulas de conteúdo novo, e quase 190
pessoas que começaram essa jornada junto com vocês, em algum momento."
""")

# --------------------------------------------------------------------------
# BLOCO C: Encerramento
# --------------------------------------------------------------------------
s = sl_section("C", "Encerramento",
               "O que fica, depois que o programa termina",
               "Fechamento")
notes(s, "5 min", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Mensagem de encerramento    3 min
  Agradecimento               2 min
""")

s = sl_bullets("Encerramento", "O que fica, depois de hoje",
               [("O conteúdo passa, o jeito de pensar fica", "SQL, Python, engenharia de dados, modelo, agente: tudo isso vocês sabem procurar de novo, quando precisar"),
                ("Vocês treinaram o hábito mais importante do time de dados", "perguntar antes de responder, e medir antes de confiar"),
                ("Esse squad que apresentou hoje pode continuar existindo", "muita gente boa em dados começou assim, resolvendo um problema pequeno junto")],
               subtitle="Fecha aqui o conteúdo. O que vem a seguir é combinado à parte, fora deste deck.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Antes de fechar de verdade, três coisas para levar.

O conteúdo específico passa, cai em desuso, alguma ferramenta que vocês aprenderam
aqui vai mudar de nome daqui a um ano. O jeito de pensar fica: perguntar antes de
responder, medir antes de confiar.

Vocês treinaram isso na prática, oito semanas seguidas, não só ouviram falar.

E esse squad que apresentou hoje não precisa acabar aqui. Muita gente boa em dados
começou exatamente assim."
""")

s = sl_statement("Obrigado",
                 "Obrigado por chegarem até aqui.\nObrigado por perguntarem,\nerrarem, e tentarem de novo.",
                 "Edmar Bevilaqua, Felipe André Bach Alves, e todo o time da White Cube.")
notes(s, "2 min", "ESSENCIAL", EU,
      """
"Obrigado por chegarem até aqui. De quase 190 pessoas no primeiro dia até esse
grupo que está na tela agora, apresentando um projeto de verdade.

Obrigado por perguntarem no chat, por errarem ao vivo, e por tentarem de novo. É
disso que é feito aprender dados e IA de verdade, não só de slide bonito."
""",
      "Se Ale e Márcio, da diretoria da White Cube, estiverem presentes, este é o "
      "momento natural para uma fala curta deles, encerrando institucionalmente, "
      "no mesmo espírito de como abriram a Aula 1.")

s = new_slide(BG_NAVY)
block(s, ML, Inches(3.4), Inches(15), Inches(1.7), "Até a próxima!", 66, WHITE, bold=True,
      space=0, line=1.0)
block(s, ML, Inches(5.3), Inches(15), Inches(0.8),
      "O AI Talent Academy termina aqui. O que vocês constroem a partir de agora é com vocês.",
      26, NAVY_TXT_SOFT, space=0)
shape(s, ML, Inches(6.65), Inches(2.4), Pt(5), fill=RED)
block(s, ML, Inches(7.2), Inches(15), Inches(1.4),
      ["Discord do AI Talent Academy: continua no ar para a comunidade.",
       "Gravação e slides desta aula chegam em até 24h."], 18, NAVY_TXT_SOFT, space=8)
footer(s, dark=True)
notes(s, "1 min", "ESSENCIAL", EU,
      """
FECHAMENTO (30 segundos):

"Foi um prazer imenso conduzir essas oito semanas com vocês. Até a próxima, e boa
sorte no que vier depois do AI Talent Academy!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Confirmar com a organização o processo de certificado e próximos passos dos
  aprovados para a próxima etapa, fora deste deck.
""")

# --------------------------------------------------------------------------
# Validações de estilo
# --------------------------------------------------------------------------
PROIBIDOS = {"—": "travessão (em dash)", "–": "meia-risca (en dash)"}
falhas = []
for i, sl in enumerate(prs.slides, 1):
    textos = [sh.text_frame.text for sh in sl.shapes if sh.has_text_frame]
    if sl.has_notes_slide:
        textos.append(sl.notes_slide.notes_text_frame.text)
    for t in textos:
        for ch, nome in PROIBIDOS.items():
            if ch in t:
                falhas.append(f"slide {i}: {nome} em {t[:70]!r}")
    for sh in sl.shapes:
        if not sh.has_text_frame:
            continue
        tamanhos = {r.font.size.pt for p in sh.text_frame.paragraphs
                    for r in p.runs if r.font.size}
        if len(tamanhos) > 1:
            falhas.append(f"slide {i}: tamanhos misturados {sorted(tamanhos)} "
                          f"em {sh.text_frame.text[:50]!r}")
        fontes = {r.font.name for p in sh.text_frame.paragraphs
                  for r in p.runs if r.font.name}
        if fontes - {FONT}:
            falhas.append(f"slide {i}: fonte fora do padrão {fontes}")

if falhas:
    raise SystemExit("FALHAS DE ESTILO:\n  " + "\n  ".join(falhas[:30]))

out = ROOT / "docs" / "aula-15"
out.mkdir(parents=True, exist_ok=True)
dest = out / "AI-Talent-Academy-Aula15.pptx"
prs.save(dest)
print(f"OK: {dest}  ({len(prs.slides._sldIdLst)} slides)  "
      f"Roboto, sem travessões, tamanho único por bloco.")
