# -*- coding: utf-8 -*-
"""
Gerador do deck da Aula 2 (Semana 1, quinta-feira) do AI Talent Academy.

Identidade visual: padrao White Cube (Roboto, azul 28347B, fundos e logo do template
oficial em assets/whitecube/).

Uso:  python scripts/gerar_slides_aula02.py
Saida: docs/aula-02/AI-Talent-Academy-Aula02.pptx

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
          align=PP_ALIGN.LEFT, space=8, line=1.18, anchor=MSO_ANCHOR.TOP):
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
          "Semana 1  ·  Primeiro laboratório do programa", 25, INK, space=0)
    shape(s, ML, Inches(5.75), Inches(2.4), Pt(5), fill=RED)
    block(s, ML, Inches(8.15), Inches(13), Inches(1.0),
          ["Aula 2  ·  Quinta-feira, 19h00 às 21h00  ·  Online",
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


# ==========================================================================
# CONTEÚDO
# ==========================================================================
EU = "Edmar"
FELIPE = "Felipe André Bach Alves"

CAMPOS = [
    (1, "Contexto", "Qual problema ou decisão de negócio precisamos melhorar?"),
    (2, "Usuários", "Quem é o usuário? Quem toma a decisão hoje?"),
    (3, "Dados necessários", "Quais dados serão necessários para desenvolver a solução?"),
    (4, "Hipóteses", "Qual o seu palpite informado sobre a resposta?"),
    (5, "Riscos", "O que está fora do escopo? E os riscos éticos?"),
    (6, "Tipo de Solução", "Que abordagem parece mais adequada? Por quê?"),
    (7, "Estrutura de Custos", "Como saberemos quanto custa desenvolver e manter?"),
    (8, "Métricas de Sucesso", "Como vamos saber se a solução deu certo?"),
]

# --------------------------------------------------------------------------
# PRÉ-AULA
# --------------------------------------------------------------------------
s = sl_cover()
notes(s, "19h00 às 19h10 (slide de espera)", "ESSENCIAL", EU,
      """
Slide projetado desde 18h55. Enquanto a sala enche, fale a cada 2 ou 3 minutos:
"Boa noite! Estamos abrindo a sala. Hoje é a nossa primeira quinta-feira, o dia de
laboratório. Enquanto todo mundo entra, deixa no chat: você conseguiu pensar num
problema real da sua rotina, como a gente pediu na segunda?"

Não comece antes de 19h08.
""",
      """
- Microfones em mudo, câmeras opcionais.
- Confirme a GRAVAÇÃO antes de 19h10.
- CRÍTICO HOJE: as salas de grupo precisam estar criadas ANTES de 19h00.
- Moderador com a lista de grupos pronta para colar no chat.
""")

s = sl_bullets("Enquanto todo mundo entra", "Hoje é dia de laboratório",
               [("Hoje é diferente de segunda", "menos slide, mais mão na massa"),
                ("Você vai trabalhar em grupo", "os grupos já estão definidos, a gente divide às 19h45"),
                ("Não precisa instalar nada", "hoje ainda é sem código"),
                ("Tenha papel e caneta por perto", "ou um documento em branco aberto"),
                ("Trouxe um problema real?", "ótimo. Se não trouxe, a gente tem casos prontos"),
                ("Escreva no chat", "seu nome e se é a primeira vez que participa de algo assim")],
               subtitle="Aula 2 · Semana 1 · começamos 19h10")
notes(s, "19h00 às 19h10", "ESSENCIAL", EU,
      """
Leia os itens uma vez, por volta de 19h05. O objetivo é baixar a ansiedade de quem
está com medo do formato "trabalho em grupo com desconhecidos".

Insista no quarto item: "não precisa instalar nada, hoje ainda é sem código".
""")

# ==========================================================================
# BLOCO A: Explicar as quintas-feiras (19h10 às 19h20)
# ==========================================================================
s = sl_section("01", "Como funcionam as quintas", "O dia de colocar a mão na massa",
               "19h10 às 19h20  ·  10 minutos")
notes(s, "19h10 às 19h20 (10 min)", "ESSENCIAL", EU,
      """
Bloco curto. O objetivo é dar o contrato do formato: o que a pessoa pode esperar de
toda quinta-feira daqui para frente, para ela reservar a energia certa.

Ritmo rápido: 10 minutos, 4 slides.
""")

s = sl_two_col("O ritmo da semana", "Duas aulas, dois propósitos diferentes",
               "SEGUNDA · 3 horas",
               ["Conceito e panorama",
                "A gente apresenta, você absorve",
                "Muito conteúdo novo por noite",
                "Formato: apresentação + chat",
                "É onde você entende o \"o quê\""],
               "QUINTA · 2 horas",
               ["Prática e laboratório",
                "Você faz, a gente orienta",
                "Pouco conteúdo novo, muita aplicação",
                "Formato: demonstração + grupo",
                "É onde você entende o \"como\""],
               subtitle="Hoje você vai passar mais tempo trabalhando do que assistindo.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Bem-vindos à primeira quinta-feira do programa. E eu quero começar explicando por que
esse dia existe, porque ele é bem diferente da segunda.

Segunda-feira é conceito. A gente apresenta, vocês absorvem, é muito conteúdo novo numa
noite só. Quem esteve na segunda sabe: foram três horas de panorama.

Quinta-feira é o contrário. Pouco conteúdo novo, muita aplicação. A gente demonstra uma
coisa, e depois VOCÊS fazem. Hoje, por exemplo, eu e o Felipe vamos falar por uns 35
minutos. O resto da noite é de vocês.

Na segunda a gente constrói o repertório. Na quinta vocês usam ele."
""")

s = sl_cards("O formato de toda quinta", "O que se repete todas as semanas",
             [("Recap curto",
               "A gente retoma o conceito da segunda que vai virar prática hoje.\n\n~10 minutos"),
              ("Demonstração",
               "Um de nós resolve um caso real na frente de vocês, pensando em voz alta.\n\n~25 minutos"),
              ("Você faz",
               "Em grupo ou individual, aplicando o mesmo método num caso novo.\n\n~45 minutos"),
              ("Fechamento",
               "O que aprendemos, o que entregar e o que vem na próxima semana.\n\n~15 minutos")],
             subtitle="Guarde este ritmo. As sete quintas seguintes vão seguir o mesmo desenho.",
             cols=4, card_h=3.2)
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Toda quinta vai ter esta mesma estrutura, então vale guardar.

Começa com um recap curto: a gente retoma o conceito da segunda que vira prática hoje.

Depois vem a demonstração. E eu quero destacar uma coisa aqui: quando a gente demonstra,
a gente pensa em voz alta. Vocês vão me ver errando, mudando de ideia, voltando atrás.
Isso é de propósito. O que vocês precisam levar daqui é o CAMINHO até a resposta, mais
do que a resposta em si.

Aí vem a parte maior: vocês fazem. Hoje em grupo.

E fecha com o que aprendemos e o que vem depois."
""",
      "Se o tempo apertar, este slide pode ser resumido em 1 minuto lendo só os 4 títulos.")

s = sl_pipeline("Onde estamos", "Lembra das 8 fases? Hoje é 100% a fase 1",
                [(1, "Entender o problema", "É AQUI QUE A GENTE ESTÁ HOJE. Transformar um pedido vago em problema resolvível."),
                 (2, "Conseguir os dados", "Semana 2 em diante."),
                 (3, "Explorar", "Semana 2, com SQL e Python."),
                 (4, "Preparar", "Semana 2."),
                 (5, "Construir a solução", "Semanas 3 e 6."),
                 (6, "Avaliar", "Semana 3."),
                 (7, "Colocar no ar", "Semanas 6 e 7."),
                 (8, "Monitorar", "Semana 7.")],
                subtitle="A fase que mais gente pula, e a que mais mata projeto. Merece uma noite inteira.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Na segunda o Felipe mostrou este slide: as oito fases de qualquer solução de dados e IA.
E ele falou uma coisa que eu quero repetir hoje: a fase 1 é a que mais gente pula, e é a
que mais mata projeto.

Então olha o que a gente vai fazer. Esta noite inteira é a fase 1. Só ela. Duas horas
para uma fase só.

Pode parecer exagero, mas a fase 1 é onde se decide se o projeto vai gerar valor ou virar
um notebook bonito que ninguém usa. As outras sete fases são execução. Se a fase 1 estiver
errada, executar bem só te leva mais rápido para o lugar errado.

A partir da semana 2 a gente começa a descer as outras fases, com SQL, com Python, com
modelo. Mas hoje, fase 1."
""")

