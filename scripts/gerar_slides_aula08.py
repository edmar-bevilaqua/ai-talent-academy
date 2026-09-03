# -*- coding: utf-8 -*-
"""
Gerador do deck da Aula 8 (Semana 4, quinta-feira) do AI Talent Academy.

Tema: laboratorio pratico de NumPy, pandas, Matplotlib e Seaborn. Aula quase
inteiramente pratica, por pedido explicito do usuario: poucos slides, a maior parte da
noite e a turma resolvendo as 20 perguntas de `docs/aula-08/avaliacao_aluno.ipynb`
contra a base de 1 milhao de transacoes, com resposta colada num Google Forms. Os
slides desta aula NAO revelam a fraude plantada nos dados (ver
`docs/aula-08/dados/historia_anomalia.md`): a investigacao e o exercicio.

Identidade visual: padrao White Cube (Roboto, azul 28347B, fundos e logo do template
oficial em assets/whitecube/).

Uso:  python scripts/gerar_slides_aula08.py
Saida: docs/aula-08/AI-Talent-Academy-Aula08.pptx

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

"Boa noite! Hoje é dia de colocar a mão na massa de verdade: pandas, NumPy, Matplotlib
e Seaborn, todos juntos, num banco de um milhão de linhas. Enquanto todo mundo entra,
escreve no chat: você já rodou algum notebook Python antes de hoje?"

Não comece antes de 19h08.
""",
      """
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- CRÍTICO HOJE: confirme que o link do notebook e do Google Forms estão fixados no
  Discord ANTES de 19h00.
- Leia docs/aula-08/dados/historia_anomalia.md antes da aula. É o gabarito da
  investigação, e não pode aparecer em slide nem em chat.
""")

s = sl_bullets("Enquanto todo mundo entra", "Hoje o pandas sai do slide e vai pra tela de vocês",
               [("Áudio e câmera", "microfone no mudo, câmera fica a seu critério"),
                ("Dúvidas", "escreva no chat a qualquer momento, temos moderação acompanhando"),
                ("Gravação", "a aula é gravada e o link chega em até 24h"),
                ("Hoje é quase inteiramente prática", "poucos slides, muito mais tempo de vocês escrevendo código"),
                ("Aqueça o teclado", "escreva no chat: você já rodou algum notebook Python antes de hoje?")],
               subtitle="Aula 8 · Semana 4 · começamos 19h10")
notes(s, "19h00 às 19h10", "ESSENCIAL", EU,
      """
Leia os itens uma vez, por volta de 19h05. Insista no quarto item: quem espera uma
aula parecida com a segunda vai se surpreender, e é bom avisar logo de cara.
""")

# ==========================================================================
# BLOCO A: Hoje é dia de investigar (19h10 às 19h30)
# ==========================================================================
s = sl_section("01", "Hoje é dia de investigar",
               "Como vai funcionar a prática de hoje",
               "19h10 às 19h30  ·  20 minutos")
notes(s, "19h10 às 19h30 (20 min)", "ESSENCIAL", EU,
      """
Bloco curto de propósito. O objetivo é explicar a mecânica e dar o gancho de
investigação, sem ensinar nada novo, para a turma sair direto para a prática com
clareza.

ESTRUTURA:
  Onde estamos              3 min
  O que muda hoje            4 min
  Como vai funcionar           5 min
  O convite                     4 min
  Regras de hoje                4 min
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
             subtitle="Semana 4 de 8. A segunda ensinou a ferramenta, hoje é a prática de verdade.",
             widths=[0.12, 0.38, 0.50])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Onde vocês estão. Segunda-feira foi a teoria inteira de Python: história da linguagem,
NumPy, pandas em profundidade, Matplotlib e Seaborn. Hoje é a prática de tudo isso,
numa base de dados muito maior do que qualquer exemplo de slide."
""")

