# -*- coding: utf-8 -*-
"""
Gerador do deck da Aula 3 (Semana 2, segunda-feira) do AI Talent Academy.

Tema: IA Generativa. Aula expositiva de ~3h10, sem mao na massa
(esticou 11 min alem do previsto para caber banco vetorial e fine-tuning).

Identidade visual: padrao White Cube (Roboto, azul 28347B, fundos e logo do template
oficial em assets/whitecube/).

Uso:  python scripts/gerar_slides_aula03.py
Saida: docs/aula-03/AI-Talent-Academy-Aula03.pptx

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
Slide projetado desde 18h55. Fale a cada 2 ou 3 minutos enquanto a sala enche.

"Boa noite! Segunda aula da semana 2, e hoje a noite inteira é sobre IA generativa.
Enquanto todo mundo entra, escreve no chat: qual foi a última coisa que você pediu para
uma IA fazer? Pode ser qualquer coisa."

Não comece antes de 19h08.
""",
      """
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- Moderador com o link do Discord pronto para colar.
- Guardar 3 ou 4 respostas boas do chat: elas viram exemplo no bloco 1.
""")

s = sl_bullets("Enquanto todo mundo entra", "Hoje a noite é inteira sobre IA Generativa",
               [("Áudio e câmera", "microfone no mudo, câmera fica a seu critério"),
                ("Dúvidas", "escreva no chat a qualquer momento, temos moderação acompanhando"),
                ("Gravação", "a aula é gravada e o link chega em até 24h"),
                ("Material", "slides e resumo vão para o Discord depois da aula"),
                ("Aqueça o teclado", "escreva no chat: qual foi a última coisa que você pediu para uma IA?")],
               subtitle="Aula 3 · Semana 2 · começamos 19h10")
notes(s, "19h00 às 19h10", "ESSENCIAL", EU,
      """
Leia os itens uma vez, por volta de 19h05, e insista no último. As respostas do chat
servem de material vivo para o bloco 1: quando você mostrar as seis tarefas que a GenAI
faz bem, dá para apontar quais delas apareceram no chat.
""")

# ==========================================================================
# BLOCO A: Abertura (19h10 às 19h20)
# ==========================================================================
s = sl_section("01", "Por que uma noite inteira sobre isso",
               "Onde a IA generativa entra no programa, e o que muda hoje",
               "19h10 às 19h20  ·  10 minutos")
notes(s, "19h10 às 19h20 (10 min)", "ESSENCIAL", EU,
      """
Bloco curto de contextualização. O objetivo é situar a turma no programa e justificar a
noite inteira num tema só. Ritmo rápido, 3 slides.
""")

s = sl_table("Onde estamos", "A jornada das 8 semanas",
             ["Semana", "Tema", "Foco"],
             [["1", "Fundamentos, nivelamento e panorama", "Todo mundo junto. Base comum"],
              ["2 · hoje", "IA Generativa", "LLM por dentro, prompt e limites"],
              ["3", "Análise de Dados com SQL", "Consultar e extrair. A base de toda análise"],
              ["4", "Análise de Dados com Python", "Manipular e visualizar. Storytelling com dados"],
              ["5", "Engenharia de Dados", "Construir os pipelines. Dado limpo, no lugar certo"],
              ["6", "Machine Learning", "Prever com dados. Do baseline ao modelo"],
              ["7", "Agentes de IA", "Da resposta à ação. IA que executa tarefas"],
              ["8", "Apresentação final", "Demo Day. Solução completa, do problema ao resultado"]],
             subtitle="Semana 2 de 8. A partir de hoje, cada semana pega uma ferramenta e aprofunda.",
             widths=[0.12, 0.38, 0.50])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Antes de começar, vamos situar onde vocês estão.

Na semana 1 a gente fez o panorama: o que é IA, o ciclo de vida de uma solução, e na
quinta vocês preencheram o Canvas do Problema em grupo.

Hoje começa a parte em que cada semana pega uma ferramenta e vai fundo. E a gente começou
por IA generativa de propósito, e eu explico o motivo no próximo slide.

Repara na sequência: SQL na semana 3, Python na 4, engenharia de dados na 5, machine
learning na 6, agentes na 7. Faz sentido nessa ordem, porque você precisa saber consultar
e limpar dado antes de modelar. E agentes vem no fim porque agente é a IA generativa de
hoje com ferramentas na mão."
""",
      "Este cronograma foi ajustado com as lideranças e difere da proposta original. Se alguém perguntar, é decisão combinada.")

s = sl_bullets("Por que agora", "Quatro razões para dedicar uma noite inteira",
               [("É a porta de entrada mais acessível da área", "aqui você não precisa treinar modelo, precisa saber pedir bem"),
                ("É onde estão as vagas mais novas", "o papel de AI Engineer quase não existia quatro anos atrás"),
                ("É também onde estão os piores projetos", "usar GenAI onde ela não cabe custa caro e falha em silêncio"),
                ("A semana 1 abriu a caixa e prometeu voltar", "hoje a gente volta, e desta vez vai mais fundo")],
               subtitle="Muita gente sabe usar o ChatGPT. Bem menos gente sabe quando não usar.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Por que uma noite inteira sobre IA generativa, se o programa tem oito semanas?

Primeira razão: é a porta de entrada mais acessível dessa área inteira. Para trabalhar com
machine learning você precisa de estatística, de Python, de dado limpo. Para trabalhar com
IA generativa você precisa entender o problema e saber pedir bem. A barreira técnica é
mais baixa, e isso é uma oportunidade real para quem está começando agora.

Segunda: é onde estão as vagas mais novas. Lembram do slide de carreiras da semana 1?
AI Engineer praticamente não existia quatro anos atrás.

Terceira, e essa é a que quase ninguém fala: é também onde estão os piores projetos. Tem
muita empresa gastando dinheiro usando IA generativa em problema que uma consulta de banco
resolveria melhor. E o pior é que falha em silêncio, porque a resposta sempre parece boa.

E a quarta: na semana 1 a gente abriu a caixa preta por noventa segundos e eu prometi que
a gente voltaria. Hoje a gente volta com calma."
""")

s = sl_cards("O plano da noite", "O que você leva daqui",
             [("Entender o que acontece por dentro",
               "Token, embedding e atenção explicados sem fórmula e sem código.\n\nDepois disso, o comportamento estranho dele para de ser mistério."),
              ("Saber escrever um pedido que funciona",
               "Os cinco elementos de um prompt, três técnicas que funcionam, e os mitos que circulam por aí."),
              ("Reconhecer onde ela resolve",
               "Os sinais de que o seu problema é bom candidato para GenAI, com exemplos de aplicação real."),
              ("Reconhecer onde ela atrapalha",
               "Os sinais de que você deveria usar outra coisa. Este é o que mais economiza dinheiro.")],
             subtitle="Quatro blocos, com intervalo de 15 minutos no meio.", cols=4, card_h=3.4)
notes(s, "3 min", "ESSENCIAL", EU,
      """
"A noite tem quatro blocos.

O primeiro é IA generativa na prática: o que ela faz de verdade hoje, com aplicações
concretas de trabalho.

O segundo abre a caixa preta: token, embedding e atenção. Sem fórmula, sem código. E eu
garanto que depois desse bloco o comportamento estranho dele para de ser mistério.

Aí a gente faz o intervalo, e o Felipe assume.

O terceiro bloco é sobre prompt e contexto: como escrever um pedido que funciona, quais
técnicas funcionam, e quais são folclore de internet.

E o quarto fecha com a parte que mais pesa na carreira de vocês: onde a GenAI resolve e
onde ela atrapalha. Esse é o bloco que economiza dinheiro de empresa."
""")

# ==========================================================================
# BLOCO B: IA Generativa na prática (19h20 às 19h55)
# ==========================================================================
s = sl_section("02", "IA Generativa na prática",
               "O que ela faz de verdade hoje, no trabalho de verdade",
               "19h20 às 19h55  ·  35 minutos")
notes(s, "19h20 às 19h55 (35 min)", "ESSENCIAL", EU,
      """
Bloco de motivação e repertório. A meta é sair daqui com a turma sabendo nomear as tarefas
que a GenAI faz bem, com exemplo de trabalho para cada uma.

ESTRUTURA:
  As quatro famílias                    4 min
  Os seis verbos                        8 min
  Tabela de aplicações reais            8 min
  Caso aprofundado: triagem             6 min
  O que mudou de verdade                4 min
  Interação                             3 min

Controle: às 19h40 você precisa estar na tabela de aplicações.
""")

s = sl_statement("Três anos",
                 "A IA generativa saiu de curiosidade de laboratório\npara ferramenta de trabalho diária.",
                 "E a maior parte das empresas ainda usa ela como brinquedo caro.")
notes(s, "2 min", "ESSENCIAL", EU,
      """
"Vamos começar com uma constatação.

Em três anos, a IA generativa saiu de curiosidade de laboratório para ferramenta de
trabalho diária. Isso é rápido demais. Nenhuma tecnologia recente entrou tão rápido na
rotina de tanta gente.

E aí vem a segunda parte, que é a que interessa para vocês: a maior parte das empresas
ainda usa ela como brinquedo caro. Assinam a licença, mandam todo mundo usar, e ninguém
mede se melhorou alguma coisa.

A diferença entre brincar e trabalhar com isso está em saber exatamente que tarefa você
está entregando para ela. É disso que trata este bloco."
""")

