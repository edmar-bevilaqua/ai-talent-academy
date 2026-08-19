# -*- coding: utf-8 -*-
"""
Gerador do deck da Aula 4 (Semana 2, quinta-feira) do AI Talent Academy.

Tema: GenAI na pratica. Segundo laboratorio do programa e a primeira aula com codigo.
Demonstracao curta (20 min: API, endpoint, SDK) seguida de mao na massa no Google Colab.

Identidade visual: padrao White Cube (Roboto, azul 28347B, fundos e logo do template
oficial em assets/whitecube/).

Uso:  python scripts/gerar_slides_aula04.py
Saida: docs/aula-04/AI-Talent-Academy-Aula04.pptx

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
Slide projetado desde 18h55. Enquanto a sala enche, fale a cada 2 ou 3 minutos:
"Boa noite! Hoje é a segunda quinta-feira do programa, e tem uma novidade: código.
Enquanto a sala enche, se puder, já abra o Colab pelo link fixado no Discord."

Não comece antes de 19h08.
""",
      """
- Microfones em mudo, câmeras opcionais.
- Confirme a GRAVAÇÃO antes de 19h10.
- CRÍTICO HOJE: confirme que o link do Colab está fixado no canal do Discord ANTES de 19h00.
- Confirme que a chave de acesso da API está distribuída ou embutida no notebook.
""")

s = sl_bullets("Enquanto todo mundo entra", "Hoje tem código pela primeira vez",
               [("Hoje é a segunda quinta do programa", "mesmo formato de sempre: pouca teoria, muita prática"),
                ("A novidade de hoje é o código", "vocês vão fazer a primeira chamada de IA generativa"),
                ("Precisa só de uma conta Google", "o Colab roda inteiro no navegador, sem instalar nada"),
                ("Abra o Colab agora, se puder", "o link está fixado no Discord, no canal desta aula"),
                ("Tenha o notebook com você", "hoje não dá para acompanhar pelo celular"),
                ("Escreva no chat", "seu nome e se essa é a primeira vez que você vê uma linha de código")],
               subtitle="Aula 4 · Semana 2 · começamos 19h10")
notes(s, "19h00 às 19h10", "ESSENCIAL", EU,
      """
Leia os itens uma vez, por volta de 19h05. O objetivo é baixar a ansiedade de quem
nunca programou.

Insista no item do notebook: quem só tem celular precisa saber agora, não às 19h30.
""")

# ==========================================================================
# BLOCO A: GenAI na prática (19h10 às 19h30)
# ==========================================================================
s = sl_section("01", "GenAI na prática", "Três conceitos antes de abrir o Colab",
               "19h10 às 19h30  ·  20 minutos")
notes(s, "19h10 às 19h30 (20 min)", "ESSENCIAL", EU,
      """
Bloco curto de propósito, focado em dar vocabulário suficiente para que ninguém fique
perdido quando o Felipe abrir o Colab.

ESTRUTURA:
  O que é uma API              6 min
  O endpoint                   6 min
  SDK                          6 min
  Transição para o Colab       2 min

Ritmo rápido, sem pausa para pergunta longa. As dúvidas técnicas aparecem melhor
depois, com o código na tela.
""")

s = sl_bullets("GenAI na prática", "O que é uma API",
               [("API é um contrato de conversa entre dois programas", "você manda um pedido num formato combinado, e recebe a resposta nesse mesmo formato"),
                ("Pense num balcão de atendimento", "você não entra na cozinha do restaurante, entrega o pedido e o balcão traz o prato pronto"),
                ("O modelo de linguagem mora num servidor de outra empresa", "a API é a porta de entrada desse servidor"),
                ("Cada provedor define suas próprias regras", "que informação enviar, em que formato, e o que volta como resposta")],
               subtitle="Hoje vocês vão bater nessa porta pela primeira vez, direto do Colab.")
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Primeiro conceito: API. Sigla para interface de programação de aplicações, mas o nome
não ajuda muito. Pensem assim: API é um contrato de conversa entre dois programas. Você
manda um pedido num formato combinado, e recebe a resposta nesse mesmo formato.

Uma analogia que ajuda: pensem num balcão de atendimento. Vocês não entram na cozinha do
restaurante para pegar o prato. Entregam o pedido no balcão, e o balcão traz pronto.