# ==========================================================================
# BLOCO B: Explicar a dinâmica e demonstrar (19h20 às 19h45)
# ==========================================================================
s = sl_section("02", "O Canvas do Problema", "A primeira ferramenta de trabalho do programa",
               "19h20 às 19h45  ·  25 minutos")
notes(s, "19h20 às 19h45 (25 min)", "ESSENCIAL", FELIPE,
      """
Bloco principal da noite, conduzido pelo Felipe. Estrutura:
  Apresentar a ferramenta (o que é, por que existe)    ~5 min
  O caso e o pedido vago                                ~2 min
  Preencher os 8 campos ao vivo, pensando em voz alta  ~15 min
  O canvas completo e o que mudou                       ~3 min

CONTROLE DE TEMPO: às 19h32 você PRECISA ter começado o campo 1. Se estiver atrasado,
acelere os campos 4 a 7 (2 frases cada) e preserve os campos 1, 2 e 8, que são os
obrigatórios da atividade em grupo.
""")

s = sl_statement("Por que uma ferramenta e não uma aula",
                 "Um problema bem definido já está meio resolvido.\nO Canvas existe para você não pular nenhuma\npergunta difícil.")
notes(s, "2 min", "ESSENCIAL", FELIPE,
      """
"Na segunda eu disse que um projeto bem definido já está meio resolvido. Hoje eu vou dar
para vocês a ferramenta que garante isso.

Chama Canvas do Problema. É uma página só, com oito campos. Você preenche antes de abrir
qualquer dado, antes de escrever qualquer linha de código.

A vantagem de ter campos, em vez de um documento livre, é que campo vazio incomoda. Quando
você tem oito caixas na sua frente e três estão em branco, você percebe na hora que não
sabe responder aquilo. Num documento livre, você simplesmente não escreve sobre o que
não sabe, e o buraco passa despercebido até o projeto estar na metade.

O canvas força a pergunta difícil a aparecer cedo, quando ela ainda é barata de resolver."
""")

s = sl_canvas("A ferramenta", "Os 8 campos do Canvas do Problema", CAMPOS,
              subtitle="Uma página. Oito perguntas. Preenchida antes de abrir qualquer dado.")
notes(s, "3 min", "ESSENCIAL, slide-âncora da noite", FELIPE,
      """
Apresente os oito de uma vez, sem aprofundar. O aprofundamento vem no caso.

"Estes são os oito campos. Vou ler rápido, porque daqui a pouco a gente preenche cada um
com um caso de verdade.

Um, CONTEXTO: qual problema ou decisão de negócio precisamos melhorar?
Dois, USUÁRIOS: quem é o usuário, quem toma essa decisão hoje?
Três, DADOS NECESSÁRIOS: quais dados vamos precisar?
Quatro, HIPÓTESES: qual o seu palpite informado sobre a resposta?
Cinco, RISCOS: o que está fora do escopo, e quais os riscos éticos?
Seis, TIPO DE SOLUÇÃO: que abordagem parece mais adequada, e por quê?
Sete, ESTRUTURA DE CUSTOS: quanto custa desenvolver e manter isso?
Oito, MÉTRICAS DE SUCESSO: como vamos saber se deu certo?

Repara numa coisa: só o campo seis fala de tecnologia. Sete dos oito campos são sobre
entender o problema, as pessoas e o valor. Isso não é acidente."
""",
      "Este slide vai ficar aberto durante a atividade em grupo. Deixe o link do PDF no chat.")

s = sl_statement("Agora na prática",
                 "\"Queremos usar IA para reduzir\nas perdas com fraude no cartão.\"",
                 "Este é o tipo de pedido que chega. Vago, amplo, começando pela solução.")
notes(s, "2 min", "ESSENCIAL", FELIPE,
      """
Leia o pedido em voz alta, com a entonação de quem recebeu isso numa reunião.

"Agora vamos preencher o canvas com um caso, e eu escolhi um que vocês já viram duas vezes
na segunda-feira: fraude em cartão.

Lembram do slide das coisas que vocês já usam sem saber? A compra bloqueada pelo banco
estava lá. E lembram do exemplo do modelo que acertava 99% e não servia para nada? Era
esse mesmo problema. Hoje a gente preenche o canvas dele.

O pedido que chega da diretoria é este: 'queremos usar IA para reduzir as perdas com
fraude no cartão'.

Vocês já sabem o que tem de errado com essa frase. Ela começa pela SOLUÇÃO. Não diz qual
decisão precisa melhorar, não diz quem decide, e não diz como a gente vai saber se
funcionou.

Se você sair daqui e começar a treinar um modelo, você vai errar. Vamos preencher o canvas
primeiro. Oito campos, um de cada vez."
""",
      """
Por que este caso: ele já apareceu duas vezes na Aula 1, então a turma tem contexto, e
vocês dois dominam o domínio. O arco fecha no campo 8, quando você retoma o exemplo do
99% de acurácia.

Este caso é hipotético e realista, sem dataset público atrelado. Se alguém perguntar onde
baixar os dados, a resposta honesta é que base de fraude real não é pública, justamente
por sigilo bancário e proteção de dados.
""")

s = sl_bullets("Campo 1 de 8 · Contexto",
               "Qual decisão de negócio precisa melhorar?",
               [("A decisão acontece em milissegundos", "a cada transação: aprovar, pedir confirmação ou recusar"),
                ("Hoje quem decide é um conjunto de regras fixas", "valor acima de X, país estrangeiro, categoria de risco"),
                ("Regra fixa não se adapta", "o fraudador testa até descobrir onde está o limite"),
                ("Errar para menos custa dinheiro", "a perda da transação fraudada, que o banco absorve"),
                ("Errar para mais custa cliente", "compra legítima recusada na frente da fila do supermercado"),
                ("Cuidado com o desejo disfarçado de problema", "\"reduzir fraude\" é vontade da diretoria. Fraude tem vários tipos e canais")],
               subtitle="Comece pela decisão que já é tomada hoje, mesmo que seja tomada por um sistema.")
notes(s, "2 min", "ESSENCIAL", FELIPE,
      """
"Campo um: contexto. A pergunta certa aqui não busca 'o problema da empresa'. Ela busca
uma DECISÃO concreta que precisa melhorar.

E existe uma decisão bem definida: a cada transação que passa na maquininha, alguém
precisa dizer em milissegundos se aprova, se pede confirmação ou se recusa.

Quem decide isso hoje é um conjunto de regras fixas, escritas por analistas: valor acima
de tanto, compra em país estrangeiro, categoria de lojista de risco. Funciona, até certo
ponto. O problema é que regra fixa não se adapta, e o fraudador testa até descobrir onde
está o limite.

Quando o sistema erra para menos, o banco absorve a perda. Quando erra para mais, o
cliente legítimo tem a compra recusada na frente da fila do supermercado.

E o último item é o de sempre: 'reduzir fraude' é vontade da diretoria. Fraude de cartão
clonado, fraude de conta invadida e fraude do próprio titular são problemas diferentes,
com dados diferentes. A gente precisa escolher um."
""")

