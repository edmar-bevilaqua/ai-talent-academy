# -*- coding: utf-8 -*-
"""
Gerador do deck da Aula 9 (Semana 5, segunda-feira) do AI Talent Academy.

Tema: Engenharia de Dados. Aula expositiva, sem mao na massa (a pratica fica para a
Aula 10, na quinta). Escopo rico de proposito, por pedido explicito do usuario, em
duas rodadas: cobre fontes de dados, batch x streaming, banco transacional x Data
Warehouse x Data Lake (com nota sobre Lakehouse), ETL x ELT com a rivalidade historica
Inmon x Kimball, qualidade de dados, pipeline de producao e DAG, a historia do Airflow
e do dbt, processamento distribuido com a historia de MapReduce, Hadoop, Spark e
Databricks, e um fechamento ponta a ponta usando o mesmo caso de fraude em cartao das
Aulas 2, 5, 6, 7 e 8. O usuario pediu para gerar tudo rico e cortar depois, entao a
aula ficou bem mais longa que o padrao de 3h: ver o total real no final da geracao.

Identidade visual: padrao White Cube (Roboto, azul 28347B, fundos e logo do template
oficial em assets/whitecube/).

Uso:  python scripts/gerar_slides_aula09.py
Saida: docs/aula-09/AI-Talent-Academy-Aula09.pptx

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
# Piso de legibilidade: 17pt para todo texto de leitura (corpo, bullet, card, tabela,
# legenda). Abaixo disso o texto nao se le numa sala compartilhada por 190 pessoas.
# As DUAS excecoes documentadas, that a propria versao final aprovada do usuario mantem
# abaixo de 17pt, sao S_FOOT (rodape, e mobilia da pagina, ninguem precisa le-lo de
# longe) e os rotulos internos dos circulos concentricos do sl_nested (fs_rings: o
# espaco fisico dentro dos aneis mais internos nao comporta 17pt sem quebrar o desenho).
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
S_TIMELINE = 17
S_PIPELINE_B = 17
S_NESTED_LEGEND = 17

assert min(S_SUB, S_BULLET, S_CARD_T, S_CARD_B, S_TABLE_H, S_TABLE_C, S_BIG, S_SRC,
           S_TIMELINE, S_PIPELINE_B, S_NESTED_LEGEND) >= S_MIN, \
    f"Tamanho de fonte de leitura abaixo do minimo de {S_MIN}pt"

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
          "Semana 5  ·  Engenharia de Dados", 25, INK, space=0)
    shape(s, ML, Inches(5.75), Inches(2.4), Pt(5), fill=RED)
    block(s, ML, Inches(8.15), Inches(13), Inches(1.0),
          ["Aula 9  ·  Segunda-feira, 19h00 às 22h40  ·  Online",
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


def sl_timeline(kicker, title, steps, subtitle=None):
    s = new_slide(BG_WHITE)
    y = chrome(s, kicker, title, subtitle)
    n = len(steps)
    gap = Inches(0.3)
    cw = int((CW - gap * (n - 1)) / n)
    line_y = y + Inches(1.25)
    shape(s, ML, line_y, CW, Pt(2.5), fill=LINE)
    for i, (ano, texto) in enumerate(steps):
        x = ML + i * (cw + gap)
        acc = ACCENTS[i % len(ACCENTS)]
        block(s, x, y + Inches(0.15), cw, Inches(0.8), ano, 26, acc, bold=True,
              align=PP_ALIGN.CENTER, space=0)
        d = Inches(0.34)
        shape(s, x + int(cw / 2) - int(d / 2), line_y - Inches(0.14), d, d, fill=acc,
              kind=MSO_SHAPE.OVAL)
        block(s, x, line_y + Inches(0.55), cw, BOTTOM - line_y - Inches(0.7),
              texto.split("\n"), S_TIMELINE, INK, align=PP_ALIGN.CENTER, space=2, line=1.22)
    footer(s)
    return s


def sl_pipeline(kicker, title, steps, subtitle=None, per_row=4):
    s = new_slide(BG_LIGHT)
    y = chrome(s, kicker, title, subtitle)
    rows = (len(steps) + per_row - 1) // per_row
    gap = Inches(0.62)
    vgap = Inches(0.42)
    cw = int((CW - gap * (per_row - 1)) / per_row)
    ch = int((BOTTOM - y - vgap * (rows - 1)) / rows)
    for i, (num, t, d) in enumerate(steps):
        r, c = divmod(i, per_row)
        x = ML + c * (cw + gap)
        yy = y + r * (ch + vgap)
        acc = ACCENTS[i % len(ACCENTS)]
        shape(s, x, yy, cw, ch, fill=WHITE, border=acc, border_w=1.5)
        b = Inches(0.56)
        shape(s, x + Inches(0.3), yy + Inches(0.3), b, b, fill=acc, kind=MSO_SHAPE.OVAL)
        block(s, x + Inches(0.3), yy + Inches(0.4), b, Inches(0.4), str(num), 17, WHITE,
              bold=True, align=PP_ALIGN.CENTER, space=0)
        block(s, x + Inches(1.02), yy + Inches(0.36), cw - Inches(1.3), Inches(0.7), t,
              18, NAVY, bold=True, space=0, line=1.05)
        block(s, x + Inches(0.32), yy + Inches(1.3), cw - Inches(0.62), ch - Inches(1.5),
              d, S_PIPELINE_B, INK, space=0, line=1.22)
        if c < per_row - 1 and i < len(steps) - 1:
            shape(s, x + cw + Inches(0.1), yy + int(ch / 2) - Inches(0.17), Inches(0.42),
                  Inches(0.34), fill=LINE, kind=MSO_SHAPE.CHEVRON)
        elif c == per_row - 1 and i < len(steps) - 1:
            # conector de virada de linha: sem isso o olho para no fim da linha e nao
            # continua a leitura na proxima. Vive na margem verdadeira, a esquerda de ML,
            # alinhado ao centro vertical da linha SEGUINTE (nao da linha atual).
            next_center = yy + ch + vgap + int(ch / 2)
            shape(s, ML - Inches(0.52), next_center - Inches(0.17), Inches(0.42),
                  Inches(0.34), fill=LINE, kind=MSO_SHAPE.CHEVRON)
    footer(s)
    return s


def sl_nested(kicker, title, subtitle=None):
    s = new_slide(BG_LIGHT)
    y = chrome(s, kicker, title, subtitle)
    avail = BOTTOM - y
    cy = y + int(avail / 2)
    cx = ML + Inches(3.15)
    rings = [
        (Inches(5.9), RGBColor(0xD5, 0xD9, 0xE8), "INTELIGÊNCIA ARTIFICIAL", NAVY, 15),
        (Inches(4.55), RGBColor(0xBC, 0xC3, 0xDD), "MACHINE LEARNING", NAVY, 14),
        (Inches(3.2), RGBColor(0x92, 0x9E, 0xC6), "DEEP LEARNING", NAVY, 13),
        (Inches(1.85), NAVY, "GenAI", WHITE, 17),
    ]
    for d, fill, _, _, _ in rings:
        shape(s, cx - int(d / 2), cy - int(d / 2), d, d, fill=fill, kind=MSO_SHAPE.OVAL)
    for i, (d, _, label, col, fs) in enumerate(rings):
        ly = cy - int(d / 2) + Inches(0.32) if i < 3 else cy - Inches(0.17)
        block(s, cx - int(d / 2), ly, d, Inches(0.4), label, fs, col, bold=True,
              align=PP_ALIGN.CENTER, space=0)
    rx = ML + Inches(6.9)
    lw = SW - ML - rx
    defs = [
        ("Inteligência Artificial",
         "Guarda-chuva. Qualquer sistema que executa tarefas que associamos à inteligência humana.", NAVY),
        ("Machine Learning",
         "O sistema aprende padrões a partir de exemplos, em vez de seguir regras escritas à mão.", NAVY_SOFT),
        ("Deep Learning",
         "ML com redes neurais profundas. Brilha em imagem, áudio e texto.", RED),
        ("IA Generativa",
         "Deep Learning que gera conteúdo novo: texto, imagem, código, áudio.", NAVY),
        ("Agentes de IA",
         "Uma GenAI que não só responde: planeja, usa ferramentas e executa tarefas.", NAVY_SOFT),
    ]
    step = int((avail - Inches(1.0)) / 4)
    yy = y + Inches(0.1)
    for t, d, col in defs:
        shape(s, rx, yy + Inches(0.05), Pt(5), Inches(0.92), fill=col)
        block(s, rx + Inches(0.3), yy, lw - Inches(0.3), Inches(0.42), t, 19, NAVY,
              bold=True, space=0)
        block(s, rx + Inches(0.3), yy + Inches(0.45), lw - Inches(0.3), Inches(0.6), d,
              S_NESTED_LEGEND, INK, space=0, line=1.16)
        yy += step
    footer(s)
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


def sl_interaction(kicker, title, pergunta, instrucoes):
    s = new_slide(BG_LIGHT)
    y = chrome(s, kicker, title)
    bh = Inches(1.5)
    shape(s, ML, y, CW, bh, fill=WHITE, border=NAVY, border_w=1.5)
    shape(s, ML, y, Pt(6), bh, fill=RED)
    block(s, ML + Inches(0.6), y + Inches(0.42), CW - Inches(1.2), Inches(0.9), pergunta,
          30, NAVY, bold=True, space=0, line=1.1)
    block(s, ML, y + bh + Inches(0.6), CW, Inches(2.6), ["→  " + i for i in instrucoes],
          19, INK, space=16)
    footer(s)
    return s


def sl_break():
    s = new_slide(BG_NAVY)
    block(s, ML, Inches(3.2), Inches(14), Inches(0.45), "INTERVALO", S_KICKER, WHITE,
          bold=True, space=0)
    block(s, ML, Inches(3.95), Inches(14), Inches(1.7), "15 minutos", 76, WHITE, bold=True,
          space=0, line=1.0)
    block(s, ML, Inches(5.85), Inches(14), Inches(0.7), "Voltamos às 20h45 em ponto.", 28,
          NAVY_TXT_SOFT, space=0)
    shape(s, ML, Inches(7.0), Inches(2.4), Pt(5), fill=RED)
    block(s, ML, Inches(7.5), Inches(15), Inches(1.4),
          ["Enquanto isso: entre no Discord do AI Talent Academy (link no chat)",
           "Deixe sua dúvida no chat. Vamos responder na volta."], 18, NAVY_TXT_SOFT, space=8)
    footer(s, dark=True)
    return s


def sl_closing():
    s = new_slide(BG_NAVY)
    block(s, ML, Inches(3.6), Inches(15), Inches(1.7), "Obrigado!", 66, WHITE, bold=True,
          space=0, line=1.0)
    block(s, ML, Inches(5.5), Inches(15), Inches(0.8), "Nos vemos na quinta-feira, 19h00.",
          30, NAVY_TXT_SOFT, space=0)
    shape(s, ML, Inches(6.85), Inches(2.4), Pt(5), fill=RED)
    block(s, ML, Inches(7.4), Inches(15), Inches(1.4),
          ["Discord do AI Talent Academy: link fixado no chat e enviado por e-mail.",
           "Gravação e slides desta aula chegam em até 24h."], 18, NAVY_TXT_SOFT, space=8)
    footer(s, dark=True)
    return s




def sl_prompt(kicker, title, ruim, bom, subtitle=None):
    """Compara prompt fraco e prompt bom lado a lado.

    `ruim` e `bom` sao tuplas (rotulo, texto_do_prompt, consequencia). Cada elemento
    fica em caixa de texto propria, para nunca misturar tamanho de fonte num bloco.
    """
    s = new_slide(BG_LIGHT)
    y = chrome(s, kicker, title, subtitle)
    gap = Inches(0.5)
    cw = int((CW - gap) / 2)
    h = BOTTOM - y
    # A regua divisoria acompanha o lado mais alto: o prompt mais longo dos dois define
    # onde ela cai. Sem isso, prompt de muitas linhas atropela a regua e a conclusao.
    linhas_max = max(len(ruim[1].split(chr(10))), len(bom[1].split(chr(10))))
    conc_max = max(len(ruim[2].split(chr(10))), len(bom[2].split(chr(10))))
    topo_texto = Inches(1.05)
    alt_linha = Inches(0.40)   # altura real de uma linha a S_MIN, medida no render
    y_regua = topo_texto + alt_linha * linhas_max + Inches(0.28)
    alt_conc = alt_linha * conc_max + Inches(0.2)
    # se o conteudo nao couber, encosta a regua no piso possivel
    y_regua = min(y_regua, h - alt_conc - Inches(0.25))
    for idx, (dados, cor) in enumerate([(ruim, MUTED), (bom, NAVY)]):
        rotulo, texto, consequencia = dados
        x = ML + idx * (cw + gap)
        shape(s, x, y, cw, h, fill=WHITE, border=LINE)
        shape(s, x, y, cw, Inches(0.72), fill=cor)
        block(s, x + Inches(0.34), y + Inches(0.18), cw - Inches(0.6), Inches(0.45),
              rotulo, S_CARD_T, WHITE, bold=True, space=0)
        block(s, x + Inches(0.34), y + topo_texto, cw - Inches(0.68), y_regua - topo_texto,
              texto.split(chr(10)), S_MIN, INK, space=4, line=1.24, italic=True)
        shape(s, x + Inches(0.34), y + y_regua, cw - Inches(0.68), Pt(2), fill=LINE)
        block(s, x + Inches(0.34), y + y_regua + Inches(0.25), cw - Inches(0.68), alt_conc,
              consequencia.split(chr(10)), S_MIN, cor, bold=True, space=4, line=1.2)
    footer(s)
    return s


def sl_canvas(kicker, title, campos, subtitle=None, destaque=None):
    """Canvas do Problema: 8 campos em grade 4x2. `destaque` (1-8) realca um campo."""
    s = new_slide(BG_LIGHT)
    y = chrome(s, kicker, title, subtitle)
    cols, rows = 4, 2
    gap = Inches(0.3)
    cw = int((CW - gap * (cols - 1)) / cols)
    ch = int((BOTTOM - y - gap) / rows)
    for i, (num, nome, guia) in enumerate(campos):
        r, c = divmod(i, cols)
        x = ML + c * (cw + gap)
        yy = y + r * (ch + gap)
        on = (destaque is None) or (destaque == num)
        acc = NAVY if on else LINE
        fill = WHITE if on else RGBColor(0xF2, 0xF3, 0xF3)
        txt_t = NAVY if on else RGBColor(0xA8, 0xAC, 0xAC)
        txt_b = INK if on else RGBColor(0xB4, 0xB8, 0xB8)
        shape(s, x, yy, cw, ch, fill=fill, border=acc, border_w=1.5 if on else 1.0)
        shape(s, x, yy, cw, Pt(6), fill=acc)
        block(s, x + Inches(0.26), yy + Inches(0.3), cw - Inches(0.5), Inches(0.4),
              f"{num}", S_MIN, txt_t, bold=True, space=0)
        block(s, x + Inches(0.26), yy + Inches(0.72), cw - Inches(0.5), Inches(0.6),
              nome, S_CARD_T, txt_t, bold=True, space=0, line=1.05)
        block(s, x + Inches(0.26), yy + Inches(1.5), cw - Inches(0.5), ch - Inches(1.7),
              guia, S_MIN, txt_b, space=0, line=1.2)
    footer(s)
    return s


def sl_code(kicker, title, codigo, items, subtitle=None):
    """Bloco de codigo em destaque, com bullets de explicacao embaixo."""
    s = new_slide(BG_WHITE)
    y = chrome(s, kicker, title, subtitle)
    linhas = codigo if isinstance(codigo, list) else codigo.split("\n")
    alt_linha = Inches(0.40)
    qh = alt_linha * len(linhas) + Inches(0.5)
    shape(s, ML, y, CW, qh, fill=RGBColor(0xF2, 0xF3, 0xF6), border=NAVY, border_w=1.0)
    shape(s, ML, y, Pt(6), qh, fill=NAVY)
    block(s, ML + Inches(0.45), y + Inches(0.25), CW - Inches(0.9), qh - Inches(0.35),
          linhas, S_MIN, NAVY, bold=True, space=3, line=1.3)
    y2 = y + qh + Inches(0.4)
    rich_block(s, ML, y2, CW, BOTTOM - y2, items, S_BULLET)
    footer(s)
    return s


# ==========================================================================
# CONTEÚDO
# ==========================================================================
EU = "Edmar"
FELIPE = "Felipe André Bach Alves"


# ==========================================================================
# CONTEÚDO
# ==========================================================================
EU = "Edmar"
FELIPE = "Felipe André Bach Alves"

# --------------------------------------------------------------------------
# RECEPÇÃO (19h00 às 19h10)
# --------------------------------------------------------------------------
s = sl_cover()
notes(s, "19h00 às 19h10 (slide de espera)", "ESSENCIAL", EU,
      """
