# -*- coding: utf-8 -*-
"""
Gerador do deck da Aula 5 (Semana 3, segunda-feira) do AI Talent Academy.

Tema: Analise de Dados com SQL. Aula expositiva de ~3h05, sem mao na massa (a pratica
com banco real fica para a Aula 6, na quinta). Todos os exemplos de consulta partem do
mesmo caso de fraude em cartao ja usado na Aula 2.

Identidade visual: padrao White Cube (Roboto, azul 28347B, fundos e logo do template
oficial em assets/whitecube/).

Uso:  python scripts/gerar_slides_aula05.py
Saida: docs/aula-05/AI-Talent-Academy-Aula05.pptx

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
          "Semana 3  ·  Análise de Dados com SQL", 25, INK, space=0)
    shape(s, ML, Inches(5.75), Inches(2.4), Pt(5), fill=RED)
    block(s, ML, Inches(8.15), Inches(13), Inches(1.0),
          ["Aula 5  ·  Segunda-feira, 19h00 às 22h05  ·  Online",
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


def sl_query(kicker, title, query, items, subtitle=None):
    """Bloco de consulta SQL em destaque, com bullets de explicacao embaixo."""
    s = new_slide(BG_WHITE)
    y = chrome(s, kicker, title, subtitle)
    linhas = query if isinstance(query, list) else query.split("\n")
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

# --------------------------------------------------------------------------
# RECEPÇÃO (19h00 às 19h10)
# --------------------------------------------------------------------------
s = sl_cover()
notes(s, "19h00 às 19h10 (slide de espera)", "ESSENCIAL", EU,
      """
Slide projetado desde 18h55. Fale a cada 2 ou 3 minutos enquanto a sala enche.

"Boa noite! Terceira semana, e hoje é a primeira aula técnica de verdade do programa:
SQL. Enquanto todo mundo entra, escreve no chat: hoje você já usa filtro ou tabela
dinâmica numa planilha? É a mesma lógica de hoje, só que com outro nome."

Não comece antes de 19h08.
""",
      """
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- Moderador com o link do Discord pronto para colar.
- Sem código ao vivo hoje. As consultas aparecem como slide, a prática é na quinta.
""")

s = sl_bullets("Enquanto todo mundo entra", "Hoje é a primeira aula técnica de verdade",
               [("Áudio e câmera", "microfone no mudo, câmera fica a seu critério"),
                ("Dúvidas", "escreva no chat a qualquer momento, temos moderação acompanhando"),
                ("Gravação", "a aula é gravada e o link chega em até 24h"),
                ("Ainda sem código ao vivo hoje", "as consultas aparecem no slide, a prática de verdade é na quinta"),
                ("Aqueça o teclado", "escreva no chat: você já usa filtro ou tabela dinâmica numa planilha?")],
               subtitle="Aula 5 · Semana 3 · começamos 19h10")
notes(s, "19h00 às 19h10", "ESSENCIAL", EU,
      """
Leia os itens uma vez, por volta de 19h05. Insista no quarto item: tem gente que vai
ficar tensa por achar que hoje é dia de escrever código na frente de todo mundo, e não é.
""")

# ==========================================================================
# BLOCO A: Abertura (19h10 às 19h25)
# ==========================================================================
s = sl_section("01", "Por que SQL, e por que agora",
               "A ferramenta mais antiga da área, ainda a mais usada todo dia",
               "19h10 às 19h25  ·  15 minutos")
notes(s, "19h10 às 19h25 (15 min)", "ESSENCIAL", EU,
      """
Bloco curto de contextualização. Situar a turma no programa e justificar por que SQL
vem antes de Python. Ritmo rápido, 3 slides.
""")

s = sl_table("Onde estamos", "A jornada das 8 semanas",
             ["Semana", "Tema", "Foco"],
             [["1", "Fundamentos, nivelamento e panorama", "Todo mundo junto. Base comum"],
              ["2", "IA Generativa", "LLM por dentro, prompt e limites"],
              ["3 · hoje", "Análise de Dados com SQL", "Consultar e extrair. A base de toda análise"],
              ["4", "Análise de Dados com Python", "Manipular e visualizar. Storytelling com dados"],
              ["5", "Engenharia de Dados", "Construir os pipelines. Dado limpo, no lugar certo"],
              ["6", "Machine Learning", "Prever com dados. Do baseline ao modelo"],
              ["7", "Agentes de IA", "Da resposta à ação. IA que executa tarefas"],
              ["8", "Apresentação final", "Demo Day. Solução completa, do problema ao resultado"]],
             subtitle="Semana 3 de 8. A primeira vez que a mão vai literalmente no dado.",
             widths=[0.12, 0.38, 0.50])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Onde vocês estão. Semana 1 foi panorama. Semana 2 foi IA generativa, de propósito antes
de qualquer coisa técnica, porque é a porta de entrada mais acessível da área.

Hoje, semana 3, começa a parte estrutural: SQL primeiro, Python na semana 4, engenharia
de dados na 5, machine learning na 6, agentes na 7. Faz sentido nessa ordem: você precisa
saber consultar e limpar dado antes de modelar qualquer coisa."
""")

