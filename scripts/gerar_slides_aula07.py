# -*- coding: utf-8 -*-
"""
Gerador do deck da Aula 7 (Semana 4, segunda-feira) do AI Talent Academy.

Tema: Analise de Dados com Python. Aula expositiva de ~4h05, sem mao na massa (a
pratica fica para a Aula 8, na quinta). A aula esticou de propósito, por pedido
explicito do usuario, para aprofundar o bloco de pandas (indice, dtype, loc/iloc,
valores ausentes, agregacao multipla, pivot_table e glossario), que e o foco real da
aula. Cobre tambem a historia da linguagem e as outras tres bibliotecas do bloco de
dados (NumPy, Matplotlib, Seaborn), com exemplos de codigo sempre voltando ao mesmo
caso de fraude em cartao ja usado nas Aulas 2, 5 e 6.

Identidade visual: padrao White Cube (Roboto, azul 28347B, fundos e logo do template
oficial em assets/whitecube/).

Uso:  python scripts/gerar_slides_aula07.py
Saida: docs/aula-07/AI-Talent-Academy-Aula07.pptx

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
          "Semana 4  ·  Análise de Dados com Python", 25, INK, space=0)
    shape(s, ML, Inches(5.75), Inches(2.4), Pt(5), fill=RED)
    block(s, ML, Inches(8.15), Inches(13), Inches(1.0),
          ["Aula 7  ·  Segunda-feira, 19h00 às 23h05  ·  Online",
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

"Boa noite! Semana 4, e hoje é a origem das ferramentas que a maioria de vocês já usa
sem saber de onde veio. Enquanto todo mundo entra, escreve no chat: você já ouviu falar
em pandas ou NumPy antes de hoje?"

Não comece antes de 19h08.
""",
      """
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- Moderador com o link do Discord pronto para colar.
- Sem código ao vivo hoje. Os exemplos aparecem no slide, a prática é na quinta.
""")

s = sl_bullets("Enquanto todo mundo entra", "Hoje é a origem das ferramentas que você já usa",
               [("Áudio e câmera", "microfone no mudo, câmera fica a seu critério"),
                ("Dúvidas", "escreva no chat a qualquer momento, temos moderação acompanhando"),
                ("Gravação", "a aula é gravada e o link chega em até 24h"),
                ("Ainda sem código ao vivo hoje", "os exemplos aparecem no slide, a prática de verdade é na quinta"),
                ("Aqueça o teclado", "escreva no chat: você já ouviu falar em pandas ou NumPy antes de hoje?")],
               subtitle="Aula 7 · Semana 4 · começamos 19h10")
notes(s, "19h00 às 19h10", "ESSENCIAL", EU,
      """
Leia os itens uma vez, por volta de 19h05. As respostas do chat servem de termômetro:
se quase ninguém conhece os nomes, vale desacelerar o bloco 2. Se boa parte já ouviu
falar, dá para andar mais rápido nos exemplos e sobrar tempo para perguntas.
""")

# ==========================================================================
# BLOCO A: Abertura (19h10 às 19h25)
# ==========================================================================
s = sl_section("01", "De onde vêm as ferramentas que você já usa",
               "A história por trás de Python, pandas e companhia",
               "19h10 às 19h25  ·  15 minutos")
notes(s, "19h10 às 19h25 (15 min)", "ESSENCIAL", EU,
      """
Bloco curto de contextualização. Situar a turma no programa e no porquê de uma aula
inteira de história antes de qualquer código. Ritmo rápido, 3 slides.
""")

s = sl_table("Onde estamos", "A jornada das 8 semanas",
             ["Semana", "Tema", "Foco"],
             [["1", "Fundamentos, nivelamento e panorama", "Todo mundo junto. Base comum"],
              ["2", "IA Generativa", "LLM por dentro, prompt e limites"],
              ["3", "Análise de Dados com SQL", "Consultar e extrair. A base de toda análise"],
              ["4 · hoje", "Análise de Dados com Python", "Manipular e visualizar. Storytelling com dados"],
              ["5", "Engenharia de Dados", "Construir os pipelines. Dado limpo, no lugar certo"],
              ["6", "Machine Learning", "Prever com dados. Do baseline ao modelo"],
              ["7", "Agentes de IA", "Da resposta à ação. IA que executa tarefas"],
              ["8", "Apresentação final", "Demo Day. Solução completa, do problema ao resultado"]],
             subtitle="Semana 4 de 8. A mesma lógica do SQL, agora dentro do Python.",
             widths=[0.12, 0.38, 0.50])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Onde vocês estão. Semana 3 foi SQL: consultar e extrair dado direto do banco. Hoje é
Python: pegar esse dado e manipular, cruzar, visualizar, contar uma história com ele.