s = sl_bullets("O que muda hoje", "Menos slide, mais tela de vocês",
               [("As últimas aulas foram teoria", "SQL na segunda da semana 3, Python e pandas na segunda desta semana"),
                ("Hoje é o oposto", "quase a noite inteira é vocês escrevendo e rodando código, a gente só acompanha"),
                ("O material da Aula 7 continua valendo", "o notebook de demonstração com as quatro bibliotecas é referência válida hoje"),
                ("Hoje o dado é grande de verdade", "um milhão de transações, não mais os exemplos pequenos dos slides")])
notes(s, "4 min", "ESSENCIAL", EU,
      """
"O que muda hoje. As últimas aulas foram teoria: SQL na segunda da semana 3, Python e
pandas em profundidade na segunda desta semana. Hoje é o oposto: quase a noite inteira
é vocês escrevendo e rodando código, a gente só acompanha.

O notebook de demonstração da Aula 7, com exemplo de NumPy, pandas, Matplotlib e
Seaborn, continua valendo como referência. Deixem ele aberto numa aba.

E uma mudança de escala: hoje o dado é grande de verdade, um milhão de transações, bem
diferente dos exemplos pequenos que couberam num slide."
""")

s = sl_cards("Como vai funcionar", "Quatro passos, do início ao fim",
             [("Abra o notebook",
               "Um notebook com 20 perguntas espera vocês no Colab, cada uma com uma célula vazia para a resposta."),
              ("Carregue os dados",
               "As mesmas 6 tabelas de sempre, agora com 1 milhão de transações."),
              ("Responda, uma de cada vez",
               "Rode a célula, confira o resultado, escreva a resposta."),
              ("Cole no formulário",
               "Cada resposta vai para o Google Forms indicado no chat.")],
             subtitle="75 minutos de prática, no ritmo de cada um.",
             cols=4, card_h=3.3)
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Como vai funcionar, em quatro passos. Primeiro, abram o notebook que está fixado no
Discord: 20 perguntas, cada uma com uma célula de código vazia logo abaixo.

Segundo, a primeira parte do notebook carrega as mesmas 6 tabelas de sempre, agora com
1 milhão de transações.

Terceiro, respondam uma pergunta de cada vez: rodem a célula, confiram o resultado, e
só depois escrevam a resposta.

Quarto, colem a resposta no Google Forms, também fixado no Discord. É por ali que a
gente confere o desempenho de cada um."
""",
      "AÇÃO DO MODERADOR: fixar o link do notebook E o link do Forms no topo do chat exatamente neste slide.")

s = sl_statement("O convite",
                 "Hoje vocês são analistas de dados.\nAlgo estranho está escondido nesses dados.",
                 "Não vamos contar o que é. É isso que a análise serve para descobrir.")
notes(s, "4 min", "ESSENCIAL", EU,
      """
"E aqui vai o convite de hoje. Essa base de 1 milhão de transações não é só grande por
ser grande. Tem alguma coisa estranha escondida nela, um padrão fora do comum, do
tamanho de um caso real de investigação.

Eu não vou contar o que é. É exatamente para isso que a análise exploratória serve:
começar largo, estranhar um número, e ir cavando até achar a explicação. Várias das 20
perguntas de hoje vão, sem avisar, ir te aproximando dessa resposta.

Quem achar algo estranho no meio do caminho, guarda a ideia. A gente conversa sobre
isso perto do fechamento."
""",
      "NÃO REVELE a resposta em nenhuma hipótese antes do fechamento. Consulte historia_anomalia.md com antecedência, é o gabarito da investigação.")

s = sl_bullets("Regras de hoje", "Antes de começar",
               [("75 minutos de prática, sem pressa", "não precisa terminar as 20 perguntas para a noite valer a pena"),
                ("Travou em alguma pergunta?", "escreva no chat com o número da pergunta, a gente ou um mentor chega até você"),
                ("O notebook da Aula 7 é cola liberada", "quase toda pergunta de hoje usa alguma técnica que já apareceu lá"),
                ("Terminou antes da hora?", "volte nas perguntas mais difíceis e tente explicar o resultado com palavras, não só rodar o código")])
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Últimas regras antes de soltar vocês.

75 minutos, sem pressa. Não precisa terminar as 20 perguntas para a noite valer a pena.

Travou em alguma pergunta? Escreve no chat com o número dela, a gente ou algum mentor
chega até você.

O notebook da Aula 7 é cola liberada, de propósito. Quase toda pergunta de hoje usa
alguma técnica que já apareceu lá.

E se terminar antes da hora, volte nas perguntas mais difíceis e tente explicar o
resultado com palavras, não só rodar o código. Isso conta tanto quanto a resposta
certa."
""")