s = sl_bullets("Campo 2 de 8 · Usuários",
               "Quem toma essa decisão hoje, e como?",
               [("Usuário direto: o sistema de autorização", "consome a resposta em menos de 100 milissegundos"),
                ("Usuário humano: o analista de prevenção", "calibra o limiar e revisa a fila de casos duvidosos"),
                ("A fila dele tem capacidade limitada por dia", "isso define quantos casos o modelo pode mandar para revisão"),
                ("Terceiro envolvido: o cliente que teve a compra recusada", "ele sofre o efeito e é quem liga no SAC reclamando"),
                ("Se o analista não entender por que o modelo marcou", "ele não consegue revisar, e a fila trava"),
                ("O prazo de 100 ms já é um requisito técnico", "e ele saiu de uma pergunta sobre gente, não sobre tecnologia")],
               subtitle="Usuário nem sempre é uma pessoa só. Aqui são três, com necessidades diferentes.")
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Campo dois: usuários. E este caso é bom justamente porque mostra que 'usuário' raramente
é uma pessoa só.

O usuário direto é um sistema, o autorizador, que consome a resposta em menos de cem
milissegundos. Isso já vira um requisito técnico duro.

O usuário humano é o analista de prevenção a fraude. Ele calibra o limiar e revisa a fila
de casos duvidosos. E a fila dele tem capacidade limitada: se o modelo mandar dez mil
casos por dia para revisão, ninguém revisa nada.

E tem um terceiro envolvido, que muita gente esquece de escrever: o cliente que teve a
compra recusada. Ele não decide nada, mas é ele quem liga no SAC reclamando, e é o custo
dele que aparece na conta no fim do mês.

O quinto item é o que trava projeto de verdade: se o analista não entender por que o
modelo marcou aquela transação, ele não consegue revisar. Aí a fila para, e o projeto
morre mesmo com o modelo funcionando.

Repara no último item: o prazo de cem milissegundos é um requisito técnico que saiu de
uma pergunta sobre gente e sobre processo, e não de uma discussão de arquitetura."
""")

s = sl_bullets("Campo 3 de 8 · Dados necessários",
               "Do que a gente precisa, e o que já existe?",
               [("Histórico do cliente", "valor, horário, categoria e local das compras que ele costuma fazer"),
                ("Dados da transação atual", "valor, lojista, país, e se é presencial ou online"),
                ("Comportamento de sessão, quando é compra online", "dispositivo, tempo de preenchimento, geolocalização"),
                ("O rótulo de fraude vem do chargeback", "e ele demora de 30 a 90 dias para chegar"),
                ("Isso significa treinar com o mundo de três meses atrás", "enquanto o fraudador já mudou de tática"),
                ("Cuidado com vazamento", "\"transação estornada\" só existe depois. Não pode entrar num modelo que roda antes")],
               subtitle="Liste o que precisa, marque o que não existe, e repare em quando cada dado fica disponível.")
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Campo três: dados. E aqui tem uma particularidade deste domínio que eu quero que vocês
guardem, porque ela aparece em muito projeto.

Os dados fáceis são o histórico do cliente e os dados da transação atual. Valor, horário,
categoria, local, se é presencial ou online. Isso o banco tem.

Agora vem a parte difícil: como a gente sabe que uma transação FOI fraude? A confirmação
chega pelo chargeback, quando o cliente contesta. E o chargeback demora de trinta a
noventa dias.

Pensa no que isso significa. O rótulo que o modelo usa para aprender chega três meses
atrasado. Você está treinando com o mundo de três meses atrás, enquanto o fraudador já
mudou de tática duas vezes. Isso muda tudo na frequência de retreino, e a gente escreve
isso no campo sete.

E o último item é o vazamento de sempre: 'transação estornada' existe na base histórica e
é tentador usar. Mas na hora em que o modelo roda, na maquininha, ela ainda não existe. Se
entrar no modelo, você acerta quase tudo no teste e nada na vida real."
""")

s = sl_bullets("Campo 4 de 8 · Hipóteses",
               "Qual o nosso palpite informado, antes de olhar o dado?",
               [("O fraudador testa valor baixo antes do valor alto", "uma compra de R$ 5 num app, e depois R$ 3.000"),
                ("Compra fora do padrão geográfico do cliente pesa muito", "e o padrão de cada cliente é diferente"),
                ("Cartão não presente arrisca mais que presencial", "compra online não tem senha nem chip"),
                ("Sequência rápida em lojistas diferentes é sinal forte", "gente de verdade não compra em cinco lojas em dez minutos"),
                ("Hipótese que eu espero derrubar", "\"fraude concentra na madrugada\". Pode ser só viés de quem olha o relatório"),
                ("Sem hipótese, você só enxerga o que o painel já mostrava", "e o painel foi feito por alguém com as mesmas suspeitas")],
               subtitle="Hipótese boa é a que pode ser derrubada pelo dado. Escreva antes de olhar.")
notes(s, "2 min", "ESSENCIAL", FELIPE,
      """
"Campo quatro: hipóteses. Aqui a gente escreve o que ACHA que vai encontrar, antes de
abrir o dado.

As minhas: o fraudador testa valor baixo antes do valor alto, então uma compra de cinco
reais num aplicativo seguida de uma de três mil merece atenção. Compra fora do padrão
geográfico do cliente pesa muito, e repara que o padrão de cada cliente é diferente:
viajante frequente tem padrão largo, aposentado que compra no mesmo mercado tem padrão
estreito. Cartão não presente arrisca mais, porque não tem senha nem chip. E sequência
rápida em lojistas diferentes é sinal forte, porque gente de verdade não compra em cinco
lojas em dez minutos.

Agora o meu item favorito: eu escrevi uma hipótese que eu ESPERO derrubar. 'Fraude
concentra na madrugada.' Todo mundo acha isso. Mas pode ser só viés de quem olha o
relatório, porque de madrugada tem menos transação legítima e a proporção engana.

E o último item explica por que este campo existe: sem hipótese, você só enxerga o que o
painel já mostrava. E o painel foi construído por alguém que tinha exatamente as mesmas
suspeitas que você."
""")

s = sl_bullets("Campo 5 de 8 · Riscos",
               "O que está fora do escopo, e o que pode dar errado com gente",
               [("FORA DO ESCOPO: fraude interna e de estabelecimento", "seguem outra lógica e outros dados"),
                ("FORA DO ESCOPO: recuperar o valor depois do chargeback", "a gente previne, quem recupera é outro time"),
                ("RISCO ÉTICO: bloquear mais em certa região ou faixa de renda", "isso é discriminação, mesmo sem ninguém programar"),
                ("O modelo aprende CEP como substituto de renda", "mesmo que ninguém entregue renda para ele"),
                ("Quem é prejudicado quando erra", "o cliente legítimo constrangido no caixa. E é ele quem reclama"),
                ("Consigo explicar o bloqueio para o cliente no telefone?", "se o SAC não consegue explicar, o cliente cancela o cartão")],
               subtitle="As quatro perguntas de uso responsável da segunda-feira moram neste campo.")
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Campo cinco: riscos. Ele tem duas metades.

A primeira metade é escopo. A gente não vai tratar fraude interna nem fraude de
estabelecimento, porque seguem outra lógica e outros dados. E a gente não vai recuperar
valor depois do chargeback, porque isso é trabalho de outro time. Escrever isso agora
evita, daqui a dois meses, alguém perguntar 'mas cadê a recuperação?'.

A segunda metade são as quatro perguntas de uso responsável da segunda-feira. E aqui tem
uma bem séria, que conecta direto com os dois casos de viés que a gente viu.

Se o modelo passar a bloquear mais em determinada região ou faixa de renda, isso é
discriminação, mesmo que ninguém tenha programado. E olha o item quatro: o modelo aprende
CEP como substituto de renda, mesmo que ninguém entregue renda para ele. Lembram do caso
da Amazon? Ninguém escreveu 'rejeite mulheres', o modelo aprendeu sozinho. Aqui é igual.