s = sl_cards("O território", "Quatro famílias de IA generativa",
             [("Texto",
               "Escreve, resume, classifica, traduz, extrai informação de documento.\n\nÉ a família mais madura e a que mais aparece no trabalho de escritório."),
              ("Imagem",
               "Gera e edita imagem a partir de descrição.\n\nUsada em marketing, design de produto e prototipagem visual."),
              ("Áudio e voz",
               "Transcreve reunião, gera narração, clona timbre de voz.\n\nA transcrição já é confiável o suficiente para uso profissional."),
              ("Código",
               "Sugere trecho, explica erro, escreve teste, traduz entre linguagens.\n\nÉ onde o ganho de produtividade é mais fácil de medir.")],
             subtitle="Hoje a gente foca em texto, que é a família que mais aparece no trabalho de dados.",
             cols=4, card_h=3.4)
notes(s, "3 min", "ESSENCIAL", EU,
      """
"IA generativa não é uma coisa só. São quatro famílias, e elas amadureceram em ritmos
diferentes.

Texto é a mais madura: escreve, resume, classifica, traduz, extrai informação de
documento. É a que mais aparece em trabalho de escritório.

Imagem gera e edita a partir de descrição. Marketing e design usam bastante.

Áudio e voz transcreve reunião, gera narração, e hoje já clona timbre de voz. A parte de
transcrição já está boa o suficiente para uso profissional de verdade.

E código: sugere trecho, explica erro, escreve teste. É onde o ganho de produtividade é
mais fácil de medir, porque dá para contar quantas linhas foram aceitas.

Hoje a gente foca em texto, porque é a família que mais encosta no trabalho de dados."
""")

s = sl_cards("O que ela faz bem", "Seis verbos que resolvem quase tudo",
             [("Resumir",
               "Reduzir texto longo mantendo o que importa.\n\nAta de reunião, thread de e-mail, relatório de 40 páginas."),
              ("Classificar",
               "Ler um texto e dizer em qual categoria ele cai.\n\nMotivo do chamado, sentimento da avaliação, tipo de documento."),
              ("Extrair",
               "Tirar campos estruturados de texto bagunçado.\n\nValor e vencimento de uma nota, partes de um contrato."),
              ("Transformar",
               "Reescrever mudando formato, tom ou público.\n\nTexto técnico para linguagem de negócio, tabela para parágrafo."),
              ("Gerar",
               "Produzir a primeira versão de alguma coisa.\n\nRascunho de e-mail, descrição de produto, roteiro de teste."),
              ("Conversar",
               "Responder pergunta em linguagem natural, com contexto.\n\nBusca interna, assistente de suporte, tira-dúvidas de manual.")],
             subtitle="Se a sua tarefa não cabe em um destes seis verbos, desconfie antes de escolher GenAI.",
             cols=3)
notes(s, "8 min", "ESSENCIAL, slide-âncora do bloco", EU,
      """
Este é o slide mais prático do bloco. Vá com calma, e conecte com o que apareceu no chat
na abertura.

"Estes seis verbos cobrem quase tudo que a IA generativa faz bem em trabalho de verdade.
Eu recomendo que vocês anotem.

RESUMIR: pegar texto longo e reduzir mantendo o que importa. Ata de reunião, aquela thread
de e-mail com quarenta respostas, relatório de quarenta páginas.

CLASSIFICAR: ler um texto e dizer em que categoria ele cai. Qual o motivo daquele chamado
de suporte, se a avaliação do cliente é positiva ou negativa, que tipo de documento é
aquele. Isso aqui é ouro em operação, e volta no próximo slide.

EXTRAIR: tirar campo estruturado de texto bagunçado. Você tem mil notas fiscais em PDF e
quer valor, data e fornecedor numa tabela. Antes isso exigia um sistema por tipo de
documento.

TRANSFORMAR: reescrever mudando formato, tom ou público. Pegar um texto técnico e virar
linguagem de negócio para a diretoria.

GERAR: produzir a primeira versão. Rascunho de e-mail, descrição de produto.

CONVERSAR: responder pergunta em linguagem natural, com contexto. É a busca interna da
empresa, o assistente de suporte.

E a linha de baixo é a régua que eu quero deixar com vocês: se a sua tarefa não cabe em um
desses seis verbos, desconfie antes de escolher IA generativa. Provavelmente o problema
pede outro degrau da escada."
""",
      "Se guardou respostas do chat na abertura, aponte quais verbos apareceram: cria conexão imediata.")

s = sl_table("Aplicação real", "Onde isso vira trabalho, e o cuidado de cada um",
             ["Aplicação", "O que a GenAI faz", "O cuidado principal"],
             [["Triagem de chamados", "Lê o texto e classifica motivo e urgência", "Classe errada manda o cliente para a fila errada"],
              ["Extração de documento", "Tira campos de contrato, nota fiscal, laudo", "Documento com valor legal exige conferência humana"],
              ["Resumo de reunião", "Transcreve e devolve tópicos e ações", "Nome próprio e número são onde ele mais erra"],
              ["Copiloto de código", "Sugere trecho, explica erro, escreve teste", "Código sugerido passa na revisão como qualquer outro"],
              ["Busca interna", "Responde com base nos documentos da empresa", "Sem mostrar a fonte, ninguém confia na resposta"],
              ["Primeira versão de texto", "Rascunho de e-mail, proposta, descrição", "Rascunho é ponto de partida, e alguém assina no final"]],
             subtitle="Repare que toda linha tem um cuidado. Nenhuma dessas aplicações roda sozinha.",
             widths=[0.24, 0.38, 0.38])
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Agora, onde isso vira trabalho de verdade. Seis aplicações que vocês vão encontrar em
qualquer empresa que esteja levando isso a sério.

Triagem de chamados: o modelo lê o texto do chamado e classifica motivo e urgência. O
cuidado é que classe errada manda o cliente para a fila errada, e ele espera mais.

Extração de documento: tira campo de contrato, nota, laudo. Cuidado com documento de valor
legal, que exige conferência humana antes de virar decisão.

Resumo de reunião: transcreve e devolve tópicos e ações. E aqui um detalhe que vocês vão
encontrar na prática: nome próprio e número são exatamente onde ele mais erra. Ele troca
nome parecido e erra valor. Confira sempre essas duas coisas.

Copiloto de código: sugere trecho, explica erro, escreve teste. O cuidado é cultural:
código sugerido por IA passa na revisão como qualquer outro código. Não entra direto.

Busca interna: responde pergunta com base nos documentos da empresa. E o cuidado aqui
define se o projeto vive ou morre: sem mostrar a fonte junto com a resposta, ninguém
confia. A gente volta nisso no bloco do Felipe.

Primeira versão de texto: rascunho. E rascunho é ponto de partida. Alguém assina no final,
e essa pessoa é responsável pelo que está escrito.

Repara numa coisa: toda linha tem um cuidado. Nenhuma dessas aplicações roda sozinha."
""")

s = sl_two_col("Caso aprofundado", "Triagem de chamados, antes e depois",
               "ANTES, SEM GenAI",
               ["Chamado chega em texto livre, escrito pelo cliente",
                "Um atendente lê e escolhe a categoria na mão",
                "Cada pessoa classifica com critério próprio",
                "A fila cresce mais rápido do que a triagem anda",
                "Relatório de motivo sai errado, porque a categoria é subjetiva"],
               "DEPOIS, COM GenAI",
               ["O modelo lê o texto e sugere motivo e urgência",
                "O atendente confirma ou corrige, em vez de escolher do zero",
                "O critério fica igual para todo mundo, porque é o mesmo prompt",
                "A fila anda mais rápido, e o caso urgente sobe na hora",
                "As correções viram material para melhorar o prompt"],
               subtitle="O ganho não foi tirar o humano. Foi trocar a tarefa dele de escolher para conferir.",
               lcolor=MUTED, rcolor=NAVY)
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Vamos aprofundar uma dessas, porque ela mostra bem como o ganho aparece.

Triagem de chamados, antes. O chamado chega em texto livre, escrito pelo cliente do jeito
que ele conseguiu explicar. Um atendente lê e escolhe a categoria na mão. E aí começa o
problema: cada pessoa classifica com critério próprio. O que para um é 'problema técnico',
para outro é 'dúvida de uso'. A fila cresce mais rápido do que a triagem anda. E no fim do
mês o relatório de motivos sai errado, porque a categoria nunca foi consistente.

Depois. O modelo lê o texto e sugere motivo e urgência. O atendente confirma ou corrige,
em vez de escolher do zero. Repara que o critério agora fica igual para todo mundo, porque
é o mesmo prompt rodando em todos os chamados. A fila anda mais rápido e o caso urgente
sobe na hora. E as correções que o atendente faz viram material para melhorar o prompt.

E aqui está a leitura que eu quero que vocês levem, que está na linha de baixo: o ganho
não foi tirar o humano do processo. Foi trocar a tarefa dele. Ele parou de escolher do
zero e passou a conferir. Conferir é muito mais rápido do que decidir."
""")

s = sl_statement("O que mudou de verdade",
                 "A IA generativa não baixou o custo de pensar.\nEla baixou o custo da primeira versão.",
                 "Quem entende isso usa ela como rascunho. Quem não entende usa como resposta final.")
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Se vocês forem levar uma frase deste bloco, que seja esta.

A IA generativa não baixou o custo de pensar. Ela baixou o custo da PRIMEIRA VERSÃO.

Pensa no que isso significa na prática. Antes, escrever o primeiro rascunho de qualquer
coisa custava caro em tempo e em energia mental. A folha em branco trava. Hoje o rascunho
sai em segundos.

Mas decidir se aquele rascunho está certo, se faz sentido para o seu contexto, se o número
ali confere: isso continua custando exatamente o mesmo que custava antes. Ninguém terceirizou
essa parte.