# ==========================================================================
# BLOCO B: Mão na massa (19h30 às 20h45)
# ==========================================================================
s = sl_section("02", "Agora é com vocês",
               "75 minutos, no seu ritmo",
               "19h30 às 20h45  ·  75 minutos")
notes(s, "19h30 às 20h45 (75 min)", "ESSENCIAL", "os dois",
      """
Bloco principal da noite, sem slide de conteúdo novo. Este slide fica projetado na
sala principal durante toda a atividade.

CHECKLIST DA DUPLA DURANTE OS 75 MINUTOS:

Minuto 0 a 10:   conferir no chat quem já abriu o notebook e carregou os dados.
Minuto 10 a 55:  responder o chat em tempo real. Priorizar quem trava nas primeiras
                 perguntas, porque quem trava cedo tende a desistir.
Minuto 55 a 70:  mandar aviso geral, "faltam alguns minutos, aproveitem para revisar
                 as perguntas que pularam".
Minuto 70 a 75:  aviso de 5 minutos e reforçar que dá para continuar em casa depois.

SE ALGUÉM TRAVAR CARREGANDO 1 MILHÃO DE LINHAS:
Confirme se está rodando no Colab mesmo (não numa cópia local), e se o Drive terminou
de montar antes de rodar a célula de leitura. O arquivo é grande, o carregamento pode
levar alguns segundos a mais que o normal, isso é esperado.

SE ALGUÉM PERGUNTAR SE A RESPOSTA ESTÁ CERTA:
Não confirme nem negue. Peça para a pessoa explicar como chegou lá. Confirmar cedo
demais tira a graça de quem ainda está investigando.
""")

s = sl_statement("Mão na massa", "75 minutos.\nVocês voltam para cá às 20h45.",
                 "Travou? Escreva no chat principal com o número da pergunta. A gente entra no seu Colab.")
notes(s, "0 min", "ESSENCIAL", "os dois",
      """
Slide de apoio visual, fica projetado. Sem fala nova aqui, o que precisa ser dito já
foi dito no bloco anterior.
""")

# ==========================================================================
# BLOCO C: Encerramento (20h45 às 21h00)
# ==========================================================================
s = sl_section("03", "Encerramento",
               "O que vocês levam de hoje e o que vem na semana 5",
               "20h45 às 21h00  ·  15 minutos")
notes(s, "20h45 às 21h00 (15 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  A revelação                4 min
  Recapitulação                3 min
  O que vem pela frente          3 min
  Q&A                              3 min
  Fechamento                        2 min

A revelação acontece em voz alta, puxando o fio a partir do chat: pergunte quem
estranhou algum número, deixe 2 ou 3 pessoas contarem o que acharam, e só então
confirme o padrão, seguindo docs/aula-08/dados/historia_anomalia.md. Não tem slide
para isso de propósito, é melhor ao vivo, olhando a reação da turma.
""")

s = sl_bullets("Encerramento", "Cinco ideias para levar de hoje",
               [("Análise exploratória começa largo, antes de focar", "vocês só chegaram no padrão porque olharam o todo primeiro"),
                ("Um número fora da curva abre uma pergunta", "a resposta só vem depois de investigar"),
                ("pandas, NumPy, Matplotlib e Seaborn se completam numa investigação real", "cada um entrou numa etapa diferente hoje"),
                ("Nem toda pergunta de negócio tem resposta fácil, e tudo bem", "isso também é parte do trabalho"),
                ("O que vocês fizeram hoje foi trabalho de verdade de quem analisa dado", "o mesmo raciocínio de um caso real, aplicado num exercício de aula")],
               subtitle="Se você levar só essas cinco frases, a noite cumpriu o objetivo.",
               numbered=True)
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Cinco ideias para levar de hoje.

Análise exploratória começa largo, antes de focar. Vocês só chegaram onde chegaram
porque olharam o todo primeiro.

Um número fora da curva abre uma pergunta. A resposta só vem depois de investigar.

pandas, NumPy, Matplotlib e Seaborn se completam numa investigação real, cada um
entrou numa etapa diferente hoje.

Nem toda pergunta de negócio tem resposta fácil, e tudo bem, isso também é parte do
trabalho.

E a mais importante: o que vocês fizeram hoje foi trabalho de verdade de quem analisa
dado, o mesmo raciocínio de um caso real, aplicado dentro de um exercício de aula."
""")