Quem é prejudicado quando erra: o cliente legítimo, constrangido na frente da fila. E é
ele quem liga reclamando.

E a última pergunta é a mais prática: se o atendente do SAC não conseguir explicar por que
a compra foi recusada, o cliente cancela o cartão. Explicabilidade aqui é requisito de
negócio."
""")

s = sl_bullets("Campo 6 de 8 · Tipo de Solução",
               "Que abordagem o problema pede, e por quê?",
               [("Isto não é um caso de IA generativa", "não tem texto para gerar nem para entender"),
                ("Classificação, mas devolvendo SCORE em vez de sim ou não", "o score permite três ações, e não duas"),
                ("Com score dá para aprovar, pedir confirmação ou recusar", "pedir confirmação salva o cliente legítimo do constrangimento"),
                ("Baseline obrigatório: as regras fixas que já existem", "elas já funcionam, e são a régua honesta"),
                ("Se o modelo não vencer as regras atuais", "a gente mantém as regras e economiza o projeto inteiro"),
                ("Restrição dura: responder em menos de 100 ms", "modelo pesado demais é inviável, por melhor que seja")],
               subtitle="Este é o único dos oito campos que fala de tecnologia. E ele vem só no sexto lugar.")
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Campo seis: tipo de solução. Finalmente tecnologia, e repara que ela veio em sexto lugar.

Primeira decisão: isso aqui não pede IA generativa. Não tem texto para gerar nem para
entender. Se alguém sugerir um chatbot, a resposta é não. Lembram da escada da segunda?
Este problema pede o degrau de machine learning.

Segunda decisão, e essa é de produto: classificação devolvendo um SCORE, em vez de um sim
ou não. Por que isso importa tanto? Com um score, você tem três ações em vez de duas.
Score baixo aprova, score médio pede confirmação por aplicativo, score alto recusa. E a
faixa do meio é ouro, porque ela salva o cliente legítimo do constrangimento sem deixar a
fraude passar.

Terceira: baseline obrigatório. E neste caso o baseline é ótimo, porque já existe: são as
regras fixas que o banco usa hoje. Mede o desempenho delas primeiro. Se o modelo não
ganhar das regras que já estão rodando, a gente mantém as regras e economiza o projeto
inteiro.

E a restrição dura: cem milissegundos. Um modelo pesado demais é inviável aqui, por melhor
que seja o acerto dele. Restrição de negócio manda na escolha técnica."
""")

s = sl_bullets("Campo 7 de 8 · Estrutura de Custos",
               "Quanto custa construir e, principalmente, manter?",
               [("O maior custo é a infraestrutura de baixa latência", "responder em 100 ms para milhões de transações sai caro"),
                ("Desenvolvimento: time de 2 ou 3 pessoas por alguns meses", "este caso não cabe num MVP de 6 semanas"),
                ("Retreino em semanas, não em trimestres", "a fraude se adapta rápido, e o rótulo já chega atrasado"),
                ("A fila de revisão manual custa tempo de gente", "cada caso duvidoso enviado ao analista tem preço"),
                ("Custo escondido: o falso bloqueio", "ligação no SAC, cliente irritado, e às vezes cartão cancelado"),
                ("Compare com a perda atual", "se hoje se perde R$ X por mês com fraude, isso define quanto vale investir")],
               subtitle="Projeto que não estima custo de manutenção morre no primeiro trimestre.")
notes(s, "2 min", "ESSENCIAL", FELIPE,
      """
"Campo sete: custos. O campo que quase ninguém preenche e que derruba projeto.

Neste caso o maior custo tem um nome: infraestrutura de baixa latência. Responder em cem
milissegundos, para milhões de transações por dia, sem cair, custa caro. Muito mais caro
que treinar o modelo.

Desenvolvimento: aqui não cabe aquele MVP de uma pessoa por seis semanas. É time de duas
ou três pessoas por alguns meses.

Manutenção: retreino em semanas, não em trimestres. Lembra do campo três? A fraude se
adapta rápido, e o rótulo ainda chega três meses atrasado. Essa combinação é o que torna
este problema difícil de verdade.

Tem também o custo da fila: cada caso duvidoso que o modelo manda para o analista consome
tempo de gente, e tempo de gente tem preço.

E o custo escondido é o falso bloqueio: ligação no SAC, cliente irritado, e às vezes
cartão cancelado. Isso raramente entra na conta, e devia.

O último item é o que fecha a conta: se hoje o banco perde tanto por mês com fraude, esse
número define quanto vale investir. Sem essa comparação, ninguém aprova o orçamento."
""")

s = sl_bullets("Campo 8 de 8 · Métricas de Sucesso",
               "Como vamos saber, com número, se deu certo?",
               [("DE NEGÓCIO: reduzir 25% da perda financeira com fraude", "medida em reais, não em percentual de acerto"),
                ("DE MODELO: priorizar recall, com teto de falso positivo", "pegar mais fraude, sem bloquear cliente legítimo demais"),
                ("CONTRA-MÉTRICA: falso bloqueio abaixo de 1%", "sem ela, existe uma solução trivial que bate a meta e quebra o banco"),
                ("DE OPERAÇÃO: a fila de revisão cabe na equipe atual", "solução que exige o dobro de analistas não é viável"),
                ("Prazo: 3 meses rodando, com grupo de controle", "sem prazo e sem controle, a discussão nunca fecha"),
                ("Repare no que ficou de fora desta lista", "acurácia. Lembram do modelo que acertava 99% e não pegava fraude nenhuma?")],
               subtitle="Sempre que possível, escolha métrica de negócio. Acurácia não paga conta.")
notes(s, "3 min", "ESSENCIAL, fechamento da demonstração", FELIPE,
      """
Este é o slide onde o arco com a Aula 1 fecha. Guarde energia para o último item.

"Campo oito, o último, e para mim o mais importante: métricas de sucesso.

A métrica de negócio: reduzir vinte e cinco por cento da perda financeira com fraude,
medida em reais. Repara que é em reais, e não em percentual de acerto.

A métrica de modelo: priorizar recall, com teto de falso positivo. Pegar mais fraude, sem
bloquear cliente legítimo demais.

A contra-métrica: falso bloqueio abaixo de um por cento. E ela é obrigatória aqui, porque
sem ela existe uma solução trivial que bate a meta: recusar tudo. Zero de fraude, zero de
cliente.

A métrica de operação: a fila de revisão precisa caber na equipe atual. Uma solução que
exige o dobro de analistas resolve um problema criando outro.

E prazo: três meses rodando, com grupo de controle, para saber o que foi efeito do modelo
e o que foi efeito do mercado.

Agora reparem no que ficou de fora dessa lista. Acurácia. E vocês sabem por quê: na
segunda a gente construiu um modelo que respondia sempre 'não é fraude', acertava
noventa e nove por cento das vezes e não pegava uma fraude sequer. Era exatamente este
problema. Por isso acurácia não entra."
""",
      "Se estiver atrasado, corte os itens 4 e 5, mas NUNCA o último. Ele fecha o arco com a Aula 1.")

s = sl_canvas("O resultado", "O mesmo pedido vago, agora resolvível",
              [(1, "Contexto", "A cada transação, decidir em milissegundos: aprovar, confirmar ou recusar."),
               (2, "Usuários", "Sistema de autorização, analista de prevenção e o cliente afetado."),
               (3, "Dados necessários", "Histórico do cliente e da transação. O rótulo de fraude atrasa 90 dias."),
               (4, "Hipóteses", "Fraudador testa valor baixo antes. Fora do padrão geográfico pesa."),
               (5, "Riscos", "Fora: fraude interna. Ético: CEP vira substituto de renda."),
               (6, "Tipo de Solução", "Score de risco, com três ações. Baseline: as regras de hoje. 100 ms."),
               (7, "Estrutura de Custos", "Baixa latência é o maior custo. Retreino em semanas."),
               (8, "Métricas de Sucesso", "Perda menor 25% em reais. Falso bloqueio abaixo de 1%.")],
              subtitle="De \"queremos usar IA para reduzir fraude\" para isto, em 15 minutos.")
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
Este é o slide de amarração. Deixe-o na tela e faça o contraste em voz alta.