É a mesma pergunta de sempre, só que com outra ferramenta na mão."
""")

s = sl_bullets("Por que Python", "A linguagem que virou padrão em dados, sem ter nascido para isso",
               [("Python não foi criado para análise de dados", "nasceu como linguagem de propósito geral, em 1989"),
                ("A comunidade científica adotou ele nos anos 2000", "e construiu bibliotecas em cima da linguagem, não dentro dela"),
                ("Hoje SQL busca o dado, Python manipula e visualiza", "os dois se completam, não competem"),
                ("As quatro bibliotecas de hoje nasceram fora de universidade e empresa de tecnologia", "vieram de gente resolvendo um problema real do próprio trabalho")])
notes(s, "4 min", "ESSENCIAL", EU,
      """
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
""")

s = sl_cards("O plano de hoje", "Quatro blocos, sempre voltando ao mesmo caso",
             [("A história do Python",
               "De onde vem a linguagem, e por que o nome não tem nada a ver com cobra.\n\n35 minutos"),
              ("NumPy",
               "A base numérica por trás de tudo o que vem depois.\n\n25 minutos"),
              ("pandas",
               "A ferramenta que vocês vão mais usar. Filtrar, agrupar, juntar, e bem mais.\n\n100 minutos"),
              ("Matplotlib e Seaborn",
               "Transformar tabela em gráfico.\n\n30 minutos")],
             subtitle="Toda vez que der, os exemplos usam o mesmo caso de fraude em cartão de sempre.",
             cols=4, card_h=3.2)
notes(s, "4 min", "ESSENCIAL", EU,
      """
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
""")

# ==========================================================================
# BLOCO B: A história do Python (19h25 às 20h00)
# ==========================================================================
s = sl_section("02", "A história do Python",
               "De um hobby de fim de ano a linguagem mais usada em dados",
               "19h25 às 20h00  ·  35 minutos")
notes(s, "19h25 às 20h00 (35 min)", "ESSENCIAL", EU,
      """
Bloco de contexto histórico. Objetivo: a turma sair sabendo de onde vem a linguagem, e
por que ela virou o padrão da área de dados sem ter sido desenhada para isso.

ESTRUTURA:
  Linha do tempo              8 min
  Por que o nome              6 min
  O Zen do Python             6 min
  Por que dominou dados       8 min
  Interação                   4 min
""")

s = sl_timeline("A história do Python", "Da concepção a hoje",
                [("1989", "Guido van Rossum começa Python como projeto de fim de ano, no feriado de Natal, no instituto de pesquisa CWI, na Holanda"),
                 ("1991", "Primeira versão pública, a 0.9.0"),
                 ("2000", "Python 2 é lançado"),
                 ("2008", "Python 3 é lançado, e no mesmo ano nascem pandas e a versão madura do NumPy"),
                 ("2018", "Guido van Rossum deixa o papel de dirigente vitalício da linguagem"),
                 ("Hoje", "Uma das linguagens mais usadas do mundo, puxada em boa parte pela área de dados e IA")],
                subtitle="Quase quatro décadas separam o hobby de Natal do Python que vocês usam hoje.")
notes(s, "8 min", "ESSENCIAL", EU,
      """
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
""")

s = sl_bullets("A história do Python", "Por que \"Python\", e não tem nada a ver com cobra",
               [("O nome vem de um programa de comédia britânico", "Monty Python's Flying Circus, o programa de televisão favorito de Guido van Rossum"),
                ("O símbolo virou cobra depois, por associação visual", "não foi essa a inspiração original do nome"),
                ("A filosofia da linguagem também vem daí", "bom humor e simplicidade fazem parte do projeto desde o início")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Pergunta clássica: por que Python? Todo mundo assume que é por causa da cobra. Não é.

O nome vem de um programa de comédia britânico, Monty Python's Flying Circus, que era o
programa de televisão favorito do Guido van Rossum na época. A cobra no símbolo veio
depois, por associação visual com o nome, não foi a inspiração original.

E essa origem não é só curiosidade: a filosofia da linguagem carrega bom humor e
simplicidade desde o início, e isso aparece até hoje na documentação oficial e nas
mensagens de erro."
""")

s = sl_bullets("A história do Python", "O Zen do Python, em quatro linhas",
               [("Bonito é melhor que feio", "código também se lê, não só executa"),
                ("Explícito é melhor que implícito", "prefira ficar claro a ser esperto"),
                ("Simples é melhor que complexo", "e complexo ainda é melhor que complicado"),
                ("Legibilidade conta", "código é escrito uma vez e lido muitas")],
               subtitle="Digite \"import this\" em qualquer instalação de Python, e o texto inteiro aparece.")
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Existe um documento não oficial, mas que todo mundo trata como oficial, chamado o Zen
do Python. Dezenove frases curtas sobre como escrever código nessa linguagem. Separei
quatro.

Bonito é melhor que feio: código também se lê, não só executa. Explícito é melhor que
implícito: prefira ficar claro a ser esperto. Simples é melhor que complexo, e complexo
ainda é melhor que complicado. E a que mais importa para quem está começando:
legibilidade conta, porque código é escrito uma vez e lido muitas.

Quem quiser ler as dezenove, é só abrir o Python e digitar import this. O texto inteiro
aparece na tela, é uma piada interna da comunidade que virou parte da linguagem."
""")

s = sl_bullets("A história do Python", "Por que Python dominou a área de dados",
               [("A sintaxe é próxima da leitura comum", "menos barreira para quem não vem de programação"),
                ("A comunidade científica adotou cedo", "físicos e estatísticos preferiram Python a linguagens mais fechadas"),
                ("O ecossistema cresceu em cima da linguagem, não trancado nela", "qualquer pessoa podia publicar uma biblioteca nova"),
                ("As quatro ferramentas de hoje são prova disso", "nenhuma delas foi criada pela equipe oficial do Python")],
               subtitle="As próximas duas horas e meia são sobre essas quatro ferramentas.")
notes(s, "8 min", "ESSENCIAL", EU,
      """
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
""")

s = sl_interaction("Interação", "De onde vem o nome",
                   "Qual dessas ferramentas tem um nome que descreve literalmente o que ela faz, diferente das outras três?",
                   ["A: Python, nome de um programa de comédia",
                    "B: pandas, termo de econometria",
                    "C: NumPy, sigla de \"Numerical Python\"",
                    "Responda na enquete, 30 segundos"])
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Testando o que a gente acabou de ver, e adiantando o próximo bloco. Qual dessas
ferramentas tem um nome que descreve literalmente o que ela faz?"

[aguarde 30 segundos]

Resposta: C. NumPy vem de "Numerical Python", nome direto ao ponto. Python vem de um
programa de comédia, sem relação com programação. pandas vem de um termo de
econometria, "panel data". A gente vai ver os dois de perto no resto da aula.
""")