O modelo de linguagem que vocês vão usar hoje mora num servidor de outra empresa. A API
é a porta de entrada desse servidor. E cada provedor define suas próprias regras: que
informação mandar, em que formato, e o que volta como resposta."
""")

s = sl_bullets("GenAI na prática", "O endpoint é o endereço da chamada",
               [("O endpoint é o link exato dentro da API", "geralmente um endereço que começa com https"),
                ("Junto do link vai uma chave de acesso", "ela identifica quem está fazendo o pedido, e evita uso indevido"),
                ("E vai o corpo do pedido", "o texto que vocês querem que o modelo responda, dentro de um pacote estruturado"),
                ("A resposta chega nesse mesmo formato estruturado", "o código extrai só o texto que interessa, e descarta o resto")],
               subtitle="Endereço, chave e pergunta. É só isso que uma chamada de LLM carrega.")
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Segundo conceito: endpoint. É o link exato dentro da API para onde vocês mandam o
pedido, geralmente um endereço que começa com https.

Junto do link vai uma chave de acesso, que identifica quem está fazendo o pedido e evita
uso indevido. Guardem essa chave como uma senha, ela não deve aparecer publicada em
nenhum lugar.

E vai o corpo do pedido: o texto que vocês querem que o modelo responda, dentro de um
pacote estruturado. A resposta chega nesse mesmo formato, e o código extrai só o texto
que interessa.

Endereço, chave e pergunta. É só isso que uma chamada de LLM carrega."
""",
      "Reforce em voz alta: a chave de acesso nunca vai num repositório público. É a primeira regra de segurança que eles levam.")

s = sl_bullets("GenAI na prática", "Um SDK faz esse trabalho por vocês",
               [("SDK é um pacote Python que já sabe montar a chamada", "vocês não escrevem o endereço, a chave e o formato à mão toda vez"),
                ("Instala uma vez com pip install", "e importa no código com um simples import"),
                ("O que seria um bloco inteiro de configuração vira uma função", "chamar o modelo passa a ser uma linha de código"),
                ("É o caminho que vocês vão usar hoje no Colab", "o SDK cuida da parte repetitiva, vocês cuidam do prompt")],
               subtitle="Dá para chamar uma API sem SDK, na unha. Hoje vocês começam pelo caminho mais rápido.")
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Terceiro conceito, e o último antes do código: SDK. É um pacote Python que já sabe
montar a chamada. Vocês não escrevem o endereço, a chave e o formato à mão toda vez.

Instala uma vez com pip install, e importa no código com um simples import. O que seria
um bloco inteiro de configuração vira uma função.

É o caminho que vocês vão usar hoje no Colab. Dá para chamar uma API sem SDK, na unha,
escrevendo o pedido inteiro à mão. Hoje vocês começam pelo caminho mais rápido, e quando
fizer sentido, a gente mostra o caminho manual também, mais para frente no programa.

Passo o Felipe agora. Ele vai abrir o Colab de verdade e mostrar cada um desses três
conceitos aparecendo na tela."
""")

# ==========================================================================
# BLOCO B: Mão na massa, Colab (19h30 às 20h45)
# ==========================================================================
s = sl_section("02", "Agora é com vocês", "Primeira chamada de LLM, dentro do Colab",
               "19h30 às 20h45  ·  75 minutos")
notes(s, "19h30 às 20h45 (75 min)", "ESSENCIAL", FELIPE,
      """
Bloco principal da noite. Estrutura:
  Como vai funcionar a próxima hora     5 min
  O roteiro do notebook                 5 min
  Mão na massa, individual             65 min

Hoje o trabalho muda de formato: cada um no próprio notebook, no próprio ritmo, diferente
do trabalho em grupo da quinta passada. Eu e o Edmar circulamos pelo chat.
""")

s = sl_cards("Antes de começar", "Como vai funcionar a próxima hora",
             [("O link já está no Discord",
               "O notebook do Colab está fixado no canal desta aula.\n\nAbra com a mesma conta Google que você já usa."),
              ("O trabalho é individual",
               "Cada um roda o próprio notebook, no próprio ritmo.\n\nTravar é normal, a maioria do grupo vai passar por isso em algum momento."),
              ("A gente circula pelo chat",
               "Eu e o Edmar respondemos direto no chat da aula.\n\nEscreva o número da célula onde travou."),
              ("Sem pressa para terminar tudo",
               "O objetivo de hoje é rodar a primeira chamada. Terminar o notebook inteiro pode ficar para depois.")],
             cols=2, card_h=2.9)
notes(s, "5 min", "ESSENCIAL", FELIPE,
      """