Slide projetado desde 18h55. Fale a cada 2 ou 3 minutos enquanto a sala enche.

"Boa noite! Semana 5, e hoje é o assunto que fecha uma pergunta que ficou em aberto
desde a Aula 1: de onde vêm os dados, e quem prepara eles antes de chegar em SQL ou em
pandas. Enquanto todo mundo entra, escreve no chat: antes de hoje, você sabia dizer o
que é engenharia de dados?"

Não comece antes de 19h08.
""",
      """
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- Moderador com o link do Discord pronto para colar.
- Sem código ao vivo hoje. Os exemplos aparecem no slide, a prática é na quinta.
""")

s = sl_bullets("Enquanto todo mundo entra", "Hoje fecha uma pergunta que ficou em aberto desde a Aula 1",
               [("Áudio e câmera", "microfone no mudo, câmera fica a seu critério"),
                ("Dúvidas", "escreva no chat a qualquer momento, temos moderação acompanhando"),
                ("Gravação", "a aula é gravada e o link chega em até 24h"),
                ("Ainda sem código ao vivo hoje", "os exemplos aparecem no slide, a prática é na quinta"),
                ("Aqueça o teclado", "escreva no chat: antes de hoje, você sabia dizer o que é engenharia de dados?")],
               subtitle="Aula 9 · Semana 5 · começamos 19h10")
notes(s, "19h00 às 19h10", "ESSENCIAL", EU,
      """