"Olha onde a gente chegou. A gente começou com esta frase: 'queremos usar IA para reduzir
as perdas com fraude no cartão'.

E terminou com isto. Uma decisão específica, com prazo de milissegundos. Três usuários
diferentes, cada um com uma necessidade. Uma lista de dados com o problema do rótulo
atrasado escrito em letras garrafais. Hipóteses que podem ser derrubadas. Escopo e riscos
éticos definidos. Uma abordagem escolhida com justificativa, incluindo a decisão de
produto de usar score em vez de sim ou não. Uma conta de custo que aponta para a
infraestrutura, e não para o modelo. E uma meta em reais, com contra-métrica e prazo.

Quinze minutos. Sem abrir um dado, sem escrever uma linha de código.

E agora a pergunta que importa. Se você fosse o diretor que fez o pedido original, qual
dos dois você aprovaria? A frase ou este canvas?

É por isso que a gente começa por aqui. Agora é a vez de vocês."
""")

# ==========================================================================
# BLOCO C: Quebra em grupos (19h45 às 20h00)
# ==========================================================================
s = sl_section("03", "Agora é com vocês", "Como vai funcionar a atividade em grupo",
               "19h45 às 20h00  ·  15 minutos")
notes(s, "19h45 às 20h00 (15 min)", "ESSENCIAL", EU,
      """
Bloco operacional. Objetivo: ninguém entrar na sala de grupo sem saber o que fazer.

ATENÇÃO: este é o momento de maior risco da noite. Com 190 pessoas indo para salas
separadas, qualquer ambiguidade vira 20 grupos parados perguntando "e agora?".

Leia as regras DEVAGAR e repita as três coisas obrigatórias duas vezes.
""")

s = sl_cards("A divisão", "Como os grupos foram formados",
             [("Os grupos já estão prontos",
               "Você não precisa procurar ninguém. A distribuição foi feita antes da aula.\n\nO moderador vai postar a lista no chat agora."),
              ("Cada grupo tem sua própria sala",
               "Você vai ser movido automaticamente para a sala do seu grupo.\n\nSe cair na sala errada, avise no chat principal."),
              ("Grupos mistos de propósito",
               "Cada grupo tem gente de formações e níveis diferentes.\n\nIsso é intencional: quem não é técnico costuma fazer a melhor pergunta do campo 1."),
              ("A gente circula entre as salas",
               "Eu e o Felipe vamos entrar e sair das salas ao longo dos 45 minutos.\n\nSe travarem, escrevam no chat principal que a gente vai até vocês.")],
             cols=2, card_h=2.9)
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Vamos para a parte prática. Vocês vão trabalhar em grupo, e eu quero explicar como isso
funciona antes de mover ninguém.

Primeiro: os grupos JÁ ESTÃO PRONTOS. Vocês não precisam procurar ninguém nem combinar
nada. A gente montou a distribuição antes da aula. O moderador está postando a lista no
chat agora.

Segundo: cada grupo tem a própria sala, e vocês vão ser movidos automaticamente. Se alguém
cair na sala errada, escreve no chat principal que a gente corrige.

Terceiro, e isso é de propósito: os grupos são MISTOS. Tem gente de formação técnica e
gente que nunca programou no mesmo grupo. E eu quero dizer uma coisa para quem está
achando que vai atrapalhar: quem NÃO é técnico costuma fazer a melhor pergunta do campo
um. Porque não tem vício de já pensar na solução.

Quarto: eu e o Felipe vamos circular pelas salas. Se travarem, escrevam no chat principal."
""",
      "AÇÃO DO MODERADOR: postar a lista de grupos no chat exatamente neste slide.")

s = sl_bullets("As regras", "Como trabalhar nos 45 minutos",
               [("Escolham um relator assim que entrarem", "a pessoa que escreve o canvas e apresenta depois. 2 minutos para decidir"),
                ("Escolham o caso", "vocês têm três opções, no próximo slide"),
                ("Preencham no documento compartilhado", "o link estará no chat da sua sala"),
                ("Não precisa preencher os oito campos", "os campos 1, 2 e 8 são obrigatórios. O resto é o que der tempo"),
                ("Discordar faz parte", "se o grupo não concordar sobre o campo 1, escrevam as duas versões"),
                ("Câmera e microfone liberados na sala", "aqui é grupo pequeno, a conversa por voz funciona")],
               subtitle="45 minutos para conversar sobre o problema. Documento bonito fica para outro dia.")
notes(s, "5 min", "ESSENCIAL, leia devagar", EU,
      """
Este é o slide mais importante do bloco operacional. Leia item por item, sem pressa.

"Agora as regras. Presta atenção porque depois que vocês entrarem na sala, eu não estou
lá para repetir.

Assim que entrarem, escolham um RELATOR. É a pessoa que escreve o canvas e apresenta no
final. Dois minutos para decidir isso, no máximo.

Depois disso, escolham o caso, entre as três opções do próximo slide, e preencham no
documento compartilhado que vai estar no chat da sala de vocês.

Agora o aviso que mais alivia: vocês NÃO precisam preencher os oito campos. Em 45 minutos,
com oito pessoas que acabaram de se conhecer, isso não acontece. Os obrigatórios são o um,
o dois e o oito: contexto, usuários e métricas de sucesso. O resto é o que der tempo.

Mais uma coisa: discordar faz parte. Se o grupo não concordar sobre qual é o problema,
escrevam as DUAS versões no canvas. Discordância explícita vale mais que consenso morno.

E por último, na sala de vocês câmera e microfone estão liberados. É grupo pequeno, ali a
conversa por voz funciona bem."
""",
      "Repita em voz alta os três campos obrigatórios: 1 Contexto, 2 Usuários, 8 Métricas.")

s = sl_cards("Escolham um", "Os três casos disponíveis",
             [("Caso A · Evasão escolar",
               "Uma rede de ensino quer reduzir o número de alunos que abandonam o curso no meio do ano.\n\nDados públicos existem: Censo Escolar do INEP.\n\nBom para quem gosta de impacto social."),
              ("Caso B · Fila de pronto-socorro",
               "Um hospital quer reduzir o tempo de espera na triagem sem contratar mais gente.\n\nBom para quem gosta de operação e processo."),
              ("Caso C · O problema de vocês",
               "Alguém do grupo trouxe um problema real do próprio trabalho ou faculdade?\n\nUsem ele. É a melhor opção das três, porque tem contexto de verdade.")],
             subtitle="A gente percebe na hora a diferença entre canvas discutido e canvas preenchido no automático.",
             cols=3)
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Três casos. Escolham um.

Caso A, evasão escolar: uma rede de ensino quer reduzir o número de alunos que abandonam
o curso no meio do ano. E aqui tem uma coisa boa: os dados existem de verdade, o INEP
publica o Censo Escolar. Bom para quem se interessa por impacto social.

Caso B, fila de pronto-socorro: um hospital quer reduzir o tempo de espera na triagem sem
contratar mais gente. Bom para quem gosta de operação e processo.

Caso C, e essa é a que eu recomendo: alguém do grupo trouxe um problema real do próprio
trabalho ou da faculdade? Usem ele. É a melhor das três opções, porque tem contexto de
verdade, e a pessoa que trouxe consegue responder as perguntas difíceis do campo dois.