s = sl_two_col("Próximos encontros", "O que vem pela frente",
               "SEGUNDA · Semana 5",
               ["Engenharia de Dados",
                "Como construir os pipelines",
                "Ainda conceitual, como toda segunda",
                "Dado limpo, no lugar certo"],
               "QUINTA · Semana 5",
               ["Primeiro contato com pipeline de verdade",
                "Mesmo formato de hoje: demonstração curta e mão na massa",
                "Vale revisar os slides da Aula 7 antes"],
               subtitle="A partir da semana 5, o dado deixa de vir pronto num CSV.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"O que vem pela frente.

Segunda que vem, semana 5: engenharia de dados. Como construir os pipelines que
entregam dado limpo, no lugar certo. Ainda conceitual, como toda segunda.

E na quinta da semana 5, primeiro contato de verdade com pipeline, no mesmo formato de
hoje: demonstração curta, e o resto é prática."
""")

s = sl_statement("Antes de ir", "Perguntas?",
                 "Escreva no chat. O que não der tempo, respondemos no Discord ainda hoje.")
notes(s, "3 min", "ESSENCIAL", f"{EU} + {FELIPE}",
      """
PERGUNTAS PREVISÍVEIS DE HOJE:

- "Não terminei as 20 perguntas, isso é um problema?"
  Não. O que importa é o esforço registrado no Forms até aqui. Dá para continuar em
  casa, o notebook e o Forms continuam abertos.

- "Como vocês descobriram esse padrão para colocar na aula?"
  Ele foi construído de propósito no gerador dos dados, para dar um objetivo real à
  análise. Mas o jeito de achar é o mesmo de um caso real.

- "Isso cai no projeto final?"
  Não direto, mas a mesma lógica de investigação serve para qualquer base que o grupo
  escolher no projeto.

- "Perdi a Aula 7, consigo acompanhar hoje?"
  Fica mais difícil. Recomendamos revisar o roteiro e o notebook da Aula 7 antes de
  continuar as perguntas de casa.
""")

s = sl_closing()
notes(s, "2 min", "ESSENCIAL", EU,
      """
FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. Vocês passaram por um caso pequeno, mas real, de como
uma investigação de dados de verdade acontece: começa largo, estranha um número, vai
fundo até achar a explicação.

O notebook e o Forms continuam abertos, terminem em casa se não deu tempo. Nos vemos
na segunda. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Exportar as respostas do Google Forms para uma planilha, e conferir contra
  gabarito_respostas em docs/aula-08 antes da próxima mentoria.
- Registrar quantas pessoas chegaram até a camada 3 da investigação sem ajuda, é um
  bom termômetro de quão bem a aula de segunda realmente fixou.
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

out = ROOT / "docs" / "aula-08"
out.mkdir(parents=True, exist_ok=True)
dest = out / "AI-Talent-Academy-Aula08.pptx"
prs.save(dest)
print(f"OK: {dest}  ({len(prs.slides._sldIdLst)} slides)  "
      f"Roboto, sem travessões, tamanho único por bloco.")