Leia os itens uma vez, por volta de 19h05. As respostas do chat servem de termômetro
para calibrar o ritmo do bloco A.
""")

# ==========================================================================
# BLOCO A: Abertura, fechando o pipeline (19h10 às 19h35)
# ==========================================================================
s = sl_section("01", "A pergunta que ficou em aberto",
               "De onde vêm os dados, antes de virarem SQL ou pandas",
               "19h10 às 19h35  ·  25 minutos")
notes(s, "19h10 às 19h35 (25 min)", "ESSENCIAL", EU,
      """
Bloco de contexto. Objetivo: reabrir o pipeline de 8 fases da Aula 1 e mostrar que
hoje fecha duas fases que ficaram soltas até aqui.

ESTRUTURA:
  Onde estamos                4 min
  O pipeline revisitado         7 min
  Por que hoje importa            6 min
  O plano de hoje                   6 min
""")

s = sl_table("Onde estamos", "A jornada das 8 semanas",
             ["Semana", "Tema", "Foco"],
             [["1", "Fundamentos, nivelamento e panorama", "Todo mundo junto. Base comum"],
              ["2", "IA Generativa", "LLM por dentro, prompt e limites"],
              ["3", "Análise de Dados com SQL", "Consultar e extrair. A base de toda análise"],
              ["4", "Análise de Dados com Python", "Manipular e visualizar. Storytelling com dados"],
              ["5 · hoje", "Engenharia de Dados", "Construir os pipelines. Dado limpo, no lugar certo"],
              ["6", "Machine Learning", "Prever com dados. Do baseline ao modelo"],
              ["7", "Agentes de IA", "Da resposta à ação. IA que executa tarefas"],
              ["8", "Apresentação final", "Demo Day. Solução completa, do problema ao resultado"]],
             subtitle="Semana 5 de 8. Antes de prever ou automatizar, o dado precisa chegar limpo.",
             widths=[0.12, 0.38, 0.50])
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Onde vocês estão. Semana 3 foi consultar dado que já estava pronto, num banco. Semana
4 foi manipular esse mesmo dado pronto, em pandas. Hoje a pergunta muda: como esse dado
chegou pronto, para começo de conversa?"
""")

s = sl_pipeline("O pipeline revisitado", "As mesmas 8 fases da Aula 1, agora com outros olhos",
                [(1, "Entender o problema", "Semana 1. Transformar um pedido vago em pergunta analítica."),
                 (2, "Conseguir os dados", "HOJE. De onde vêm, e como chegam até quem analisa."),
                 (3, "Explorar", "Semanas 3 e 4, com SQL e Python. Vocês já fizeram esta parte."),
                 (4, "Preparar", "HOJE. Limpar, validar e organizar antes de qualquer análise valer a pena."),
                 (5, "Construir a solução", "Mais adiante no programa, com Machine Learning."),
                 (6, "Avaliar", "Mais adiante no programa."),
                 (7, "Colocar no ar", "Mais adiante no programa, com agentes de IA."),
                 (8, "Monitorar", "Mais adiante no programa.")],
                subtitle="Duas fases inteiras da Aula 1 ficaram em aberto até hoje. São elas.")
notes(s, "7 min", "ESSENCIAL", EU,
      """
"Lembram deste desenho, lá da Aula 1? As oito fases de qualquer solução de dados e IA.

Vocês já viveram a fase 1, entender o problema, na semana 1. E já viveram bastante a
fase 3, explorar, com SQL na semana 3 e Python na semana 4.

Mas reparem: as fases 2 e 4, conseguir os dados e preparar, ficaram soltas. Ninguém
explicou ainda de onde vem o CSV que vocês sempre receberam pronto, nem quem garantiu
que aquele dado estava limpo antes de chegar em vocês.

É exatamente isso que a aula de hoje fecha. Engenharia de dados, resumida de um jeito
simples, é o nome para as fases 2 e 4 desse desenho."
""")

s = sl_bullets("Por que hoje importa", "O trabalho que ninguém vê, mas que sustenta tudo",
               [("Todo exemplo que vocês usaram até aqui já chegou pronto", "alguém decidiu de onde vinha o dado, e alguém limpou ele antes"),
                ("Sem esse trabalho, SQL e pandas não têm em cima do que rodar", "nenhuma ferramenta ajuda com dado que não existe ou que está errado"),
                ("É o trabalho que mais consome tempo num projeto real", "a maior parte do esforço de um projeto de dados está aqui, não no modelo"),
                ("E é o trabalho mais invisível quando dá certo", "ninguém elogia um pipeline que nunca quebrou")],
               subtitle="Hoje é sobre o que acontece antes de qualquer coisa interessante aparecer na tela.")
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Por que dedicar uma noite inteira a isso. Quatro razões.

Todo exemplo que vocês usaram até aqui, o CSV da Aula 6, a base da Aula 8, já chegou
pronto. Alguém decidiu de onde vinha, e alguém limpou antes de vocês verem.

Sem esse trabalho, SQL e pandas não têm em cima do que rodar. Nenhuma ferramenta
ajuda com dado que não existe, ou que está errado.

É também o trabalho que mais consome tempo num projeto real. Quem já ouviu que
oitenta por cento do trabalho de um projeto de dados é limpeza, essa conta vem daqui.

E é o trabalho mais invisível quando dá certo. Ninguém elogia um pipeline que nunca
quebrou, só repara quando quebra."
""")

s = sl_cards("O plano de hoje", "Sete blocos, sempre voltando ao mesmo caso de fraude",
             [("De onde vêm os dados",
               "Fontes comuns, e a diferença entre lote e fluxo.\n\n25 minutos"),
              ("Onde os dados moram",
               "Banco transacional, Data Warehouse, Data Lake.\n\n30 minutos"),
              ("ETL x ELT",
               "A ordem importa, e tem uma rivalidade histórica por trás.\n\n30 minutos"),
              ("Qualidade de dados",
               "Por que dado sujo é o problema número um.\n\n25 minutos"),
              ("Pipeline de verdade",
               "DAG, Airflow e dbt.\n\n30 minutos"),
              ("Processamento distribuído",
               "Spark, Databricks, e o que fazer quando uma máquina não basta.\n\n40 minutos"),
              ("Do problema ao pipeline",
               "O caso de fraude, do início ao fim.\n\n15 minutos")],
             subtitle="Com intervalo no meio. Bastante conteúdo hoje, de propósito.",
             cols=4, card_h=3.6)
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Sete blocos hoje, mais do que o normal, de propósito: engenharia de dados tem muita
coisa boa para conhecer, e preferimos trazer tudo e ajustar depois do que deixar
faltar.

De onde vêm os dados. Onde eles moram. ETL contra ELT, com uma briga histórica de
verdade no meio. Qualidade de dados. Pipeline de produção, com Airflow e dbt.
Processamento distribuído, com Spark e Databricks. E fechamos amarrando tudo no caso
de fraude em cartão que vocês já conhecem."
""")

# ==========================================================================
# BLOCO B: De onde vêm os dados (19h35 às 20h00)
# ==========================================================================
s = sl_section("02", "De onde vêm os dados",
               "Fontes comuns, e a diferença entre lote e fluxo",
               "19h35 às 20h00  ·  25 minutos")
notes(s, "19h35 às 20h00 (25 min)", "ESSENCIAL", EU,
      """
Bloco de vocabulário e panorama. Objetivo: nomear as fontes de dados mais comuns, e
entender a diferença entre lote e fluxo com exemplo concreto de cada.

ESTRUTURA:
  Fontes comuns de dados     6 min
  Lote x fluxo                 6 min
  Exemplos do dia a dia          6 min
  Interação                       5 min
""")

s = sl_cards("Fontes comuns de dados", "De onde o dado bruto normalmente vem",
             [("Banco transacional",
               "O sistema que atende o cliente na hora, tipo o banco por trás de uma compra no cartão.\n\nVocês já consultaram um desses com SQL."),
              ("API",
               "Outro sistema entrega o dado sob pedido, um pouco de cada vez.\n\nO mesmo conceito de endpoint da Aula 4."),
              ("Arquivo",
               "Planilha, CSV, exportação manual de outro sistema.\n\nO jeito mais simples de existir, e o mais comum em empresa pequena."),
              ("Evento",
               "Um registro de algo que aconteceu agora, tipo um clique ou um login.\n\nChega um de cada vez, sem esperar formar lote.")],
             subtitle="Quase todo pipeline do mundo real combina mais de uma dessas quatro.",
             cols=4, card_h=3.4)
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Quatro fontes que aparecem o tempo todo. Banco transacional, o sistema que atende o
cliente na hora, o mesmo tipo de banco que vocês já consultaram com SQL.

API, outro sistema entregando dado sob pedido, o mesmo conceito de endpoint da Aula 4.

Arquivo, planilha ou CSV, o jeito mais simples de existir.

E evento, um registro de algo que aconteceu agora, chegando um de cada vez.