E a linha de baixo é o critério de hoje: a gente percebe na hora a diferença entre um
canvas que foi DISCUTIDO e um que foi preenchido no automático. É isso que a gente olha."
""")

# ==========================================================================
# BLOCO D: Atividade em grupo (20h00 às 20h45)
# ==========================================================================
s = sl_statement("Atividade em grupo",
                 "45 minutos.\nVocês voltam para a sala principal às 20h45.",
                 "Campos obrigatórios: 1 Contexto · 2 Usuários · 8 Métricas de Sucesso\nSe travarem, escrevam no chat principal que a gente entra na sala.")
notes(s, "20h00 às 20h45 (45 min)", "ESSENCIAL", "os dois",
      """
Este slide fica projetado na sala principal durante toda a atividade.

CHECKLIST DA DUPLA DURANTE OS 45 MINUTOS:

Minuto 0 a 5:   mover todo mundo para as salas. Conferir que ninguém ficou para trás.
Minuto 5 a 15:  cada um entra em 3 ou 4 salas, só para conferir que começaram.
                Pergunta padrão: "já escolheram o relator e o caso?"
Minuto 15 a 35: circular nas salas que pediram ajuda no chat. Não fique mais de 5 min
                numa sala só.
Minuto 35 a 40: mandar aviso geral: "faltam 10 minutos, foquem nos campos 1, 2 e 8".
Minuto 40 a 45: aviso de 5 minutos e trazer todo mundo de volta.

O QUE FAZER SE UMA SALA ESTIVER PARADA E EM SILÊNCIO:
Não pergunte "está tudo bem?", porque a resposta automática é sim. Pergunte direto:
"me conta o campo 1 de vocês, qual decisão vocês estão tentando melhorar?"
Isso destrava, porque força alguém a falar algo concreto.

SE UM GRUPO TERMINAR CEDO:
Peça para eles preencherem o campo 5 (riscos) com mais profundidade, ou para escreverem
qual hipótese eles mais gostariam de derrubar.
""")

# ==========================================================================
# BLOCO E: Encerramento (20h45 às 21h00)
# ==========================================================================
s = sl_section("04", "Encerramento", "O que a gente leva de hoje e o que vem na semana 2",
               "20h45 às 21h00  ·  15 minutos")
notes(s, "20h45 às 21h00 (15 min)", "ESSENCIAL", FELIPE,
      """
DISTRIBUIÇÃO:
  Ouvir 3 ou 4 grupos      6 min  (30 a 60 segundos cada, cronometrado)
  Recapitulação            3 min
  O que vem na semana 2    3 min
  Q&A                      3 min
  Fechamento               1 min

Ao pedir relatos, NÃO pergunte "alguém quer compartilhar?". Chame grupos pelo número:
"grupo 3, me conta em 30 segundos qual foi o campo mais difícil de vocês".
""")

s = sl_bullets("O que a gente viu hoje", "Cinco ideias para levar da primeira quinta",
               [("A fase 1 merece uma noite inteira", "porque é onde o projeto vive ou morre"),
                ("Sete dos oito campos não falam de tecnologia", "o problema pesa mais que a ferramenta"),
                ("O usuário define o formato da entrega", "20 minutos de decisão significa lista, não dashboard"),
                ("Marcar o que você não tem sai barato", "uma conversa agora, três semanas se descobrir no meio"),
                ("Métrica boa vem com número, prazo e contra-métrica", "senão existe sempre uma solução trivial que quebra a empresa")],
               subtitle="Se você levar só essas cinco frases, a noite cumpriu o objetivo.",
               numbered=True)
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Cinco ideias para levar de hoje.

A primeira: a fase 1 merece uma noite inteira, porque é onde o projeto vive ou morre.

Repara que sete dos oito campos do canvas não falam de tecnologia. Quem achava que essa
área era só modelo e código teve a prova hoje de que o problema pesa mais que a ferramenta.

Terceira ideia: o usuário define o formato da entrega. O coordenador tem vinte minutos,
então a resposta vira uma lista priorizada.

Marcar o que você não tem sai barato: custa uma conversa agora, e três semanas se você
descobrir no meio do projeto.

E fecha com a mais importante: métrica boa vem com número, prazo e contra-métrica. Sem
contra-métrica, sempre existe uma solução trivial que bate a meta e quebra a empresa."
""")

s = sl_two_col("Próximos encontros", "O que vem pela frente",
               "SEGUNDA · Semana 2",
               ["IA Generativa na prática",
                "Como um LLM funciona por dentro",
                "Prompt, contexto e limites",
                "Onde GenAI resolve e onde ela atrapalha",
                "Formato conceitual, como toda segunda"],
               "QUINTA · Semana 2",
               ["Primeiro contato com código",
                "Google Colab, gratuito e no navegador",
                "Só precisa de uma conta Google",
                "Traga o notebook, não só o celular",
                "Vamos do zero, ninguém fica para trás"],
               subtitle="A partir da semana 2 entra código. E ele entra devagar.")
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"O que vem pela frente.

Segunda que vem, semana 2: IA generativa na prática. Como um LLM funciona por dentro,
prompt, contexto, limites, e principalmente onde a GenAI resolve e onde ela atrapalha.
Formato conceitual, como toda segunda.

E na quinta da semana 2 vem o momento que parte de vocês está esperando e parte está
temendo: o primeiro contato com código. Google Colab, que é gratuito e roda no navegador.
Vocês só precisam de uma conta Google.

Dois avisos práticos. Primeiro: tragam notebook, não dá para acompanhar Colab pelo celular.
Segundo, e esse é para quem está com medo: a gente vai do ZERO. Ninguém fica para trás.
Quem nunca escreveu uma linha de código na vida vai conseguir acompanhar."
""",
      "CONFERIR antes da aula: o tema da semana 2 mudou no cronograma novo. Confirme com o Edmar se é GenAI mesmo antes de anunciar.")

s = sl_statement("Agora é com vocês", "Perguntas?",
                 "Escreva no chat. O que não der tempo, respondemos no Discord ainda hoje.")
notes(s, "3 min", "ESSENCIAL", f"{FELIPE} + {EU}",
      """
PERGUNTAS PREVISÍVEIS DE HOJE:

• "O canvas que a gente preencheu vale nota?"
  Hoje não vale nota. É treino. O canvas que vai contar é o do mini-desafio da semana 4.

• "Posso mudar de grupo?"
  Os grupos de hoje foram só para esta atividade. Nas próximas a gente reorganiza.

• "E se o meu grupo não terminou o canvas?"
  Nenhum grupo terminou os oito campos. Isso era esperado, o exercício é a conversa.

• "Onde eu pego o canvas em branco para usar sozinho?"
  Está no Discord, no canal de materiais, em PDF.

• "Vou precisar saber programar na quinta que vem?"
  Não. A gente começa do zero, no navegador.

• "Perdi a aula de segunda, consigo acompanhar?"
  Sim. A gravação está no Discord, e o material de apoio tem o glossário completo.
""")

s = sl_closing()
notes(s, "1 min", "ESSENCIAL", FELIPE,
      """
FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. Foi a primeira vez que vocês trabalharam juntos, e eu sei
que grupo com desconhecido no primeiro dia é desconfortável. Vocês foram muito bem.

Entrem no Discord, o canvas em branco está lá para vocês usarem quando quiserem.