Quem entende isso usa a ferramenta como rascunho e revisa. Quem não entende usa como
resposta final, e é assim que aparece petição com jurisprudência inventada. Lembram do caso
de Londrina, da semana 1?"
""")

s = sl_interaction("Interação", "Antes de abrir a caixa preta",
                   "Qual desses seis verbos você usaria hoje, no seu trabalho ou estudo?",
                   ["Resumir   ·   Classificar   ·   Extrair",
                    "Transformar   ·   Gerar   ·   Conversar",
                    "Responda na enquete, 30 segundos",
                    "Guarde a sua resposta: no último bloco a gente testa se ela sobrevive"])
notes(s, "3 min", "DESCARTÁVEL", EU,
      """
"Antes de a gente abrir a caixa preta, uma pergunta rápida. Dos seis verbos, qual você
usaria hoje, no seu trabalho ou no seu estudo?"

[aguarde 30 a 45 segundos e comente o resultado]

Comente o vencedor. Se "resumir" ou "gerar" ganharem, é o padrão esperado, e vale dizer
que classificar e extrair costumam gerar mais valor em operação, mesmo sendo menos
lembrados.

Feche com o gancho: "Guardem a resposta de vocês. No último bloco a gente vai testar se
ela sobrevive à pergunta de quando NÃO usar."
""",
      "Enquete nativa da plataforma. Ver o plano de interação da aula 1 para a configuração.")

# ==========================================================================
# BLOCO C: Como um LLM funciona por dentro (19h55 às 20h30)
# ==========================================================================
s = sl_section("03", "Como um LLM funciona por dentro",
               "Token, embedding e atenção. Sem fórmula e sem código",
               "19h55 às 20h30  ·  35 minutos")
notes(s, "19h55 às 20h30 (35 min)", "ESSENCIAL", EU,
      """
Bloco mais técnico da noite. A meta é que a turma saia entendendo o mecanismo bem o
suficiente para explicar por que ele alucina, por que ele esquece e por que ele responde
diferente para a mesma pergunta.

REGRA DESTE BLOCO: nenhuma fórmula, nenhuma matriz, nenhum código. Só analogia concreta.
Se você sentir vontade de escrever "vetor de 768 dimensões" na lousa, respire.

ESTRUTURA:
  Recap da semana 1                     3 min
  Token                                 4 min
  Embedding                             8 min
  Atenção                               8 min
  Como o texto sai                      4 min
  Temperatura e treino                  5 min
  Agora a alucinação faz sentido        3 min
""")

s = sl_bullets("De onde a gente parou", "O que a semana 1 disse, em 90 segundos",
               [("Ele quebra o texto em pedaços chamados tokens", "e trabalha só com esses pedaços"),
                ("O que ele aprendeu a fazer é prever o próximo token", "uma coisa só, repetida milhões de vezes"),
                ("Não existe banco de respostas dentro dele", "ele compõe a resposta, em vez de consultar"),
                ("Por isso ele às vezes inventa com confiança", "ele sabe o que soa provável, e provável difere de verdadeiro"),
                ("Hoje a gente abre cada uma dessas três caixas", "token, o que ele faz com o token, e como ele decide")],
               subtitle="Se você faltou na semana 1, este slide é tudo que você precisa para acompanhar hoje.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Rápido, para quem faltou na semana 1 e para refrescar a memória de quem estava aqui.

A gente viu que o modelo quebra o texto em pedaços chamados tokens, e que a única coisa
que ele aprendeu a fazer é prever qual é o próximo token mais provável. Uma coisa só,
repetida milhões de vezes.

E a consequência disso: não existe um banco de respostas dentro dele. Ele COMPÕE a
resposta na hora, em vez de consultar. Por isso ele às vezes inventa com uma confiança
absoluta.

Isso foi o que a gente falou em noventa segundos, na semana passada. Hoje a gente abre
cada uma dessas caixas: o que é um token de verdade, o que ele faz com esse token, e como
ele decide qual vem depois."
""")

s = sl_bullets("Peça 1 de 3 · Token", "Como o texto vira número",
               [("O modelo não lê letra, nem palavra inteira", "ele lê pedaços de palavra, chamados tokens"),
                ("Em português, uma palavra costuma virar 2 ou 3 tokens", "\"inteligência\" vira mais de um pedaço"),
                ("Palavra comum vira 1 token, palavra rara vira vários", "por isso texto técnico consome mais"),
                ("Cada token vira um número de identificação", "e é com esse número que a máquina trabalha"),
                ("Isso importa no bolso e no limite", "preço de API e tamanho da janela são contados em token, não em palavra"),
                ("Português gasta mais token que inglês", "o mesmo texto traduzido pode custar 30% a mais")],
               subtitle="Token é a unidade de conta desse mundo. Preço, limite e velocidade se medem nela.")
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Peça número um: token.

O modelo não lê letra, e não lê palavra inteira. Ele lê pedaços de palavra. Esses pedaços
se chamam token.

Em português, uma palavra costuma virar dois ou três tokens. Uma palavra muito comum, tipo
'casa', vira um token só. Uma palavra rara ou técnica vira vários pedaços.

Cada token vira um número de identificação, e é com esse número que a máquina trabalha
daqui para a frente. O texto some, ficam os números.

E agora a parte que importa no bolso de vocês: preço de API e tamanho da janela de contexto
são contados em TOKEN, não em palavra. Quando alguém disser que um modelo aceita duzentos
mil tokens, isso equivale a bem menos que duzentas mil palavras.

E tem um detalhe que afeta a gente diretamente: português gasta mais token que inglês. O
mesmo texto traduzido pode custar uns trinta por cento a mais. Quem for construir produto
com isso precisa saber."
""")

s = sl_bullets("Peça 2 de 3 · Embedding", "Como o número vira significado",
               [("Pensa em cor: toda cor vira três números", "vermelho é 255, 0, 0. É a coordenada dele"),
                ("Cores parecidas têm números parecidos", "vermelho e vinho ficam perto no mapa de cores"),
                ("Palavra funciona igual, com centenas de coordenadas", "em vez de 3 números, são centenas"),
                ("Palavras de sentido próximo caem perto no mapa", "\"demitir\", \"desligar\" e \"rescindir\" viram vizinhas"),
                ("Isso permite buscar por significado, não por letra", "procurar \"demissão\" acha um texto que só fala em \"desligamento\""),
                ("É o que faz busca interna e RAG funcionarem", "e o Felipe volta nisso depois do intervalo")],
               subtitle="Embedding é o mapa onde significado vira distância. Perto quer dizer parecido.")
notes(s, "8 min", "ESSENCIAL, conceito mais difícil da noite", EU,
      """
Vá devagar. Use a analogia da cor até a turma acompanhar, e só depois pule para palavra.

"Peça número dois, e essa é a mais difícil da noite. Embedding.

Vamos começar com cor, que todo mundo entende. Toda cor na tela do computador vira três
números: quanto de vermelho, quanto de verde, quanto de azul. Vermelho puro é 255, 0, 0.
Isso é a coordenada daquela cor.

E repara numa coisa: cores parecidas têm números parecidos. Vermelho e vinho ficam perto
nesse mapa de três dimensões. Vermelho e azul ficam longe. A distância entre os números
representa a semelhança entre as cores.

Palavra funciona exatamente igual, com uma diferença: em vez de três números, são
centenas. Cada palavra vira uma coordenada num mapa de centenas de dimensões. Ninguém
consegue desenhar isso, e tudo bem, porque a ideia é a mesma.

E o que acontece nesse mapa é bonito: palavras de sentido próximo caem perto. 'Demitir',
'desligar' e 'rescindir' viram vizinhas, mesmo sem ter uma letra em comum.

Agora, por que isso importa para vocês na prática. Isso permite buscar por SIGNIFICADO, e
não por letra. Você procura por 'demissão' e o sistema acha um documento que só usa a
palavra 'desligamento'. Busca tradicional nunca acharia.

E é exatamente isso que faz a busca interna da empresa funcionar. O Felipe vai voltar
nisso depois do intervalo, quando falar de RAG."
""",
      "Se alguém perguntar de \"rei menos homem mais mulher igual rainha\": é real, é o exemplo clássico, mas só use se sobrar tempo.")

s = sl_bullets("Peça 3 de 3 · Atenção", "O problema que ela resolve",
               [("Leia: \"o prefeito negou a licença aos manifestantes\"", "e agora complete de dois jeitos"),
                ("\"...porque ELE temia violência\"", "aqui, \"ele\" é o prefeito"),
                ("\"...porque ELES pregavam violência\"", "aqui, \"eles\" são os manifestantes"),
                ("Uma letra muda o dono da frase inteira", "e você resolveu isso sem perceber"),
                ("Para resolver, você olhou a frase toda de uma vez", "não leu palavra por palavra em ordem"),
                ("Atenção é o mecanismo que faz o modelo fazer isso", "para cada palavra, ele pesa o quanto cada outra importa")],
               subtitle="Antes de 2017, o modelo lia em ordem e esquecia o começo. A atenção olha tudo junto.")
notes(s, "8 min", "ESSENCIAL", EU,
      """
Este é o slide que faz a turma entender por que o Transformer mudou tudo. Leia as duas
frases em voz alta, com pausa, e deixe a sala resolver sozinha.

"Peça número três: atenção. E eu vou explicar com um exemplo, porque é mais fácil sentir
do que definir.

Leiam comigo: 'o prefeito negou a licença aos manifestantes'. Agora eu vou completar de
dois jeitos.

Primeiro: 'porque ELE temia violência'. Quem é 'ele'? [pausa] O prefeito.

Segundo: 'porque ELES pregavam violência'. Quem são 'eles'? [pausa] Os manifestantes.

Uma letra. Uma letra muda o dono da frase inteira. E vocês resolveram isso agora, sem
esforço nenhum, provavelmente sem perceber que resolveram.