Quase todo pipeline real combina mais de uma dessas quatro ao mesmo tempo."
""")

s = sl_two_col("Duas formas de processar", "Lote (batch) contra fluxo (streaming)",
               "PROCESSAMENTO EM LOTE",
               ["Processa um bloco de dados de uma vez",
                "Roda de hora em hora, ou uma vez por dia",
                "Mais simples de construir e de manter",
                "Aceita atraso de minutos ou horas sem problema"],
               "PROCESSAMENTO EM FLUXO",
               ["Processa cada evento assim que ele chega",
                "Roda o tempo todo, sem pausa",
                "Mais complexo e mais caro de manter",
                "Só compensa quando o atraso realmente importa"],
               subtitle="A maioria dos pipelines do mundo real é em lote. Fluxo continua sendo a exceção.")
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Duas formas de processar o mesmo dado. Lote processa um bloco de uma vez, de hora em
hora ou uma vez por dia. Mais simples de construir, aceita atraso de minutos ou horas
sem problema nenhum.

Fluxo processa cada evento assim que ele chega, rodando o tempo todo, sem pausa. Mais
complexo, mais caro de manter, e só compensa quando o atraso realmente importa.

E aqui vai uma verdade que surpreende: a maioria dos pipelines do mundo real é em
lote. Fluxo chama mais atenção, mas continua sendo a exceção."
""")

s = sl_bullets("Exemplos do dia a dia", "A mesma pergunta, aplicada a situações reais",
               [("Extrato bancário fechado à noite", "processamento em lote, ninguém precisa ver o saldo mudar no segundo exato"),
                ("Alerta de fraude no cartão, na hora da compra", "processamento em fluxo, atraso de minutos já é tarde demais"),
                ("Relatório de vendas do mês", "lote, roda uma vez, no início do mês seguinte"),
                ("Painel de estoque de um marketplace", "fluxo, o estoque muda a cada venda em qualquer lugar do site")],
               subtitle="A pergunta certa é sempre o que a decisão de negócio realmente exige.")
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Quatro situações reais. Extrato bancário fechado à noite: lote, ninguém precisa ver o
saldo mudar no segundo exato.

Alerta de fraude no cartão, na hora da compra: fluxo, porque atraso de minutos já é
tarde demais, o dinheiro já saiu.

Relatório de vendas do mês: lote, roda uma vez, no início do mês seguinte.

Painel de estoque de um marketplace: fluxo, o estoque muda a cada venda em qualquer
lugar do site, o tempo todo.

A pergunta certa é sempre a mesma: o que a decisão de negócio realmente exige."
""")

s = sl_interaction("Interação", "Lote ou fluxo",
                   "Um hospital quer saber, em tempo real, quando um paciente internado tem um sinal vital fora da faixa segura. Qual dos dois serve aqui?",
                   ["A: processamento em lote, uma vez por dia",
                    "B: processamento em fluxo, a cada leitura do monitor",
                    "C: tanto faz, o resultado final é o mesmo",
                    "Responda na enquete, 30 segundos"])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Testando o que a gente acabou de ver. Um hospital quer saber, em tempo real, quando
um paciente internado tem um sinal vital fora da faixa segura. Qual dos dois serve
aqui?"

[aguarde 30 segundos]

Resposta: B. Aqui o atraso custa vida, é exatamente o caso em que fluxo compensa o
custo extra de manter. C está errado: o resultado final muda bastante, um paciente em
risco às vezes só apareceria no relatório do dia seguinte.
""")

# ==========================================================================
# BLOCO C: Onde os dados moram (20h00 às 20h30)
# ==========================================================================
s = sl_section("03", "Onde os dados moram",
               "Banco transacional, Data Warehouse e Data Lake",
               "20h00 às 20h30  ·  30 minutos")
notes(s, "20h00 às 20h30 (30 min)", "ESSENCIAL", EU,
      """
Bloco de armazenamento. Objetivo: explicar por que uma empresa madura usa mais de um
tipo de banco ao mesmo tempo, cada um para um trabalho diferente.

ESTRUTURA:
  Banco transacional (OLTP)   5 min
  Data Warehouse (OLAP)         6 min
  Data Lake                       6 min
  Os três lado a lado               6 min
  Bônus: Data Lakehouse               4 min
  Transição                             3 min
""")