E fica com isso: hoje vocês preencheram, em grupo, em 45 minutos, um documento que em
muita empresa ninguém preenche nunca. Nos vemos na segunda. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Salvar os documentos preenchidos pelos grupos (são insumo para calibrar a semana 2).
- 10 minutos de retrospectiva entre os dois: quantos grupos travaram e por quê.
""")

# ==========================================================================
# MATERIAL DE RESERVA (OCULTO): caso alternativo · pouso de booster
# ==========================================================================
# Mesma estrutura de 10 slides do caso de fraude (pedido vago + 8 campos + resultado),
# marcados como slide oculto no PowerPoint (show="0"). Fica fora do fluxo de
# apresentação, mas pronto para trocar de lugar com o caso de fraude se um dia fizer
# sentido usar o tema espacial na demonstração.
#
# NAO GARANTIDO: a Canva pode nao respeitar a flag de slide oculto do PowerPoint na
# importacao. Confira manualmente apos importar, e oculte a mao se preciso.

def oculto(slide):
    """Marca o slide como oculto (show=0). PowerPoint pula em modo apresentacao.
    Nao ha garantia de que o Canva respeite isso na importacao: confira apos importar."""
    slide._element.set("show", "0")
    return slide


s = oculto(sl_section("", "Material de reserva (oculto)",
                       "Caso alternativo: pouso de booster. Não faz parte do fluxo da aula.",
                       "Não apresentar, a menos que decidam trocar o caso"))
notes(s, "não apresentar", "RESERVA", "ninguém",
      """
Este slide e os 9 seguintes estão marcados como OCULTOS no PowerPoint (não aparecem em
modo apresentação). Existem como alternativa pronta ao caso de fraude em cartão, com a
mesma estrutura de 10 slides: pedido vago, 8 campos do canvas, resultado.

Se um dia decidirem trocar o caso da demonstração para o tema espacial, é só desocultar
estes 10 slides e ocultar os 10 do cartão de crédito (slides 10 a 19 do fluxo principal).

LEMBRETE: confirmar se o Canva de fato oculta estes slides depois do import. Se não
ocultar, mova-os manualmente para o fim, ou apague antes de subir para o Canva.
""")

s = oculto(sl_statement("Agora na prática",
                         "\"Queremos usar IA para aumentar\na taxa de pousos bem-sucedidos dos boosters.\"",
                         "Este é o tipo de pedido que chega. Vago, amplo, começando pela solução."))
notes(s, "2 min", "RESERVA", FELIPE,
      """
Leia o pedido em voz alta, com a entonação de quem recebeu isso numa reunião.

"Agora vamos preencher o canvas com um caso diferente: pouso de booster.

Toda vez que um foguete lança, o primeiro estágio, o booster, pode ser recuperado para
reaproveitar depois. Isso é o que torna o lançamento mais barato. E o pedido que chega da
diretoria é este: 'queremos usar IA para aumentar a taxa de pousos bem-sucedidos'.

Vocês já sabem o que tem de errado com essa frase. Ela começa pela SOLUÇÃO. Não diz qual
decisão precisa melhorar, não diz quem decide, e não diz como a gente vai saber se
funcionou.

Vamos preencher o canvas primeiro. Oito campos, um de cada vez."
""",
      """
Por que este caso funciona: a decisão de tentar ou não tentar o pouso é real e documentada
publicamente (missões de alta energia às vezes são lançadas em modo "expendable", sem
tentativa de pouso, por falta de margem de combustível: isso já foi anunciado antes de
vários lançamentos reais).

Cuidado ao apresentar: o histórico de sucesso e falha de pousos é rastreado publicamente
pela comunidade de entusiastas de espaço, algo bem diferente de dado oficial da empresa.
E a telemetria de bordo usada para prever o pouso em tempo real fica só dentro de casa.
Deixe isso claro no campo 3, é parte da lição.
""")

s = oculto(sl_bullets("Campo 1 de 8 · Contexto",
                       "Qual decisão de negócio precisa melhorar?",
                       [("A decisão real tem dois momentos", "qual modo de recuperação tentar, e se confirmar a tentativa"),
                        ("Modo 1: RTLS, o booster volta e pousa perto do local de lançamento", "gasta mais combustível de volta"),
                        ("Modo 2: pouso num drone-ship no oceano", "gasta menos combustível, mas depende do clima no mar"),
                        ("Modo 3: não tentar pouso, o booster é descartado", "escolhido quando a missão não deixa margem de combustível"),
                        ("Hoje a escolha do modo vem da massa da carga e da órbita alvo", "calculado semanas antes, no planejamento da missão"),
                        ("Cuidado com o desejo disfarçado de problema", "\"aumentar a taxa de sucesso\" é vontade. A decisão real é qual modo escolher, e quando confirmar")]))
notes(s, "2 min", "RESERVA", FELIPE,
      """
"Campo um: contexto. A decisão real tem dois momentos, e isso já é incomum.

Primeiro momento: qual modo de recuperação tentar. RTLS, o booster volta e pousa perto do
local de lançamento, o que gasta mais combustível na volta. Pouso num drone-ship no
oceano, que gasta menos combustível mas depende do clima no mar. Ou não tentar pouso
nenhum, descartando o booster, quando a missão não deixa margem.

Essa escolha vem da massa da carga e da órbita alvo, calculada semanas antes, no
planejamento da missão.

E o último item de sempre: 'aumentar a taxa de sucesso' é vontade da diretoria. A decisão
real e específica é qual modo escolher, e quando confirmar a tentativa."
""")

s = oculto(sl_bullets("Campo 2 de 8 · Usuários",
                       "Quem toma essa decisão hoje, e como?",
                       [("Time de mission management decide o modo", "semanas antes, no planejamento da missão"),
                        ("Time de operações de recuperação decide a confirmação final", "horas antes, olhando o clima no local do drone-ship"),
                        ("Dois momentos, duas equipes, dois prazos diferentes", "um modelo só serve se encaixar nos dois"),
                        ("A decisão de modo já vem travada pelo planejamento anterior", "ninguém decide isso de última hora"),
                        ("Se o modelo não respeitar esse prazo, ele não é usado", "e vira um relatório que ninguém consulta a tempo")]))
notes(s, "2 min", "RESERVA", FELIPE,
      """
"Campo dois: usuários. E aqui tem duas equipes diferentes, com dois prazos diferentes.

O time de mission management decide o modo de recuperação, semanas antes, no planejamento
da missão. O time de operações de recuperação decide a confirmação final, horas antes,
olhando o clima real no local do drone-ship.

Um modelo só serve se encaixar nos dois momentos. E a decisão de modo já vem travada pelo
planejamento de semanas antes: ninguém decide isso de última hora. Se o modelo não
respeitar esse prazo, ele vira um relatório que chega tarde demais para qualquer um dos
dois times usar."
""")

s = oculto(sl_bullets("Campo 3 de 8 · Dados necessários",
                       "Do que a gente precisa, e o que já existe?",
                       [("Massa da carga e órbita alvo", "define a margem de combustível disponível. Dado interno"),
                        ("Histórico de sucesso e falha de pousos anteriores", "rastreado publicamente pela comunidade de entusiastas de espaço"),
                        ("Meteorologia no local do drone-ship", "público, via serviço meteorológico marítimo"),
                        ("A telemetria de bordo usada para prever o pouso em tempo real", "essa é proprietária. Não é pública"),
                        ("Sabemos o resultado histórico, não o motivo técnico", "sucesso ou falha, sim. Os sensores que explicam o porquê, não"),
                        ("Isso limita o que o modelo consegue aprender sozinho", "sem a telemetria interna, ele aprende padrão de missão, não de engenharia")]))
notes(s, "3 min", "RESERVA", FELIPE,
      """
"Campo três: dados. E este caso tem uma particularidade parecida com a do cartão de
crédito: parte do dado existe, parte não.

Massa da carga e órbita alvo definem a margem de combustível, e isso é dado interno.
Histórico de sucesso e falha de pousos é rastreado publicamente pela comunidade de
entusiastas de espaço, então dá para calcular uma taxa histórica. Meteorologia no local do
drone-ship também é pública.

Mas a telemetria de bordo, os sensores que explicam por que um pouso deu certo ou errado
em tempo real, essa é proprietária da empresa. Não é pública.