Como vocês fizeram? Vocês olharam a frase inteira de uma vez. Não leram palavra por
palavra em ordem, decorando o que veio antes. Vocês pesaram: 'temia' combina com quem
tinha medo, 'pregavam' combina com quem estava protestando.

Atenção é o mecanismo que faz o modelo fazer exatamente isso. Para cada palavra que ele
vai gerar, ele calcula o quanto cada outra palavra do texto importa naquele momento.

E a linha de baixo é o marco histórico: antes de 2017, os modelos liam em ordem, uma
palavra de cada vez, e esqueciam o começo de textos longos. A arquitetura Transformer
trouxe a atenção, que olha tudo junto. É isso que está por trás de toda IA generativa que
vocês usam hoje."
""")

s = sl_pipeline("Juntando as três peças", "O que acontece quando você aperta enter",
                [(1, "Entra o texto", "A sua pergunta, mais tudo que já foi dito na conversa."),
                 (2, "Vira token", "O texto é quebrado em pedaços e cada um vira um número."),
                 (3, "Vira coordenada", "Cada token vira um ponto no mapa de significados."),
                 (4, "A atenção pesa", "Para cada posição, o modelo calcula o que importa no contexto."),
                 (5, "Sai uma lista de probabilidades", "Não um token, mas a chance de cada token possível ser o próximo."),
                 (6, "Um token é escolhido", "E o processo inteiro recomeça, agora com esse token junto.")],
                subtitle="Repare no passo 6: ele refaz tudo isso a cada palavra que escreve.",
                per_row=3)
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Agora juntando as três peças. O que acontece quando você digita uma pergunta e aperta
enter.

Entra o texto: a sua pergunta, mais tudo que já foi dito naquela conversa.

Esse texto vira token, cada pedaço com seu número.

Cada token vira coordenada no mapa de significados, o embedding.

A atenção entra e pesa: para cada posição, o que importa no contexto.

E aí sai uma coisa que quase ninguém sabe: não sai um token. Sai uma LISTA de
probabilidades. A chance de cada token possível ser o próximo. Tipo: 'aprovado' com
quarenta por cento, 'negado' com trinta, 'pendente' com dez, e assim por diante.

Aí um token é escolhido dessa lista, e o processo inteiro recomeça, agora com esse token
fazendo parte do texto.

Olha o passo seis de novo. Ele refaz tudo isso a cada palavra que escreve. Uma resposta de
duzentas palavras passou por esse ciclo umas trezentas vezes."
""")

s = sl_bullets("A escolha", "Por que a mesma pergunta gera respostas diferentes",
               [("Do passo 5 sai uma lista de candidatos com probabilidade", "e alguém precisa escolher um"),
                ("Temperatura é o botão que controla essa escolha", "temperatura baixa escolhe sempre o mais provável"),
                ("Temperatura alta dá chance aos candidatos improváveis", "é o que produz texto mais variado e mais surpreendente"),
                ("Por isso consistência e criatividade brigam", "você escolhe uma, e paga na outra"),
                ("Em extração e classificação, use temperatura baixa", "você quer a mesma resposta toda vez"),
                ("Em redação e ideias, temperatura alta ajuda", "aqui variedade conta como qualidade")],
               subtitle="Quando alguém reclama que a IA respondeu diferente da última vez, quase sempre é isto.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Do passo cinco sai aquela lista de candidatos com probabilidade. Alguém precisa escolher
um. E existe um botão que controla como essa escolha acontece: temperatura.

Temperatura baixa, perto de zero: ele escolhe sempre o candidato mais provável. Resposta
previsível, repetível, sem graça.

Temperatura alta: ele dá chance aos candidatos menos prováveis. Texto mais variado, mais
surpreendente, e às vezes mais errado.

Por isso consistência e criatividade brigam. Você escolhe uma e paga na outra. Não tem
configuração mágica que dê as duas.

Na prática: se você está extraindo campo de documento ou classificando chamado, use
temperatura baixa. Você quer a mesma resposta toda vez, porque é operação. Se você está
gerando ideia de campanha ou rascunho de texto, temperatura alta ajuda.

E quando alguém reclamar que 'a IA respondeu diferente da última vez', quase sempre é
isto aqui."
""")

s = sl_cards("Como ele ficou assim", "Três fases de treino, três habilidades diferentes",
             [("1 · Pré-treino",
               "Leu texto em escala absurda e aprendeu a completar frase.\n\nNo fim desta fase ele sabe muito e não sabe conversar. Se você perguntar algo, ele pode responder com outra pergunta parecida."),
              ("2 · Ajuste por instrução",
               "Aprendeu que, quando recebe um pedido, deve atender o pedido.\n\nÉ aqui que ele para de completar texto e passa a responder pergunta."),
              ("3 · Alinhamento com humano",
               "Pessoas compararam respostas e disseram qual preferiam.\n\nÉ o que deixa ele educado, prestativo e recusando pedido perigoso.")],
             subtitle="A terceira fase é a que mais muda entre um modelo e outro. Personalidade vem daqui.",
             cols=3)
notes(s, "3 min", "DESCARTÁVEL se atrasado", EU,
      """
"Rápido, porque ajuda a entender diferença entre modelos.

Fase um, pré-treino: ele leu texto numa escala absurda e aprendeu a completar frase. No fim
dessa fase ele sabe muito e não sabe conversar. Se você perguntasse alguma coisa, ele podia
responder com outra pergunta parecida, porque na internet pergunta costuma vir seguida de
pergunta.

Fase dois, ajuste por instrução: ele aprendeu que, quando recebe um pedido, deve atender o
pedido. É aqui que ele para de completar texto e passa a responder.

Fase três, alinhamento: pessoas compararam respostas e disseram qual preferiam. É o que
deixa ele educado, prestativo, e recusando pedido perigoso.

E a linha de baixo explica uma coisa prática: a fase três é a que mais muda entre um modelo
e outro. Quando vocês sentem que um modelo tem 'personalidade' diferente do outro, ou é
mais formal, ou recusa mais, é daí que vem."
""")

s = sl_bullets("O limite físico", "Janela de contexto, ou a mesa de trabalho dele",
               [("Imagine uma mesa onde cabe uma quantidade fixa de papel", "tudo que está na mesa, ele enxerga"),
                ("A sua pergunta, o histórico da conversa e os arquivos colados", "tudo disputa espaço na mesma mesa"),
                ("Quando enche, o começo cai da mesa", "e ele nunca mais vê aquilo"),
                ("Por isso ele esquece o início de conversa longa", "e por isso repetir a informação resolve"),
                ("Mesa cheia custa mais caro e responde mais devagar", "você paga por token de entrada também"),
                ("Informação no meio de texto muito longo se perde", "coloque o que importa no começo ou no fim")],
               subtitle="Ele não tem memória entre conversas. Cada conversa nova começa com a mesa vazia.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Última peça antes de fechar o bloco: janela de contexto.

Imaginem uma mesa de trabalho onde cabe uma quantidade fixa de papel. Tudo que está em
cima da mesa, ele enxerga. O que não está, para ele não existe.

E o que disputa espaço nessa mesa? A sua pergunta, o histórico inteiro da conversa, e
qualquer arquivo que você colou. Tudo junto.

Quando a mesa enche, o começo cai. E ele nunca mais vê aquilo. Por isso, numa conversa
longa, ele esquece o que vocês combinaram no início. E por isso repetir a informação
resolve o problema: você está colocando aquele papel de volta na mesa.

Duas consequências práticas. Mesa cheia custa mais caro e responde mais devagar, porque
você paga por token de entrada também, não só pela resposta. E informação enfiada no meio
de um texto muito longo tende a se perder: coloque o que importa no começo ou no fim.

E o mais importante, que está embaixo: ele não tem memória entre conversas. Cada conversa
nova começa com a mesa vazia. Quando um produto parece lembrar de você, é porque alguém
programou para recolocar aquilo na mesa toda vez."
""")

s = sl_statement("Agora dá para explicar",
                 "Ele escolhe o token mais provável.\nProvável e verdadeiro são coisas diferentes.",
                 "Alucinação é o mecanismo funcionando como foi construído. Nenhuma versão futura conserta isso.")
notes(s, "3 min", "ESSENCIAL, fechamento do bloco", EU,
      """
Fechamento do bloco. Amarre com o caso da semana 1.

"Agora, com as três peças na mão, dá para explicar direito uma coisa que na semana passada
eu pedi para vocês aceitarem: a alucinação.

Ele escolhe o token mais provável, dada a sequência anterior. Só isso. E 'provável' e
'verdadeiro' são coisas diferentes.

Lembram do advogado de Londrina, que apresentou petição com número de processo inventado?
Agora vocês conseguem explicar tecnicamente o que aconteceu. Um número de processo tem uma
FORMA muito previsível: tantos dígitos, ponto, traço, ano, tribunal. Para o modelo, gerar
uma sequência com essa forma é altamente provável. Ele não tem nenhum mecanismo interno
que consulte se aquele processo existe. Ele não sabe que existe uma diferença entre gerar
a forma certa e gerar o fato certo.

Então a alucinação é o mecanismo funcionando exatamente como foi construído. Nenhuma
versão futura vai consertar isso, porque não existe o que consertar.

O que muda, e o Felipe vai mostrar depois do intervalo, é COMO a gente trabalha em volta
disso."
""")

# --------------------------------------------------------------------------
s = sl_break()
notes(s, "20h30 às 20h45 (15 min)", "ESSENCIAL", "os dois",
      """
DURANTE O INTERVALO:
- Deixe o slide na tela com o horário de retorno visível.
- Moderador posta o link do Discord e recolhe as dúvidas do bloco técnico.
- Alinhem em 2 minutos: o bloco 2 atrasou? O Felipe corta o quê?
- Confirme que a gravação continua rodando.

VOLTA: comece 20h45 em ponto, mesmo com gente faltando.
""")