s = sl_bullets("Banco transacional (OLTP)", "O banco que vocês já conhecem",
               [("OLTP: Online Transaction Processing", "o banco que atende UMA operação de cada vez, rápido"),
                ("Vocês já usaram um desses", "toda consulta das Aulas 5 e 6 rodou num banco deste tipo"),
                ("Bom para escrever e ler pouco dado por vez", "ruim para somar milhões de linhas de uma vez só"),
                ("Não foi desenhado para análise", "foi desenhado para o sistema não travar enquanto vende")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Primeiro tipo, o que vocês já conhecem. OLTP, Online Transaction Processing: o banco
que atende uma operação de cada vez, rápido. Toda consulta que vocês fizeram nas Aulas
5 e 6 rodou num banco deste tipo.

Ele é bom para escrever e ler pouco dado por vez, e ruim para somar milhões de linhas
de uma vez só. Isso vem de uma escolha de projeto: ele foi desenhado para o sistema
não travar enquanto vende. Análise fica para outra ferramenta, mais à frente."
""")

s = sl_bullets("Data Warehouse (OLAP)", "O banco desenhado para somar e cruzar",
               [("OLAP: Online Analytical Processing", "banco desenhado para somar, agrupar e cruzar muito dado de uma vez"),
                ("Os dados chegam de vários bancos transacionais diferentes", "um warehouse junta a empresa inteira num lugar só"),
                ("Fica lento para escrever um registro de cada vez", "e é exatamente por isso que ele não serve de banco do sistema"),
                ("Exemplos reais", "BigQuery, Snowflake, Redshift")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Segundo tipo. OLAP, Online Analytical Processing: banco desenhado para somar, agrupar
e cruzar muito dado de uma vez, exatamente o oposto do OLTP.

Os dados chegam de vários bancos transacionais diferentes, e um warehouse junta a
empresa inteira num lugar só, pronto para pergunta grande.

Ele fica lento para escrever um registro de cada vez, e é por isso que nenhum sistema
usa ele como banco principal. Os nomes que mais aparecem no mercado hoje são BigQuery,
Snowflake e Redshift."
""")

s = sl_bullets("Data Lake", "Guarda tudo, sem decidir a estrutura antes",
               [("Guarda o dado bruto, do jeito que ele chegou", "estruturado, semiestruturado ou nem isso, tipo imagem ou log"),
                ("Schema on read, não schema on write", "você decide a estrutura na hora de ler, não na hora de guardar"),
                ("Armazenamento bem mais barato que um banco tradicional", "o custo de guardar tudo cai bastante"),
                ("O risco: virar um \"pântano de dados\"", "sem organização, ninguém acha nada lá dentro")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Terceiro tipo, o mais diferente dos dois primeiros. Data Lake guarda o dado bruto, do
jeito que ele chegou: estruturado, semiestruturado, ou nem isso, tipo imagem ou log de
sistema.

A frase que resume ele: schema on read, não schema on write. Você decide a estrutura
na hora de LER, não na hora de guardar. Isso dá flexibilidade, e o armazenamento fica
bem mais barato que um banco tradicional.

O risco mora no mesmo lugar da vantagem: sem organização, um data lake vira o que o
mercado chama de pântano de dados, um monte de arquivo que ninguém mais acha."
""")

s = sl_table("Os três lado a lado", "A mesma pergunta, três respostas diferentes",
             ["", "Banco transacional", "Data Warehouse", "Data Lake"],
             [["Serve para", "Operar o sistema", "Analisar a empresa inteira", "Guardar tudo, bruto"],
              ["Estrutura", "Rígida, definida antes", "Rígida, definida antes", "Livre, decide depois"],
              ["Escrita", "Muito rápida, um registro por vez", "Lenta para um registro só", "Rápida, aceita qualquer formato"],
              ["Custo de guardar", "Alto", "Alto", "Baixo"],
              ["Exemplo real", "O banco por trás de uma compra", "BigQuery, Snowflake, Redshift", "Amazon S3, Google Cloud Storage"]],
             subtitle="Uma empresa madura normalmente usa os três ao mesmo tempo, cada um para um trabalho.",
             widths=[0.18, 0.27, 0.28, 0.27])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Os três lado a lado. Reparem que não existe um vencedor: cada linha desta tabela é
uma escolha de projeto diferente, não um ranking.

Uma empresa madura normalmente usa os três ao mesmo tempo. O banco transacional vende.
O data lake guarda tudo, bruto, barato. E o warehouse organiza o que interessa para
quem analisa. Cada um faz o trabalho que o outro faz mal."
""")

s = sl_bullets("Bônus: Data Lakehouse", "Uma ideia recente, juntando os dois últimos",
               [("A ideia central: juntar os dois", "armazenamento barato do lake, com a organização e a velocidade de consulta do warehouse"),
                ("Popularizado pela Databricks", "por volta de 2020, como resposta ao problema do pântano de dados")],
               subtitle="Guardem o nome Databricks. A história completa por trás dele vem mais à frente hoje.")
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Um bônus rápido antes de seguir. Data Lakehouse é a ideia de juntar os dois últimos:
armazenamento barato de um lake, com a organização e a velocidade de consulta de um
warehouse.

Foi popularizado pela Databricks, por volta de 2020, como resposta direta ao problema
do pântano de dados que acabamos de falar. Guardem esse nome: a história completa por
trás da Databricks, e do motor que ela comercializa, tem um bloco inteiro reservado
mais à frente hoje."
""")

# ==========================================================================
# BLOCO D: ETL x ELT (20h30 às 21h00)
# ==========================================================================
s = sl_section("04", "ETL x ELT",
               "A ordem importa, e tem uma rivalidade histórica por trás",
               "20h30 às 21h00  ·  30 minutos")
notes(s, "20h30 às 21h00 (30 min)", "ESSENCIAL", EU,
      """
Bloco de transformação. Objetivo: entender a diferença entre ETL e ELT, e por que a
escolha entre os dois já foi motivo de disputa séria no mercado de dados.

ESTRUTURA:
  O que é ETL              6 min
  O que é ELT                 6 min
  A rivalidade Inmon x Kimball  8 min
  ETL x ELT lado a lado           6 min
  Interação                         4 min
""")

s = sl_bullets("O que é ETL", "Extract, Transform, Load",
               [("Extrai o dado da fonte, transforma FORA do destino, carrega já pronto", "a ordem das três letras é literal"),
                ("Nasceu numa época em que processar e guardar dado era caro", "por isso a transformação acontecia antes de ocupar espaço no banco final"),
                ("A transformação roda numa ferramenta separada", "fora do banco de destino, antes de qualquer coisa chegar lá"),
                ("Ainda é o padrão em muita empresa grande e mais antiga", "principalmente onde o warehouse roda fora da nuvem")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"ETL: Extract, Transform, Load. A ordem das três letras é literal. Extrai o dado da
fonte, transforma FORA do destino, e só carrega o que já está pronto.

Isso nasceu numa época em que processar e guardar dado era caro de verdade, então a
transformação acontecia antes, para não gastar espaço caro com dado bruto e
desorganizado.

A transformação roda numa ferramenta separada, fora do banco de destino. E ainda é o
padrão em muita empresa grande e mais antiga, principalmente onde o warehouse roda
fora da nuvem."
""")

s = sl_bullets("O que é ELT", "Extract, Load, Transform, e por que virou popular",
               [("Extrai, carrega o dado bruto direto no destino, transforma DEPOIS, lá dentro", "as mesmas três letras, ordem diferente"),
                ("Só ficou viável com data warehouse em nuvem", "guardar e processar dado bruto ficou barato o suficiente para não precisar economizar antes"),
                ("A transformação roda em SQL, dentro do próprio warehouse", "usando o poder de processamento que já está pago"),
                ("É o modelo por trás do dbt", "que volta no bloco de pipeline, mais à frente")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"ELT: Extract, Load, Transform. As mesmas três letras do ETL, ordem diferente. Extrai,
carrega o dado bruto direto no destino, e transforma DEPOIS, já lá dentro.

Isso só ficou viável com data warehouse em nuvem. Guardar e processar dado bruto ficou
barato o suficiente para não precisar economizar espaço antes de carregar.

A transformação roda em SQL, dentro do próprio warehouse, usando o poder de
processamento que a empresa já está pagando de qualquer jeito. E é exatamente o modelo
por trás do dbt, que a gente reencontra no bloco de pipeline."
""")

s = sl_timeline("A rivalidade Inmon x Kimball", "Duas visões sobre como construir um Data Warehouse",
                [("1992", "Bill Inmon publica \"Building the Data Warehouse\", defendendo um warehouse único e central para a empresa inteira, de cima para baixo"),
                 ("1996", "Ralph Kimball publica \"The Data Warehouse Toolkit\", defendendo construir por área de negócio, de baixo para cima, com modelagem dimensional"),
                 ("Anos 2000", "As duas escolas dividem o mercado, e cada consultoria de dados escolhe um lado"),
                 ("Anos 2010", "A nuvem barateia processamento, e o ELT tira parte da urgência da discussão"),
                 ("Hoje", "As duas ideias convivem, misturadas, muitas vezes dentro da mesma empresa")],
                subtitle="Duas visões, a mesma pergunta: construir de cima para baixo, ou de baixo para cima?")
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Uma história real, e ainda hoje citada em entrevista de emprego da área.

1992, Bill Inmon publica um livro chamado Building the Data Warehouse, defendendo um
warehouse único e central para a empresa inteira, construído de cima para baixo,
começando pelo modelo geral.

1996, Ralph Kimball publica The Data Warehouse Toolkit, defendendo o oposto: construir
por área de negócio, de baixo para cima, com um jeito de organizar tabela chamado
modelagem dimensional.

Nos anos 2000, as duas escolas dividem o mercado inteiro, e cada consultoria de dados
escolhe um lado, quase como time de futebol.

Nos anos 2010, a nuvem barateia processamento, e o ELT tira parte da urgência dessa
discussão: fica mais barato experimentar dos dois jeitos.

E hoje, as duas ideias convivem, muitas vezes dentro da mesma empresa. Ninguém venceu
de verdade, as duas viraram ferramenta do dia a dia."
""",
      "Se aparecer pergunta de entrevista sobre 'star schema' ou 'modelagem dimensional', a origem é o livro do Kimball de 1996.")

s = sl_two_col("ETL x ELT lado a lado", "A mesma sigla embaralhada, duas filosofias",
               "ETL",
               ["Transforma antes de carregar",
                "Mais comum em warehouse fora da nuvem",
                "Ferramenta de transformação separada do banco",
                "Bom quando processar é caro"],
               "ELT",
               ["Transforma depois de carregar, dentro do banco",
                "Mais comum em warehouse na nuvem",
                "Usa o próprio SQL do warehouse para transformar",
                "Bom quando armazenar e processar é barato"],
               subtitle="Na dúvida, hoje a resposta mais comum é ELT. Mas ETL não desapareceu.")
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Lado a lado, para fixar. ETL transforma antes de carregar, mais comum fora da nuvem,
com ferramenta separada, bom quando processar é caro.

ELT transforma depois, dentro do próprio banco, mais comum na nuvem, usando o SQL que
já está ali, bom quando armazenar e processar é barato.

Na dúvida, hoje a resposta mais comum do mercado é ELT. Mas ETL não desapareceu, ainda
é a escolha certa em muito contexto."
""")

s = sl_interaction("Interação", "ETL ou ELT",
                   "Uma empresa pequena usa um warehouse na nuvem, paga só pelo que processa, e quer testar formatos diferentes de transformação sem compromisso. Qual caminho combina mais com essa realidade?",
                   ["A: ETL, transformar tudo antes de carregar",
                    "B: ELT, carregar bruto e transformar depois, dentro do warehouse",
                    "C: os dois custam exatamente igual aqui",
                    "Responda na enquete, 30 segundos"])
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Testando o bloco. Uma empresa pequena usa warehouse na nuvem, paga só pelo que
processa, e quer testar formatos diferentes de transformação sem compromisso. Qual
caminho combina mais?"

[aguarde 30 segundos]

Resposta: B. Carregar bruto primeiro dá liberdade para testar transformação diferente
sem repetir a extração, e o custo de guardar e processar na nuvem já é baixo. C está
errado, o custo muda bastante dependendo de quando o processamento pesado acontece.
""")

# ==========================================================================
# BLOCO E: Qualidade de dados (21h15 às 21h40)
# ==========================================================================
s = sl_section("05", "Qualidade de dados",
               "Por que dado sujo é o problema número um",
               "21h15 às 21h40  ·  25 minutos")
notes(s, "21h15 às 21h40 (25 min)", "ESSENCIAL", EU,
      """
Primeiro bloco depois do intervalo. Objetivo: dar nome técnico a um problema que a
turma já sentiu na prática, sem saber que tinha nome.

ESTRUTURA:
  Por que é o problema número um   5 min
  Quatro dimensões de qualidade      6 min
  A ponte com o que já viram           6 min
  Testes de dados                        6 min
  Transição                                2 min
""")

s = sl_bullets("Por que dado sujo é o problema número um", "O erro mais caro é o que ninguém viu chegar",
               [("Todo o resto do pipeline depende da qualidade do que entra primeiro", "modelo bom com dado ruim continua dando resposta ruim"),
                ("O custo de um erro cresce quanto mais tarde ele é descoberto", "achar um erro na fonte é barato, achar no relatório do diretor é caro"),
                ("Não existe pipeline sem erro nenhum", "existe pipeline que detecta o erro antes que ele vire decisão errada")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Depois do intervalo, o problema que mais gasta tempo de quem trabalha com dado de
verdade.

Todo o resto do pipeline depende da qualidade do que entra primeiro. Modelo bom com
dado ruim continua dando resposta ruim, sem exceção.

E o custo de um erro cresce quanto mais tarde ele é descoberto. Achar um erro na
fonte custa uma correção pequena. Achar o mesmo erro dentro do relatório que já foi
para o diretor custa reputação.

A meta nunca é zero erro, isso não existe. A meta é um pipeline que detecta o erro
antes que ele vire decisão errada de alguém."
""")

s = sl_bullets("Quatro dimensões de qualidade", "As perguntas que todo pipeline deveria se fazer",
               [("Completude", "falta algum dado que deveria estar ali?"),
                ("Consistência", "o mesmo dado aparece igual em lugares diferentes?"),
                ("Duplicidade", "a mesma linha está contada mais de uma vez?"),
                ("Validade de schema", "o tipo e o formato de cada coluna são o que deveriam ser?")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Quatro perguntas que resumem qualidade de dado, e valem para qualquer pipeline do
mundo.

Completude: falta algum dado que deveria estar ali? Consistência: o mesmo dado aparece
igual em lugares diferentes, ou um sistema chama de uma forma e outro de outra?

Duplicidade: a mesma linha está contada mais de uma vez, inflando uma soma?

E validade de schema: o tipo e o formato de cada coluna são realmente o que deveriam
ser?"
""")

s = sl_bullets("A ponte com o que vocês já viram", "Vocês já praticavam isso, só sem o nome",
               [("NULL, na Aula 5", "SQL já tratava valor ausente como um problema de completude, sem chamar assim"),
                ("NaN, na Aula 7", "pandas fazia exatamente a mesma pergunta, com outro nome"),
                ("dtype errado, também na Aula 7", "número que virou texto é, na prática, um problema de validade de schema"),
                ("Faltava só um nome", "para organizar ideias que vocês já tinham praticado")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"E aqui a notícia boa: vocês já praticavam qualidade de dado, só sem esse nome.

NULL, na Aula 5, já era SQL tratando valor ausente como um problema de completude.
NaN, na Aula 7, era pandas fazendo exatamente a mesma pergunta, com outro símbolo.

E dtype errado, também na Aula 7, é na prática um problema de validade de schema:
número que virou texto porque uma célula do arquivo original veio fora do padrão.

Faltava só um nome para organizar ideias que vocês já tinham na mão."
""")

s = sl_bullets("Testes de dados", "A mesma lógica de teste de software, aplicada ao dado",
               [("Em vez de testar código, testa se o dado continua no formato esperado", "a mesma disciplina, outro alvo"),
                ("Exemplos de teste comuns", "coluna nunca vazia, valor sempre positivo, chave sempre única"),
                ("Ferramentas que fazem isso na prática", "dbt tests e Great Expectations são as mais citadas hoje"),
                ("O objetivo não muda", "quebrar o pipeline antes do dado ruim chegar em alguém que decide algo com ele")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"E se qualidade é importante, tem que ter jeito de checar automaticamente, não só
olhando na mão. É para isso que existem os testes de dados: a mesma lógica de teste de
software, aplicada ao dado.

Exemplos comuns: essa coluna nunca pode estar vazia, esse valor sempre tem que ser
positivo, essa chave nunca pode se repetir.

As ferramentas mais citadas hoje são dbt tests e Great Expectations, e o dbt volta no
próximo bloco.

O objetivo nunca muda: quebrar o pipeline antes do dado ruim chegar em alguém que vai
tomar uma decisão real com ele."
""")

# ==========================================================================
# BLOCO F: Pipeline de verdade (21h40 às 22h10)
# ==========================================================================
s = sl_section("06", "Pipeline de verdade",
               "DAG, Airflow e dbt",
               "21h40 às 22h10  ·  30 minutos")
notes(s, "21h40 às 22h10 (30 min)", "ESSENCIAL", EU,
      """
Bloco de orquestração. Objetivo: mostrar o que separa um script solto de um pipeline
de produção, e nomear as duas ferramentas mais citadas do mercado hoje.

ESTRUTURA:
  Script x pipeline de produção   6 min
  DAG                                6 min
  Airflow                              6 min
  dbt e a engenharia analítica           6 min
  Interação                                4 min
""")

s = sl_bullets("O que separa script de pipeline de produção", "O que conta mora em volta do código",
               [("Um script roda quando alguém lembra de rodar ele", "um pipeline roda sozinho, no horário certo"),
                ("Um script quebra em silêncio", "um pipeline de produção avisa alguém quando quebra"),
                ("Um script não sabe o que já rodou", "um pipeline sabe a ordem certa, e o que depende do quê"),
                ("A diferença mora no que cerca o código", "agendamento, aviso de erro, ordem de dependência")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Vocês já escreveram script antes, mesmo sem saber. A pergunta de hoje é: o que
transforma um script solto num pipeline de produção de verdade?

Um script roda quando alguém lembra de rodar ele. Um pipeline roda sozinho, no horário
certo, todo dia, sem ninguém precisar lembrar.

Um script quebra em silêncio, ninguém fica sabendo até reclamarem. Um pipeline de
produção avisa alguém quando quebra.

E um script não sabe o que já rodou antes dele. Um pipeline sabe a ordem certa, e o
que depende do quê.

A diferença mora no que cerca o código, no agendamento, no aviso de erro, na ordem
de dependência entre as tarefas."
""")

s = sl_bullets("DAG: o mapa de dependências", "A sigla que aparece em toda ferramenta de pipeline",
               [("DAG: grafo acíclico dirigido", "um jeito de desenhar quais tarefas dependem de quais, sem formar um ciclo"),
                ("\"Sem ciclo\" quer dizer isto", "a tarefa B nunca pode depender da tarefa A, se A já depende de B"),
                ("Cada seta do desenho é uma regra", "isso só roda depois daquilo terminar"),
                ("É assim que a ferramenta de orquestração sabe a ordem certa", "sem alguém decidir manualmente todo dia")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"DAG: grafo acíclico dirigido. Parece complicado, a ideia é simples: um jeito de
desenhar quais tarefas dependem de quais, sem formar um ciclo.

'Sem ciclo' quer dizer isto: a tarefa B nunca pode depender da tarefa A, se A já
depende de B. Senão nenhuma das duas nunca começaria.

Cada seta do desenho é uma regra: isso só roda depois daquilo terminar. E é assim que
a ferramenta de orquestração sabe a ordem certa, sem alguém decidir manualmente todo
santo dia."
""")

s = sl_bullets("Airflow", "Nasceu porque script solto não dava mais conta",
               [("Maxime Beauchemin criou o Airflow em 2014", "trabalhando no time de dados do Airbnb, que crescia rápido demais para script solto dar conta"),
                ("Cada pipeline vira um DAG, escrito em Python", "o mesmo Python que vocês já usam"),
                ("Hoje é um projeto da Apache Software Foundation", "um dos orquestradores mais usados do mundo"),
                ("Não é a única opção", "Dagster e Prefect são alternativas mais recentes, com a mesma ideia central")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"A ferramenta de orquestração mais citada do mercado. Maxime Beauchemin criou o
Airflow em 2014, trabalhando no time de dados do Airbnb, numa época em que a empresa
crescia rápido demais para script solto continuar dando conta.

Cada pipeline vira um DAG, escrito em Python, o mesmo Python que vocês já usam desde a
Aula 7.

Hoje é um projeto da Apache Software Foundation, um dos orquestradores mais usados do
mundo. E não é a única opção: Dagster e Prefect são alternativas mais recentes, com a
mesma ideia central por trás."
""")

s = sl_bullets("dbt e a engenharia analítica", "SQL tratado como se fosse software",
               [("dbt nasceu por volta de 2016", "criado pela equipe que depois virou a dbt Labs"),
                ("A ideia central: tratar SQL como se fosse software", "com versionamento, teste automático e documentação"),
                ("Deu nome a uma função nova no mercado: engenheiro analítico", "entre quem só escreve SQL solto e quem constrói pipeline inteiro"),
                ("Roda direto dentro do warehouse", "o exemplo mais claro de ELT na prática, do bloco anterior")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"E fechando com a ferramenta que já apareceu duas vezes hoje, sem apresentação
completa. dbt nasceu por volta de 2016, criado pela equipe que depois virou a dbt
Labs.

A ideia central: tratar SQL como se fosse software de verdade, com versionamento,
teste automático e documentação, não mais um arquivo solto que só uma pessoa entende.

Isso deu nome a uma função nova no mercado, engenheiro analítico, alguém entre quem só
escreve SQL solto e quem constrói pipeline inteiro do zero.

E ele roda direto dentro do warehouse, usando SQL puro. É o exemplo mais claro de ELT
na prática, do bloco de agora há pouco."
""")

s = sl_interaction("Interação", "O que falta aqui",
                   "Um time roda um script Python toda sexta-feira, na mão, para atualizar um relatório. Ninguém sabe quando o script quebra, e às vezes esquecem de rodar. O que mais falta para virar um pipeline de verdade?",
                   ["A: trocar Python por outra linguagem",
                    "B: agendamento automático e aviso quando quebra",
                    "C: nada, já é um pipeline",
                    "Responda na enquete, 30 segundos"])
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Última pergunta antes do fechamento. Um time roda um script Python toda sexta-feira,
na mão, para atualizar um relatório. Ninguém sabe quando o script quebra, e às vezes
esquecem de rodar. O que falta para virar pipeline de verdade?"

[aguarde 30 segundos]

Resposta: B. A linguagem nunca foi o problema, do slide de script contra pipeline.
Falta rodar sozinho no horário certo, e avisar alguém quando quebra. C está errado,
isso ainda é exatamente o script solto que descrevemos.
""")

# ==========================================================================
# BLOCO G: Processamento distribuído (22h10 às 22h50)
# ==========================================================================
s = sl_section("07", "Processamento distribuído",
               "Spark, Databricks, e o que acontece quando uma máquina não basta",
               "22h10 às 22h50  ·  40 minutos")
notes(s, "22h10 às 22h50 (40 min)", "ESSENCIAL", EU,
      """
Bloco de aprofundamento, por pedido explícito do usuário depois da primeira versão da
aula: o conceito de processamento distribuído, e a história de Spark e Databricks.

ESTRUTURA:
  Por que processamento distribuído existe   6 min
  MapReduce, a ideia que começou tudo          6 min
  Spark, a mesma ideia na memória                6 min
  Um exemplo: pandas e Spark lado a lado           6 min
  Databricks                                         6 min
  Onde cada peça se encaixa                            5 min
  Interação                                              4 min
""")

s = sl_bullets("Processamento distribuído", "O problema que nenhuma máquina sozinha resolve",
               [("Toda conta até aqui rodou numa máquina só", "um notebook, um banco, um warehouse, tudo processando numa CPU de cada vez"),
                ("Em algum volume, uma máquina só não dá mais conta", "existe um teto, não importa quão potente ela seja"),
                ("A solução: dividir o trabalho entre várias máquinas ao mesmo tempo", "cada uma processa um pedaço, e os resultados se juntam no final"),
                ("Isso tem nome: processamento distribuído", "o princípio por trás de todo sistema que lida com volume realmente grande")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Último conceito grande da noite, e um dos mais citados em vaga de dados. Toda conta
que vocês viram até aqui hoje, e em toda a aula de pandas, rodou numa máquina só: um
notebook, um banco, um warehouse, processando numa CPU de cada vez.

Em algum volume, uma máquina só não dá mais conta. Não importa quão potente ela seja,
existe um teto de memória e de processamento.

A solução é dividir o trabalho entre várias máquinas ao mesmo tempo, cada uma
processando um pedaço, com os resultados se juntando no final. Isso tem nome:
processamento distribuído."
""")

s = sl_bullets("MapReduce, a ideia que começou tudo", "De um paper do Google a um padrão do mercado",
               [("O Google publicou o paper do MapReduce em 2004", "descrevendo como eles processavam a escala da própria busca"),
                ("A ideia central: separar em duas etapas", "Map processa cada pedaço em paralelo, Reduce junta os resultados"),
                ("O Hadoop nasceu logo depois, como versão open source dessa ideia", "criado por Doug Cutting e Mike Cafarella, também em meados dos anos 2000"),
                ("O Hadoop dominou a década seguinte", "mas tinha um ponto fraco sério: escrevia resultado intermediário em disco o tempo todo")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"A história começa com um paper. Em 2004, o Google publicou o paper do MapReduce,
descrevendo como eles processavam a escala gigantesca da própria busca.

A ideia central é separar o trabalho em duas etapas. Map processa cada pedaço dos
dados em paralelo, em máquinas diferentes. Reduce junta os resultados parciais numa
resposta só.

O Hadoop nasceu logo depois, como versão open source dessa ideia, criado por Doug
Cutting e Mike Cafarella. E o Hadoop dominou a década seguinte inteira.

Mas tinha um ponto fraco sério: a cada etapa, ele escrevia o resultado intermediário
em disco, que é bem mais lento que memória. Isso ia deixando tudo mais devagar."
""")

s = sl_bullets("Spark: a mesma ideia, mas na memória", "A virada que tornou tudo mais rápido",
               [("Matei Zaharia criou o Spark em 2009", "durante o doutorado dele na UC Berkeley, no laboratório AMPLab"),
                ("A virada: processar em memória, não em disco", "isso tornou o Spark de 10 a 100 vezes mais rápido que o Hadoop MapReduce em muitos casos"),
                ("O DataFrame do Spark se parece muito com o do pandas", "mesma ideia de linhas e colunas, agora espalhada por várias máquinas"),
                ("Hoje é o motor de processamento distribuído mais usado do mercado", "praticamente todo Data Lake grande tem Spark rodando por trás")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Matei Zaharia criou o Spark em 2009, durante o doutorado dele na UC Berkeley, no
laboratório AMPLab.

A virada foi processar em memória, não em disco. Isso tornou o Spark de dez a cem
vezes mais rápido que o Hadoop MapReduce, dependendo do tipo de tarefa.

E aqui vai a boa notícia para vocês: o DataFrame do Spark se parece muito com o
DataFrame do pandas que vocês já sabem usar. Mesma ideia de linhas e colunas, agora
espalhada por várias máquinas ao mesmo tempo.

Hoje o Spark é o motor de processamento distribuído mais usado do mercado.
Praticamente todo Data Lake de porte grande tem Spark rodando por trás."
""")

s = sl_code("Processamento distribuído", "Um exemplo: pandas e Spark lado a lado",
            ["# pandas, numa máquina só",
             "transacoes.groupby(\"id_lojista\")[\"valor\"].sum()",
             "",
             "# PySpark, em várias máquinas ao mesmo tempo",
             "transacoes.groupBy(\"id_lojista\").sum(\"valor\")"],
            [("A sintaxe é quase igual, de propósito", "quem já sabe pandas reconhece a maior parte do PySpark de cara"),
             ("Por trás, o Spark divide a tabela entre várias máquinas", "cada uma agrupa e soma o próprio pedaço, e os resultados se juntam no final"),
             ("A diferença aparece só no volume", "1 milhão de linhas roda bem nos dois. Muitos bilhões só rodam de forma distribuída")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Um exemplo rápido, para fixar. Em cima, o mesmo groupby de pandas que vocês já usaram
hoje. Embaixo, a versão em PySpark, a biblioteca Python que fala com o Spark.

Reparem que a sintaxe é quase igual, de propósito: quem já sabe pandas reconhece a
maior parte do PySpark de cara.

Por trás, o Spark divide a tabela entre várias máquinas, cada uma agrupa e soma o
próprio pedaço, e os resultados se juntam no final, sem vocês precisarem escrever
nenhuma linha a mais para isso acontecer.

E a diferença entre usar um ou outro aparece só no volume. Um milhão de linhas, como o
banco de vocês da Aula 8, roda bem nos dois. Muitos bilhões de linhas só rodam de
forma distribuída."
""")

s = sl_bullets("Databricks", "A empresa que transformou o Spark em plataforma",
               [("Os criadores do Spark fundaram a Databricks em 2013", "incluindo o próprio Matei Zaharia"),
                ("A empresa transformou um projeto de pesquisa em plataforma comercial", "hospedagem, interface e integração prontas, em vez de instalar e configurar tudo na mão"),
                ("É a mesma empresa por trás do termo Data Lakehouse", "do bônus lá no bloco de armazenamento, agora com a história completa"),
                ("Hoje é uma das plataformas de dados mais usadas em empresa grande", "o Spark deixou de ser só um projeto de pesquisa")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"E fechando a linha do tempo: os criadores do Spark fundaram a Databricks em 2013,
incluindo o próprio Matei Zaharia.

A empresa pegou um projeto de pesquisa de universidade e transformou em plataforma
comercial: hospedagem, interface, integração pronta, em vez de cada empresa precisar
instalar e configurar tudo na mão.

E é a mesma empresa por trás do termo Data Lakehouse, do bônus lá no bloco de
armazenamento. Agora vocês têm a história completa: Databricks nasceu do Spark, e o
Lakehouse foi a resposta dela para juntar lake e warehouse numa coisa só.

Hoje é uma das plataformas de dados mais usadas dentro de empresa grande. O que
começou como projeto de doutorado virou parte do dia a dia do mercado."
""")

s = sl_table("Onde cada peça se encaixa", "As cinco ferramentas nomeadas hoje, juntas",
             ["Ferramenta", "Papel", "Origem"],
             [["Hadoop", "Processamento distribuído em disco, o pioneiro", "2006, baseado no paper do Google"],
              ["Spark", "Processamento distribuído em memória, o padrão de hoje", "2009, UC Berkeley"],
              ["Databricks", "Plataforma comercial construída em cima do Spark", "2013, os mesmos criadores"],
              ["Airflow", "Orquestra quando cada etapa roda", "2014, Airbnb"],
              ["dbt", "Transforma dado com SQL versionado", "2016, dbt Labs"]],
             subtitle="Cada uma resolve uma parte diferente do mesmo pipeline.",
             widths=[0.2, 0.5, 0.3])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Um resumo, juntando as cinco ferramentas que ganharam nome próprio hoje.

Hadoop processa de forma distribuída, em disco, foi o pioneiro. Spark faz a mesma
coisa em memória, e é o padrão de hoje. Databricks é a plataforma comercial construída
em cima do Spark. Airflow orquestra quando cada etapa roda. E dbt transforma dado com
SQL versionado.

Reparem que nenhuma delas faz o trabalho da outra. Cada uma resolve uma parte
diferente do mesmo pipeline, e é exatamente por isso que aparecem juntas com tanta
frequência numa vaga de emprego da área."
""")

s = sl_interaction("Interação", "Vale a pena distribuir",
                   "Você tem uma tabela de 50 mil linhas, que já processa em segundos no pandas de um notebook comum. Faz sentido migrar isso para Spark?",
                   ["A: Sim, Spark é sempre mais rápido, para qualquer volume",
                    "B: Não, o ganho de processar de forma distribuída só aparece em volume que uma máquina não aguenta",
                    "C: Só faz diferença se os dados estiverem na Databricks",
                    "Responda na enquete, 30 segundos"])
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Última pergunta antes do fechamento. Uma tabela de 50 mil linhas, que já processa em
segundos no pandas de um notebook comum. Faz sentido migrar para Spark?"

[aguarde 30 segundos]

Resposta: B. Distribuir tem custo de coordenação entre as máquinas, e esse custo só
compensa quando o volume realmente exige. Para 50 mil linhas, pandas sozinho já é mais
rápido, porque não perde tempo dividindo e juntando trabalho entre máquinas. C está
errado, a plataforma não é o que decide isso, o volume é.
""")

# ==========================================================================
# BLOCO H: Do problema ao pipeline (22h50 às 23h05)
# ==========================================================================
s = sl_section("08", "Do problema ao pipeline",
               "O caso de fraude em cartão, do início ao fim",
               "22h50 às 23h05  ·  15 minutos")
notes(s, "22h50 às 23h05 (15 min)", "ESSENCIAL", EU,
      """
Bloco de fechamento e amarração. Objetivo: mostrar, num desenho só, tudo que a aula de
hoje cobriu, aplicado ao caso que a turma já conhece de cor.
""")

s = sl_pipeline("Do problema ao pipeline", "O caso de fraude em cartão, do início ao fim",
                [(1, "Fonte", "A maquininha e o banco emissor geram o registro bruto de cada transação, no formato deles."),
                 (2, "Ingestão", "Um pipeline em lote traz essas transações a cada poucos minutos para dentro da empresa."),
                 (3, "Armazenamento", "O dado bruto entra num data lake primeiro. Só o que passa por transformação vira tabela no warehouse."),
                 (4, "Qualidade", "Testes automáticos conferem: id_transacao é único? valor é sempre positivo? data_hora tem um formato válido?"),
                 (5, "Transformação", "SQL dentro do warehouse organiza as 6 tabelas que vocês já conhecem: clientes, cartões, lojistas, transações, contestações."),
                 (6, "Consumo", "Só depois de tudo isso chega o que vocês fizeram nas Aulas 5 a 8: consultar, filtrar, agrupar, investigar.")],
                subtitle="As Aulas 5 a 8 inteiras aconteceram DEPOIS de tudo isso. Hoje vocês viram o antes.",
                per_row=3)
notes(s, "10 min", "ESSENCIAL", EU,
      """
"Fechando com um desenho só. O mesmo caso de fraude em cartão que vocês já conhecem de
cor, agora mostrando tudo o que acontece antes de chegar em vocês.

A fonte: a maquininha e o banco emissor geram o registro bruto, no formato deles, não
no formato bonito que vocês sempre receberam.

A ingestão: um pipeline em lote traz essas transações a cada poucos minutos.

O armazenamento: o dado bruto entra num data lake primeiro, e só o que passa por
transformação vira tabela dentro do warehouse.

A qualidade: testes automáticos conferem completude, duplicidade e validade antes de
qualquer coisa seguir adiante.

A transformação: SQL dentro do warehouse organiza as seis tabelas exatas que vocês já
conhecem.

E só então chega o consumo: tudo que vocês fizeram nas Aulas 5 a 8, consultar,
filtrar, agrupar, investigar.

Guardem esta frase: as Aulas 5 a 8 inteiras aconteceram DEPOIS de tudo isso. Hoje
vocês viram o antes."
""")

# ==========================================================================
# BLOCO I: Encerramento (23h05 às 23h20)
# ==========================================================================
s = sl_section("09", "Encerramento",
               "O que vocês levam de hoje e o que vem na semana 6",
               "23h05 às 23h20  ·  15 minutos")
notes(s, "23h05 às 23h20 (15 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Recapitulação            4 min
  O que vem pela frente    3 min
  Q&A                      6 min  (elástico, absorve atraso)
  Fechamento               2 min
""")

s = sl_bullets("Encerramento", "Seis ideias para levar de hoje",
               [("Engenharia de dados fecha as fases 2 e 4 do pipeline da Aula 1", "conseguir os dados, e prepará-los"),
                ("Lote é a regra, fluxo é a exceção que custa mais caro", "escolha pelo que a decisão de negócio realmente exige"),
                ("Banco transacional, warehouse e data lake resolvem problemas diferentes", "uma empresa madura normalmente usa os três juntos"),
                ("ETL e ELT são a mesma sigla embaralhada, por um motivo histórico real", "a nuvem mudou qual ordem costuma valer mais a pena"),
                ("Um pipeline de produção se prova pelo que existe em volta do código", "agendamento, aviso de erro, e ordem de dependência entre as tarefas"),
                ("Processamento distribuído só compensa acima de um certo volume", "Spark existe para o dia em que uma máquina não aguenta mais sozinha")],
               subtitle="Se você levar só essas seis frases, a noite cumpriu o objetivo.",
               numbered=True)
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Seis ideias para levar de hoje.

Engenharia de dados fecha as fases 2 e 4 do pipeline da Aula 1: conseguir os dados, e
prepará-los.

Lote é a regra, fluxo é a exceção que custa mais caro. Escolham pelo que a decisão de
negócio realmente exige.

Banco transacional, warehouse e data lake resolvem problemas diferentes, e uma empresa
madura normalmente usa os três juntos.

ETL e ELT são a mesma sigla embaralhada, por um motivo histórico real, e a nuvem mudou
qual ordem costuma valer mais a pena.

Um pipeline de produção se prova pelo que existe em volta do código, agendamento,
aviso de erro, ordem de dependência, não pelo código em si.

E a mais nova de hoje: processamento distribuído só compensa acima de um certo
volume. Spark existe para o dia em que uma máquina sozinha não aguenta mais, e é isso
que separa quem sabe o nome da ferramenta de quem sabe quando usar ela."
""")

s = sl_two_col("Próximos encontros", "O que vem pela frente",
               "SEGUNDA · Semana 6",
               ["Machine Learning",
                "Do baseline ao primeiro modelo",
                "Ainda conceitual, como toda segunda",
                "Prever com dados, não só descrever"],
               "QUINTA · Semana 5",
               ["Primeiro contato com pipeline de verdade",
                "Mesmo formato de hoje: demonstração curta e mão na massa",
                "Vale revisar os slides de hoje antes"],
               subtitle="A partir da semana 6, o foco muda de descrever o passado para prever o futuro.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"O que vem pela frente.

Na quinta desta semana, primeiro contato de verdade com pipeline, no mesmo formato de
sempre: demonstração curta, e o resto é prática.

E na segunda da semana 6, Machine Learning: do baseline ao primeiro modelo. Aí o foco
muda de descrever o passado para prever o futuro."
""")

s = sl_statement("Antes de ir", "Perguntas?",
                 "Escreva no chat. O que não der tempo, respondemos no Discord ainda hoje.")
notes(s, "6 min", "ESSENCIAL", EU,
      """
PERGUNTAS PREVISÍVEIS DE HOJE:

- "Preciso decorar Airflow e dbt para a prova?"
  Não. O que importa é reconhecer o nome e saber para que serve. Sintaxe fica para
  quem for atuar direto nisso.

- "Isso ajuda no projeto final?"
  Ajuda direto. Todo grupo vai precisar decidir de onde vem a base, e como garantir
  que ela chega limpa, mesmo em pequena escala.

- "Toda empresa tem essa estrutura inteira, warehouse, lake, pipeline agendado?"
  Não. Empresa pequena às vezes só tem um banco e um script. A estrutura completa
  aparece conforme o volume de dado cresce.

- "Perdi a Aula 7, consigo acompanhar a prática da Aula 10?"
  Fica mais difícil. Recomendamos revisar o roteiro e o notebook da Aula 7 antes.
""")

s = sl_closing()
notes(s, "2 min", "ESSENCIAL", EU,
      """
FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. Foi bastante conteúdo, de propósito: engenharia de
dados é o trabalho que ninguém vê, mas que sustenta tudo que vocês já fizeram até
aqui.

Revisem os slides antes da quinta, principalmente o desenho do caso de fraude do
fechamento. Nos vemos lá. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Anotar quais dos seis blocos geraram mais pergunta no chat, para calibrar onde
  cortar se a Aula 9 precisar ficar mais curta numa próxima turma.
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

out = ROOT / "docs" / "aula-09"
out.mkdir(parents=True, exist_ok=True)
dest = out / "AI-Talent-Academy-Aula09.pptx"
prs.save(dest)
print(f"OK: {dest}  ({len(prs.slides._sldIdLst)} slides)  "
      f"Roboto, sem travessões, tamanho único por bloco.")