# ==========================================================================
# BLOCO C: NumPy (20h00 às 20h25)
# ==========================================================================
s = sl_section("03", "NumPy",
               "A base numérica por trás de tudo o que vem depois",
               "20h00 às 20h25  ·  25 minutos")
notes(s, "20h00 às 20h25 (25 min)", "ESSENCIAL", EU,
      """
Primeira biblioteca de verdade da noite. Objetivo: entender que NumPy existe para fazer
conta em massa rápido, e que tudo o que vem depois herda essa base.

ESTRUTURA:
  A origem do NumPy       6 min
  Criando um array          8 min
  Operação vetorizada       8 min
  Transição                 3 min
""")

s = sl_bullets("NumPy", "De duas bibliotecas rivais para uma só",
               [("Nos anos 1990, existiam duas bibliotecas numéricas concorrentes", "Numeric e Numarray, cada uma com um ponto forte diferente"),
                ("Em 2005, Travis Oliphant uniu as duas", "e o resultado se chamou NumPy"),
                ("A peça central é o array", "uma estrutura que guarda números do mesmo tipo, em bloco, na memória"),
                ("Todo o resto do ecossistema de dados roda em cima do array do NumPy", "incluindo o pandas, que vocês vão ver no próximo bloco")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Nos anos 1990, existiam duas bibliotecas numéricas concorrentes em Python, a Numeric e
a Numarray, cada uma melhor em uma coisa e pior em outra. Isso dividia esforço e
confundia quem estava escolhendo qual usar.

Em 2005, Travis Oliphant uniu as duas, e o resultado se chamou NumPy.

A peça central é o array: uma estrutura que guarda números do mesmo tipo, em bloco, na
memória, de um jeito bem mais compacto que uma lista comum de Python.

E aqui vai a frase mais importante do bloco: todo o resto do ecossistema de dados roda
em cima do array do NumPy, incluindo o pandas, que a gente vê depois do intervalo."
""")

s = sl_code("NumPy", "Criando um array e comparando com uma lista comum",
            ["import numpy as np", "", "valores = np.array([120.50, 89.90, 4500.00])",
             "valores.mean()"],
            [("np.array cria o array a partir de uma lista comum", "mas por dentro guarda os números de um jeito bem mais compacto"),
             (".mean() calcula a média direto", "sem precisar escrever um laço somando e dividindo"),
             ("Uma lista comum de Python não tem esse tipo de operação pronta", "é por isso que o array existe")])
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Primeiro exemplo de código da noite. np.array pega uma lista comum, com três valores de
transação, e transforma num array. Por fora parece uma lista, por dentro é uma estrutura
bem mais compacta.

E já aparece a vantagem: .mean() calcula a média direto, sem escrever um laço somando
item por item e dividindo pelo total. Uma lista comum de Python não tem esse tipo de
operação pronta. É exatamente para isso que o array existe."
""")

s = sl_code("NumPy", "Operação vetorizada: aplicar em tudo de uma vez",
            ["import numpy as np", "", "valores = np.array([120.50, 89.90, 4500.00])",
             "valores * 1.1"],
            [("A operação se aplica em cada posição do array de uma vez", "sem escrever um laço percorrendo item por item"),
             ("Isso se chama vetorização", "e é a razão do NumPy ser tão mais rápido que Python puro para conta em massa"),
             ("O pandas, que vem no próximo bloco, herda essa mesma ideia", "cada coluna de uma tabela pandas é, por dentro, um array do NumPy")])
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Segundo exemplo: multiplicar o array inteiro por 1,1, simulando um reajuste de 10% em
todas as transações de uma vez.

Repara que não tem laço nenhum. A operação se aplica em cada posição do array ao mesmo
tempo. Isso se chama vetorização, e é a razão do NumPy ser tão mais rápido que Python
puro quando a conta é em massa, com milhares ou milhões de números.

E fica a ponte para o próximo bloco: o pandas herda exatamente essa ideia. Cada coluna
de uma tabela pandas é, por dentro, um array do NumPy. Vocês vão sentir essa mesma
rapidez lá."
""")

# ==========================================================================
# BLOCO D: pandas (20h40 às 22h20)
# ==========================================================================
s = sl_section("04", "pandas",
               "A ferramenta que você vai mais usar no dia a dia",
               "20h40 às 22h20  ·  100 minutos")
notes(s, "20h40 às 22h20 (100 min)", "ESSENCIAL", EU,
      """
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
""")

s = sl_bullets("pandas", "Nasceu dentro de um fundo de investimento, não de uma universidade",
               [("Wes McKinney criou o pandas em 2008", "trabalhando na AQR Capital Management, um fundo de investimento quantitativo"),
                ("Ele precisava analisar dado financeiro no dia a dia", "e Python, na época, não tinha nada parecido com o que a linguagem R oferecia"),
                ("O nome vem de \"panel data\"", "um termo de econometria para dado que combina tempo e categoria na mesma tabela"),
                ("Em 2009 o projeto virou open source", "e hoje é a ferramenta mais usada para manipular tabela em Python")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"pandas. A ferramenta que vocês vão mais usar a partir de hoje, e por isso este bloco
é bem mais longo que os outros.

Wes McKinney criou o pandas em 2008, trabalhando na AQR Capital Management, um fundo de
investimento quantitativo. Ele precisava analisar dado financeiro no dia a dia, e
Python, na época, não tinha nada parecido com o que a linguagem R já oferecia para isso.

O nome vem de "panel data", um termo de econometria para dado que combina tempo e
categoria na mesma tabela, exatamente o tipo de dado que ele analisava no fundo.

Em 2009 o projeto virou open source, e hoje é a ferramenta mais usada para manipular
tabela em Python, dentro e fora do mercado financeiro."
""")