# ==========================================================================
# BLOCO D: Prompt, contexto e limites (20h45 às 21h36)
# ==========================================================================
s = sl_section("04", "Prompt, contexto e limites",
               "Como escrever um pedido que funciona, e o que é folclore",
               "20h45 às 21h36  ·  51 minutos")
notes(s, "20h45 às 21h36 (51 min)", "ESSENCIAL", FELIPE,
      """
ABERTURA DO SEU BLOCO (retomada pós-intervalo, ~1 min):

"Bem-vindos de volta. O Edmar mostrou o que a IA generativa faz e como ela funciona por
dentro. Agora eu vou mostrar como conversar com ela de um jeito que produza trabalho útil.

Um aviso rápido de agenda: este bloco cresceu, porque vamos incluir dois assuntos a mais,
banco vetorial e fine-tuning. Isso significa que hoje vamos até uns dez minutos depois das
22h. Se alguém precisar sair no horário exato, sem problema, o conteúdo inteiro fica
gravado.

E eu vou começar com uma provocação: a maior parte das reclamações de que 'a IA respondeu
mal' nasce de um pedido mal escrito."

ESTRUTURA:
  Prompt como especificação             4 min
  Os cinco elementos                    6 min
  Três antes e depois                  12 min
  Três técnicas que funcionam           8 min
  O que é folclore                      5 min
  RAG (o pipeline)                      5 min
  Banco vetorial                        6 min
  RAG × fine-tuning                     5 min

Este bloco cresceu 11 minutos em relação ao desenho original, com a entrada de banco
vetorial e fine-tuning. A decisão foi esticar a aula em vez de cortar conteúdo já
existente: a noite agora fecha por volta de 22h11, não 22h00. Avisar a turma disso
explicitamente no início do bloco, para ninguém ficar surpreso perto do fim.
""")

s = sl_statement("A provocação de abertura",
                 "Prompt é especificação de trabalho.\nEspecificação vaga produz entrega vaga.",
                 "Isso vale para estagiário, para fornecedor e para modelo de linguagem.")
notes(s, "4 min", "ESSENCIAL", FELIPE,
      """
"Vou começar com uma provocação.

Prompt é especificação de trabalho. E especificação vaga produz entrega vaga.

Pensa numa situação que vocês já viveram. Você pede para alguém 'dar uma olhada naquele
relatório'. A pessoa volta com uma coisa completamente diferente do que você esperava. De
quem é a culpa?

É do pedido. Você não disse o que era 'dar uma olhada', não disse o que te preocupava, não
disse em que formato queria a resposta, e não disse quando.

Com modelo de linguagem é igual, com um agravante: ele nunca vai te perguntar 'o que
exatamente você quer dizer com isso?'. Ele vai chutar o que você quis dizer, com
confiança, e entregar.

Então a habilidade que vocês vão treinar neste bloco chama-se escrever especificação. E
ela serve para a carreira inteira de vocês, mesmo sem IA nenhuma envolvida."
""")

s = sl_cards("A anatomia", "Cinco elementos de um pedido que funciona",
             [("Papel",
               "Quem o modelo deve ser ao responder.\n\n\"Você é um analista de dados explicando para um gerente comercial.\""),
              ("Tarefa",
               "O verbo, específico. Um dos seis do primeiro bloco.\n\n\"Classifique cada chamado abaixo.\" Melhor que \"analise\"."),
              ("Contexto",
               "O material que ele precisa ter para responder.\n\nO texto da política, os dados, o histórico. Cole junto."),
              ("Formato",
               "Como você quer receber a resposta.\n\n\"Uma linha de tabela por item, com estas três colunas.\""),
              ("Restrição",
               "Tamanho, tom, o que evitar, o que fazer na dúvida.\n\n\"Máximo 3 frases. Se faltar informação, escreva NÃO SEI.\"")],
             subtitle="Nenhum prompt precisa dos cinco. Mas todo prompt ruim está sem pelo menos três.",
             cols=5, card_h=4.2)
notes(s, "6 min", "ESSENCIAL, slide-âncora do bloco", FELIPE,
      """
Este é o slide de referência do bloco. Vale pedir para fotografarem.

"Cinco elementos. Não precisa dos cinco toda vez, mas todo prompt ruim está sem pelo menos
três deles.

PAPEL: quem o modelo deve ser ao responder. 'Você é um analista de dados explicando para
um gerente comercial.' Isso muda vocabulário e profundidade de uma vez só.

TAREFA: o verbo, e específico. Lembram dos seis verbos do bloco do Edmar? Use um deles.
'Classifique cada chamado abaixo' funciona muito melhor que 'analise esses chamados',
porque 'analisar' não diz o que fazer.

CONTEXTO: o material que ele precisa ter em mãos. O texto da política, os dados, o
histórico. Cola junto. Ele não sabe nada da sua empresa.

FORMATO: como você quer receber. 'Uma linha de tabela por item, com estas três colunas.'
Sem isso, você recebe três parágrafos de texto corrido e tem que reformatar na mão.

RESTRIÇÃO: tamanho, tom, o que evitar, e principalmente o que fazer na dúvida. Aquele
último pedaço é o que mais gente esquece: 'se faltar informação, escreva NÃO SEI'. Sem
isso, ele preenche o buraco com invenção.

Vale fotografar este slide."
""")

s = sl_prompt("Antes e depois · 1", "Especificidade",
              ("PEDIDO VAGO",
               "\"Escreva sobre nosso produto.\"",
               "Volta um texto genérico, que serviria para\nqualquer empresa de qualquer setor."),
              ("PEDIDO ESPECÍFICO",
               "\"Escreva 3 parágrafos apresentando nosso sistema\nde gestão de estoque para donos de pequenos\nsupermercados. O ponto principal é reduzir perda\npor produto vencido. Tom direto, sem jargão\ntécnico. Máximo 500 caracteres por parágrafo.\"",
               "Volta um texto que fala com uma pessoa\nespecífica sobre um problema específico."),
              subtitle="O que separa os dois é quantas decisões você tomou antes de pedir.")
notes(s, "4 min", "ESSENCIAL", FELIPE,
      """
"Primeiro par. Especificidade.

À esquerda: 'escreva sobre nosso produto'. O que volta? Um texto genérico que serviria para
qualquer empresa de qualquer setor. Você lê e pensa 'está ok, mas não é isso'. E aí você
fica reescrevendo na mão, e perdeu o ganho todo.

À direita, repara no que foi decidido antes de pedir: quantos parágrafos, qual produto,
para QUEM (dono de pequeno supermercado, não 'clientes'), qual o ponto principal (perda por
vencimento), qual o tom, e qual o tamanho.

E olha a linha de baixo, que é a lição: o que separa os dois é quantas decisões você tomou
antes de pedir. Se você não sabe para quem está escrevendo, o modelo também não vai saber."
""")

s = sl_prompt("Antes e depois · 2", "Contexto",
              ("SEM CONTEXTO",
               "\"A política de férias da empresa\npermite acumular dois períodos?\"",
               "Ele responde com base no que leu na internet.\nPode acertar por sorte, ou inventar\ncom convicção total."),
              ("COM CONTEXTO",
               "\"Texto da política:\n[cole aqui o trecho do documento]\n\nCom base APENAS no texto acima, responda:\na política permite acumular dois períodos?\nSe o texto não disser, responda NÃO CONSTA.\"",
               "Ele responde a partir do seu documento,\ne admite quando a informação não está lá."),
              subtitle="Ele não sabe nada da sua empresa. Tudo que ele sabe do seu caso, você colou.")
notes(s, "4 min", "ESSENCIAL, o par mais importante", FELIPE,
      """
Este é o par mais importante do bloco. Insista nele.

"Segundo par. Contexto. E este é o mais importante dos três.

À esquerda, alguém pergunta sobre a política de férias da empresa. Sem colar a política. O
que acontece? Ele responde com base no que leu na internet sobre políticas de férias em
geral. Pode até acertar por sorte, porque muita empresa segue a CLT. Ou pode inventar com
convicção total, e a pessoa acredita porque a resposta é fluente.

À direita, a política vai colada. E tem três coisas ali que valem ouro.

Primeiro, o texto vem antes da pergunta.

Segundo: 'com base APENAS no texto acima'. Isso restringe a fonte.

Terceiro, e esse é o que mais salva: 'se o texto não disser, responda NÃO CONSTA'. Você deu
para ele uma saída honesta. Sem essa linha, o modelo tende a preencher o buraco, porque a
tarefa dele é produzir texto plausível.

Guardem esse padrão. Ele resolve boa parte dos problemas de alucinação em uso corporativo."
""")

s = sl_prompt("Antes e depois · 3", "Formato",
              ("SEM FORMATO",
               "\"Analise esses 50 chamados de suporte\ne me diga o que você achou.\"",
               "Volta um texto corrido de 4 parágrafos.\nNão dá para colocar em planilha,\nnem contar, nem comparar depois."),
              ("COM FORMATO",
               "\"Para cada chamado abaixo, devolva uma linha:\nid | motivo | urgência\n\nmotivo: escolha entre ACESSO, COBRANCA,\nTECNICO, OUTRO\nurgência: 1 (baixa), 2 (média), 3 (alta)\n\nNão escreva nada fora da tabela.\"",
               "Volta uma tabela que entra direto\nna planilha e vira número."),
              subtitle="Formato definido transforma texto em dado. E dado você consegue contar.")