Isso significa que a gente sabe O RESULTADO histórico, sucesso ou falha, mas não o MOTIVO
técnico. E isso limita o que um modelo treinado só com dado público consegue aprender: ele
aprende padrão de missão, não padrão de engenharia."
""",
      "Se um aluno perguntar 'onde eu baixo esse dado', a resposta honesta é: o histórico de sucesso e falha dá para montar com fonte da comunidade, mas a telemetria de verdade não é pública em lugar nenhum.")

s = oculto(sl_bullets("Campo 4 de 8 · Hipóteses",
                       "Qual o nosso palpite informado, antes de olhar o dado?",
                       [("Missões de órbita mais distante reduzem a margem de combustível", "e aumentam o risco de falha no pouso"),
                        ("Mau tempo no oceano aumenta o risco no drone-ship", "comparado ao RTLS, que pousa em terra firme"),
                        ("Boosters com mais voos acumulados têm mais desgaste", "e isso aumentaria o risco de falha"),
                        ("Hipótese que eu espero derrubar", "\"reuso alto sempre aumenta o risco\". O dado público sugere que a correlação é mais fraca do que parece"),
                        ("Sem hipótese, a gente só confirma o que a engenharia já sabia", "e não descobre nada novo")]))
notes(s, "2 min", "RESERVA", FELIPE,
      """
"Campo quatro: hipóteses. Antes de abrir o dado, o que a gente acha que vai encontrar.

Missões de órbita mais distante reduzem a margem de combustível e aumentam o risco de
falha. Mau tempo no oceano aumenta o risco no drone-ship, comparado ao RTLS, que pousa em
terra firme. Boosters com mais voos acumulados teriam mais desgaste, e isso aumentaria o
risco.

E a que eu espero derrubar: 'reuso alto sempre aumenta o risco'. O dado público sugere que
essa correlação é mais fraca do que a intuição sugere. Se a gente só confirma o que a
engenharia já sabia, o projeto não descobriu nada novo."
""")

s = oculto(sl_bullets("Campo 5 de 8 · Riscos",
                       "O que está fora do escopo, e o que pode dar errado com gente",
                       [("FORA DO ESCOPO: falha de motor durante o voo", "é outro sistema, com outra equipe e outra decisão"),
                        ("RISCO DE SEGURANÇA FÍSICA: decisão errada perto de área povoada", "o RTLS pousa perto do local de lançamento"),
                        ("Quem é prejudicado se o modelo errar", "a equipe operacional que confiou na recomendação, e o patrimônio da empresa"),
                        ("Aqui o risco troca de natureza: vira segurança física e patrimonial", "e a pergunta de uso responsável continua valendo"),
                        ("Consigo explicar a recomendação para quem decide?", "se a equipe não confiar, ela ignora o modelo e decide como sempre decidiu")]))
notes(s, "2 min", "RESERVA", FELIPE,
      """
"Campo cinco: riscos. Falha de motor durante o voo fica fora do escopo, é outro sistema e
outra equipe.

O risco que importa aqui é de segurança física: uma decisão errada perto de área povoada,
no caso do RTLS, tem consequência que vai além de dinheiro perdido.

E as perguntas de uso responsável continuam valendo, só que o risco muda de natureza:
aqui pesa mais a segurança física do que a discriminação dos outros casos. Quem é prejudicado se o modelo errar? A
equipe que confiou na recomendação, e o patrimônio da empresa. E se a equipe não conseguir
entender por que o modelo recomendou aquilo, ela ignora e decide como sempre decidiu."
""")

s = oculto(sl_bullets("Campo 6 de 8 · Tipo de Solução",
                       "Que abordagem o problema pede, e por quê?",
                       [("Isto não é um caso de IA generativa", "não tem texto para gerar nem para entender"),
                        ("Classificação, com score de probabilidade de sucesso", "alimenta a decisão de modo e a confirmação final"),
                        ("Baseline obrigatório: taxa histórica média por tipo de missão", "o dado público de sucesso e falha permite calcular isso"),
                        ("Se o modelo não vencer a taxa histórica", "a decisão continua sendo tomada como hoje, pela experiência de engenharia"),
                        ("Dado o risco físico, a decisão final não pode ser 100% automática", "precisa manter uma pessoa no loop, sempre")]))
notes(s, "2 min", "RESERVA", FELIPE,
      """
"Campo seis: tipo de solução. Aqui não tem texto para gerar nem para entender, então IA
generativa sai de cena. Este problema pede classificação, com um score de probabilidade
de sucesso.

Baseline obrigatório: a taxa histórica média por tipo de missão, que dá para calcular só
com o dado público de sucesso e falha. Se o modelo sofisticado não vencer essa taxa, a
decisão continua sendo tomada como hoje.

E, dado o risco físico envolvido, a decisão final não pode ser cem por cento automática.
Precisa manter uma pessoa no loop, sempre. Essa é uma escolha de segurança, que vem antes
de qualquer escolha técnica."
""")

s = oculto(sl_bullets("Campo 7 de 8 · Estrutura de Custos",
                       "Quanto custa construir e, principalmente, manter?",
                       [("Um booster perdido custa dezenas de milhões de dólares", "é a maior parte do custo de um lançamento"),
                        ("Os dados de engenharia necessários são caros e difíceis de obter", "boa parte fica trancada dentro da própria empresa"),
                        ("O perfil de risco muda conforme os boosters envelhecem", "reuso alto muda o padrão continuamente, exige retreino"),
                        ("Compare sempre com o custo de manter a decisão como está hoje", "feita por engenheiros experientes, sem modelo nenhum")]))
notes(s, "2 min", "RESERVA", FELIPE,
      """
"Campo sete: custos. Um booster perdido custa dezenas de milhões de dólares, é a maior
parte do custo de um lançamento. Isso justifica o interesse no problema.

Mas os dados de engenharia necessários para modelar isso de verdade são caros e difíceis
de obter, boa parte é proprietária. E o perfil de risco muda conforme os boosters
envelhecem e voam mais vezes, então o modelo pede retreino constante.

E, como sempre, comparar com o custo de manter a decisão como está hoje: feita por
engenheiros experientes, sem modelo nenhum. Às vezes esse é o baseline mais difícil de
vencer."
""")

s = oculto(sl_canvas("O resultado", "O mesmo pedido vago, agora resolvível",
                      [(1, "Contexto", "Escolher modo de recuperação (RTLS, drone-ship ou descarte) e confirmar a tentativa."),
                       (2, "Usuários", "Mission management decide o modo. Operações confirma horas antes."),
                       (3, "Dados necessários", "Sucesso e falha são públicos. Telemetria de bordo é proprietária."),
                       (4, "Hipóteses", "Órbita distante reduz margem. Reuso alto pode pesar menos do que parece."),
                       (5, "Riscos", "Fora: falha de motor em voo. Risco de segurança física perto de área povoada."),
                       (6, "Tipo de Solução", "Score de sucesso. Baseline: taxa histórica. Humano sempre no loop."),
                       (7, "Estrutura de Custos", "Booster perdido custa dezenas de milhões. Dado de engenharia é caro."),
                       (8, "Métricas de Sucesso", "Aumentar taxa de sucesso sem elevar risco físico à equipe.")],
                      subtitle="De \"queremos usar IA para aumentar a taxa de pousos\" para isto, em 15 minutos."))
notes(s, "3 min", "RESERVA", FELIPE,
      """
Slide de amarração do caso de reserva. Mesma lógica do caso de fraude: contraste em voz
alta entre o pedido original e o canvas completo, terminando na pergunta "qual dos dois
você aprovaria?".
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
    # um unico tamanho de fonte por caixa de texto
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

out = ROOT / "docs" / "aula-02"
out.mkdir(parents=True, exist_ok=True)
dest = out / "AI-Talent-Academy-Aula02.pptx"
prs.save(dest)
print(f"OK: {dest}  ({_n['i']} slides)  Roboto, sem travessões, tamanho único por bloco.")