"Vamos para a parte prática. Quatro avisos antes de começarmos.

Primeiro: o link do notebook já está fixado no Discord, no canal desta aula. Abram com a
mesma conta Google que vocês já usam para o Colab.

Segundo: hoje o trabalho é individual, diferente da quinta passada. Cada um no próprio
ritmo.

Terceiro: eu e o Edmar vamos estar direto no chat. Se travarem, escrevam o número da
célula onde travaram, isso acelera muito a nossa resposta.

Quarto, e esse é o mais importante: não tem pressa para terminar o notebook inteiro. O
objetivo de hoje é rodar a primeira chamada de verdade. Se você chegar só até ali, a
noite já cumpriu o que precisava cumprir."
""",
      "AÇÃO DO MODERADOR: fixar o link do Colab no topo do chat exatamente neste slide.")

s = sl_bullets("O roteiro do notebook", "O que as próximas células vão pedir",
               [("Instalar o SDK", "uma célula de pip install, já pronta para rodar"),
                ("Guardar a chave de acesso", "a chave de uma API gratuita de LLM, já fornecida no notebook"),
                ("Fazer a primeira chamada", "usando os cinco elementos de prompt da última segunda"),
                ("Repetir com temperatura diferente", "para ver ao vivo o que muda na resposta"),
                ("Anotar o que surpreendeu", "vocês vão usar essa anotação no fechamento de hoje")],
               subtitle="Nenhuma etapa exige escrever código do zero. Vocês editam o que já está lá.")
notes(s, "5 min", "ESSENCIAL", FELIPE,
      """
"O notebook tem cinco partes, nessa ordem: instalar o SDK, guardar a chave de acesso,
fazer a primeira chamada, repetir com temperatura diferente, e anotar o que surpreendeu.

Ninguém vai escrever código do zero. Vocês editam o que já está lá, principalmente o
texto do prompt. É ali que entram os cinco elementos que o Edmar ensinou na segunda:
papel, tarefa, contexto, formato e restrição.

Guardem a última parte: anotar o que surpreendeu. A gente usa isso daqui a pouco, no
fechamento."
""")

s = sl_statement("Mão na massa", "65 minutos.\nVocês voltam para cá às 20h45.",
                 "Travou? Escreva no chat principal com o número da célula. A gente entra no seu Colab.")
notes(s, "20h00 às 20h45 (65 min)", "ESSENCIAL", "os dois",
      """
Este slide fica projetado na sala principal durante toda a atividade.

CHECKLIST DA DUPLA DURANTE OS 65 MINUTOS:

Minuto 0 a 10:  conferir no chat quem já instalou o SDK e quem travou no início.
Minuto 10 a 40: responder o chat em tempo real. Priorizar quem nunca programou antes.
Minuto 40 a 55: mandar aviso geral, "faltam 10 minutos, foco em rodar a primeira chamada".
Minuto 55 a 65: aviso de 5 minutos e reforçar que dá para continuar em casa depois.

SE ALGUÉM TRAVAR NA INSTALAÇÃO DO SDK:
Pergunte se está rodando no Colab mesmo, e não numa cópia local. É o erro mais comum.

SE ALGUÉM TERMINAR CEDO:
Peça para repetir a chamada mudando um dos cinco elementos do prompt, e comparar as duas
respostas lado a lado.
""")

# ==========================================================================
# BLOCO C: Encerramento (20h45 às 21h00)
# ==========================================================================
s = sl_section("03", "Encerramento", "O que vocês levam de hoje e o que vem na semana 3",
               "20h45 às 21h00  ·  15 minutos")
notes(s, "20h45 às 21h00 (15 min)", "ESSENCIAL", FELIPE,
      """
DISTRIBUIÇÃO:
  Ouvir o que surpreendeu   5 min  (pedir 3 ou 4 respostas direto no chat)
  Recapitulação             3 min
  O que vem na semana 3     3 min
  Q&A                       3 min
  Fechamento                1 min