s = sl_bullets("Por que SQL", "Por que a ferramenta mais antiga ainda é a mais usada",
               [("É a habilidade mais pedida em vaga de dados", "aparece em quase toda descrição, do estágio ao cargo sênior"),
                ("Funciona em praticamente qualquer banco", "você aprende uma vez, usa em qualquer empresa que entrar"),
                ("Existe desde os anos 1970 e continua sendo a base", "Python e outras ferramentas se conectam nela, não a substituem"),
                ("Sem SQL, todo pedido de dado vira um pedido para outra pessoa", "com SQL, você mesmo busca a resposta")],
               subtitle="A ferramenta mais antiga da área ainda é a mais usada todo dia.")
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Quatro razões para dedicar uma noite inteira a SQL.

Primeira: é a habilidade mais pedida em vaga de dados, sem exceção de nível.

Segunda: funciona em praticamente qualquer banco. Aprende uma vez, usa a vida inteira.

Terceira: SQL existe desde os anos 1970 e continua sendo a base. Python se conecta nela,
não substitui ela.

E a quarta, a mais prática: sem SQL, todo pedido de dado vira um pedido para outra
pessoa. Com SQL, você mesmo busca a resposta, sem depender de fila de outro time."
""")

s = sl_cards("O plano de hoje", "Quatro blocos, sempre voltando ao mesmo caso",
             [("Anatomia de uma consulta",
               "SELECT, FROM, WHERE, ORDER BY e LIMIT.\n\n35 minutos"),
              ("Filtros e condições",
               "Refinar o que a consulta traz de volta.\n\n25 minutos"),
              ("Agregações",
               "Resumir muitas linhas numa resposta só.\n\n35 minutos"),
              ("Juntando tabelas",
               "JOIN, e por que os dados vivem separados.\n\n30 minutos")],
             subtitle="Todo exemplo parte do mesmo caso: fraude em cartão, da Aula 2.",
             cols=4, card_h=3.2)
notes(s, "4 min", "ESSENCIAL", EU,
      """
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
""")

# ==========================================================================
# BLOCO B: Anatomia de uma consulta (19h25 às 20h00)
# ==========================================================================
s = sl_section("02", "Anatomia de uma consulta",
               "SELECT, FROM, WHERE, ORDER BY e LIMIT",
               "19h25 às 20h00  ·  35 minutos")
notes(s, "19h25 às 20h00 (35 min)", "ESSENCIAL", EU,
      """
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
""")

s = sl_table("O caso de hoje", "Três tabelas, o mesmo caso da Aula 2",
             ["Tabela", "O que guarda", "Colunas principais"],
             [["transacoes", "Cada compra no cartão", "id_transacao, id_cliente, id_lojista, valor, data_hora, canal, status"],
              ["clientes", "Quem é o dono do cartão", "id_cliente, nome, cidade, data_cadastro"],
              ["lojistas", "Onde a compra aconteceu", "id_lojista, nome, categoria, cidade"]],
             subtitle="O mesmo caso de fraude em cartão da Aula 2. Toda consulta de hoje parte daqui.",
             widths=[0.18, 0.32, 0.50])
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Antes de qualquer consulta, as três tabelas que vamos usar a noite inteira.

Transações: cada compra no cartão, com valor, data, canal e status.

Clientes: quem é o dono do cartão.

Lojistas: onde a compra aconteceu.

Repara que o dado não está tudo numa tabela só. A gente vai voltar nisso no bloco de
JOIN, mas já fica o aviso: isso é proposital. A razão aparece mais à frente."
""")