notes(s, "4 min", "ESSENCIAL", FELIPE,
      """
"Terceiro par. Formato.

À esquerda: 'analise esses cinquenta chamados e me diga o que você achou'. Volta um texto
corrido de quatro parágrafos, bem escrito e completamente inútil para trabalho. Não dá para
colocar em planilha, não dá para contar, não dá para comparar com o mês passado.

À direita, três decisões: qual a estrutura de cada linha, quais são as categorias
possíveis, e o que fazer com o resto. Repara que as categorias foram FECHADAS: acesso,
cobrança, técnico, outro. Sem isso, ele inventa uma categoria nova para cada chamado, e
você fica com cinquenta categorias diferentes.

E aquela última linha, 'não escreva nada fora da tabela', evita que ele mande um parágrafo
educado de introdução antes dos dados, que quebra qualquer processamento automático.

A lição está embaixo: formato definido transforma texto em dado. E dado você consegue
contar."
""")

s = sl_cards("O que funciona", "Três técnicas que valem o esforço",
             [("Dar exemplos",
               "Mostre 2 ou 3 exemplos do que você quer, com entrada e saída.\n\nDois exemplos costumam valer mais que três parágrafos de instrução.\n\nUse quando o formato é difícil de descrever mas fácil de mostrar."),
              ("Pedir o raciocínio",
               "\"Explique seu raciocínio antes de dar a resposta final.\"\n\nMelhora tarefa que tem etapas ou comparação.\n\nCusta mais token e demora mais. Não use em tarefa simples."),
              ("Definir papel e público",
               "\"Você é um auditor explicando para alguém sem formação técnica.\"\n\nMuda vocabulário e profundidade de uma vez só.\n\nMais barato que reescrever o texto depois.")],
             subtitle="Estas três têm efeito consistente. As da próxima lista, nem tanto.",
             cols=3)
notes(s, "8 min", "ESSENCIAL", FELIPE,
      """
"Três técnicas que valem o esforço de aprender.

DAR EXEMPLOS. Em vez de descrever o formato que você quer em três parágrafos, mostre dois
ou três exemplos com entrada e saída. Isso funciona muito bem porque o modelo é bom em
reconhecer padrão. Use quando o formato é difícil de descrever mas fácil de mostrar. Tem
nome técnico, few-shot, mas o que importa é a ideia.

PEDIR O RACIOCÍNIO. 'Explique seu raciocínio antes de dar a resposta final.' Isso melhora
resultado em tarefa que tem etapas, comparação ou conta. Mas custa mais token e demora
mais, então não use em tarefa simples. Se você só quer classificar um chamado, pedir
raciocínio é desperdício.

DEFINIR PAPEL E PÚBLICO. 'Você é um auditor explicando para alguém sem formação técnica.'
Isso muda vocabulário e profundidade de uma vez só. É muito mais barato que gerar o texto
técnico e depois pedir para simplificar."
""")

s = sl_bullets("O que é folclore", "Coisas que circulam por aí e não se sustentam",
               [("Dizer \"por favor\" e \"obrigado\"", "não há efeito confiável na qualidade da resposta"),
                ("Prometer gorjeta ou ameaçar o modelo", "virou meme, e não é técnica"),
                ("Escrever tudo em CAIXA ALTA para enfatizar", "gasta mais token e não obriga nada"),
                ("Repetir a mesma instrução três vezes", "instrução repetida não vira instrução mais forte"),
                ("Prompt gigante é sempre melhor", "instrução contraditória no meio de texto longo piora o resultado"),
                ("Dizer só o que NÃO fazer", "\"não use jargão\" funciona pior que \"escreva como se fosse para um leigo\"")],
               subtitle="Na dúvida entre uma técnica e outra, prefira a que você consegue explicar por que funciona.")
notes(s, "5 min", "ESSENCIAL, bom momento de leveza", FELIPE,
      """
Este slide costuma render riso e engajamento. Aproveite.

"Agora a parte divertida: o que circula por aí e não se sustenta.

Dizer 'por favor' e 'obrigado'. Não existe efeito confiável na qualidade da resposta. Se
você faz por educação ou por hábito, tudo bem, mas não é técnica de prompt.

Prometer gorjeta ou ameaçar o modelo. Isso virou meme na internet. Não é técnica.

Escrever tudo em caixa alta para enfatizar. Gasta mais token, porque caixa alta costuma
quebrar em mais pedaços, e não obriga nada.

Repetir a mesma instrução três vezes. Instrução repetida não vira instrução mais forte.

Prompt gigante é sempre melhor. Esse é o mais perigoso dos cinco, porque parece razoável.
Prompt longo com instrução contraditória no meio piora o resultado. Se você escreveu 'seja
conciso' no começo e 'explique detalhadamente' no fim, ele vai obedecer um dos dois e você
não controla qual.

E o último, que é o mais útil: dizer só o que NÃO fazer funciona pior do que dizer o que
fazer. 'Não use jargão técnico' é pior que 'escreva como se fosse para um leigo'. Diga o
alvo, e não o que evitar.

A régua está embaixo: na dúvida entre duas técnicas, prefira a que você consegue explicar
por que funciona."
""")

s = sl_pipeline("Quando o contexto vem de fora", "RAG, ou como fazer ele falar da sua empresa",
                [(1, "A pergunta chega", "\"A política de férias permite acumular dois períodos?\""),
                 (2, "O sistema busca", "Procura nos documentos da empresa os trechos mais próximos em significado."),
                 (3, "Os trechos são colados", "Os pedaços encontrados entram no prompt, junto com a pergunta."),
                 (4, "O modelo responde", "Com base no que foi colado, e citando de onde tirou.")],
                subtitle="É o embedding do bloco anterior trabalhando: busca por significado, não por palavra exata.",
                per_row=4)
notes(s, "5 min", "ESSENCIAL", FELIPE,
      """
"Último tema do meu bloco, e ele conecta direto com o embedding que o Edmar explicou.

Vocês já entenderam que o modelo não sabe nada da sua empresa, e que tudo que ele sabe do
seu caso, você colou. Mas você não vai colar dez mil documentos a cada pergunta. Não cabe
na mesa, e custaria caro demais.

A solução tem nome: RAG. E funciona em quatro passos.

A pergunta chega. O sistema busca, nos documentos da empresa, os trechos mais próximos em
significado. E repara: em significado, não em palavra exata. É o mapa de coordenadas do
bloco anterior trabalhando. Alguém pergunta sobre 'demissão' e o sistema acha o documento
que fala em 'desligamento'.

Os trechos encontrados são colados no prompt junto com a pergunta. E o modelo responde com
base no que foi colado, citando de onde tirou.

Duas consequências que vocês precisam levar. Primeira: com RAG, a resposta vem com fonte, e
fonte é o que faz o usuário confiar. Segunda: se a busca do passo dois trouxer o trecho
errado, o modelo responde errado com toda a confiança do mundo. A qualidade do RAG depende
mais da busca do que do modelo."
""",
      "Assunto aprofundado nos dois slides a seguir: banco vetorial e fine-tuning.")

s = sl_bullets("Banco vetorial", "O mapa do embedding precisa morar em algum lugar",
               [("O embedding transforma texto em coordenada", "o banco vetorial é onde essas coordenadas moram"),
                ("Cada pedaço de documento vira uma linha", "o texto original, mais a coordenada dele"),
                ("A pergunta também vira coordenada na hora de buscar", "e o banco procura os vizinhos mais próximos"),
                ("É como um aplicativo de mapa achando o restaurante mais perto", "sem comparar a distância até cada restaurante do país, um por um"),
                ("Um índice especializado permite buscar entre milhões de coordenadas em milissegundos", "sem esse índice, RAG não escala além de uma pasta de documentos"),
                ("Busca por coordenada, chamada de densa, acha sentido parecido", "mas pode perder uma palavra-chave exata, como um código de produto ou número de lei"),
                ("Por isso sistema bom combina busca densa com busca por palavra exata", "essa segunda é chamada de esparsa")],
               subtitle="É o mesmo mapa de coordenadas do embedding, só que guardado para busca em escala.")
notes(s, "6 min", "ESSENCIAL", FELIPE,
      """
"Vocês entenderam o embedding: texto vira coordenada num mapa de significados. Mas esse
mapa precisa morar em algum lugar, e precisa ser buscável rápido. É isso que é um banco
vetorial.

Cada pedaço de documento vira uma linha nesse banco: o texto original, mais a coordenada
dele. E quando a pergunta chega, ela também vira coordenada na hora, e o banco procura os
vizinhos mais próximos.

Pensa num aplicativo de mapa achando o restaurante mais perto de você. Ele não compara a
distância até cada restaurante do país, um por um. Existe um índice que já organiza tudo
por proximidade, e a busca sai instantânea. Banco vetorial faz exatamente isso, só que a
'distância' é semelhança de significado, e não metro na rua.

E esse índice é o que permite buscar entre milhões de coordenadas em milissegundos. Sem
ele, RAG funciona numa pasta de vinte documentos e trava numa base de verdade.

Último ponto, e ele importa para quem for montar isso na prática: busca por coordenada,
que tem nome técnico de busca densa, acha sentido parecido. Mas ela pode perder uma
palavra-chave exata, tipo um código de produto ou o número de um artigo de lei, porque
esses tokens específicos às vezes não carregam significado nenhum sozinhos. Por isso um
sistema de busca bem feito combina busca densa com busca por palavra exata, chamada de
esparsa. Um pega o sentido, o outro pega a forma exata."
""",
      "Se sobrar tempo e quiserem citar exemplo de produto: Pinecone, Weaviate, pgvector. Cite como exemplo, sem recomendar nenhum.")