Ao pedir relatos, puxe pelo chat: "quem quer colar aqui o que anotou como surpresa?"
Não force ninguém a abrir câmera ou microfone para isso.
""")

s = sl_bullets("O que a gente viu hoje", "Cinco ideias para levar da segunda quinta",
               [("Uma API é um contrato de conversa entre programas", "hoje vocês usaram um pela primeira vez"),
                ("O endpoint carrega três coisas", "endereço, chave de acesso e o texto do pedido"),
                ("Um SDK poupa o trabalho manual", "e foi o caminho que vocês usaram no Colab"),
                ("Prompt bem montado muda a resposta", "os cinco elementos da última segunda apareceram na prática hoje"),
                ("Temperatura muda o quanto a resposta varia", "baixa repete, alta arrisca")],
               subtitle="Se você levar só essas cinco frases, a noite cumpriu o objetivo.",
               numbered=True)
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Cinco ideias para levar de hoje.

A primeira: uma API é um contrato de conversa entre programas, e hoje vocês usaram um
pela primeira vez.

O endpoint carrega três coisas: endereço, chave de acesso e o texto do pedido.

Um SDK poupa o trabalho manual, e foi o caminho que vocês usaram no Colab.

Prompt bem montado muda a resposta. Os cinco elementos que o Edmar ensinou na segunda
apareceram na prática hoje, dentro do código de vocês.

E fecha com a temperatura: baixa repete, alta arrisca. Vocês viram isso ao vivo, não só
ouviram a explicação."
""")

s = sl_two_col("Próximos encontros", "O que vem pela frente",
               "SEGUNDA · Semana 3",
               ["A linguagem que fala direto com banco de dados",
                "Como transformar uma pergunta em consulta",
                "Ainda conceitual, como toda segunda",
                "Primeira ferramenta técnica do programa"],
               "QUINTA · Semana 3",
               ["Primeiro contato com SQL de verdade",
                "Consultas na prática, com dados reais",
                "Mesmo formato de hoje: demonstração e mão na massa"],
               subtitle="A partir da semana 3 entra a primeira ferramenta técnica do programa.")
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"O que vem pela frente.

Segunda que vem, semana 3: a linguagem que fala direto com banco de dados. Como
transformar uma pergunta de negócio numa consulta. Ainda conceitual, como toda segunda.

E na quinta da semana 3, primeiro contato de verdade com ela, consultando dados reais.
Mesmo formato de hoje: a gente demonstra, e depois vocês fazem."
""")

s = sl_statement("Antes de ir", "Perguntas?",
                 "Escreva no chat. O que não der tempo, respondemos no Discord ainda hoje.")
notes(s, "3 min", "ESSENCIAL", f"{FELIPE} + {EU}",
      """
PERGUNTAS PREVISÍVEIS DE HOJE:

- "Preciso saber programar para acompanhar?"
  Não. Hoje vocês só editaram o que já estava pronto no notebook.

- "A API que usamos hoje é a mesma que vou usar depois no programa?"
  Ainda não é definitivo. A confirmação sai no Discord antes da próxima aula com código.

- "Posso continuar meu notebook em casa?"
  Sim. Ele fica salvo na sua conta Google, e dá para reabrir quando quiser.

- "Isso vale nota?"
  Não hoje. É treino.

- "Perdi a aula de segunda, consigo acompanhar os cinco elementos de prompt?"
  Sim. A gravação e o material de apoio da Aula 3 estão no Discord.
""")

s = sl_closing()
notes(s, "1 min", "ESSENCIAL", FELIPE,
      """
FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. Foi a primeira vez que a maioria de vocês rodou uma linha
de código, e boa parte também foi a primeira chamada de LLM da vida. Isso fica.

O notebook continua salvo na sua conta Google, entrem quando quiserem revisitar.

Nos vemos na segunda. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Recolher no chat quantas pessoas relataram travar na instalação do SDK, para calibrar
  o próximo notebook.
- 10 minutos de retrospectiva entre os dois: quantas pessoas nunca tinham programado
  antes, e como reagiram.
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

out = ROOT / "docs" / "aula-04"
out.mkdir(parents=True, exist_ok=True)
dest = out / "AI-Talent-Academy-Aula04.pptx"
prs.save(dest)
print(f"OK: {dest}  ({len(prs.slides._sldIdLst)} slides)  "
      f"Roboto, sem travessões, tamanho único por bloco.")