s = sl_bullets("O que é SQL", "SQL não é programação no sentido comum",
               [("SQL é uma linguagem declarativa", "você descreve o que quer, não o passo a passo de como buscar"),
                ("O banco decide o caminho mais rápido", "por trás da consulta existe um otimizador escolhendo a rota"),
                ("A base de tudo são cinco palavras", "SELECT, FROM, WHERE, ORDER BY e LIMIT resolvem boa parte das perguntas do dia a dia")])
notes(s, "4 min", "ESSENCIAL", EU,
      """
"SQL significa Structured Query Language, mas o nome ajuda pouco. O que importa é isto:
SQL é uma linguagem declarativa. Você descreve O QUE quer, não escreve o passo a passo de
como buscar. Quem decide o caminho mais rápido é o banco, por trás, com um otimizador.

E a base de tudo, para o que vocês vão precisar no dia a dia, são cinco palavras: SELECT,
FROM, WHERE, ORDER BY e LIMIT. Vamos ver as cinco agora."
""")

s = sl_query("Anatomia de uma consulta", "SELECT e FROM: de onde vem o dado",
             ["SELECT nome, cidade", "FROM clientes"],
             [("SELECT escolhe as colunas", "só o que você pede aparece no resultado"),
              ("FROM escolhe a tabela", "de onde essas colunas são lidas"),
              ("A ordem das colunas no resultado segue o SELECT", "não a ordem da tabela original"),
              ("SELECT * traz todas as colunas", "prático para explorar, mas evite deixar assim num relatório final")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"A consulta mais simples possível. SELECT nome, cidade, FROM clientes.

SELECT escolhe as colunas, só o que você pede aparece. FROM escolhe a tabela, de onde
essas colunas são lidas.

Repara que a ordem das colunas no resultado segue o SELECT, não a ordem que elas estão
guardadas na tabela.

E um atalho comum: SELECT asterisco traz todas as colunas de uma vez. Prático para
explorar uma tabela nova, mas evite deixar isso num relatório final. É mais lento e traz
coluna que ninguém vai usar."
""",
      "Deixe este slide um pouco mais de tempo na tela. É o primeiro contato de muita gente com uma consulta de verdade.")

s = sl_query("Anatomia de uma consulta", "WHERE: filtrando antes de trazer o resultado",
             ["SELECT nome, cidade", "FROM clientes", "WHERE cidade = 'Curitiba'"],
             [("WHERE decide quais linhas entram", "aqui, só clientes de Curitiba aparecem no resultado"),
              ("Texto vai entre aspas simples", "número não precisa de aspas"),
              ("Sem WHERE, a consulta traz a tabela inteira", "numa tabela grande, isso pode travar o banco")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Agora um filtro. WHERE cidade igual Curitiba.

WHERE decide quais LINHAS entram no resultado, diferente do SELECT, que decide quais
COLUNAS aparecem. Aqui, só os clientes de Curitiba passam pelo filtro.

Detalhe de sintaxe: texto vai entre aspas simples. Número não precisa.

E um aviso de segurança: sem WHERE, a consulta traz a tabela inteira. Numa tabela com
milhões de linhas, isso pode travar o banco para todo mundo, não só para você."
""")

s = sl_query("Anatomia de uma consulta", "ORDER BY e LIMIT: ordenando e cortando",
             ["SELECT nome, valor", "FROM transacoes", "ORDER BY valor DESC", "LIMIT 10"],
             [("ORDER BY organiza o resultado", "ASC do menor para o maior, DESC do maior para o menor"),
              ("LIMIT corta o tamanho do resultado", "aqui, só as 10 transações de maior valor aparecem"),
              ("Juntos, respondem quais são os maiores", "um dos pedidos mais comuns em qualquer análise")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"ORDER BY valor DESC, LIMIT 10. Duas palavras que resolvem um pedido clássico: quais são
as dez maiores transações.

ORDER BY organiza o resultado. ASC é do menor para o maior, DESC é do maior para o menor.
LIMIT corta o tamanho do que volta.

Juntos, esses dois respondem 'quais são os maiores' ou 'quais são os menores', um dos
pedidos mais comuns em qualquer análise de negócio."
""")

s = sl_bullets("A ordem real", "A ordem que você escreve não é a ordem que o banco executa",
               [("FROM", "o banco decide primeiro de qual tabela vai ler"),
                ("WHERE", "filtra as linhas, antes de escolher qualquer coluna"),
                ("GROUP BY", "agrupa as linhas que sobraram, quando existe agrupamento"),
                ("HAVING", "filtra os grupos, depois de agrupar"),
                ("SELECT", "só agora escolhe as colunas do resultado"),
                ("ORDER BY", "organiza o que sobrou"),
                ("LIMIT", "corta o tamanho, por último")],
               subtitle="Você escreve SELECT primeiro. O banco lê FROM primeiro. Guarde essa ordem.",
               numbered=True)
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Este é o slide para fotografar. A ordem que você ESCREVE uma consulta não é a ordem que
o banco EXECUTA ela.

Primeiro o banco decide de qual tabela ler, o FROM. Depois filtra linha por linha, o
WHERE. Se existir agrupamento, agrupa, o GROUP BY, e filtra os grupos, o HAVING. Só
então escolhe as colunas do resultado, o SELECT. Organiza o que sobrou, o ORDER BY. E
corta o tamanho por último, o LIMIT.

GROUP BY e HAVING a gente ainda não usou, eles vêm no bloco de agregação, depois do
intervalo. Mas guardem esta ordem agora, porque ela explica um erro clássico de
iniciante que a gente vai ver lá na frente."
""")

s = sl_interaction("Interação", "Qual filtro resolve isso",
                   "Você quer as transações entre R$100 e R$300, feitas em São Paulo ou Curitiba. Qual cláusula resolve isso de um jeito só?",
                   ["A: WHERE valor > 100 AND cidade = 'São Paulo'",
                    "B: WHERE valor BETWEEN 100 AND 300 AND cidade IN ('São Paulo', 'Curitiba')",
                    "C: WHERE valor = 200 OR cidade = 'São Paulo'",
                    "Responda na enquete, 30 segundos"])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Testando o que a gente acabou de ver. Você quer transações entre R$100 e R$300, feitas
em São Paulo ou Curitiba. Qual opção resolve isso de um jeito só?"

[aguarde 30 segundos]

Resposta: B. BETWEEN resolve a faixa de valor numa linha só, e IN resolve a lista de
cidades sem precisar escrever OR duas vezes. A é incompleto, falta o limite superior do
valor. C está errado nos dois pedidos.
""")

# ==========================================================================
# BLOCO C: Filtrando e refinando (20h00 às 20h25)
# ==========================================================================
s = sl_section("03", "Filtrando e refinando",
               "Operadores, combinações e o cuidado com valor vazio",
               "20h00 às 20h25  ·  25 minutos")
notes(s, "20h00 às 20h25 (25 min)", "ESSENCIAL", EU,
      """
Bloco de aprofundamento do WHERE. Menos conceito novo, mais repertório de sintaxe.

ESTRUTURA:
  Comparação e faixa      7 min
  OR e IN                 7 min
  Texto e valor vazio      8 min
  Transição                3 min
""")

s = sl_query("Filtrando e refinando", "Comparando e testando faixas de valor",
             ["SELECT id_transacao, valor", "FROM transacoes", "WHERE valor > 500", "  AND valor <= 2000"],
             [("Operadores de comparação", "maior que, menor que, maior ou igual, menor ou igual, diferente"),
              ("AND exige que as duas condições sejam verdadeiras", "só entra quem passa nas duas ao mesmo tempo"),
              ("BETWEEN faz a mesma faixa numa linha só", "WHERE valor BETWEEN 500 AND 2000")])
notes(s, "7 min", "ESSENCIAL", EU,
      """
"Além do igual, os operadores de comparação: maior que, menor que, maior ou igual, menor
ou igual, diferente.

AND exige que as duas condições sejam verdadeiras ao mesmo tempo. Aqui, valor acima de
500 E até 2000.

E existe um atalho para faixa: BETWEEN escreve a mesma coisa numa linha só. Os dois
jeitos funcionam, BETWEEN só é mais direto de ler."
""")

s = sl_query("Filtrando e refinando", "OR e IN: combinando opções possíveis",
             ["SELECT nome, categoria", "FROM lojistas", "WHERE categoria = 'Eletrônicos'", "   OR categoria = 'Joalheria'"],
             [("OR exige que pelo menos uma condição seja verdadeira", "entra quem passa em qualquer uma das duas"),
              ("IN substitui uma fila de OR na mesma coluna", "WHERE categoria IN ('Eletrônicos', 'Joalheria')"),
              ("Cuidado ao misturar AND e OR", "sem parênteses, o resultado pode não ser o que você imaginou")])
notes(s, "7 min", "ESSENCIAL", EU,
      """
"OR é diferente de AND: exige só que UMA das condições seja verdadeira, não as duas.
Aqui, categoria eletrônicos OU joalheria.

Quando o OR se repete várias vezes na mesma coluna, existe um atalho: IN. Faz a mesma
coisa, com menos linha de código.

E um aviso importante: quando você mistura AND e OR na mesma consulta, sem parênteses o
banco pode agrupar as condições de um jeito que não é o que você pensou. Na dúvida, use
parênteses para deixar explícito."
""")

s = sl_query("Filtrando e refinando", "Texto e valor vazio",
             ["SELECT nome", "FROM clientes", "WHERE nome LIKE 'Ana%'", "  AND cidade IS NOT NULL"],
             [("LIKE busca por padrão de texto", "o símbolo % substitui qualquer sequência de caracteres"),
              ("Valor vazio no banco não é zero nem texto vazio", "é NULL, um estado próprio, sem valor definido"),
              ("Por isso NULL não se compara com igual", "usa IS NULL ou IS NOT NULL, nunca igual a NULL")])
notes(s, "8 min", "ESSENCIAL", EU,
      """
"LIKE busca por padrão de texto. 'Ana%' encontra qualquer nome que começa com Ana. O
símbolo % substitui qualquer sequência de caracteres.

E agora o ponto que mais confunde quem está começando: valor vazio no banco tem nome
próprio, NULL, um estado que significa 'sem valor definido', diferente de zero e
diferente de texto vazio.

Por causa disso, NULL não se compara com igual. Um erro comum de iniciante é escrever
WHERE cidade = NULL, e isso simplesmente não retorna nada, mesmo quando existe linha com
cidade vazia. O jeito certo é IS NULL, ou IS NOT NULL para o contrário."
""",
      "Este é o erro mais comum de quem está aprendendo. Vale repetir em voz alta: NULL nunca usa igual.")

# ==========================================================================
# BLOCO D: Agregações (20h40 às 21h15)
# ==========================================================================
s = sl_section("04", "Agregações",
               "Resumindo muitas linhas numa resposta só",
               "20h40 às 21h15  ·  35 minutos")
notes(s, "20h40 às 21h15 (35 min)", "ESSENCIAL", EU,
      """
Bloco da segunda metade, logo após o intervalo. É onde SQL passa de listar linha para
responder pergunta de negócio de verdade.

ESTRUTURA:
  Por que agregar        5 min
  Funções agregadas       8 min
  GROUP BY               10 min
  HAVING                 10 min
  Transição               2 min
""")

s = sl_bullets("Agregações", "A pergunta muda de forma",
               [("Até aqui, cada linha do resultado é uma transação", "'quais são as compras acima de R$500 em São Paulo'"),
                ("Agora a pergunta muda de forma", "'quanto São Paulo faturou no total' resume tudo num número só"),
                ("Cinco funções resolvem boa parte dos casos", "COUNT, SUM, AVG, MIN e MAX")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Até agora, toda consulta devolveu uma lista de linhas. Cada linha, uma transação.

Mas boa parte das perguntas de negócio quer um número, não uma lista fila por fila.
'Quanto São Paulo faturou no total' resume as transações numa resposta só.

E cinco funções resolvem a maior parte desses casos: COUNT, SUM, AVG, MIN e MAX."
""")

s = sl_query("Agregações", "Uma resposta só, a partir de muitas linhas",
             ["SELECT COUNT(*) AS total_transacoes,", "       SUM(valor) AS valor_total,", "       AVG(valor) AS valor_medio", "FROM transacoes"],
             [("COUNT conta linhas", "aqui, quantas transações existem no total"),
              ("SUM soma um valor numérico", "o total movimentado em todas as transações"),
              ("AVG calcula a média", "MIN e MAX trazem o menor e o maior valor da coluna"),
              ("AS dá um nome ao resultado da coluna", "sem ele, a coluna sai com um nome pouco legível")])
notes(s, "8 min", "ESSENCIAL", EU,
      """
"COUNT conta linhas. SUM soma um valor numérico. AVG calcula a média. E MIN e MAX trazem
o menor e o maior valor de uma coluna, que não estão nesta consulta mas funcionam igual.

Repara no AS: ele dá um nome ao resultado de cada função. Sem isso, a coluna sai do
banco com um nome esquisito, tipo o texto inteiro da função. AS deixa o resultado
legível para quem for ler depois."
""")

s = sl_query("Agregações", "GROUP BY: agrupando antes de agregar",
             ["SELECT id_lojista, COUNT(*) AS total,", "       SUM(valor) AS valor_total", "FROM transacoes", "GROUP BY id_lojista"],
             [("GROUP BY separa as linhas em grupos", "aqui, um grupo para cada lojista"),
              ("A função agregada roda dentro de cada grupo", "COUNT e SUM calculam por lojista, não pela tabela inteira"),
              ("Toda coluna do SELECT precisa estar no GROUP BY, ou dentro de uma função", "senão o banco não sabe qual linha do grupo mostrar")])
notes(s, "10 min", "ESSENCIAL", EU,
      """
"GROUP BY é o que transforma a pergunta de 'no total' para 'por lojista'. Ele separa as
linhas em grupos, um grupo para cada valor de id_lojista.

E aqui está o pulo do gato: a função agregada roda DENTRO de cada grupo. COUNT e SUM não
calculam mais pela tabela inteira, calculam por lojista.

Regra que trava muita gente no início: toda coluna que aparece no SELECT precisa estar
no GROUP BY, ou estar dentro de uma função como COUNT ou SUM. Senão o banco fica sem
saber qual linha específica do grupo deveria mostrar naquela coluna, e dá erro."
""")

s = sl_query("Agregações", "HAVING: filtrando depois de agrupar",
             ["SELECT id_lojista, SUM(valor) AS valor_total", "FROM transacoes", "GROUP BY id_lojista", "HAVING SUM(valor) > 10000"],
             [("WHERE filtra antes de agrupar, HAVING filtra depois", "são dois momentos diferentes da mesma consulta"),
              ("HAVING trabalha com o resultado da agregação", "aqui, só lojistas que somaram mais de R$10.000"),
              ("Usar SUM dentro do WHERE dá erro", "nesse ponto da execução, a soma ainda não existe")])
notes(s, "10 min", "ESSENCIAL", EU,
      """
"Última peça do bloco: HAVING. E aqui a gente volta no slide da ordem real de execução,
lá do primeiro bloco.

WHERE filtra ANTES de agrupar, linha por linha. HAVING filtra DEPOIS de agrupar, grupo
por grupo. São dois momentos diferentes da mesma consulta, e por isso existem os dois.

Aqui, HAVING SUM(valor) maior que 10 mil deixa só os lojistas que somaram mais de dez mil
reais em transações.

E o erro clássico: tentar escrever WHERE SUM(valor) maior que 10 mil. Isso dá erro,
porque na ordem de execução, quando o WHERE roda, a soma ainda nem existe. Ela só existe
depois do GROUP BY. Por isso o SUM precisa estar no HAVING, não no WHERE."
""")

# ==========================================================================
# BLOCO E: Juntando tabelas (21h15 às 21h45)
# ==========================================================================
s = sl_section("05", "Juntando tabelas",
               "JOIN, chave primária e chave estrangeira",
               "21h15 às 21h45  ·  30 minutos")
notes(s, "21h15 às 21h45 (30 min)", "ESSENCIAL", EU,
      """
Bloco mais esperado da noite. É onde as três tabelas do início finalmente se encontram.

ESTRUTURA:
  Por que os dados vivem separados    5 min
  Chave primária e estrangeira        5 min
  JOIN                                8 min
  INNER x LEFT                        8 min
  Interação                           4 min
""")

s = sl_bullets("Juntando tabelas", "Cada tabela guarda um assunto só",
               [("Guardar tudo numa tabela só parece mais simples", "mas repete nome e cidade do cliente em toda transação dele"),
                ("Separar em tabelas evita essa repetição", "o nome do cliente mora uma vez só, na tabela clientes"),
                ("A ligação entre tabelas é feita por uma chave", "um identificador que aparece nas duas tabelas")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Lá no começo eu falei que o dado não estava tudo numa tabela só, e prometi voltar
nisso. Chegou a hora.

Guardar tudo numa tabela só parece mais simples à primeira vista. Mas isso repete o
nome e a cidade do cliente em TODA transação dele. Se o cliente tiver mil compras, o
nome dele aparece escrito mil vezes.

Separar em tabelas evita essa repetição. O nome do cliente mora uma vez só, na tabela
clientes. E a ligação entre as tabelas é feita por uma chave, um identificador que
aparece nas duas."
""")

s = sl_table("Juntando tabelas", "Chave primária e chave estrangeira",
             ["Termo", "O que é", "Exemplo no nosso caso"],
             [["Chave primária", "identifica cada linha de forma única, dentro da própria tabela", "id_cliente, dentro de clientes"],
              ["Chave estrangeira", "aponta para a chave primária de outra tabela", "id_cliente, dentro de transacoes"]],
             subtitle="É esse par que o JOIN usa para juntar as tabelas.",
             widths=[0.24, 0.42, 0.34])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Dois termos que aparecem sempre que se fala de banco relacional.

Chave primária identifica cada linha de forma única, dentro da própria tabela. Em
clientes, é o id_cliente.

Chave estrangeira aponta para a chave primária de outra tabela. Em transações, o
id_cliente que aparece ali não identifica a transação, ele aponta de volta para o
cliente dono dela.

É esse par, chave primária de um lado, chave estrangeira do outro, que o JOIN usa para
juntar as tabelas. Vamos ver isso agora."
""")

s = sl_query("Juntando tabelas", "JOIN: juntando transação com o nome do cliente",
             ["SELECT t.id_transacao, c.nome, t.valor", "FROM transacoes t", "JOIN clientes c", "  ON t.id_cliente = c.id_cliente"],
             [("JOIN junta linhas de duas tabelas", "usando a chave que elas têm em comum"),
              ("ON diz qual coluna de cada lado combina", "aqui, o id_cliente de um lado com o id_cliente do outro"),
              ("t e c são apelidos das tabelas", "encurtam o nome e evitam ambiguidade quando a coluna se repete"),
              ("Sem JOIN, esse cruzamento teria que ser feito manualmente", "fora do banco, numa planilha")])
notes(s, "8 min", "ESSENCIAL", EU,
      """
"JOIN junta linhas de duas tabelas, usando a chave que elas têm em comum.

ON diz exatamente qual coluna de cada lado combina. Aqui, o id_cliente de transações com
o id_cliente de clientes.

Repara nos apelidos, t e c. Eles encurtam o nome da tabela e evitam ambiguidade quando a
mesma coluna existe nas duas tabelas, como id_cliente.

E o motivo de tudo isso existir: sem JOIN, esse cruzamento teria que ser feito
manualmente, fora do banco, numa planilha, linha por linha. Com milhares de transações,
isso não é viável."
""")

s = sl_query("Juntando tabelas", "INNER e LEFT: duas formas de juntar",
             ["SELECT c.nome, t.valor", "FROM clientes c", "LEFT JOIN transacoes t", "  ON c.id_cliente = t.id_cliente"],
             [("INNER JOIN só traz quem existe nas duas tabelas", "cliente sem nenhuma transação some do resultado"),
              ("LEFT JOIN mantém tudo da tabela da esquerda", "clientes sem transação aparecem, com valor vazio"),
              ("A escolha muda a resposta", "'quantos clientes nunca compraram' só aparece com LEFT JOIN")])
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Existe mais de um tipo de JOIN, e a escolha muda o resultado.

INNER JOIN, o que a gente viu no slide anterior, só traz quem existe nas DUAS tabelas.
Cliente sem nenhuma transação simplesmente some do resultado.

LEFT JOIN mantém tudo da tabela da esquerda, mesmo sem correspondência do outro lado.
Aqui, todo cliente aparece, e quem não tem transação vem com valor vazio.

E por que isso importa: a pergunta 'quantos clientes nunca compraram' só é respondível
com LEFT JOIN. Com INNER JOIN, esses clientes já teriam sumido antes de você poder
contar."
""")

s = sl_interaction("Interação", "Qual JOIN resolve isso",
                   "Você quer saber quais lojistas nunca receberam nenhuma transação. Qual caminho resolve isso?",
                   ["A: INNER JOIN partindo de transacoes",
                    "B: LEFT JOIN partindo de lojistas, procurando transacoes",
                    "C: WHERE sozinho, sem nenhum JOIN",
                    "Responda na enquete, 30 segundos"])
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Última pergunta antes do fechamento. Você quer saber quais lojistas nunca receberam
nenhuma transação. Qual caminho resolve isso?"

[aguarde 30 segundos]

Resposta: B. LEFT JOIN partindo de lojistas mantém todo lojista no resultado, e quem não
tem transação correspondente aparece com valor vazio, é só filtrar por isso depois. A
elimina justamente quem você quer encontrar. C não tem como cruzar as duas tabelas sem
JOIN.
""")

# ==========================================================================
# BLOCO F: Da pergunta à query (21h45 às 22h05)
# ==========================================================================
s = sl_section("06", "Da pergunta à query",
               "Fechando o dia e olhando para a quinta",
               "21h45 às 22h05  ·  20 minutos")
notes(s, "21h45 às 22h05 (20 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Recapitulação            5 min
  O que vem pela frente    4 min
  Q&A                      9 min  (elástico, absorve atraso)
  Fechamento               2 min
""")

s = sl_bullets("Encerramento", "Cinco ideias para levar de hoje",
               [("SQL descreve o que você quer, não o passo a passo", "quem decide o caminho é o banco"),
                ("A ordem de execução não é a ordem que você escreve", "FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER BY, LIMIT"),
                ("Agregação muda o formato da resposta", "de uma lista de linhas para um resumo"),
                ("JOIN existe porque os dados vivem separados de propósito", "e o tipo de JOIN muda o resultado"),
                ("Toda consulta boa começa numa pergunta de negócio clara", "não numa tabela aberta sem destino")],
               subtitle="Se você levar só essas cinco frases, a noite cumpriu o objetivo.",
               numbered=True)
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Cinco ideias para levar de hoje.

SQL descreve o que você quer, não o passo a passo de como buscar.

A ordem de execução não é a ordem que você escreve: FROM, WHERE, GROUP BY, HAVING,
SELECT, ORDER BY, LIMIT.

Agregação muda o formato da resposta, de uma lista de linhas para um resumo.

JOIN existe porque os dados vivem separados de propósito, e o tipo de JOIN muda a
resposta.

E a mais importante: toda consulta boa começa numa pergunta de negócio clara, não numa
tabela aberta sem destino."
""")

s = sl_two_col("Próximos encontros", "O que vem pela frente",
               "SEGUNDA · Semana 4",
               ["Análise de dados com Python",
                "Mesma lógica de hoje, agora com pandas",
                "Ainda conceitual, como toda segunda",
                "Ganchos diretos com o que vimos aqui"],
               "QUINTA · Semana 3",
               ["Primeiro contato com SQL de verdade, num banco real",
                "Consultas na prática, com o caso de fraude",
                "Mesmo formato: demonstração e mão na massa",
                "Vale revisar os slides de hoje antes"],
               subtitle="A quinta desta semana é onde SQL sai do slide e vai para a tela de vocês.")
notes(s, "4 min", "ESSENCIAL", EU,
      """
"O que vem pela frente.

Na quinta desta semana, SQL sai do slide e vai para a tela de vocês, num banco real, com
o mesmo caso de fraude que vocês já conhecem. Vale revisar estes slides antes.

E na segunda da semana 4, análise de dados com Python. Mesma lógica de hoje, filtrar,
agrupar, cruzar, agora com pandas. O que vocês aprenderam hoje não fica para trás, ele
volta."
""")

s = sl_statement("Antes de ir", "Perguntas?",
                 "Escreva no chat. O que não der tempo, respondemos no Discord ainda hoje.")
notes(s, "9 min", "ESSENCIAL", EU,
      """
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
""")

s = sl_closing()
notes(s, "2 min", "ESSENCIAL", EU,
      """
FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. SQL parece árido no slide, mas é a ferramenta que mais
volta a aparecer no trabalho de vocês, semana após semana.

Revisem os slides antes da quinta, principalmente a ordem real de execução. Nos vemos
lá, com um banco de verdade na tela. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Confirmar com quem conduz a quinta que o caso de fraude e as três tabelas de hoje são
  exatamente o que vai aparecer no banco real da prática.
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

out = ROOT / "docs" / "aula-05"
out.mkdir(parents=True, exist_ok=True)
dest = out / "AI-Talent-Academy-Aula05.pptx"
prs.save(dest)
print(f"OK: {dest}  ({len(prs.slides._sldIdLst)} slides)  "
      f"Roboto, sem travessões, tamanho único por bloco.")