s = sl_bullets("pandas", "Duas estruturas para guardar quase tudo",
               [("Series é uma coluna só", "uma sequência de valores, cada um com um rótulo"),
                ("DataFrame é a tabela inteira", "várias Series lado a lado, com linhas e colunas nomeadas"),
                ("Se você já usou planilha, já entendeu o essencial", "DataFrame é a versão programável de uma aba de Excel")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Duas estruturas resolvem quase tudo em pandas. Series é uma coluna só, uma sequência de
valores, cada um com um rótulo. DataFrame é a tabela inteira, várias Series lado a lado,
com linhas e colunas nomeadas.

E se você já usou planilha, já entendeu o essencial: DataFrame é a versão programável de
uma aba de Excel ou Google Sheets. A diferença é que aqui cada passo fica escrito em
código, então dá para repetir, revisar e automatizar."
""")

s = sl_bullets("pandas", "O índice: a terceira peça, além de linhas e colunas",
               [("Toda tabela pandas tem um índice, além das colunas", "por padrão, é só um número sequencial: 0, 1, 2..."),
                ("O índice não é uma coluna comum", "ele identifica cada linha, e várias operações usam ele por trás dos panos"),
                ("Dá para trocar o índice padrão por uma coluna que faça mais sentido", "como id_transacao, com set_index"),
                ("reset_index desfaz essa troca", "volta para o índice numérico padrão")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Antes do primeiro exemplo de código, uma peça que ninguém vê de cara: o índice. Toda
tabela pandas tem um índice, além das colunas de verdade. Por padrão, é só um número
sequencial, 0, 1, 2, e por aí vai.

O índice não é uma coluna comum, ele identifica cada linha, e várias operações que
vocês vão ver hoje usam ele por trás dos panos, mesmo sem vocês pedirem diretamente.

Dá para trocar esse índice padrão por uma coluna que faça mais sentido, como
id_transacao, usando set_index. E reset_index desfaz essa troca, volta para o número
sequencial. Guardem esse nome, ele vai voltar no bloco de loc e iloc."
""")

s = sl_code("pandas", "Lendo um arquivo e olhando as primeiras linhas",
            ["import pandas as pd", "", "transacoes = pd.read_csv(\"transacoes.csv\")",
             "transacoes.head()"],
            [("read_csv lê o arquivo inteiro e monta um DataFrame", "uma linha de código, uma tabela pronta"),
             ("head() mostra só as cinco primeiras linhas", "bom para conferir se o arquivo carregou certo, sem imprimir tudo"),
             ("Este é o mesmo transacoes.csv que vocês usaram na Aula 6", "o caminho muda, o dado é o mesmo")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Primeiro exemplo de pandas. read_csv lê o arquivo inteiro e já monta um DataFrame, numa
linha de código. head() mostra só as cinco primeiras linhas, bom para conferir se
carregou certo sem imprimir a tabela inteira na tela.

E olha a continuidade: esse é o mesmo transacoes.csv que vocês carregaram no FreeSQL na
Aula 6. O caminho do arquivo muda, o dado é exatamente o mesmo."
""")

s = sl_bullets("pandas", "Tipos de dado, o dtype de cada coluna",
               [("Cada coluna tem um tipo por trás, o dtype", "int64 e float64 para número, object para texto, datetime64 para data"),
                ("Um erro comum: número que chega como texto", "acontece quando o arquivo original tem alguma célula fora do padrão, e a coluna inteira vira object"),
                ("astype converte o tipo à força", "transacoes[\"valor\"].astype(float), por exemplo"),
                ("Data quase sempre precisa de conversão manual", "pd.to_datetime(coluna) transforma texto em data de verdade")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Cada coluna de um DataFrame tem um tipo por trás, o dtype. int64 e float64 para número,
object para texto, datetime64 para data.

E aqui mora um erro clássico de quem está começando: número que chega como texto. Isso
acontece quando o arquivo original tem alguma célula fora do padrão, uma vírgula, um
espaço, um texto onde devia ter número, e a coluna inteira vira object. Nesse estado,
soma e média simplesmente não funcionam, mesmo a coluna parecendo cheia de número.

astype converte o tipo à força, quando vocês já sabem que está tudo certo por trás. E
data quase sempre precisa de conversão manual: pd.to_datetime transforma um texto em
data de verdade, com todas as operações de data e hora liberadas depois disso."
""")

s = sl_code("pandas", "Um primeiro raio-x da tabela",
            ["transacoes.info()", "transacoes.describe()"],
            [("info() mostra o tipo de cada coluna e quantos valores não vazios existem", "o primeiro lugar para conferir se algo veio errado do arquivo"),
             ("describe() resume as colunas numéricas", "conta, média, desvio, mínimo, máximo e os quartis, tudo de uma vez"),
             ("Os dois juntos respondem a primeira pergunta de qualquer análise", "o que eu tenho na mão, antes de fazer qualquer conta")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Com o dtype na cabeça, o primeiro raio-x de qualquer tabela nova. info() mostra o tipo
de cada coluna e quantos valores não vazios existem em cada uma, o primeiro lugar para
conferir se algo veio errado do arquivo.

describe() resume as colunas numéricas de uma vez: contagem, média, desvio padrão,
mínimo, máximo e os quartis. Onde vocês usariam COUNT, AVG, MIN e MAX separados em SQL,
aqui sai tudo junto, numa linha de código.

Os dois juntos respondem a primeira pergunta de qualquer análise: o que eu tenho na
mão, antes de fazer qualquer conta de verdade."
""")

s = sl_code("pandas", "Contando valores únicos",
            ["transacoes[\"canal\"].value_counts()", "transacoes[\"id_lojista\"].nunique()"],
            [("value_counts conta quantas vezes cada valor aparece", "aqui, quantas transações são presenciais e quantas são online"),
             ("nunique conta quantos valores DIFERENTES existem", "aqui, quantos lojistas distintos aparecem na tabela"),
             ("Os dois são o primeiro passo para entender uma coluna de categoria", "antes de filtrar ou agrupar por ela")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Duas funções pequenas que vocês vão usar toda hora. value_counts conta quantas vezes
cada valor aparece numa coluna, aqui quantas transações são presenciais e quantas são
online.

nunique conta quantos valores DIFERENTES existem, aqui quantos lojistas distintos
aparecem na tabela inteira, sem repetir.

Os dois são o primeiro passo para entender uma coluna de categoria, antes de decidir
como filtrar ou agrupar por ela."
""")

s = sl_code("pandas", "Filtrando linhas, a versão pandas do WHERE",
            ["caras = transacoes[transacoes[\"valor\"] > 1000]", "len(caras)"],
            [("Dentro dos colchetes vai uma condição", "e o pandas devolve só as linhas que passam nela"),
             ("É a mesma ideia do WHERE que vocês praticaram na Aula 5", "muda a sintaxe, não muda o raciocínio"),
             ("len() conta quantas linhas sobraram", "o equivalente ao COUNT(*) depois do filtro")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Filtro. Dentro dos colchetes vai uma condição, e o pandas devolve só as linhas que
passam nela. Aqui, só transações acima de 1000 reais.

É a mesma ideia do WHERE que vocês praticaram na Aula 5. Muda a sintaxe, não muda o
raciocínio: definir uma condição, e deixar a ferramenta filtrar.

len() conta quantas linhas sobraram depois do filtro, o equivalente ao COUNT(*) que
vocês já usaram em SQL."
""")

s = sl_code("pandas", "loc e iloc: duas formas de selecionar",
            ["transacoes.loc[0, \"valor\"]", "transacoes.iloc[0, 3]"],
            [("loc seleciona pelo rótulo", "o nome do índice e o nome da coluna"),
             ("iloc seleciona pela posição", "a posição numérica da linha e da coluna, começando em zero"),
             ("Quando o índice é o número padrão, os dois parecem iguais", "a diferença aparece quando o índice vira outra coisa, como id_transacao"),
             ("Este é o ponto que mais confunde quem está começando", "guardem a regra: loc é nome, iloc é posição")])
notes(s, "7 min", "ESSENCIAL", EU,
      """
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
""")

s = sl_interaction("Interação", "loc ou iloc",
                   "A tabela tem o índice trocado para id_transacao. Você quer a linha cujo id_transacao é 500. Qual comando resolve isso?",
                   ["A: transacoes.loc[500]",
                    "B: transacoes.iloc[500]",
                    "C: os dois dão o mesmo resultado sempre",
                    "Responda na enquete, 30 segundos"])
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Testando loc e iloc. A tabela tem o índice trocado para id_transacao. Você quer a linha
cujo id_transacao é 500. Qual comando resolve isso?"

[aguarde 30 segundos]

Resposta: A. loc busca pelo rótulo, e o rótulo aqui é o próprio id_transacao. iloc
buscaria a linha na posição 500 da tabela, que só por acaso seria a transação 500. C
está errado: os dois só coincidem quando o índice é o número sequencial padrão.
""")

s = sl_code("pandas", "Valores ausentes: encontrar e tratar",
            ["transacoes.isna().sum()",
             "transacoes[\"telefone\"].fillna(\"não informado\")"],
            [("No pandas, valor ausente se chama NaN", "o equivalente ao NULL que vocês já usaram em SQL"),
             ("isna() marca onde está vazio, sum() conta quantos por coluna", "o primeiro raio-x de qualidade de dado"),
             ("fillna substitui o vazio por um valor combinado", "aqui, um texto padrão no lugar do telefone que falta"),
             ("dropna faz o oposto, descarta a linha com valor ausente", "usa um ou outro dependendo do que a análise pede")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
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
""")

s = sl_code("pandas", "Criando uma coluna nova",
            ["transacoes[\"valor_com_taxa\"] = transacoes[\"valor\"] * 1.03"],
            [("Atribuir a uma coluna que ainda não existe cria ela", "sem precisar de nenhum comando especial"),
             ("A conta roda em todas as linhas de uma vez", "a mesma vetorização que vocês viram no bloco do NumPy"),
             ("É assim que se calcula métrica derivada", "taxa, margem, faixa de valor, o que a análise pedir")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Criar uma coluna nova é só atribuir a um nome que ainda não existe na tabela. Sem
comando especial, sem declarar nada antes.

E a conta roda em todas as linhas de uma vez, a mesma vetorização que vocês viram no
bloco do NumPy. Aqui, aplicando uma taxa de 3% em cima do valor de cada transação.

É assim que se calcula qualquer métrica derivada: taxa, margem, faixa de valor, o que a
análise pedir. Vocês vão fazer isso o tempo todo a partir de agora."
""")

s = sl_code("pandas", "Agrupando e somando, a versão pandas do GROUP BY",
            ["resumo = transacoes.groupby(\"id_lojista\")[\"valor\"].sum()",
             "resumo.sort_values(ascending=False)"],
            [("groupby separa as linhas em grupos", "um grupo para cada id_lojista, igual ao GROUP BY"),
             ("sum() soma o valor dentro de cada grupo", "a mesma agregação, escrita diferente"),
             ("sort_values ordena o resultado", "a versão pandas do ORDER BY")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"groupby separa as linhas em grupos, um grupo para cada id_lojista, exatamente como o
GROUP BY da Aula 5. sum() soma o valor dentro de cada grupo, a mesma agregação, só
escrita diferente.

E sort_values ordena o resultado, a versão pandas do ORDER BY. Reparem que em três
linhas de código a gente respondeu a mesma pergunta que levava um GROUP BY inteiro em
SQL: quanto cada lojista faturou, do maior para o menor."
""")

s = sl_code("pandas", "Mais de uma agregação de uma vez",
            ["transacoes.groupby(\"id_lojista\")[\"valor\"].agg([\"count\", \"sum\", \"mean\"])"],
            [("agg aceita uma lista de funções de uma vez", "aqui, contagem, soma e média, numa linha só"),
             ("Sem agg, seria preciso repetir o groupby uma vez para cada conta", "um jeito bem mais longo de chegar no mesmo lugar"),
             ("O resultado sai como uma tabela, uma coluna por função pedida", "pronta para virar relatório")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"O groupby do slide anterior calculou uma agregação só. Na prática, quase sempre vocês
vão querer mais de uma ao mesmo tempo, e é para isso que existe o agg.

agg aceita uma lista de funções de uma vez, aqui contagem, soma e média, numa linha só.
Sem ele, seria preciso repetir o groupby inteiro uma vez para cada conta, um jeito bem
mais longo de chegar no mesmo lugar.

O resultado já sai como uma tabela, uma coluna por função pedida, pronta para virar
relatório ou gráfico, que é exatamente o assunto do próximo bloco."
""")

s = sl_bullets("pandas", "Tabela dinâmica: pivot_table",
               [("pivot_table é a versão programável da tabela dinâmica do Excel", "quem já usou uma reconhece a lógica na hora"),
                ("Ela cruza duas colunas de categoria, com uma agregação no meio", "por exemplo, lojista nas linhas e canal nas colunas"),
                ("É a ferramenta certa quando um groupby de coluna só não é suficiente", "quando a pergunta envolve duas dimensões ao mesmo tempo")])
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Última ferramenta nova antes do merge: pivot_table, a versão programável da tabela
dinâmica do Excel ou Google Sheets. Quem já montou uma reconhece a lógica na hora.

Ela cruza duas colunas de categoria, com uma agregação no meio. Por exemplo, um lojista
por linha, um canal por coluna, e o valor somado em cada cruzamento.

É a ferramenta certa quando o groupby de uma coluna só não é suficiente, quando a
pergunta de negócio envolve duas dimensões ao mesmo tempo, não uma."
""")

s = sl_code("pandas", "Um exemplo de pivot_table",
            ["pd.pivot_table(transacoes, index=\"id_lojista\", columns=\"canal\",",
             "               values=\"valor\", aggfunc=\"sum\")"],
            [("index define as linhas da tabela final", "aqui, um lojista por linha"),
             ("columns define as colunas", "aqui, uma coluna para presencial, outra para online"),
             ("values e aggfunc dizem o que calcular em cada cruzamento", "aqui, a soma do valor")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"index define as linhas da tabela final, aqui um lojista por linha. columns define as
colunas, aqui uma coluna para presencial, outra para online.

values e aggfunc dizem o que calcular em cada cruzamento, aqui a soma do valor. O
resultado é uma tabela nova: cada lojista, quanto vendeu presencial, quanto vendeu
online, lado a lado. Essa pergunta não sairia de um groupby de uma coluna só."
""")

s = sl_code("pandas", "Juntando tabelas, a versão pandas do JOIN",
            ["completo = transacoes.merge(cartoes, on=\"id_cartao\")", "completo.head()"],
            [("merge junta duas tabelas por uma coluna em comum", "aqui, id_cartao, a mesma chave que o JOIN usava"),
             ("Por padrão, merge se comporta como INNER JOIN", "só entra quem existe nas duas tabelas"),
             ("Para o equivalente de LEFT JOIN, existe o parâmetro how", "how=\"left\" muda esse comportamento")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"merge, a versão pandas do JOIN. Junta duas tabelas por uma coluna em comum, aqui
id_cartao, a mesma chave que vocês usaram na Aula 6.

Por padrão, merge se comporta como INNER JOIN: só entra quem existe nas duas tabelas.
Para o equivalente de LEFT JOIN, existe o parâmetro how, e how igual a "left" muda esse
comportamento.

Se você entendeu JOIN na Aula 5 e 6, você já entendeu merge. É a mesma lógica, com
outro nome."
""")

s = sl_table("pandas", "Glossário rápido",
             ["Termo", "O que significa"],
             [["DataFrame", "a tabela inteira, linhas e colunas"],
              ["Series", "uma coluna só, com índice"],
              ["Índice (index)", "o rótulo que identifica cada linha"],
              ["dtype", "o tipo de dado por trás de uma coluna"],
              ["NaN", "valor ausente, o NULL do pandas"],
              ["Vetorização", "aplicar uma conta em todas as linhas de uma vez, sem laço"],
              ["axis", "a direção de uma operação: 0 é por linha, 1 é por coluna"],
              ["inplace", "quando uma operação altera a própria tabela, em vez de devolver uma cópia"]],
             subtitle="Termos que aparecem toda hora em documentação e em vaga de emprego.",
             widths=[0.3, 0.7])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Antes de fechar o bloco, um glossário rápido. Estes oito termos aparecem toda hora em
documentação e em vaga de emprego, e vale reconhecer todos.

DataFrame, a tabela inteira. Series, uma coluna só. Índice, o rótulo de cada linha.
dtype, o tipo por trás de uma coluna. NaN, valor ausente, o NULL do pandas. Vetorização,
aplicar uma conta em todas as linhas de uma vez. axis, a direção de uma operação, 0 por
linha, 1 por coluna. E inplace, quando uma operação altera a própria tabela, em vez de
devolver uma cópia nova.

Não precisa decorar agora. Precisa reconhecer quando aparecer de novo, e vai aparecer."
""")

s = sl_interaction("Interação", "Qual comando resolve isso",
                   "Você quer o valor médio de transação por canal, presencial ou online. Qual sequência resolve isso?",
                   ["A: transacoes.groupby(\"canal\")[\"valor\"].mean()",
                    "B: transacoes[\"canal\"].mean()",
                    "C: transacoes.merge(\"canal\")",
                    "Responda na enquete, 30 segundos"])
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Testando o bloco inteiro numa pergunta só. Você quer o valor médio de transação por
canal. Qual sequência resolve isso?"

[aguarde 30 segundos]

Resposta: A. groupby separa por canal, e mean() calcula a média do valor dentro de cada
grupo. B tenta calcular média de uma coluna de texto, não funciona. C tenta um merge sem
sentido, canal não é uma tabela para juntar.
""")

# ==========================================================================
# BLOCO E: Matplotlib e Seaborn (22h20 às 22h50)
# ==========================================================================
s = sl_section("05", "Matplotlib e Seaborn",
               "Transformar tabela em gráfico",
               "22h20 às 22h50  ·  30 minutos")
notes(s, "22h20 às 22h50 (30 min)", "ESSENCIAL", EU,
      """
Último bloco de conteúdo. Objetivo: sair sabendo que as duas ferramentas se completam,
uma desenha, a outra deixa bonito por padrão.

ESTRUTURA:
  A origem do Matplotlib     6 min
  Um gráfico de barras         7 min
  A origem do Seaborn           6 min
  Um histograma                  7 min
  Transição                       4 min
""")

s = sl_bullets("Matplotlib", "Um neurocientista que queria replicar o MATLAB em Python",
               [("John Hunter criou o Matplotlib a partir de 2002", "ele analisava sinal de eletroencefalograma, e usava o MATLAB para os gráficos"),
                ("O objetivo inicial era simples", "ter no Python o mesmo tipo de gráfico que ele já fazia no MATLAB"),
                ("Hoje é a base de quase todo gráfico feito em Python", "inclusive o Seaborn, que vem a seguir, é construído em cima dele")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Matplotlib. John Hunter criou a partir de 2002. Ele era neurocientista, analisava sinal
de eletroencefalograma, e usava o MATLAB para gerar os gráficos da pesquisa.

O objetivo inicial era simples: ter no Python o mesmo tipo de gráfico que ele já fazia
no MATLAB, sem precisar trocar de ferramenta no meio do trabalho.

Hoje o Matplotlib é a base de quase todo gráfico feito em Python. Inclusive o Seaborn,
que vem a seguir, usa o Matplotlib por baixo, em vez de ser uma ferramenta separada."
""")

s = sl_code("Matplotlib", "Um gráfico de barras, do resumo por lojista",
            ["import matplotlib.pyplot as plt", "", "plt.bar(resumo.index, resumo.values)",
             "plt.show()"],
            [("bar() desenha uma barra para cada posição", "aqui, uma barra por lojista"),
             ("resumo.index vira o eixo horizontal, resumo.values a altura das barras", "o mesmo resumo que veio do groupby, agora virando desenho"),
             ("show() é o que efetivamente exibe o gráfico na tela", "sem ele, o gráfico fica montado mas invisível")])
notes(s, "7 min", "ESSENCIAL", EU,
      """
"bar() desenha uma barra para cada posição, aqui uma barra por lojista. resumo.index
vira o eixo horizontal, resumo.values a altura de cada barra. É o mesmo resumo que saiu
do groupby no bloco anterior, agora virando desenho.

E não esqueçam do show(): é o que efetivamente exibe o gráfico na tela. Sem ele, o
gráfico fica montado por dentro do programa, mas invisível para quem está olhando."
""")

s = sl_bullets("Seaborn", "Construído em cima do Matplotlib, com outro objetivo",
               [("Michael Waskom criou o Seaborn a partir de 2012", "para deixar gráfico estatístico bonito por padrão, sem configurar tudo à mão"),
                ("O nome é uma referência a um personagem de série de TV", "Sam Seaborn, de The West Wing"),
                ("Seaborn não substitui o Matplotlib, ele se apoia nele", "por baixo, quem desenha continua sendo o Matplotlib")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Seaborn. Michael Waskom criou a partir de 2012, com um objetivo diferente do
Matplotlib: deixar gráfico estatístico bonito por padrão, sem precisar configurar cor,
proporção e estilo à mão toda vez.

Uma curiosidade: o nome é uma referência a um personagem de série de TV, Sam Seaborn,
de The West Wing.

E o ponto técnico mais importante: Seaborn não substitui o Matplotlib, ele se apoia
nele. Por baixo, quem desenha continua sendo o Matplotlib. Seaborn só decide as cores,
proporções e ajustes por vocês."
""")

s = sl_code("Seaborn", "Um histograma, para ver a distribuição do valor",
            ["import seaborn as sns", "", "sns.histplot(transacoes[\"valor\"])"],
            [("histplot desenha um histograma", "quantas transações caem em cada faixa de valor"),
             ("Em uma linha, já sai com eixo, cor e proporção ajustados", "no Matplotlib puro, isso levaria várias linhas de configuração"),
             ("Seaborn entende DataFrame do pandas nativamente", "por isso os três nomes de hoje trabalham tão bem juntos")])
notes(s, "7 min", "ESSENCIAL", EU,
      """
"Último exemplo de código da noite. histplot desenha um histograma: quantas transações
caem em cada faixa de valor.

Em uma linha só, já sai com eixo, cor e proporção ajustados. No Matplotlib puro, chegar
nesse mesmo resultado levaria várias linhas de configuração manual.

E reparem que a função recebeu a coluna de um DataFrame direto, sem conversão nenhuma.
Seaborn entende pandas nativamente. É por isso que NumPy, pandas, Matplotlib e Seaborn
trabalham tão bem juntos: cada um foi construído sabendo que o anterior já existia."
""")

# ==========================================================================
# BLOCO F: Encerramento (22h50 às 23h05)
# ==========================================================================
s = sl_section("06", "Encerramento",
               "O que vocês levam de hoje e o que vem na semana 5",
               "22h50 às 23h05  ·  15 minutos")
notes(s, "22h50 às 23h05 (15 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Recapitulação            4 min
  O que vem pela frente    3 min
  Q&A                      6 min  (elástico, absorve atraso)
  Fechamento               2 min
""")

s = sl_bullets("Encerramento", "Cinco ideias para levar de hoje",
               [("Python nasceu como hobby, não como ferramenta de dados", "o ecossistema de dados foi construído em cima dele depois"),
                ("NumPy existe para fazer conta em massa rápido", "com array e operação vetorizada, sem laço explícito"),
                ("pandas faz em Python o que vocês já sabem fazer em SQL", "filtrar, agrupar e juntar, com outra sintaxe"),
                ("Matplotlib desenha, Seaborn deixa bonito por padrão", "um se apoia no outro, não competem"),
                ("Nenhuma das quatro ferramentas veio de dentro do time oficial do Python", "vieram de gente resolvendo o próprio problema, e publicando depois")],
               subtitle="Se você levar só essas cinco frases, a noite cumpriu o objetivo.",
               numbered=True)
notes(s, "4 min", "ESSENCIAL", EU,
      """
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
""")

s = sl_two_col("Próximos encontros", "O que vem pela frente",
               "SEGUNDA · Semana 5",
               ["Engenharia de Dados",
                "Como construir os pipelines",
                "Ainda conceitual, como toda segunda",
                "Dado limpo, no lugar certo"],
               "QUINTA · Semana 4",
               ["Primeiro contato com pandas de verdade, no Colab",
                "Filtrar, agrupar e juntar o caso de fraude, com código",
                "Mesmo formato: demonstração e mão na massa",
                "Vale revisar os slides de hoje antes"],
               subtitle="A quinta desta semana é onde Python sai do slide e vai para o Colab de vocês.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"O que vem pela frente.

Na quinta desta semana, Python sai do slide e vai para o Colab de vocês, com o mesmo
caso de fraude. Vale revisar estes slides antes.

E na segunda da semana 5, engenharia de dados: como construir os pipelines que entregam
dado limpo, no lugar certo. Ainda conceitual, como toda segunda."
""")

s = sl_statement("Antes de ir", "Perguntas?",
                 "Escreva no chat. O que não der tempo, respondemos no Discord ainda hoje.")
notes(s, "6 min", "ESSENCIAL", EU,
      """
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
""")

s = sl_closing()
notes(s, "2 min", "ESSENCIAL", EU,
      """
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

out = ROOT / "docs" / "aula-07"
out.mkdir(parents=True, exist_ok=True)
dest = out / "AI-Talent-Academy-Aula07.pptx"
prs.save(dest)
print(f"OK: {dest}  ({len(prs.slides._sldIdLst)} slides)  "
      f"Roboto, sem travessões, tamanho único por bloco.")