s = sl_two_col("Duas formas de adaptar", "RAG ou fine-tuning: qual escolher",
               "RAG",
               ["Você entrega os documentos certos na hora da pergunta",
                "Resolve conhecimento que muda: política, preço, estoque",
                "Atualiza na hora, troca o documento e pronto",
                "Mantém o jeito de responder do modelo igual",
                "Mais barato e mais rápido de montar"],
               "FINE-TUNING",
               ["Você retreina o modelo com exemplos do seu padrão de resposta",
                "Resolve comportamento: tom, formato, jargão do seu setor",
                "Atualizar exige treinar de novo, processo mais lento",
                "Ensina jeito de responder, não fato confiável",
                "Mais caro e mais lento de montar"],
               subtitle="Na dúvida, comece por RAG. Ele resolve a maior parte dos casos reais de conhecimento desatualizado.",
               lcolor=NAVY, rcolor=NAVY_SOFT)
notes(s, "5 min", "ESSENCIAL", FELIPE,
      """
"Última peça antes da interação. RAG resolve um problema. Fine-tuning resolve outro. E
muita gente confunde os dois.

RAG: você entrega os documentos certos na hora da pergunta. Resolve conhecimento que muda,
tipo política, preço, estoque. Atualiza na hora, você troca o documento e pronto. E o jeito
de responder do modelo continua igual, você só mudou o que ele sabe.

Fine-tuning: você retreina o modelo com exemplos do seu padrão de resposta. Resolve
comportamento: tom, formato, jargão do seu setor. Quer que ele sempre responda no formato
da sua empresa, sempre com aquele tom? Fine-tuning ensina isso. Mas atualizar exige treinar
de novo, é processo mais lento e mais caro. E um detalhe importante: fine-tuning ensina
jeito de responder, não fato confiável. Ele não substitui RAG para conhecimento que muda.

Guardem a régua de baixo: na dúvida, comecem por RAG. Ele resolve a maior parte dos casos
reais de conhecimento desatualizado, que é o problema mais comum. Fine-tuning entra quando
o alvo do ajuste é o comportamento do modelo."
""")


s = sl_interaction("Interação", "Testando o que a gente acabou de ver",
                   "Qual destes quatro pedidos você melhoraria primeiro?",
                   ["A: \"Resuma este relatório\"   ·   B: \"Você é um analista. Resuma em 5 tópicos\"",
                    "C: \"Analise os dados e me diga o que achou\"   ·   D: \"Extraia valor e data. Se faltar, escreva NÃO CONSTA\"",
                    "Responda na enquete, 30 segundos",
                    "Depois eu explico qual falta mais elemento dos cinco"])
notes(s, "3 min", "DESCARTÁVEL", FELIPE,
      """
"Uma última antes de fechar. Qual destes quatro pedidos você melhoraria primeiro?"

[aguarde 30 a 45 segundos]

Comentário: o C é o pior dos quatro. "Analise os dados e me diga o que achou" usa um verbo
que não especifica tarefa nenhuma, e ainda deixa de fora formato, restrição e público.
Falta quatro dos cinco elementos.

O A tem tarefa (resumir) mas falta formato e restrição.
O B tem papel, tarefa e formato.
O D tem tarefa, formato e a regra de dúvida, que é o melhor detalhe dos quatro.
""")

# ==========================================================================
# BLOCO E: Onde resolve e onde atrapalha (21h36 às 22h01)
# ==========================================================================
s = sl_section("05", "Onde GenAI resolve e onde atrapalha",
               "O bloco que economiza dinheiro de empresa",
               "21h36 às 22h01  ·  25 minutos")
notes(s, "21h36 às 22h01 (25 min)", "ESSENCIAL", FELIPE,
      """
Bloco de julgamento crítico. É o que mais pesa na carreira deles, e o que diferencia quem
usa a ferramenta de quem escolhe a ferramenta.

ESTRUTURA:
  A escada de volta                     3 min
  Sinais de que resolve                 4 min
  Sinais de que atrapalha               5 min
  Tabela problema para ferramenta       4 min
  O erro mais comum                     5 min
  Como avaliar saída                    4 min
""")

s = sl_table("A escada, de volta", "A pergunta continua a mesma da semana 1",
             ["Ferramenta", "Responde o quê", "Exemplo"],
             [["Relatório / BI", "O que aconteceu?", "Quantos clientes cancelaram no mês passado"],
              ["Estatística / Analytics", "Por que aconteceu?", "Por que a conversão caiu no último trimestre"],
              ["Machine Learning", "O que vai acontecer?", "Quais clientes vão cancelar nos próximos 60 dias"],
              ["Otimização", "O que eu devo fazer?", "Qual a melhor rota de entrega para amanhã"],
              ["IA Generativa", "Como seria isso escrito ou lido?", "Resumir os motivos escritos em 500 cancelamentos"],
              ["Agentes de IA", "Faça isso por mim, do início ao fim", "Levantar, analisar, redigir e enviar o relatório"]],
             subtitle="Hoje a gente passou a noite no quinto degrau. Ele é um degrau, e não a escada inteira.",
             widths=[0.24, 0.30, 0.46])
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Vocês lembram desta tabela. Ela apareceu na semana 1.

Relatório responde o que aconteceu. Analytics responde por quê. Machine learning responde
o que vai acontecer. Otimização responde o que eu devo fazer. IA generativa responde como
seria isso escrito ou lido. E agentes fazem do início ao fim.

Hoje a gente passou a noite inteira no quinto degrau. E eu preciso fechar a noite lembrando
que ele é UM degrau, e não a escada inteira.

Olha a linha da IA generativa e a linha do relatório. 'Quantos clientes cancelaram no mês
passado' é uma pergunta de banco de dados. Se você mandar essa pergunta para um modelo de
linguagem com uma planilha colada, ele vai tentar contar, e vai errar. A gente vai ver isso
em detalhe daqui a pouco."
""")

s = sl_two_col("O teste rápido", "Seis sinais de cada lado",
               "SINAL DE QUE GenAI RESOLVE",
               ["O trabalho principal é ler ou escrever texto",
                "Existe variação demais para escrever regra fixa",
                "Errar de vez em quando é tolerável",
                "Tem um humano conferindo antes de virar decisão",
                "O ganho é tempo, e o volume é alto",
                "Não existe uma única resposta certa"],
               "SINAL DE QUE ELA ATRAPALHA",
               ["O problema pede número exato e reproduzível",
                "Existe uma resposta certa e auditável",
                "A decisão é automática, sem humano no meio",
                "O custo de errar é alto e difícil de desfazer",
                "Já existe regra simples que resolve",
                "Você precisa explicar a decisão de forma determinística"],
               subtitle="Conte quantos sinais de cada lado o seu problema tem. O lado com mais sinais decide.",
               lcolor=NAVY, rcolor=MUTED)
notes(s, "9 min", "ESSENCIAL, slide-âncora do bloco", FELIPE,
      """
Este é o slide que vale fotografar. Percorra os dois lados com calma.

"Seis sinais de cada lado. Este é o teste rápido que eu quero deixar com vocês.

Do lado esquerdo, sinais de que GenAI resolve bem.

O trabalho principal é ler ou escrever texto. Se o núcleo da tarefa é linguagem, é bom
candidato.

Existe variação demais para escrever regra fixa. Se você tentou escrever um 'se-então' e
apareceram trinta exceções, é sinal.

Errar de vez em quando é tolerável. Repara que eu não disse 'errar não importa'. Disse
tolerável.

Tem um humano conferindo antes de virar decisão.

O ganho é tempo, e o volume é alto. Sem volume, não compensa o esforço de construir.

E não existe uma única resposta certa. Resumo bom tem várias formas.

Agora o lado direito, sinais de que ela atrapalha.

O problema pede número exato e reproduzível. Modelo de linguagem não é calculadora.

Existe uma resposta certa e auditável. Se alguém pode processar a empresa por causa da
resposta, cuidado.

A decisão é automática, sem humano no meio. Aí o erro vira decisão direto.

O custo de errar é alto e difícil de desfazer.

Já existe regra simples que resolve. Esse é o mais comum de todos, e o mais caro de
ignorar.

E o último: você precisa explicar a decisão de forma determinística. Se o regulador
perguntar por que aquela decisão foi tomada, 'o modelo escolheu' não é resposta aceitável.

A régua está embaixo: conte quantos sinais de cada lado o seu problema tem."
""")

s = sl_bullets("O erro mais comum", "Pedir para o modelo calcular",
               [("Alguém cola uma planilha e pede a soma de uma coluna", "e a resposta vem, com aparência perfeita"),
                ("Nos primeiros testes com poucas linhas, costuma acertar", "e a pessoa confia"),
                ("Com volume maior, ele erra e não avisa", "porque ele está compondo texto plausível, e não somando"),
                ("Pior: a mesma pergunta pode dar número diferente", "e conta que muda de valor não serve para nada"),
                ("A correção é simples e vale para sempre", "o modelo escreve a fórmula ou o código. A planilha executa"),
                ("Use ele para a linguagem, e a máquina certa para a conta", "cada degrau da escada faz o que sabe fazer")],
               subtitle="Este erro é comum porque falha em silêncio. O número errado parece tão bom quanto o certo.")
notes(s, "5 min", "ESSENCIAL, exemplo de maior retenção", FELIPE,
      """
Este é o exemplo mais prático e mais memorável do bloco. Conte devagar.

"Vou mostrar o erro mais comum que eu vejo, e ele é traiçoeiro porque falha em silêncio.

Alguém cola uma planilha na conversa e pede: 'some a coluna de vendas'. E a resposta vem,
com aparência perfeita, formatada, com o cifrão no lugar certo.

Nos primeiros testes, com poucas linhas, ele costuma acertar. E aí a pessoa confia, e passa
a usar aquilo para valer.

Com volume maior, ele erra. E não avisa. Porque ele nunca esteve somando. Ele está
compondo uma sequência de tokens que se parece com o resultado de uma soma. É a mesma
mecânica do número de processo inventado que o Edmar mostrou.

E tem uma coisa pior ainda: a mesma pergunta pode dar número diferente em duas tentativas.
Vocês entenderam por quê, no bloco da temperatura. E conta que muda de valor não serve para
nada em lugar nenhum.

A correção é simples e vale para o resto da carreira de vocês: o modelo escreve a FÓRMULA
ou o CÓDIGO. A planilha, ou o Python, executa. Você usa a IA generativa para a parte de
linguagem, que é traduzir o seu pedido em fórmula, e usa a ferramenta certa para a conta.

Cada degrau da escada fazendo o que sabe fazer."
""")

s = sl_bullets("Antes de colocar em produção", "Como avaliar saída de GenAI",
               [("Defina o que é boa resposta ANTES de começar", "depois, a métrica sempre vira justificativa do que saiu"),
                ("Monte um conjunto de 20 a 50 casos com resposta esperada", "isso já é suficiente para pegar piora grande"),
                ("Rode esse conjunto a cada mudança de prompt ou de modelo", "prompt novo pode consertar um caso e quebrar cinco"),
                ("Use regra para o que é objetivo", "formato, campo obrigatório, categoria dentro da lista permitida"),
                ("Use pessoa para o que é subjetivo", "tom, utilidade, se responde mesmo a pergunta"),
                ("Sem esse conjunto, \"melhorei o prompt\" é só opinião", "e opinião não sustenta decisão de produção")],
               subtitle="O modelo muda de versão sozinho. Sem conjunto de teste, você descobre a piora pelo cliente.")
notes(s, "4 min", "ESSENCIAL", FELIPE,
      """
"Fechando: como avaliar isso, já que na semana 1 a gente viu que GenAI não tem gabarito.

Defina o que é uma boa resposta antes de começar. Se você definir depois, a métrica vira
justificativa do que já saiu.

Monte um conjunto de vinte a cinquenta casos com a resposta esperada. Não precisa de mil.
Vinte a cinquenta já pega piora grande.

Rode esse conjunto a cada mudança de prompt ou de modelo. E aqui vai um detalhe que
surpreende quem está começando: prompt novo pode consertar um caso e quebrar cinco. Sem
conjunto de teste, você só vê o caso que consertou.

Para o que é objetivo, use regra: o formato está certo, o campo obrigatório veio, a
categoria está dentro da lista permitida. Isso dá para checar por código.

Para o que é subjetivo, use pessoa: o tom está certo, a resposta é útil, ela responde
mesmo o que foi perguntado.

E a linha final, que vale como aviso: o modelo muda de versão sozinho, do lado do
fornecedor. Sem conjunto de teste, você descobre que piorou pelo cliente reclamando."
""")

# ==========================================================================
# BLOCO F: Encerramento (22h01 às 22h11)
# ==========================================================================
s = sl_section("06", "Encerramento", "O que você leva de hoje e o que vem na quinta",
               "22h01 às 22h11  ·  10 minutos")
notes(s, "22h01 às 22h11 (10 min)", "ESSENCIAL", FELIPE,
      """
DISTRIBUIÇÃO:
  Recapitulação        3 min
  O que vem na quinta  2 min
  Q&A                  4 min  (elástico, absorve atraso)
  Fechamento           1 min

Não passe das 22h15. A aula esticou por decisão, não por atraso.
""")

s = sl_bullets("Recapitulando", "As 6 ideias que a gente quer que você leve hoje",
               [("Token, embedding e atenção explicam o comportamento dele", "inclusive o comportamento estranho"),
                ("Ele escolhe o provável, e provável difere de verdadeiro", "por isso a alucinação é esperada, e não um bug"),
                ("Prompt é especificação: papel, tarefa, contexto, formato, restrição", "prompt ruim está sem pelo menos três desses"),
                ("Mostrar dois exemplos vale mais que escrever três parágrafos", "e dizer o alvo funciona melhor que dizer o que evitar"),
                ("RAG é o que faz ele falar da sua empresa com fonte", "e a qualidade depende mais da busca do que do modelo"),
                ("Ela brilha em texto e falha em conta exata", "o modelo escreve a fórmula, a planilha executa")],
               subtitle="Se você levar só essas seis frases, a noite cumpriu o objetivo dela.",
               numbered=True)
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
Leia as seis com calma. É a última chance de fixar.

"Seis ideias para levar de hoje.

A primeira: token, embedding e atenção explicam o comportamento dele, inclusive o
comportamento estranho. Quem entende essas três peças para de brigar com a ferramenta.

Segunda: ele escolhe o provável, e provável é diferente de verdadeiro. Por isso a
alucinação é comportamento esperado.

Terceira: prompt é especificação, com cinco elementos. E todo prompt ruim está sem pelo
menos três deles.

Quarta: mostrar dois exemplos vale mais que escrever três parágrafos de instrução. E dizer
o alvo funciona melhor que dizer o que evitar.

Quinta: RAG é o que faz ele falar da sua empresa citando fonte. E a qualidade do RAG
depende mais da busca do que do modelo.

E a sexta, que é a que mais vai economizar dinheiro de vocês: ela brilha em texto e falha
em conta exata. O modelo escreve a fórmula, a planilha executa."
""")

s = sl_two_col("Próximo encontro", "Quinta-feira, 19h00 às 21h00",
               "O QUE VAMOS FAZER",
               ["Primeiro contato com o Google Colab",
                "Rodar o primeiro código, no navegador, sem instalar nada",
                "Conectar numa API gratuita de LLM e fazer a primeira chamada",
                "Colocar em prática os cinco elementos de prompt que vimos hoje",
                "Comparar respostas com temperatura diferente, na prática"],
               "O QUE VOCÊ PRECISA LEVAR",
               ["Uma conta Google, para usar o Colab",
                "Nada instalado, tudo roda no navegador",
                "As dúvidas técnicas que ficaram de hoje",
                "Disposição para ver código pela primeira vez, se for o seu caso",
                "Estar no Discord, o material vai ser postado lá antes"],
               subtitle="A partir da quinta entra código. E ele entra devagar, do zero.",
               lcolor=NAVY, rcolor=NAVY_SOFT)
notes(s, "2 min", "ESSENCIAL", FELIPE,
      """
"Quinta-feira, 19h às 21h. E é a aula em que entra código pela primeira vez.

Calma para quem nunca programou: vai entrar devagar, do zero, e roda tudo no navegador.
Vocês vão usar o Google Colab, que é uma ferramenta gratuita do Google. Não precisa
instalar nada, só ter uma conta Google.

O que a gente vai fazer: rodar o primeiro código, conectar numa API gratuita de modelo de
linguagem e fazer a primeira chamada de verdade. E aí colocar em prática os cinco elementos
de prompt que vocês viram hoje, e comparar o que muda com temperatura diferente.

Ou seja: tudo que foi teoria hoje, vocês vão ver acontecendo na tela de vocês."
""",
      "PENDÊNCIA: confirmar qual API gratuita será usada e testar o notebook antes de prometer em detalhe.")

s = sl_statement("Agora é com vocês", "Perguntas?",
                 "Escreva no chat. Vamos responder o máximo que o tempo permitir.\nO que não der tempo, respondemos no Discord ainda esta semana.")
notes(s, "4 min (elástico)", "ESSENCIAL", f"{FELIPE} + {EU}",
      """
Q&A com moderação. O moderador seleciona e agrupa as repetidas.

PERGUNTAS PREVISÍVEIS DESTA AULA, com resposta pronta:

• "Qual modelo é o melhor?"
  Depende da tarefa, do custo e do idioma. Para trabalho em português vale testar mais de
  um com o SEU caso, usando aquele conjunto de 20 a 50 exemplos.

• "Preciso pagar por ChatGPT para acompanhar o curso?"
  Não. Na quinta a gente usa API gratuita, e o Colab também é gratuito.

• "IA vai substituir o meu trabalho?"
  Ela troca a tarefa de escolher pela tarefa de conferir, como no exemplo da triagem de
  chamados. Quem sabe conferir bem fica mais valorizado.

• "Dá para usar isso com dado da empresa? E a LGPD?"
  Depende do contrato com o fornecedor e da política interna. Nunca cole dado pessoal ou
  sigiloso numa ferramenta pública sem autorização. Isso é assunto da semana de governança.

• "Qual a diferença entre RAG e fine-tuning?"
  RAG serve para conhecimento que muda. Fine-tuning serve para comportamento e formato.
  Na dúvida, comece por RAG, que é mais barato e mais fácil de atualizar.

• "Esses modelos aprendem com o que eu escrevo?"
  Depende do produto e do plano contratado. Em plano corporativo costuma haver garantia de
  não treinar com o seu dado. Confira sempre antes de usar com material da empresa.
""")

s = sl_closing()
notes(s, "1 min", "ESSENCIAL", FELIPE,
      """
FECHAMENTO (30 segundos, com energia):

"Obrigado pela noite de hoje. Foi a aula mais técnica até agora, e vocês seguraram bem.

Entrem no Discord, o resumo com o glossário de hoje vai estar lá.

E fica com isso: hoje vocês passaram a entender por dentro uma ferramenta que a maior parte
das pessoas usa no escuro. Isso já muda a conversa que vocês conseguem ter sobre ela. Nos
vemos na quinta, com código na tela. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Postar no Discord o resumo e o glossário.
- 10 minutos de retrospectiva entre os dois: qual bloco atrasou e por quê.
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

out = ROOT / "docs" / "aula-03"
out.mkdir(parents=True, exist_ok=True)
dest = out / "AI-Talent-Academy-Aula03.pptx"
prs.save(dest)
print(f"OK: {dest}  ({_n['i']} slides)  Roboto, sem travessões, tamanho único por bloco.")
