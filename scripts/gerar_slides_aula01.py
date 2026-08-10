# -*- coding: utf-8 -*-
"""
Gerador do deck da Aula 1 (Semana 1, segunda-feira) do AI Talent Academy.

Identidade visual: padrao White Cube (Roboto, azul 28347B, fundos e logo do template
oficial em assets/whitecube/).

Uso:  python scripts/gerar_slides_aula01.py
Saida: docs/aula-01/AI-Talent-Academy-Aula01.pptx

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
S_KICKER = 20
S_TITLE = 40
S_SUB = 17
S_BULLET = 21
S_CARD_T = 20
S_CARD_B = 15.5
S_TABLE_H = 16
S_TABLE_C = 15
S_BIG = 36
S_SRC = 18
MAX_LINHA_BIG = 62   # caracteres por linha em S_BIG antes de quebrar sozinho
S_FOOT = 13

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
    _n["i"] += 1
    c = NAVY_TXT_SOFT if dark else MUTED
    block(slide, ML, FOOT_Y, Inches(6), Inches(0.4), "whitecube.com.br", S_FOOT, c, space=0)
    block(slide, SW - ML - Inches(1.5), FOOT_Y, Inches(1.5), Inches(0.4), str(_n["i"]),
          S_FOOT, c, align=PP_ALIGN.RIGHT, space=0)


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
          "Semana 1  ·  Panorama de Dados, IA e resolução de problemas", 25, INK, space=0)
    shape(s, ML, Inches(5.75), Inches(2.4), Pt(5), fill=RED)
    block(s, ML, Inches(8.15), Inches(13), Inches(1.0),
          ["Aula 1  ·  Segunda-feira, 19h00 às 22h00  ·  Online",
           "White Cube  ·  Bevilaqua Data Labs  ·  BPTECH"], 16, INK, space=5)
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
              texto.split("\n"), 16, INK, align=PP_ALIGN.CENTER, space=2, line=1.22)
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
              d, 14, INK, space=0, line=1.22)
        if c < per_row - 1 and i < len(steps) - 1:
            shape(s, x + cw + Inches(0.1), yy + int(ch / 2) - Inches(0.17), Inches(0.42),
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
              15, INK, space=0, line=1.16)
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


# ==========================================================================
# CONTEÚDO
# ==========================================================================
EU = "Edmar"
FELIPE = "Felipe André Bach Alves"

# --------------------------------------------------------------------------
# PRÉ-AULA
# --------------------------------------------------------------------------
s = sl_cover()
notes(s, "19h00 às 19h10 (slide de espera)", "ESSENCIAL", EU,
      """
Este slide fica projetado desde 18h55. Compartilhe a tela ANTES de abrir a sala.

Enquanto as pessoas entram, fale a cada 2 ou 3 minutos (não deixe silêncio total):
"Boa noite, pessoal! Estamos abrindo a sala. Enquanto todo mundo entra, aproveita
para deixar no chat seu nome e de qual cidade você está falando com a gente."

Com 190 pessoas, a entrada leva tempo. Não comece antes de 19h08.
""",
      """
- Microfones de todos em MUDO (configure na sala antes de abrir).
- Câmeras: desligadas por padrão. Só os apresentadores com câmera.
- Confirme que a GRAVAÇÃO está ligada antes de 19h10.
- Moderador: fixe no chat o link do Discord e o link da enquete.
""")

s = sl_bullets("Enquanto todo mundo entra", "Bem-vindo(a) ao AI Talent Academy",
               [("Áudio e câmera", "deixe o microfone mudo; câmera é opcional"),
                ("Dúvidas", "escreva no chat a qualquer momento, temos um moderador acompanhando"),
                ("Gravação", "a aula é gravada e o link chega para você em até 24h"),
                ("Material", "os slides são enviados por e-mail depois de cada encontro"),
                ("Comunidade", "entre no Discord do programa, o link está fixado no chat"),
                ("Comece agora", "escreva no chat: seu nome + sua cidade")],
               subtitle="Aula 1 · Semana 1 · começamos 19h10")
notes(s, "19h00 às 19h10", "ESSENCIAL", EU,
      """
Fica em loop com o slide de capa. Leia os itens em voz alta uma vez, por volta de 19h05,
e repita o convite do chat. Objetivo: quebrar a sensação de "sala vazia" e já criar o
primeiro micro-compromisso (escrever no chat).
""",
      "Se o chat estourar, o moderador não precisa responder um a um, basta reagir a alguns nomes.")

# --------------------------------------------------------------------------
# BLOCO 0: diretoria
# --------------------------------------------------------------------------
s = sl_section("", "Quem é a White Cube?", "Contexto, números e para onde estamos indo",
               "19h10 às 19h30  ·  20 minutos")
notes(s, "19h10 às 19h30 (20 min)", "ESSENCIAL, não é seu bloco", "Ale e Márcio (diretoria)",
      """
ABERTURA (você, 60 segundos, antes de passar a palavra):

"Boa noite, pessoal! Sejam muito bem-vindos à primeira aula do AI Talent Academy.
Meu nome é Edmar, eu sou Cientista de Dados Sênior, e junto comigo está o Felipe.
Nós dois vamos conduzir vocês pelas próximas 8 semanas.

Antes de a gente entrar no conteúdo, quem abre a noite são o Ale e o Márcio, que vão
contar quem é a White Cube, os números da empresa e para onde a gente está indo.
Ale, Márcio, o palco é de vocês."

DEPOIS, quando eles terminarem, faça a ponte (30 segundos):
"Obrigado, Ale e Márcio. Guardem essa visão que eles trouxeram, porque tudo que a
gente vai fazer nas próximas 8 semanas é exatamente sobre isso: transformar dados
e IA em decisão de negócio."
""",
      """
PLANO B DE TEMPO: se a diretoria estourar para 30 ou 45 min, corte na seguinte ordem:
1º) slide de mitos sobre entrar na área
2º) slide "hype x realidade"
3º) interação #2 (papel preferido)
4º) metodologia / 4 pilares
Ver o mapa completo em docs/aula-01/01-plano-da-aula.md
""")

# ==========================================================================
# BLOCO A: Cronograma e metodologia (19h30 às 19h45)
# ==========================================================================
s = sl_section("01", "Cronograma e metodologia",
               "Como funcionam as 8 semanas e o que esperamos de você",
               "19h30 às 19h45  ·  15 minutos")
notes(s, "19h30 às 19h45 (15 min)", "ESSENCIAL", EU,
      """
Bloco de contrato. O objetivo aqui NÃO é ensinar nada, é dar segurança.
Público de 190 pessoas leigas precisa sair deste bloco sabendo:
(a) que não vão ser jogadas num conteúdo impossível,
(b) que existe um caminho claro,
(c) o que precisam fazer para continuar.

Ritmo: rápido. 15 minutos, 8 slides. Não se apaixone por nenhum slide aqui.
""")

s = sl_cards("Quem conduz", "Vocês não estão sozinhos nessa jornada",
             [("Edmar Bevilaqua",
               "Cientista de Dados Sênior\n\n[1 linha sobre o que você faz no dia a dia]"),
              ("Felipe André Bach Alves",
               "Cientista de Dados Sênior Análogo a Marte\n\nFotógrafo profissional")],
             subtitle="Duas pessoas conduzindo, um programa desenhado para quem está começando.",
             cols=2, card_h=2.5)
notes(s, "1 min", "ESSENCIAL", EU,
      """
Apresentação curta e HUMANA, não currículo. Máximo 30 segundos por pessoa.

"Eu sou o Edmar, sou Cientista de Dados Sênior e no dia a dia eu faço [X]. E o que me
trouxe para cá é simples: eu já estive exatamente onde vocês estão hoje."

Passe a palavra para o Felipe se apresentar, ou apresente-o você mesmo.

Feche olhando para a sala:
"E vocês são 190 pessoas de formações completamente diferentes. Tem gente de
engenharia, de administração, de biologia, de direito. Isso não é um problema,
isso é de propósito."
""",
      "PREENCHER a linha [1 linha sobre o que você faz no dia a dia] antes da aula.")

s = sl_statement("A promessa deste programa",
                 "Em 8 semanas você vai sair sabendo o que é possível fazer\ncom dados e IA, como se constrói uma solução de verdade\ne onde você se encaixa nisso.",
                 "E não: você não precisa saber programar hoje para acompanhar.")
notes(s, "1 min", "ESSENCIAL", EU,
      """
Este é o slide mais importante do bloco. Diga devagar.

"Eu quero ser muito honesto sobre o que este programa é e o que ele não é.
Ele NÃO vai transformar vocês em cientistas de dados em 8 semanas. Ninguém consegue
isso, e quem promete está mentindo.
O que ele VAI fazer é te dar três coisas: entender o que é possível fazer com dados e
IA hoje; entender COMO uma solução dessas nasce, do problema até o resultado; e
descobrir onde, dentro desse mundo, você se encaixa.

E aquela linha de baixo é a mais importante da noite: você NÃO precisa saber programar
hoje para acompanhar este curso."
""",
      "Pausa de 2 segundos depois da última frase. É o momento de aliviar a ansiedade da sala.")

s = sl_table("A jornada", "8 semanas, 2 etapas",
             ["", "Semanas", "O quê", "Foco"],
             [["Etapa 1", "1 a 4", "Fundamentos, nivelamento e panorama",
               "Todo mundo junto. Base comum."],
              ["", "Semana 4", "Mini-Desafio Data & AI", "Sua primeira entrega avaliada"],
              ["Etapa 2", "5 a 8", "Imersão prática em projeto real",
               "Grupo restrito. Mão na massa."],
              ["", "Semana 8", "Demo Day", "Apresentação final do projeto"]],
             subtitle="80 horas no total  ·  40h de encontros ao vivo + 40h de acompanhamento e avaliação",
             widths=[0.13, 0.13, 0.37, 0.37])
notes(s, "2 min", "ESSENCIAL", EU,
      """
"O programa tem duas etapas bem diferentes.

A Etapa 1, que é onde a gente está agora, vai da semana 1 até a 4. É aberta, é para
todo mundo, e o objetivo é nivelar: colocar todo mundo falando a mesma língua sobre
dados e IA. No fim da semana 4 tem o Mini-Desafio Data & AI, que é a primeira entrega
avaliada de vocês.

A Etapa 2, das semanas 5 a 8, é uma imersão prática. Aí muda o jogo: vocês vão
trabalhar num projeto de verdade, em grupo, com mentoria, e apresentar num Demo Day
no final."

NÃO diga quantas pessoas seguem para a Etapa 2. Se perguntarem no chat, responda:
"Isso vai depender do desempenho da turma. O nosso interesse é levar o maior número
possível de pessoas que estiverem realmente engajadas."
""",
      "PROIBIDO nesta aula: mencionar número de vagas de trainee. Combine isso com o moderador.")

s = sl_two_col("O ritmo da semana", "Duas aulas por semana, papéis diferentes",
               "SEGUNDA · 19h às 22h  (3h)",
               ["Aula principal, conceitual",
                "Panorama, fundamentos e frameworks",
                "Exemplos e estudos de caso",
                "É aqui que você entende o \"o quê\" e o \"por quê\"",
                "Formato: apresentação + perguntas no chat"],
               "QUINTA · 19h às 21h  (2h)",
               ["Laboratório e mão na massa",
                "Ferramentas de verdade (Google Colab)",
                "Mentoria, dúvidas e checkpoints",
                "É aqui que você entende o \"como\"",
                "Formato: prática guiada + orientação da entrega"],
               subtitle="5 horas ao vivo por semana. Reserve as duas noites na sua agenda hoje.")
notes(s, "2 min", "ESSENCIAL", EU,
      """
"Todas as semanas têm dois encontros, e eles são bem diferentes um do outro.

Segunda-feira, das 19h às 22h, é a aula principal. É mais conceitual: é onde a gente
constrói o repertório, mostra exemplos, discute casos. É onde você entende O QUÊ e
POR QUÊ.

Quinta-feira, das 19h às 21h, é o laboratório. Aí a gente coloca a mão na massa,
abre ferramenta, resolve problema junto e tira dúvida. É onde você entende COMO.

E eu vou pedir uma coisa muito prática agora: abram a agenda de vocês e bloqueiem
essas duas noites, pelas próximas 8 semanas. Quem só assiste a gravação não acompanha
o mesmo ritmo de quem está aqui ao vivo."

Sobre o Colab (só 1 frase): "Na quinta a gente vai usar o Google Colab, que é uma
ferramenta gratuita, roda no navegador, não precisa instalar nada. Basta ter uma
conta Google."
""")

s = sl_cards("Metodologia", "Como a gente ensina",
             [("1 · Teoria aplicada",
               "Conceito sempre amarrado a um problema real.\n\n~25% do tempo"),
              ("2 · Demonstração",
               "A gente resolve na frente de vocês, explicando cada decisão.\n\n~25% do tempo"),
              ("3 · Mão na massa",
               "Você faz. Errar aqui é parte do método, é assim que se aprende.\n\n~30% do tempo"),
              ("4 · Mentoria e feedback",
               "Você entrega, a gente devolve com orientação concreta.\n\n~20% do tempo")],
             subtitle="Você vai passar mais tempo fazendo do que assistindo.", cols=4,
             card_h=3.2)
notes(s, "1 min", "DESCARTÁVEL (cortar se atrasado)", EU,
      """
Rápido. Leia os quatro títulos e pare no terceiro:

"Repara na distribuição: mais da metade do tempo do programa é você FAZENDO alguma
coisa, não assistindo a gente falar. E eu quero deixar isso muito claro desde hoje:
errar aqui não é problema, é o método. Ninguém aprende a nadar assistindo vídeo."
""")

s = sl_bullets("Avaliação", "Você é avaliado o tempo todo, e isso é bom",
               [("Não existe uma prova final", "a avaliação é contínua, ao longo das 8 semanas"),
                ("O que a gente olha", "como você pensa, como aprende, como prioriza e como comunica"),
                ("Entregas práticas", "cada semana tem um pequeno entregável, nada gigante"),
                ("Mini-Desafio da Semana 4", "sua primeira entrega avaliada, com trilha à sua escolha"),
                ("Trilhas por perfil", "Analytics · Programação · Machine Learning · GenAI"),
                ("Presença e participação contam", "estar aqui, perguntar e entregar já é meio caminho"),
                ("Solução perfeita não é o objetivo", "raciocínio claro vale mais do que código bonito")],
               subtitle="Um recado: quem não programa hoje também consegue se destacar aqui.")
notes(s, "2 min", "ESSENCIAL", EU,
      """
Este bloco resolve a maior ansiedade da sala. Vá com calma.

"Todo mundo quer saber como vai ser avaliado, então vamos falar disso agora.

Primeira coisa: não existe uma prova final. A avaliação é contínua. A gente vai
acompanhando o que vocês entregam ao longo das semanas.

Segunda coisa, e essa é a mais importante: o que a gente avalia não é se você acertou
a resposta. É COMO você pensa. Como você estrutura o problema, como você aprende com
o feedback, como você prioriza quando o tempo é curto e como você comunica o que fez.

Na semana 4 tem o Mini-Desafio, que é a primeira entrega avaliada. E aí vem uma coisa
que eu acho muito importante: ele tem TRILHAS. Você escolhe entregar como Analytics,
como Programação, como Machine Learning ou como GenAI, o que combina mais com você.
Quem nunca programou pode entregar uma análise e uma recomendação de negócio bem
feitas e se destacar do mesmo jeito.

A gente não está procurando o mais técnico. A gente está procurando quem pensa bem,
aprende rápido, entrega e comunica."
""",
      "Se alguém perguntar sobre nota de corte: \"Os critérios detalhados a gente apresenta na semana 3.\"")

s = sl_cards("Combinados", "Como a gente vai se falar",
             [("Discord do programa",
               "É o nosso canal oficial. Avisos, materiais, dúvidas entre as aulas e conversa com a turma.\n\nLink no chat."),
              ("As aulas são gravadas",
               "Você recebe o link em até 24h. Mas gravação é rede de segurança, não substituto do ao vivo."),
              ("Slides e materiais",
               "Enviados por e-mail e postados no Discord depois de cada encontro."),
              ("Chat sempre aberto",
               "Pergunte durante a aula. Temos moderação acompanhando e a gente responde ao longo do caminho."),
              ("Google Colab",
               "Ferramenta das aulas práticas. Gratuita, roda no navegador. Só precisa de conta Google.")],
             cols=3)
notes(s, "2 min", "ESSENCIAL", EU,
      """
Passe rápido pelos cinco, mas insista no Discord:

"O Discord é o coração do programa fora da aula. É lá que a gente posta material,
tira dúvida no meio da semana e onde vocês vão se conhecer. Eu vou pedir para o
moderador jogar o link no chat AGORA. Entra hoje, ainda esta noite."
""",
      "AÇÃO DO MODERADOR: postar o convite do Discord no chat exatamente neste slide.")

# ==========================================================================
# BLOCO B: Introdução ao universo de Dados e IA (19h45 às 20h30)
# ==========================================================================
s = sl_section("02", "Introdução ao universo de\nDados e Inteligência Artificial",
               "O que é IA de verdade, por que agora, e quem trabalha com isso",
               "19h45 às 20h30  ·  45 minutos")
notes(s, "19h45 às 20h30 (45 min)", "ESSENCIAL", EU,
      """
Bloco central da sua parte. Estrutura em 4 movimentos:
  1) Por que agora (contexto e hype)          ~10 min
  2) O mapa das siglas e como isso funciona   ~15 min
  3) O que a IA NÃO faz                       ~8 min
  4) Carreiras e papéis                       ~12 min

Controle de tempo: às 20h05 você PRECISA estar entrando em "O que a IA não faz".
Se estiver atrasado, corte "hype x realidade" e "mitos sobre entrar na área".
""")

s = sl_statement("Vamos começar por uma pergunta",
                 "Quantas vezes você usou inteligência artificial hoje,\nsem perceber que estava usando?")
notes(s, "1 min", "ESSENCIAL", EU,
      """
Faça a pergunta e ESPERE. Não responda por eles.

"Quantas vezes você usou inteligência artificial hoje? Não estou falando de ChatGPT.
Estou falando de hoje, no seu dia normal. Joga no chat um número."

[espere 15 a 20 segundos, leia 2 ou 3 números do chat em voz alta]

"A resposta real, para quase todo mundo aqui, é: dezenas de vezes."
""")

s = sl_cards("IA que você já usa", "Você conviveu com IA hoje pelo menos 8 vezes",
             [("O caminho no Waze / Google Maps",
               "Previsão de trânsito e do melhor trajeto usando dados de milhões de celulares em tempo real."),
              ("O feed do Instagram / TikTok",
               "Um modelo de recomendação decide, a cada rolagem, o que prende sua atenção."),
              ("O e-mail que caiu no spam",
               "Um classificador. Uma das aplicações mais antigas e bem-sucedidas de ML."),
              ("A compra bloqueada pelo banco",
               "Detecção de fraude em tempo real: o modelo achou seu comportamento atípico."),
              ("O corretor do teclado",
               "Modelo de linguagem prevendo a próxima palavra. É o primo simples do ChatGPT."),
              ("O que a Netflix recomenda",
               "Sistema de recomendação. A Netflix pagou US$ 1 milhão em 2009 para melhorá-lo.")],
             subtitle="Nenhum desses foi chamado de \"IA\" na propaganda. Todos são.", cols=3)
notes(s, "3 min", "ESSENCIAL", EU,
      """
Passe pelos seis exemplos rápido, com energia. É o slide que "abre a cabeça" da sala.

"Vamos por partes. Você acordou e olhou o trânsito no Waze: isso é IA, é um modelo
prevendo tempo de trajeto com dados de milhões de celulares em tempo real.

Rolou o feed do Instagram: cada vídeo que apareceu foi escolhido por um modelo de
recomendação que aprendeu o que segura sua atenção.

Abriu o e-mail e não viu spam: tem um classificador filtrando. Aliás, esse é um dos
casos de sucesso mais antigos de machine learning, dos anos 90.

Se algum de vocês já teve uma compra bloqueada pelo banco: foi um modelo de detecção
de fraude que achou seu comportamento estranho.

E o corretor do teclado do celular? Ele prevê a próxima palavra que você vai digitar.
Guarda essa, porque daqui a pouco eu vou mostrar que o ChatGPT é, no fundo, uma versão
muito, muito mais poderosa disso.

Ponto importante: nenhum desses produtos foi vendido para você como "inteligência
artificial". Todos são."
""",
      "Fato verificável: Netflix Prize, US$ 1 milhão, concluído em 2009.")

s = sl_nested("O mapa das siglas", "IA, ML, Deep Learning, GenAI: o que é o quê",
              "Toda GenAI é IA. Nem toda IA é GenAI. Essa distinção resolve 80% da confusão do mercado.")
notes(s, "4 min", "ESSENCIAL, slide-chave da aula", EU,
      """
ESTE É O SLIDE MAIS IMPORTANTE DO SEU BLOCO. Vá devagar, use as mãos, desenhe no ar.

"Vamos organizar as siglas, porque isso é o que mais confunde quem está chegando.

Pensa em bonecas russas, uma dentro da outra.

A caixa maior é INTELIGÊNCIA ARTIFICIAL. É o guarda-chuva: qualquer sistema que faz
uma tarefa que a gente associa à inteligência humana. Um sistema de regras "se o cliente
tem mais de 3 atrasos, marque como risco" já é IA num sentido amplo.

Dentro dela tem MACHINE LEARNING. E aqui muda uma coisa fundamental: em vez de alguém
escrever a regra, o sistema DESCOBRE a regra sozinho, olhando exemplos. Você não diz o
que é fraude. Você mostra 100 mil transações, marca quais foram fraude, e o modelo
aprende o padrão.

Dentro de ML tem DEEP LEARNING, que é machine learning com redes neurais profundas.
É o que faz a máquina enxergar imagem, entender áudio e processar linguagem bem.

E dentro do deep learning tem a IA GENERATIVA. É a parte que não só classifica ou prevê,
mas GERA conteúdo novo: texto, imagem, código, áudio.

E aí tem os AGENTES, que é a fronteira de hoje: pega uma IA generativa e dá para ela
ferramentas, memória e um objetivo. Ela para de só responder e começa a executar.

Guardem a frase de baixo: toda GenAI é IA, mas nem toda IA é GenAI. Isso resolve 80%
da confusão que vocês vão ver em notícia e em LinkedIn."
""",
      "Se a sala travar aqui, o resto do curso trava. Confirme entendimento pelo chat antes de virar o slide.")

s = sl_timeline("Por que agora?", "A IA não é nova",
                [("1956", "Nasce o termo\n\"inteligência artificial\"\nem Dartmouth"),
                 ("1997", "Deep Blue vence\nKasparov no xadrez.\nRegras + força bruta"),
                 ("2012", "Deep learning explode\nno reconhecimento\nde imagens"),
                 ("2017", "Nasce a arquitetura\nTransformer, a base\nde todos os LLMs"),
                 ("2022", "ChatGPT.\nIA vira produto\nde massa"),
                 ("Hoje", "Agentes: a IA sai\ndo chat e começa\na executar tarefas")],
                subtitle="70 anos de pesquisa. Os últimos 4 mudaram o que é possível fazer no trabalho.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Muita gente acha que IA nasceu em 2022, com o ChatGPT. Não nasceu. O termo tem quase
70 anos, foi cunhado numa conferência em Dartmouth, em 1956.

Em 1997 o Deep Blue venceu o Kasparov no xadrez, e foi um marco enorme. Mas repara:
aquilo era regra escrita por gente, mais muita força bruta de cálculo. Não era um
sistema que aprendia.

O que muda o jogo é 2012, quando o deep learning começa a ganhar competições de
reconhecimento de imagem por uma margem absurda. Aí a indústria acorda.

Em 2017 sai um artigo do Google que cria a arquitetura Transformer. Esse é o alicerce
de TODOS os modelos de linguagem que vocês conhecem hoje: ChatGPT, Claude, Gemini.

E em 2022 o ChatGPT vira produto de massa. E aqui está o ponto que interessa para nós:
o que mudou em 2022 não foi a inteligência da máquina. Foi o acesso. Pela primeira vez
qualquer pessoa, sem saber programar, conseguiu usar um modelo de ponta escrevendo em
português.

E hoje a gente está no próximo passo: agentes. A IA saindo do chat e começando a
EXECUTAR tarefas. A gente vai falar bastante disso no curso."
""",
      "Não entre em detalhe técnico do Transformer. Se alguém perguntar: \"a gente vê isso mais para frente.\"")

s = sl_cards("O que destravou", "Três coisas aconteceram ao mesmo tempo",
             [("Dados em escala",
               "O mundo passou a registrar tudo digitalmente. Modelo bom precisa de exemplo, e passou a existir exemplo de sobra."),
              ("Poder de computação",
               "GPUs e nuvem tornaram possível treinar modelos gigantes e, mais importante, alugar essa capacidade por hora."),
              ("Algoritmos melhores",
               "Deep learning e a arquitetura Transformer resolveram problemas de linguagem e imagem que estavam travados há décadas.")],
             subtitle="Nenhum dos três sozinho seria suficiente. Os três juntos criaram o momento atual.",
             cols=3, card_h=3.3)
notes(s, "2 min", "ESSENCIAL", EU,
      """
"Por que agora e não em 2005? Porque três coisas aconteceram ao mesmo tempo.

Primeiro, dados. O mundo inteiro virou digital. Cada compra, cada clique, cada sensor
gera registro. E modelo aprende com exemplo. Antes não existia exemplo suficiente.

Segundo, capacidade de computação. As GPUs, que nasceram para rodar videogame, se
mostraram perfeitas para treinar redes neurais. E a nuvem fez com que você não
precisasse comprar um data center: você aluga por hora.

Terceiro, algoritmos melhores. Deep learning e Transformer destravaram problemas de
linguagem e imagem que estavam parados havia décadas.

Nenhum dos três sozinho resolveria. Os três juntos criaram o momento em que a gente
está vivendo."
""")

s = sl_statement("Onde estamos na curva",
                 "Estamos no momento em que a IA está sendo\nsuperestimada no curto prazo\ne subestimada no longo prazo.",
                 "Sua vantagem competitiva não é o hype. É saber separar o que funciona do que é promessa.")
notes(s, "2 min", "DESCARTÁVEL, 2º item a cortar", EU,
      """
"Eu quero fazer uma calibragem honesta com vocês.

A gente está num momento de barulho enorme. Todo dia sai uma notícia de que a IA vai
substituir todo mundo, e no dia seguinte sai outra dizendo que é tudo bolha.

A verdade é essa frase aí: no curto prazo a gente superestima o que a IA faz. Todo
mundo já viu um projeto de IA que prometeu muito e entregou pouco. E no longo prazo a
gente subestima.

O que eu quero que vocês levem daqui: o seu diferencial no mercado NÃO vai ser saber
usar a ferramenta da moda. Vai ser conseguir olhar para um problema e responder duas
perguntas: isso é resolvível com dados? E vale a pena resolver assim?

Isso é o que a gente vai treinar em 8 semanas."
""")

s = sl_two_col("A virada de chave", "Programação tradicional × Machine Learning",
               "PROGRAMAÇÃO TRADICIONAL",
               ["Um humano escreve as REGRAS",
                "Entram: regras + dados",
                "Sai: a resposta",
                "Exemplo: \"se o valor > R$ 5.000 E for fora do país, bloqueie\"",
                "Funciona bem quando a regra é conhecida e estável",
                "Quebra quando o mundo muda e o fraudador se adapta"],
               "MACHINE LEARNING",
               ["A máquina DESCOBRE as regras",
                "Entram: dados + respostas conhecidas",
                "Sai: a regra (o modelo)",
                "Exemplo: mostro 100 mil transações marcadas como fraude ou não",
                "Funciona bem quando o padrão é complexo demais para escrever",
                "Melhora sozinho conforme chegam dados novos"],
               subtitle="Essa inversão é a ideia mais importante de toda a área.",
               lcolor=MUTED, rcolor=NAVY)
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Se vocês entenderem só uma coisa técnica hoje, que seja essa.

Na programação tradicional, um humano escreve a regra. Você diz: se o valor for maior
que 5 mil reais E a compra for fora do país, bloqueia. Entram regras e dados, sai a
resposta. Funciona muito bem quando você CONHECE a regra.

O problema é que fraude não funciona assim. O fraudador se adapta. E existem padrões
complexos demais para alguém escrever à mão: combinações de horário, valor, local,
histórico, dispositivo.

Em machine learning a lógica é invertida. Você entrega os DADOS e as RESPOSTAS
conhecidas: 100 mil transações, com o rótulo de quais foram fraude. E o que sai não é
a resposta. É a REGRA. É o modelo.

Entrou regra e saiu resposta, é programação tradicional. Entrou resposta e saiu regra,
é machine learning. Essa inversão é o coração de toda a área."
""")

s = sl_cards("Como a máquina aprende", "Três formas de aprendizado",
             [("Supervisionado",
               "Aprende com exemplos ROTULADOS: você mostra a pergunta e a resposta certa.\n\n▸ Prever se o cliente vai cancelar\n▸ Classificar e-mail como spam\n▸ Estimar o preço de um imóvel\n\nÉ o mais usado no mercado."),
              ("Não supervisionado",
               "Não existe resposta certa. O modelo procura estrutura escondida nos dados.\n\n▸ Agrupar clientes parecidos\n▸ Encontrar comportamento atípico\n▸ Reduzir complexidade dos dados\n\nÚtil quando você não sabe o que procura."),
              ("Por reforço",
               "Aprende por tentativa e erro, com prêmio e punição.\n\n▸ Robótica e jogos\n▸ Otimização de rotas\n▸ Ajuste fino de LLMs\n\nÉ como se ensina truque para cachorro.")],
             subtitle="Você não precisa decorar. Precisa reconhecer qual deles o seu problema pede.",
             cols=3)
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Existem três formas de a máquina aprender.

Supervisionado é o mais comum, uns 80% do que se faz no mercado. Você mostra a pergunta
E a resposta certa. "Esse cliente cancelou, esse não cancelou." O modelo aprende a
associação. Prever churn, classificar spam, estimar preço: tudo supervisionado.

Não supervisionado é quando você NÃO tem a resposta. Você só joga os dados e pergunta:
tem alguma estrutura aqui? Agrupar clientes parecidos sem dizer quais grupos existem,
achar o comportamento fora da curva. É exploração.

E por reforço é tentativa e erro com recompensa. É como você ensina truque para
cachorro: acertou, ganha petisco. É o que faz robô andar e o que ajuda a ajustar o
comportamento dos LLMs para eles serem úteis e educados.

Não precisa decorar isso. Precisa, daqui a algumas semanas, olhar para um problema e
saber qual desses três ele pede."
""")

s = sl_statement("IA Generativa em uma frase",
                 "Enquanto o ML clássico responde \"qual é a resposta?\",\na IA generativa responde \"como seria uma resposta?\"",
                 "Um classifica e prevê. O outro cria. São ferramentas para problemas diferentes.")
notes(s, "1 min", "ESSENCIAL", EU,
      """
"Qual é a diferença real entre o ML que a gente acabou de ver e a IA generativa?

O ML clássico responde "qual é a resposta": esse cliente vai cancelar, sim ou não?
Esse imóvel vale quanto? Essa transação é fraude?

A IA generativa responde "como SERIA uma resposta": escreva um resumo deste contrato.
Gere uma imagem. Escreva o código que faz X.

Um classifica e prevê. O outro cria. E isso não é "um é melhor que o outro", são
ferramentas para problemas completamente diferentes. Uma das coisas que separa quem
sabe do que não sabe é justamente escolher a ferramenta certa."
""")

s = sl_bullets("Sem mistério", "Como um LLM funciona, em linhas gerais",
               [("Ele quebra o texto em pedaços chamados tokens", "≈ 3/4 de uma palavra cada"),
                ("Ele foi treinado lendo uma quantidade gigantesca de texto", "livros, sites, código, artigos"),
                ("O que ele aprendeu a fazer é uma coisa só:", "prever qual é o próximo token mais provável"),
                ("Ele escreve uma palavra, olha tudo de novo, e escreve a próxima", "e assim por diante"),
                ("Não existe banco de respostas dentro dele", "ele não \"consulta\", ele compõe"),
                ("Ele não sabe se está certo", "ele sabe o que soa provável, e isso não é a mesma coisa")],
               subtitle="É o corretor do seu teclado, levado a um extremo que ninguém previu.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Vamos abrir a caixa preta rapidinho. E eu prometo: sem matemática.

Um LLM quebra o texto em pedacinhos chamados tokens. Um token é mais ou menos três
quartos de uma palavra.

Ele foi treinado lendo uma quantidade absurda de texto: livros, sites, código,
artigos. E o que ele aprendeu a fazer é UMA coisa só: prever qual é o próximo token
mais provável.

Ele escreve uma palavra, olha tudo o que já escreveu, escreve a próxima, olha de novo,
escreve a próxima. Palavra por palavra.

E agora vem a parte que muda tudo: NÃO existe um banco de respostas dentro dele. Ele
não consulta uma base e devolve. Ele COMPÕE, na hora, a sequência de palavras mais
provável.

Por isso ele às vezes inventa uma resposta com uma confiança absoluta. Ele não sabe se
está certo. Ele sabe o que SOA provável. E isso não é a mesma coisa.

Lembram do corretor do teclado do celular, lá do começo? É exatamente isso. Levado a um
extremo que sinceramente ninguém previu que funcionaria tão bem."
""",
      "Não entre em atenção, embedding, camada. Se perguntarem: \"boa pergunta, a gente aprofunda na semana 3.\"")

s = sl_cards("Três coisas que explicam quase todo comportamento estranho",
             "Treino, contexto e inferência",
             [("Treino",
               "Acontece UMA vez, antes de você usar. É caríssimo e demorado.\n\n➜ Por isso o modelo tem uma \"data de corte\" e não sabe o que aconteceu depois."),
              ("Contexto",
               "É o que cabe na conversa atual, o que você colou ali.\n\n➜ Por isso ele \"esquece\" o começo de conversas longas e não lembra do chat de ontem."),
              ("Inferência",
               "É o momento em que ele responde. Cada resposta é gerada do zero.\n\n➜ Por isso a mesma pergunta pode gerar respostas diferentes.")],
             subtitle="Quase toda frustração com IA generativa vem de confundir esses três.",
             cols=3)
notes(s, "2 min", "ESSENCIAL", EU,
      """
"Três palavras que resolvem quase toda dúvida prática sobre esses modelos.

TREINO acontece uma vez, antes de você usar. Custa milhões e leva meses. Por isso todo
modelo tem uma data de corte e não sabe o que aconteceu depois dela.

CONTEXTO é o que cabe na conversa atual. É o que você colou ali. Por isso ele parece
"esquecer" o começo de uma conversa muito longa, e por isso ele não lembra do que vocês
conversaram ontem, a não ser que o produto guarde isso para ele.

INFERÊNCIA é o momento em que ele te responde. E cada resposta é gerada do zero. Por
isso a mesma pergunta pode dar respostas diferentes.

Se vocês entenderem esses três, param de brigar com a ferramenta e começam a usá-la
bem."
""")

s = sl_cards("A fronteira de hoje", "De chatbot para agente",
             [("Um LLM sozinho",
               "Recebe texto → devolve texto.\n\nNão consulta seu banco de dados. Não manda e-mail. Não executa nada.\n\nÉ um cérebro sem braços."),
              ("Um agente",
               "LLM + ferramentas + memória + objetivo.\n\nEle planeja os passos, usa as ferramentas, olha o resultado e decide o próximo passo.\n\nCérebro com braços."),
              ("Na prática",
               "\"Levante os 10 clientes com maior risco de cancelar, monte um resumo de cada um e me mande por e-mail.\"\n\nO agente consulta o banco, analisa, escreve e envia.")],
             subtitle="É por isso que \"agentes\" é a palavra do momento.", cols=3)
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Vocês vão ouvir a palavra AGENTE o tempo todo. Vamos desmistificar.

Um LLM sozinho é um cérebro sem braços. Ele recebe texto e devolve texto. Ele não sabe
o que tem no seu banco de dados, não manda e-mail, não executa nada. Ele só fala.

Um agente é esse mesmo cérebro com braços: você dá ferramentas para ele (acesso ao
banco, capacidade de mandar e-mail, de rodar código), mais memória e um objetivo.
E aí ele passa a planejar: "para resolver isso eu preciso primeiro consultar o banco,
depois calcular, depois escrever o resumo". Ele executa, olha o resultado e decide o
próximo passo.

Exemplo concreto: em vez de você perguntar "como eu identifico clientes em risco?", você
diz: "levante os 10 clientes com maior risco de cancelar, monte um resumo de cada um e
me mande por e-mail". E ele faz.

Isso é a fronteira hoje, e sim, isso entra no escopo do nosso curso."
""")

s = sl_table("Escolher a ferramenta certa", "A escada: quando usar o quê",
             ["Ferramenta", "Responde o quê", "Exemplo típico"],
             [["Relatório / BI", "O que aconteceu?", "Painel de vendas do mês, indicadores de operação"],
              ["Estatística / Analytics", "Por que aconteceu?", "Investigar a queda de conversão do último trimestre"],
              ["Machine Learning", "O que vai acontecer?", "Prever quais clientes vão cancelar nos próximos 60 dias"],
              ["Otimização", "O que eu devo fazer?", "Definir a melhor rota de entrega ou o melhor preço"],
              ["IA Generativa", "Como seria isso escrito ou criado?", "Resumir 500 chamados de suporte e classificar o motivo"],
              ["Agentes de IA", "Faça isso por mim, do início ao fim", "Levantar, analisar, redigir e enviar o relatório sozinho"]],
             subtitle="A pergunta certa não é \"como uso IA aqui?\". É \"qual degrau esse problema pede?\"",
             widths=[0.24, 0.28, 0.48])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Agora que a gente sabe o que é cada coisa, a pergunta é: quando usar cada uma?

Pensa numa escada.

O primeiro degrau é relatório, BI: responde O QUE ACONTECEU. Painel de vendas.

O segundo é analytics e estatística: POR QUE aconteceu. Por que a conversão caiu.

O terceiro é machine learning: o que VAI acontecer. Quais clientes vão cancelar.

O quarto é otimização: o que eu DEVO FAZER. Qual a melhor rota, qual o melhor preço.

O quinto é IA generativa: como seria isso escrito ou criado. Resumir 500 chamados de
suporte.

E o sexto são agentes: faça isso por mim, do começo ao fim.

E aqui vai um dos conselhos mais valiosos que eu posso dar para vocês em toda a
carreira: a pergunta certa NUNCA é "como eu uso IA aqui?". A pergunta certa é "qual
degrau desta escada esse problema pede?". Um monte de gente resolve com IA generativa
o que uma tabela dinâmica resolveria melhor, mais barato e mais confiável."
""")

s = sl_statement("Antes de falar de carreiras",
                 "Uma solução de IA só é boa se alguém confia nela\npara tomar uma decisão de verdade.",
                 "É por isso que os próximos três slides são sobre limites, não sobre poderes.")
notes(s, "1 min", "ESSENCIAL", EU,
      """
Mude o tom aqui. Mais sério, mais devagar.

"Eu passei os últimos 25 minutos falando do que a IA faz. Agora eu vou passar 8 minutos
falando do que ela NÃO faz. E eu considero essa a parte mais importante do meu bloco.

Porque uma solução de IA só vale alguma coisa se alguém confiar nela para tomar uma
decisão de verdade. E confiança se constrói conhecendo o limite, não o poder."
""")

s = sl_cards("Calibrando expectativas", "Seis coisas que a IA não faz",
             [("Ela não entende o que diz",
               "Um LLM não tem compreensão nem intenção. Ele produz texto estatisticamente plausível, e plausível não é sinônimo de verdadeiro."),
              ("Ela não inventa dado que não existe",
               "Sem dado bom, não existe modelo bom. \"Garbage in, garbage out\" continua sendo a lei mais respeitada da área."),
              ("Ela não é neutra",
               "O modelo aprende com dados do mundo, e o mundo tem viés. Se o histórico é enviesado, o modelo automatiza esse viés em escala."),
              ("Ela não explica sozinha o porquê",
               "Vários modelos são caixas-pretas. Em crédito, saúde e RH, não conseguir explicar a decisão pode ser um impeditivo legal."),
              ("Ela não substitui o julgamento humano",
               "A IA reduz o esforço de chegar até a decisão. A responsabilidade pela decisão continua sendo de uma pessoa."),
              ("Ela não é de graça",
               "Tem custo de infraestrutura, de dado, de manutenção e de pessoas. Projeto de IA que ignora custo morre no primeiro trimestre.")],
             cols=3)
notes(s, "3 min", "ESSENCIAL", EU,
      """
Vá pelos seis com firmeza. Este é o slide que evita frustração nas próximas 7 semanas.

"Primeiro: ela não ENTENDE o que diz. Isso é contraintuitivo porque o texto é muito bom.
Mas ele produz o que é plausível. E plausível não é a mesma coisa que verdadeiro.

Segundo: ela não inventa dado que não existe. Se sua empresa não registra o motivo do
cancelamento, nenhum modelo do mundo vai descobrir o motivo do cancelamento. Lixo entra,
lixo sai. É a lei mais respeitada da nossa área.

Terceiro, e esse é sério: ela não é neutra. O modelo aprende com dados do mundo real, e o
mundo real tem viés. Se seu histórico de contratação favoreceu um grupo, o modelo vai
aprender isso e vai fazer em escala e com aparência de objetividade.

Quarto: ela não explica sozinha o porquê. Muitos modelos são caixa-preta. Em crédito,
saúde e RH isso pode ser um impeditivo LEGAL, não só técnico.

Quinto: ela não substitui julgamento humano. Ela reduz o caminho até a decisão. A
responsabilidade continua sendo de uma pessoa, e essa pessoa pode ser você.

E sexto, o que todo mundo esquece: ela não é de graça."
""")

s = sl_bullets("Caso real · alucinação", "O advogado que citou processos que nunca existiram",
               [("Nova York, 2023", "advogados usaram o ChatGPT para pesquisar jurisprudência de um caso"),
                ("O modelo devolveu 6 decisões judiciais", "com nome das partes, números e citações completas"),
                ("Nenhuma delas existia", "estavam todas inventadas, mas soavam perfeitamente reais"),
                ("A petição foi protocolada assim mesmo", "sem ninguém conferir a fonte"),
                ("O juiz descobriu e aplicou sanção aos advogados", "o caso virou referência mundial"),
                ("A lição não é \"não use IA\"", "é: IA generativa não é fonte. Ela é ponto de partida que exige verificação.")],
               subtitle="Isso se chama alucinação, e é comportamento esperado, não defeito raro.")
notes(s, "2 min", "ESSENCIAL", EU,
      """
Conte como história. Baixe o ritmo. Este é o slide que a sala vai lembrar semana que vem.

"Deixa eu contar um caso real que virou referência mundial.

Nova York, 2023. Dois advogados estão preparando um processo e usam o ChatGPT para
pesquisar jurisprudência. O modelo devolve seis decisões judiciais anteriores, com nome
das partes, número do processo, citação, tudo formatado direitinho.

Eles protocolam a petição com aquilo. Aí a parte contrária vai procurar as decisões...
e nenhuma delas existe. Todas as seis foram inventadas pelo modelo.

O juiz descobre e aplica sanção aos advogados.

Agora, a lição aqui não é "não use IA". Eles usariam de novo se tivessem feito uma coisa
só: conferir. A lição é que IA generativa NÃO é fonte. Ela é ponto de partida. E ponto de
partida exige verificação.

Isso tem nome: chama alucinação. E é importante vocês entenderem que isso é comportamento
ESPERADO do funcionamento dele, não um bug raro que vão consertar semana que vem."
""",
      "Caso: Mata v. Avianca, Southern District of New York, 2023. Amplamente noticiado.")

s = sl_bullets("Caso real · viés", "O sistema de recrutamento que aprendeu a rejeitar mulheres",
               [("A Amazon desenvolveu uma IA para triar currículos", "objetivo: acelerar a seleção técnica"),
                ("O modelo foi treinado com 10 anos de currículos da própria empresa", "e com quem havia sido contratado"),
                ("O histórico do setor era majoritariamente masculino", "o modelo aprendeu esse padrão como sinal de sucesso"),
                ("Ele passou a penalizar currículos com marcas femininas", "sem que ninguém tivesse programado isso"),
                ("O projeto foi descontinuado em 2018", "o viés não estava no código, estava nos dados"),
                ("Por isso ética não é um bloco à parte deste curso", "é uma pergunta que a gente faz em toda etapa")],
               subtitle="Ninguém escreveu uma regra discriminatória. O modelo aprendeu a discriminar sozinho.")
notes(s, "2 min", "ESSENCIAL", EU,
      """
"Segundo caso, e esse é ainda mais desconfortável.

A Amazon construiu uma IA para triar currículos. Ideia ótima: acelerar a seleção.

Treinaram o modelo com dez anos de currículos da própria empresa e com o histórico de
quem tinha sido contratado. Faz todo sentido, né? Aprender com quem deu certo aqui.

Só que o histórico de contratação em tecnologia era esmagadoramente masculino. E o modelo
aprendeu isso como se fosse sinal de sucesso. Ele começou a penalizar currículos que
tinham marcas femininas.

Ninguém escreveu uma regra dizendo "rejeite mulheres". Ninguém. O modelo aprendeu a
discriminar sozinho, olhando o passado.

O projeto foi descontinuado em 2018.

E é exatamente por isso que neste curso ética não vai ser uma aula separada no final,
daquelas que todo mundo pula. Vai ser uma pergunta que a gente faz em toda etapa: de onde
veio esse dado? Quem ele representa? Quem ele deixa de fora? Quem é prejudicado se o
modelo errar?"
""",
      "Amazon, projeto descontinuado em 2018. Reportado pela Reuters. Fato público e documentado.")

s = sl_cards("Uso responsável", "Quatro perguntas para fazer em todo projeto",
             [("De onde veio o dado?",
               "Tenho autorização para usar? A LGPD se aplica? Tem dado pessoal aqui dentro?"),
              ("Quem esse dado representa, e quem ele deixa de fora?",
               "Se o histórico é enviesado, o modelo herda o viés e escala."),
              ("Quem é prejudicado se o modelo errar?",
               "Errar numa recomendação de filme e errar numa negativa de crédito não são a mesma coisa."),
              ("Eu consigo explicar essa decisão para uma pessoa afetada?",
               "Se a resposta é não, talvez você não devesse usar esse modelo para isso.")],
             subtitle="Isso não é um bloco de ética. É uma checklist que atravessa as 8 semanas.",
             cols=2, card_h=2.4)
notes(s, "2 min", "ESSENCIAL (mas passe rápido)", EU,
      """
Não transforme em palestra de ética. São quatro perguntas, 30 segundos cada.

"Eu não vou dar uma aula de ética hoje. Vou dar quatro perguntas, e eu quero que vocês
levem essas quatro perguntas para o resto do curso e para o resto da carreira.

De onde veio o dado? Quem ele representa e quem ele deixa de fora? Quem é prejudicado
se o modelo errar? E: eu consigo explicar essa decisão para a pessoa afetada?

Se você fizer essas quatro perguntas em todo projeto, você já está à frente de muita
gente que está no mercado há anos."
""")

s = sl_section("03", "E quem faz isso acontecer?",
               "Os papéis que existem no mundo de dados e IA", "≈ 20h12  ·  12 minutos")
notes(s, "20 s", "ESSENCIAL", EU,
      """
Slide de virada. Faça a ponte:

"Até agora a gente falou de tecnologia. Agora eu quero falar de GENTE. Porque nada disso
acontece sozinho: existe um time por trás, com papéis bem diferentes.

E eu quero que, nos próximos 12 minutos, vocês fiquem se perguntando: com qual desses
eu me pareço mais?"
""")

s = sl_table("O mapa", "Os papéis do mundo de dados e IA",
             ["Papel", "A pergunta que ele responde", "Ferramentas típicas"],
             [["Analista de Dados", "O que os dados estão dizendo sobre o negócio?", "SQL, Excel, Power BI, Python"],
              ["Engenheiro de Dados", "Como o dado chega até aqui, limpo e no horário?", "SQL, Python, pipelines, nuvem"],
              ["Cientista de Dados", "O que vai acontecer, e por quê?", "Python, estatística, ML, notebooks"],
              ["ML Engineer", "Como esse modelo funciona em produção, todo dia?", "Python, APIs, MLOps, nuvem"],
              ["AI / LLM Engineer", "Como eu construo um produto sobre modelos de IA?", "LLMs, prompts, RAG, agentes"],
              ["Analytics Engineer", "Como transformo dado bruto em base confiável?", "SQL, dbt, modelagem"],
              ["Governança / Data Steward", "Esse dado é confiável, seguro e legal de usar?", "Catálogo, LGPD, qualidade"]],
             subtitle="Não decore. Repare só em qual dessas perguntas te dá vontade de responder.",
             widths=[0.26, 0.42, 0.32])
notes(s, "3 min", "ESSENCIAL", EU,
      """
Não leia a tabela inteira em voz alta. Escolha o ângulo:

"Olha essa coluna do meio. Cada papel dessa área existe porque alguém precisa responder
uma pergunta diferente.

O analista de dados responde: o que os dados estão dizendo? O engenheiro de dados
responde: como o dado chega aqui, limpo e no horário? O cientista de dados: o que vai
acontecer, e por quê? O ML engineer: como isso funciona em produção todo santo dia? E o
AI engineer, que é o papel mais novo dessa lista: como eu construo um produto em cima
desses modelos de IA?

Eu não quero que vocês decorem essa tabela. Quero que vocês reparem numa coisa só: qual
dessas perguntas te deu vontade de responder? Segura essa sensação, porque nos próximos
slides eu vou destrinchar cada um."
""")

s = sl_cards("Papel a papel · 1", "Quem trabalha mais perto do negócio",
             [("Analista de Dados",
               "Traduz dado em decisão. Constrói indicadores, investiga variações, responde perguntas do negócio.\n\nFORTE EM: SQL, visualização, comunicação, curiosidade.\n\nÓTIMA PORTA DE ENTRADA para quem vem de áreas não técnicas."),
              ("Analytics Engineer",
               "Fica entre a engenharia e a análise. Transforma dado bruto em bases limpas e confiáveis que o resto da empresa usa.\n\nFORTE EM: SQL avançado, modelagem de dados, organização.\n\nPapel que cresceu muito nos últimos anos."),
              ("Governança / Data Steward",
               "Cuida de qualidade, catálogo, privacidade e conformidade. É quem garante que o dado seja confiável e legal de usar.\n\nFORTE EM: processo, LGPD, documentação, articulação.\n\nCaminho forte para quem vem de auditoria, jurídico ou processos.")],
             cols=3)
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Vamos por grupos. Primeiro, quem trabalha mais perto do negócio.

ANALISTA DE DADOS é quem traduz dado em decisão. Ele constrói o indicador, investiga por
que a venda caiu, responde a pergunta que o gestor fez. As ferramentas principais são SQL
e visualização, mas o que separa um analista bom de um mediano é COMUNICAÇÃO e
curiosidade. E eu quero dizer isso com todas as letras para quem está preocupado com a
parte técnica: essa é a melhor porta de entrada da área para quem vem de administração,
marketing, engenharia de produção, economia.

ANALYTICS ENGINEER é um papel mais novo, fica entre a engenharia e a análise. É quem
pega o dado bruto e transforma nas bases limpas que o resto da empresa consome. Muito
SQL, muita organização.

GOVERNANÇA é quem garante que o dado é confiável, seguro e legal de usar. Se você vem de
auditoria, de jurídico, de processos, esse caminho conversa demais com o seu repertório."
""")

s = sl_cards("Papel a papel · 2", "Quem constrói a máquina por trás",
             [("Engenheiro de Dados",
               "Constrói as estradas por onde o dado anda: coleta, pipelines, armazenamento, orquestração.\n\nFORTE EM: SQL, Python, nuvem, arquitetura.\n\nSem ele, não existe análise nem modelo. É a base de tudo."),
              ("Cientista de Dados",
               "Formula hipótese, explora, modela e mede. Une estatística, ML e entendimento de negócio.\n\nFORTE EM: estatística, Python, ML, pensamento crítico.\n\nO papel mais falado e o mais mal compreendido."),
              ("ML Engineer / MLOps",
               "Pega o modelo que funcionou no notebook e faz funcionar em produção, todo dia, para milhares de pessoas.\n\nFORTE EM: engenharia de software, APIs, monitoramento.\n\nÉ onde a maioria dos projetos de IA morre por falta de gente.")],
             cols=3)
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Segundo grupo: quem constrói a máquina por trás.

ENGENHEIRO DE DADOS constrói as estradas por onde o dado anda. Coleta, pipeline,
armazenamento. É um papel muito técnico, e é a base de tudo: sem ele não existe análise
nem modelo. E olha, é uma das áreas com mais demanda e menos gente.

CIENTISTA DE DADOS é o papel mais falado e o mais mal compreendido. Todo mundo acha que
ele fica o dia inteiro treinando modelo. Na prática, ele passa a maior parte do tempo
entendendo o problema e brigando com dado sujo. Estatística, Python, ML, mas
principalmente pensamento crítico.

ML ENGINEER é quem pega o modelo que funcionou no notebook e faz funcionar em produção,
todo dia, para milhares de pessoas. E eu quero destacar esse: é AQUI que a maior parte
dos projetos de IA morre. Tem muito modelo bom que nunca virou produto por falta de gente
que sabe fazer essa ponte."
""")

s = sl_cards("Papel a papel · 3", "O papel que praticamente não existia há 4 anos",
             [("AI Engineer / LLM Engineer",
               "Constrói produtos em cima de modelos de IA generativa: assistentes, copilotos, buscas inteligentes, agentes.\n\nFORTE EM: engenharia de prompt, RAG, integração de APIs, avaliação de respostas."),
              ("Por que ele surgiu",
               "Antes, usar IA exigia treinar um modelo do zero. Hoje os modelos já existem e são acessíveis por API.\n\nO trabalho deixou de ser treinar e passou a ser ORQUESTRAR bem."),
              ("Por que isso te interessa",
               "É o papel com a menor barreira de entrada da lista, e o mais disputado.\n\nQuem entra agora não está atrasado. Praticamente ninguém tem 5 anos de experiência nisso.")],
             cols=3)
notes(s, "2 min", "ESSENCIAL, bom momento de energia", EU,
      """
Levante a energia aqui. É o slide mais motivador do bloco.

"E aí tem esse papel, que praticamente não existia quatro anos atrás: AI Engineer, ou
LLM Engineer.

É quem constrói produto em cima de modelo de IA generativa. Assistente, copiloto, busca
inteligente, agente.

E por que ele surgiu? Porque antes, para usar IA, você tinha que treinar um modelo do
zero, o que exigia doutorado, GPU e milhões de reais. Hoje o modelo já existe e está a
uma chamada de API de distância. O trabalho deixou de ser TREINAR e passou a ser
ORQUESTRAR bem.

E agora o ponto que eu mais quero que vocês guardem desta aula inteira: esse é o papel
com a menor barreira de entrada da lista, e é um dos mais disputados. Quem está entrando
agora NÃO está atrasado. Não existe quase ninguém no mundo com cinco anos de experiência
nisso, porque isso não tem cinco anos de existência."
""")

s = sl_bullets("Três mitos", "Mitos sobre entrar nessa área",
               [("\"Preciso ser gênio da matemática\"", "precisa de lógica e de vontade de investigar. O resto se aprende."),
                ("\"Preciso saber programar antes de começar\"", "programar é ferramenta. Muita gente boa começou pelo problema, não pelo código."),
                ("\"Já estou velho, estou atrasado\"", "maturidade e repertório de negócio são vantagem enorme aqui, não desvantagem."),
                ("\"Preciso escolher uma trilha agora\"", "não precisa. As fronteiras entre esses papéis são bem porosas."),
                ("\"Preciso decidir sozinho\"", "é exatamente para isso que existem as próximas 7 semanas.")],
               subtitle="Se algum desses passou pela sua cabeça esta noite, esse slide é para você.")
notes(s, "2 min", "DESCARTÁVEL, 1º item a cortar", EU,
      """
"Eu tenho certeza que pelo menos um desses passou pela cabeça de alguém aqui esta noite.

"Preciso ser gênio da matemática." Não. Precisa de lógica e de vontade de investigar. A
matemática que você usa no dia a dia é bem menos do que parece.

"Preciso saber programar antes de começar." Não. Programar é ferramenta. Muita gente
excelente nessa área entrou pelo problema, não pelo código.

"Estou velho, estou atrasado." Olha, repertório de negócio é uma vantagem GIGANTE aqui.
Quem já entende de um setor e aprende dados tem um diferencial que quem só sabe dados
não tem.

"Preciso escolher uma trilha agora." Não precisa. As fronteiras são muito porosas.

E o último: "preciso decidir sozinho". Não. É exatamente para isso que existem as
próximas sete semanas."
""")

s = sl_interaction("Interação", "Antes do intervalo: com qual papel você mais se identificou?",
                   "Qual desses papéis mais te chamou atenção hoje?",
                   ["Analista de Dados   ·   Engenheiro de Dados   ·   Cientista de Dados",
                    "ML Engineer   ·   AI / LLM Engineer   ·   Ainda não sei",
                    "Responda na enquete, 30 segundos",
                    "E não se preocupe: \"ainda não sei\" é uma resposta perfeitamente válida hoje"])
notes(s, "2 min", "DESCARTÁVEL", EU,
      """
Coleta que serve para calibrar as próximas aulas e para gerar identificação.

"Última coisa antes do intervalo. Abre a enquete que o moderador postou no chat: qual
desses papéis mais te chamou atenção hoje?"

[aguarde ~45 s e comente o resultado]

Se "ainda não sei" ganhar, celebre:
"Olha lá, "ainda não sei" na frente. Isso é ÓTIMO. Vocês estão na semana 1 de 8. Se
vocês já soubessem, o curso não faria sentido."

Depois anuncie o intervalo com clareza de horário:
"Vamos para o intervalo. 15 minutos, voltamos 20h45 EM PONTO. Quando a gente voltar, o
Felipe assume e vai mostrar como uma solução de dados e IA nasce, na prática, do
problema até o resultado."
""",
      "Passe o bastão ANTES do intervalo, não depois. Isso dá motivo para a pessoa voltar.")

# --------------------------------------------------------------------------
s = sl_break()
notes(s, "20h30 às 20h45 (15 min)", "ESSENCIAL", "os dois",
      """
DURANTE O INTERVALO (checklist da dupla):
- Deixe este slide na tela com o horário de retorno visível.
- Moderador posta no chat: link do Discord + as 3 perguntas mais votadas para responder.
- Vocês dois: alinhem em 2 minutos se o bloco 2 atrasou e o que o bloco 3 corta.
- Confirme que a gravação continua rodando.
- Se possível, deixe uma música baixa tocando (ajuda a sala a saber que o áudio funciona).

VOLTA: comece 20h45 mesmo com gente faltando. Pontualidade na aula 1 define a cultura
das outras 7 semanas.
""")

# ==========================================================================
# BLOCO C: Ciclo de vida (20h45 às 21h45)
# ==========================================================================
s = sl_section("04", "Ciclo de vida de soluções\nde Dados e IA",
               "Do problema de negócio ao resultado que alguém usa",
               "20h45 às 21h45  ·  60 minutos")
notes(s, "20h45 às 21h45 (60 min)", "ESSENCIAL", FELIPE,
      """
ABERTURA DO SEU BLOCO (retomada pós-intervalo, ~1 min):

"Bem-vindos de volta! Eu sou o Felipe, e eu vou conduzir esta segunda metade com vocês.

O Edmar passou a primeira parte mostrando O QUE existe nesse mundo: as siglas, o que a
IA faz, o que ela não faz e quem trabalha com isso.

Agora eu vou mostrar COMO isso acontece. Como uma solução de dados e IA nasce, do
problema de negócio até alguém realmente usar o resultado.

E eu vou dar um spoiler: a parte que todo mundo acha que é o coração, treinar o modelo,
é a menor parte do trabalho."

ESTRUTURA DOS 60 MIN:
  Abertura + por que projetos falham          5 min
  Mapa das 8 fases                            5 min
  Fases 1 e 2 (problema e dados)             15 min
  Fases 3 a 5 (exploração, preparo, modelo)  12 min
  Fases 6 a 8 (avaliar, produção, monitorar) 13 min
  Caso completo ponta a ponta                 8 min
  Amarração com os papéis + interação         2 min
""")

s = sl_statement("Vamos começar pelo desconfortável",
                 "A maior parte dos projetos de IA nunca chega\na ser usada por alguém de verdade.",
                 "E quase nunca o motivo é técnico.")
notes(s, "2 min", "ESSENCIAL", FELIPE,
      """
"Vou começar pelo desconfortável.

A maior parte dos projetos de dados e IA nunca chega a ser usada por alguém de verdade.
Eles morrem no meio do caminho: viram um notebook bonito que ninguém abriu, um
dashboard que ninguém consulta, um modelo que ficou pronto e nunca foi ligado.

E aqui está a parte que interessa: quase nunca o motivo é técnico.

Os motivos costumam ser: o problema estava mal definido; o dado não existia com a
qualidade necessária; ninguém combinou como medir sucesso; ou a solução foi entregue
sem ninguém pensar em quem ia usar aquilo no dia a dia.

Nos próximos 60 minutos eu vou dar para vocês um mapa que evita cada um desses erros."
""",
      "Se quiser citar número de mercado sobre % de projetos que não chegam à produção, CONFIRA a fonte atualizada antes da aula. Sem fonte, mantenha a afirmação qualitativa como está.")

s = sl_pipeline("O mapa", "As 8 fases de uma solução de dados e IA",
                [(1, "Entender o problema", "Qual decisão de negócio precisa melhorar? Quem é o usuário? Como vamos medir sucesso?"),
                 (2, "Conseguir os dados", "O dado existe? Onde? Eu tenho acesso e autorização para usar?"),
                 (3, "Explorar", "O que os dados dizem? Qual a qualidade real? Que hipóteses se sustentam?"),
                 (4, "Preparar", "Limpar, tratar, organizar e criar as variáveis que o modelo vai usar."),
                 (5, "Construir a solução", "Regra, modelo de ML, GenAI ou agente: o que o problema pedir."),
                 (6, "Avaliar", "Funciona? Melhor do que o que existe hoje? Melhor que o baseline?"),
                 (7, "Colocar no ar", "Alguém consegue usar isso de verdade, no dia a dia?"),
                 (8, "Monitorar", "Continua funcionando daqui a 3 meses? O mundo mudou?")],
                subtitle="Guarde este slide. É o esqueleto de tudo que vocês vão fazer nas próximas 7 semanas.")
notes(s, "4 min", "ESSENCIAL, slide-âncora do bloco", FELIPE,
      """
Este é o slide-mapa. Você vai voltar mentalmente nele o tempo todo. Apresente-o de uma
vez, sem aprofundar. O aprofundamento vem nos próximos slides.

"Toda solução de dados e IA, não importa se é um dashboard simples ou um agente de IA,
passa por essas oito fases.

Um: entender o problema. Dois: conseguir os dados. Três: explorar. Quatro: preparar.
Cinco: construir a solução. Seis: avaliar. Sete: colocar no ar. Oito: monitorar.

Duas observações antes de a gente entrar em cada uma.

Primeira: repara que "construir a solução", que é o que todo mundo imagina quando pensa em
IA, é a fase CINCO de oito. E na prática costuma consumir menos de 20% do tempo do
projeto.

Segunda: isso não é uma linha reta. Você vai voltar. Você chega na fase 3 e descobre que
o dado não presta, e volta para a 2. Você chega na 6 e descobre que a métrica estava
errada, e volta para a 1. Isso é normal, isso é o trabalho.

Guardem este slide. É o esqueleto de tudo que vocês vão fazer nas próximas sete semanas."
""")

s = sl_bullets("Fase 1", "Entender o problema, a fase que mais gente pula",
               [("Qual DECISÃO precisa melhorar?", "não \"que dado eu tenho\", mas \"que decisão está ruim hoje\""),
                ("Quem toma essa decisão hoje, e como?", "se não existe decisão, não existe projeto"),
                ("O que acontece se a gente não fizer nada?", "o custo do problema justifica o esforço da solução?"),
                ("Como vamos saber que deu certo?", "defina a métrica ANTES de começar, depois vira desculpa"),
                ("O que está fora do escopo?", "dizer o que NÃO será feito evita 80% da frustração"),
                ("Qual o menor resultado útil?", "o que já geraria valor mesmo sendo simples?")],
               subtitle="Um projeto bem definido já está meio resolvido. Um mal definido não se salva com tecnologia.")
notes(s, "4 min", "ESSENCIAL", FELIPE,
      """
"Fase 1. E eu vou insistir nela, porque é a que mais gente pula.

A primeira pergunta NÃO é "que dado eu tenho". É: qual DECISÃO precisa melhorar? Alguém,
em algum lugar da empresa, toma uma decisão hoje e toma mal, ou toma devagar, ou toma no
escuro. É essa decisão que a gente quer melhorar.

Segunda: quem toma essa decisão hoje, e como? Se você não consegue responder,
provavelmente não existe projeto, existe uma curiosidade.

Terceira: o que acontece se a gente não fizer nada? Isso mede se vale a pena.

Quarta, e essa é crítica: como a gente vai saber que deu certo? Defina a métrica ANTES.
Se você define depois, ela sempre vira uma justificativa para o resultado que você
conseguiu.

Quinta: o que está FORA do escopo? Escrever o que não será feito evita a maior parte das
brigas no final do projeto.

E sexta: qual é o menor resultado que já seria útil? Porque quase sempre dá para entregar
alguma coisa em duas semanas em vez de sumir por três meses."
""")

s = sl_two_col("Fase 1 · a tradução", "De problema de negócio para pergunta analítica",
               "O QUE O NEGÓCIO DIZ",
               ["\"A gente está perdendo cliente\"",
                "\"Preciso entender melhor meu cliente\"",
                "\"Quero usar IA no atendimento\"",
                "\"O time gasta tempo demais com relatório\"",
                "Vago, amplo, sem métrica"],
               "O QUE VIRA PERGUNTA ANALÍTICA",
               ["\"Quais clientes têm alta probabilidade de cancelar nos próximos 60 dias?\"",
                "\"Existem grupos de clientes com comportamento de compra distinto?\"",
                "\"Dá para classificar automaticamente o motivo dos chamados de suporte?\"",
                "\"Dá para gerar o resumo executivo mensal a partir da base?\"",
                "Específico, mensurável, com prazo"],
               subtitle="Essa tradução é uma das habilidades mais valiosas e menos ensinadas da área.",
               lcolor=MUTED, rcolor=NAVY)
notes(s, "4 min", "ESSENCIAL", FELIPE,
      """
"Agora, na prática. O negócio nunca chega com pergunta analítica. O negócio chega com
uma frase vaga.

"A gente está perdendo cliente." Isso não é um problema resolvível, é um sintoma. A sua
tradução é: quais clientes têm alta probabilidade de cancelar nos próximos 60 dias?
Repara: virou específico, virou mensurável e ganhou prazo.

"Preciso entender melhor meu cliente" vira: existem grupos de clientes com comportamento
de compra distinto?

"Quero usar IA no atendimento", essa é a pior de todas, porque já começa pela solução,
vira: dá para classificar automaticamente o motivo dos chamados de suporte?

Essa tradução é uma das habilidades mais valiosas da nossa área. E é uma das menos
ensinadas. Vocês vão treinar isso na quinta-feira."
""",
      "Ponte com a quinta: o Canvas do Problema é exatamente a ferramenta que estrutura essa tradução.")

s = sl_cards("Fase 1 · fechamento", "Antes de sair da fase 1, você precisa de três coisas",
             [("A pergunta",
               "Escrita em uma frase. Específica, com recorte de tempo e de público.\n\n\"Quais clientes do plano mensal têm alta chance de cancelar em 60 dias?\""),
              ("A hipótese",
               "O seu palpite informado sobre a resposta, para poder ser confirmado ou derrubado.\n\n\"Quem reduziu o uso nos últimos 30 dias tem mais risco de cancelar.\""),
              ("A métrica de sucesso",
               "Como você vai provar que funcionou. De preferência, uma métrica de NEGÓCIO.\n\n\"Reduzir o cancelamento mensal em 2 pontos percentuais.\"")],
             subtitle="Se você não consegue escrever essas três frases, ainda não é hora de abrir o dado.",
             cols=3)
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Antes de sair da fase 1, você precisa conseguir escrever três frases.

A PERGUNTA, em uma frase, específica.

A HIPÓTESE: qual é o seu palpite informado sobre a resposta? Isso é importante porque
hipótese pode ser DERRUBADA. Se você não tem hipótese, você não está investigando, está
pescando.

E a MÉTRICA DE SUCESSO. E aqui vai um detalhe que separa júnior de sênior: sempre que
possível, escolha uma métrica de NEGÓCIO, não só técnica. "Reduzir cancelamento em 2
pontos" é muito melhor do que "atingir 85% de acurácia". Porque acurácia não paga conta
de ninguém.

Regra prática que eu quero deixar com vocês: se você não consegue escrever essas três
frases, ainda NÃO é hora de abrir o dado."
""")

s = sl_cards("Fase 2", "Conseguir os dados: de onde eles vêm",
             [("Sistemas internos",
               "Banco de dados do ERP, CRM, sistema de vendas, sistema de atendimento.\n\nÉ a fonte mais comum e a mais valiosa, e quase sempre precisa de tratamento."),
              ("Logs e eventos",
               "Cliques, acessos, uso do produto, sensores.\n\nVolume gigante, muito ricos em comportamento, difíceis de organizar."),
              ("Fontes externas e públicas",
               "IBGE, clima, indicadores de mercado, dados abertos do governo.\n\nÓtimos para enriquecer o que você já tem."),
              ("Texto e documentos",
               "Chamados, contratos, e-mails, avaliações, laudos.\n\nAntes eram inutilizáveis em escala. Com GenAI, deixaram de ser."),
              ("Imagens e sinais",
               "Fotos, satélite, drone, raio-X, áudio.\n\nExigem visão computacional e costumam ter altíssimo valor."),
              ("A pergunta que vem antes de todas",
               "Eu tenho AUTORIZAÇÃO para usar esse dado?\n\nLGPD, contrato com cliente, política interna. Não é detalhe jurídico, é pré-requisito.")],
             cols=3)
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Fase 2: onde estão os dados?

Sistemas internos: ERP, CRM, sistema de vendas. É a fonte mais comum e a mais valiosa,
e quase sempre precisa de tratamento pesado.

Logs e eventos: clique, acesso, uso do produto, sensor. Volume gigante, muito ricos, e
difíceis de organizar.

Fontes externas: IBGE, clima, dados abertos. Excelentes para enriquecer o que você já
tem. Muita gente esquece disso.

Texto e documentos: chamado, contrato, e-mail, avaliação. E aqui tem uma mudança
histórica: até três anos atrás, texto em escala era praticamente inutilizável para a
maioria das empresas. Com GenAI, deixou de ser. Isso destravou um volume enorme de dado
que estava parado.

Imagem e sinal: foto, satélite, drone, raio-X.

E o último card é o mais importante de todos: eu tenho AUTORIZAÇÃO para usar esse dado?
LGPD, contrato com o cliente, política interna. Isso não é um detalhe jurídico para o
final, é pré-requisito. Projeto que ignora isso morre depois de pronto, que é a pior
hora de morrer."
""")

s = sl_bullets("Fase 2 · realidade", "Os seis problemas que você VAI encontrar no dado",
               [("Dado faltando", "campos vazios, período sem registro, cliente sem histórico"),
                ("Dado duplicado", "o mesmo cliente cadastrado três vezes com grafias diferentes"),
                ("Dado inconsistente", "\"SP\", \"S.P.\", \"São Paulo\" e \"sao paulo\" na mesma coluna"),
                ("Dado desatualizado", "a base foi ótima em 2021 e ninguém mais alimentou"),
                ("Dado enviesado", "só existe registro de quem foi aprovado, você nunca vê quem foi recusado"),
                ("Vazamento de informação", "uma coluna que só existe DEPOIS do fato que você quer prever")],
               subtitle="Preparar dado costuma consumir de 60% a 80% do tempo do projeto. Isso não é fracasso, é o trabalho.")
notes(s, "4 min", "ESSENCIAL", FELIPE,
      """
"Vocês vão encontrar esses seis. Todos. Sempre.

Dado faltando: campo vazio, período sem registro.

Dado duplicado: o mesmo cliente cadastrado três vezes com grafias diferentes.

Dado inconsistente: "SP", "S ponto P ponto", "São Paulo" e "sao paulo" minúsculo, tudo na
mesma coluna. Para você é óbvio que é a mesma coisa. Para a máquina são quatro estados
diferentes.

Dado desatualizado: a base era ótima em 2021 e ninguém mais alimentou.

Dado enviesado, e esse é sutil: você só tem registro de quem foi APROVADO. Você nunca vê
o que teria acontecido com quem foi recusado. Seu modelo aprende num mundo incompleto.

E o sexto, que é o erro clássico de quem está começando: VAZAMENTO de informação. Você
inclui no modelo uma coluna que só existe DEPOIS do fato que você quer prever. Exemplo:
prever cancelamento usando a coluna "motivo do cancelamento". O modelo acerta 99% no
teste e não serve para absolutamente nada no mundo real, porque na hora de prever essa
coluna ainda está vazia.

E agora o número que assusta e liberta ao mesmo tempo: preparar dado consome de 60 a 80%
do tempo de um projeto. Quando isso acontecer com vocês, não achem que estão fazendo
errado. Isso É o trabalho."
""")

s = sl_cards("Fases 3 e 4", "Explorar e preparar",
             [("Fase 3 · Exploração (EDA)",
               "É a conversa inicial com o dado. Quantos registros? Como as variáveis se distribuem? O que se relaciona com o quê? Onde estão os pontos fora da curva?\n\nSAÍDA: você entende o terreno, e várias hipóteses já caem aqui."),
              ("Fase 4 · Preparação",
               "Limpar, padronizar, tratar faltantes e criar novas variáveis a partir das que existem (feature engineering).\n\nEx.: da data de cadastro nasce \"tempo de casa\"; do histórico nasce \"variação de uso nos últimos 30 dias\"."),
              ("O detalhe que separa amador de profissional",
               "Boas variáveis vencem modelos sofisticados com uma frequência que surpreende.\n\nQuem conhece o negócio cria variáveis melhores. Por isso repertório de setor vale tanto aqui.")],
             subtitle="Muita gente pula a exploração com pressa de modelar. É onde se perde mais tempo depois.",
             cols=3)
notes(s, "4 min", "ESSENCIAL (o 3º card é DESCARTÁVEL se atrasado)", FELIPE,
      """
"Fase 3, exploração. É a primeira conversa que você tem com o dado. Quantos registros?
Como as variáveis se distribuem? O que se relaciona com o quê? Cadê os pontos fora da
curva?

E aqui acontece uma coisa boa: várias hipóteses caem nesta fase. Você achava que o preço
explicava o cancelamento, olha o dado e vê que não explica nada. Isso é ótimo, e é
barato: descobrir isso agora custa uma tarde, descobrir isso depois de modelar custa
três semanas.

Fase 4, preparação. Limpar, padronizar, tratar faltante e criar variáveis novas a partir
das que existem. Isso tem nome: feature engineering. Exemplo simples: você tem a data de
cadastro do cliente. Sozinha, ela vale pouco. Mas dela nasce "tempo de casa", que costuma
ser uma das variáveis mais preditivas que existem.

E o terceiro card é o que eu mais quero que vocês guardem desta parte: boas variáveis
vencem modelos sofisticados com uma frequência que surpreende todo mundo. E quem cria
variável boa é quem CONHECE O NEGÓCIO. É por isso que o repertório de vocês, de
qualquer área que vocês venham, vale tanto aqui."
""")

s = sl_table("Fase 5", "Escolher a abordagem: nem tudo precisa de IA",
             ["Se o problema é...", "A resposta certa costuma ser", "Cuidado com"],
             [["A regra é conhecida e estável", "Uma regra simples. Sem modelo.", "Complicar por status: \"tem que ter IA\""],
              ["Prever um número", "Regressão (ML supervisionado)", "Prever sem ter histórico suficiente"],
              ["Prever uma categoria", "Classificação (ML supervisionado)", "Classes muito desbalanceadas"],
              ["Achar grupos sem rótulo", "Clusterização (não supervisionado)", "Achar grupo onde só há ruído"],
              ["Entender ou gerar texto", "IA generativa / LLM", "Alucinação e custo por chamada"],
              ["Executar uma tarefa fim a fim", "Agente de IA", "Perder controle e rastreabilidade"]],
             subtitle="Comece sempre pela solução mais simples que resolve. Complexidade se conquista, não se assume.",
             widths=[0.32, 0.34, 0.34])
notes(s, "4 min", "ESSENCIAL", FELIPE,
      """
"Fase 5: construir a solução. E a primeira decisão é qual abordagem usar.

Se a regra é conhecida e estável, a resposta certa é: uma regra simples. Sem modelo
nenhum. E eu quero enfatizar isso porque tem muito projeto que usa IA por status, não por
necessidade. Se um "se-então" resolve, use o "se-então": é mais barato, mais rápido, mais
fácil de explicar e não quebra.

Se você precisa prever um número (preço, demanda, tempo) é regressão.

Se precisa prever uma categoria (vai cancelar ou não, é fraude ou não) é classificação.

Se precisa achar grupos sem ter rótulo, é clusterização.

Se precisa entender ou gerar texto, aí sim IA generativa.

E se precisa executar uma tarefa do início ao fim, aí é agente.

A regra de ouro: comece sempre pela solução mais simples que resolve o problema.
Complexidade se conquista, não se assume."
""")

s = sl_statement("A regra do baseline",
                 "Antes de qualquer modelo sofisticado,\nconstrua a solução mais simples que funciona.",
                 "Se o modelo avançado não vence a solução simples, ele não vale o custo de manter.")
notes(s, "2 min", "ESSENCIAL", FELIPE,
      """
"Existe um conceito que eu queria ter aprendido no primeiro mês de carreira: BASELINE.

Baseline é a solução mais simples que funciona. Antes de treinar qualquer coisa
sofisticada, você constrói ela.

Exemplo: quero prever a venda de amanhã. Baseline: "amanhã vai vender o mesmo que hoje".
Pronto. Isso é o baseline. Agora meça o erro dele.

Aí você treina o seu modelo bonito e compara. Se o modelo não ganha do "vai vender o
mesmo que hoje", ele não vale o custo de existir. E acontece muito mais do que vocês
imaginam.

O baseline faz duas coisas: dá uma régua honesta, e te protege de entregar complexidade
que não gera valor."
""")

s = sl_cards("Fase 6", "Avaliar: como saber se funciona de verdade",
             [("Separe treino e teste",
               "O modelo aprende com uma parte dos dados e é avaliado em outra que ele NUNCA viu.\n\nAvaliar no mesmo dado do treino é como corrigir a prova com o gabarito colado."),
              ("Cuidado com overfitting",
               "É o aluno que decorou a prova antiga: vai muito bem no que já viu e mal no que é novo.\n\nSinal clássico: excelente no treino, medíocre no teste."),
              ("Compare sempre com o baseline",
               "\"85% de acurácia\" não significa nada sozinho.\n\nSignifica alguma coisa se o baseline fazia 60%. E significa fracasso se o baseline fazia 88%.")],
             subtitle="A pergunta nunca é \"o modelo é bom?\". É \"o modelo é melhor do que a alternativa?\"",
             cols=3)
notes(s, "4 min", "ESSENCIAL", FELIPE,
      """
"Fase 6: avaliar. Três ideias.

Primeira: separe treino e teste. O modelo aprende com uma parte dos dados e é avaliado
numa parte que ele NUNCA viu. Se você avalia no mesmo dado do treino, é como corrigir a
prova com o gabarito colado na folha. Vai dar 100% e não quer dizer nada.

Segunda: overfitting. Essa palavra vocês vão ouvir muito. É o aluno que decorou a prova
do ano passado: ele vai maravilhosamente bem no que já viu e mal no que é novo. O modelo
memorizou em vez de aprender o padrão. O sinal clássico é: excelente no treino, medíocre
no teste.

Terceira: compare sempre com o baseline. "85% de acurácia" não significa NADA sozinho.
Se o baseline fazia 60%, é um belo resultado. Se o baseline fazia 88%, você acabou de
gastar três semanas para piorar.

A pergunta nunca é "o modelo é bom?". É "o modelo é melhor do que a alternativa?"."
""")

s = sl_bullets("Fase 6 · a armadilha das métricas", "Por que acurácia sozinha engana",
               [("Imagine detectar fraude", "onde 1 em cada 100 transações é fraude"),
                ("Eu construo um modelo que diz sempre \"não é fraude\"", "sem olhar nada"),
                ("Ele acerta 99% das vezes", "acurácia de 99%, parece excelente"),
                ("E ele não detecta uma única fraude", "ou seja: é perfeitamente inútil"),
                ("Por isso existem outras métricas", "precisão, recall, F1: cada uma responde uma pergunta diferente"),
                ("E acima de todas: a métrica de negócio", "quanto de fraude a gente evitou, em reais?")],
               subtitle="Escolher a métrica errada é o jeito mais elegante de fracassar com aparência de sucesso.")
notes(s, "4 min", "ESSENCIAL, melhor exemplo do bloco", FELIPE,
      """
Conte isso devagar, é o exemplo que mais gera "aha" na sala.

"Deixa eu mostrar por que acurácia sozinha é perigosa.

Imagina que a gente quer detectar fraude. E na base, 1 a cada 100 transações é fraude.

Eu vou construir um modelo aqui, ao vivo, sem código nenhum. Meu modelo é: sempre
responda "não é fraude". Sempre. Sem olhar nada.

Qual a acurácia dele? 99%. Em 100 transações ele acerta 99.

Noventa e nove por cento! Em qualquer apresentação isso soa espetacular.

E quantas fraudes ele detectou? Zero. Ele é perfeitamente inútil.

É por isso que existem outras métricas: precisão, recall, F1. Cada uma responde uma
pergunta diferente. Recall pergunta "de todas as fraudes que existiam, quantas eu
peguei?". Precisão pergunta "de todas que eu apontei como fraude, quantas eram mesmo?".

E acima de todas elas está a métrica de negócio: quanto de prejuízo a gente evitou, em
reais?

Escolher a métrica errada é o jeito mais elegante de fracassar com aparência de sucesso."
""",
      "Se o tempo estiver curto, ESTE slide fica e o de overfitting sai. É o mais memorável.")

s = sl_two_col("Fase 6 · GenAI é diferente", "Avaliar IA generativa não é como avaliar ML",
               "ML CLÁSSICO",
               ["Existe um gabarito: certo ou errado",
                "A mesma entrada dá a mesma saída",
                "Métricas numéricas consolidadas",
                "Avaliação automática e barata",
                "\"O modelo acertou 87% dos casos\""],
               "IA GENERATIVA",
               ["Muitas vezes não existe UMA resposta certa",
                "A mesma entrada pode dar saídas diferentes",
                "Qualidade envolve julgamento humano",
                "Exige revisão por pessoas ou por outro modelo",
                "\"A resposta é útil, correta, segura e no tom certo?\""],
               subtitle="Por isso um projeto de GenAI precisa definir, desde o início, o que é uma boa resposta.")
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Um aviso importante: avaliar IA generativa NÃO é como avaliar ML clássico.

No ML clássico existe gabarito. O cliente cancelou ou não cancelou. Você compara e conta.
A mesma entrada dá a mesma saída, e a avaliação é automática e barata.

Na IA generativa, muitas vezes não existe UMA resposta certa. Se eu peço um resumo de um
contrato, existem dez resumos bons e diferentes. Além disso, a mesma pergunta pode gerar
saídas diferentes.

Então a avaliação passa a envolver julgamento: a resposta é útil? Está correta? É segura?
Está no tom certo? E isso exige revisão por pessoas, ou por outro modelo atuando como
avaliador, o que é uma técnica bem comum hoje.

Consequência prática: num projeto de GenAI, você precisa definir LOGO NO COMEÇO o que é
uma boa resposta. Senão você não tem como saber se melhorou."
""")

s = sl_cards("Fase 7", "Colocar no ar: de experimento a solução usada",
             [("Protótipo",
               "Prova que a ideia funciona. Roda no seu computador, com dado congelado.\n\nPúblico: você e seu time.\n\nÉ onde termina a maioria dos projetos que fracassam."),
              ("MVP",
               "A menor versão que já entrega valor real para alguém.\n\nPúblico: um grupo pequeno de usuários reais.\n\nAqui você descobre o que o mundo real pensa da sua ideia."),
              ("Produção",
               "Roda sozinho, no horário, com dado novo, com monitoramento e com alguém responsável.\n\nPúblico: todo mundo.\n\nExige engenharia, não só ciência.")],
             subtitle="Modelo que fica no notebook não gera valor nenhum. Nem para a empresa, nem para a sua carreira.",
             cols=3)
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Fase 7: colocar no ar. Existem três estágios, e é importante não confundir.

PROTÓTIPO prova que a ideia funciona. Roda no seu computador, com dado congelado, e o
público é você e seu time. E aqui vai o alerta: é exatamente onde termina a maioria dos
projetos que fracassam. O protótipo funcionou, todo mundo achou lindo na apresentação, e
acabou ali.

MVP é a menor versão que já entrega valor real para alguém de verdade. Um grupo pequeno
de usuários. E é aqui que você descobre o que o mundo real acha da sua ideia, que é
quase sempre diferente do que você imaginou.

PRODUÇÃO é quando aquilo roda sozinho, no horário, com dado novo chegando, com
monitoramento e com alguém responsável quando quebrar. E isso exige ENGENHARIA, não só
ciência de dados. Por isso o papel de ML Engineer que o Edmar mostrou é tão disputado.

Frase para levar: modelo que fica no notebook não gera valor. Nem para a empresa, nem
para a sua carreira."
""")

s = sl_bullets("Fase 8", "O modelo envelhece, e ninguém te avisa",
               [("O mundo muda depois que você treinou", "novo concorrente, nova campanha, nova crise, novo comportamento"),
                ("Isso tem nome: drift", "os dados de hoje não se parecem mais com os dados do treino"),
                ("O modelo não avisa que ficou ruim", "ele continua respondendo com a mesma confiança de sempre"),
                ("Por isso se monitora: dados de entrada, desempenho e uso", "não só se o sistema está no ar"),
                ("Retreinar faz parte do ciclo de vida", "não é sinal de que você errou"),
                ("E o mais importante: alguém precisa ser dono disso", "projeto sem dono depois do lançamento vira ruína silenciosa")],
               subtitle="Solução de dados não é obra pronta. É jardim: precisa de manutenção.")
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Fase 8, e é a mais esquecida de todas.

O modelo envelhece. Você treinou com o mundo de seis meses atrás. Aí entrou um
concorrente novo, teve uma campanha, teve uma crise, o comportamento do cliente mudou.

Isso tem nome: DRIFT. Os dados de hoje já não se parecem com os dados do treino.

E o pior: o modelo NÃO avisa. Ele continua respondendo com a mesma confiança de sempre.
Ele só está errando mais.

Por isso a gente monitora três coisas: os dados que estão entrando, o desempenho do
modelo e o uso da solução. Não só se o sistema está no ar.

Retreinar faz parte do ciclo. Não é sinal de que você errou.

E a última linha é organizacional, não técnica: alguém precisa ser DONO disso depois do
lançamento. Projeto sem dono vira ruína silenciosa: continua rodando, continua errando,
e ninguém percebe.

Solução de dados não é obra pronta. É jardim: precisa de manutenção."
""")

s = sl_table("Ponta a ponta", "Um caso completo: previsão de cancelamento",
             ["Fase", "O que foi feito", "O que quase deu errado"],
             [["1 · Problema", "\"Quem vai cancelar em 60 dias?\" Meta: reduzir churn em 2 p.p.",
               "O pedido original era só \"usar IA para reter cliente\""],
              ["2 · Dados", "Cadastro, uso do produto, chamados de suporte, pagamentos",
               "\"Motivo do cancelamento\" só existe depois do fato: vazamento"],
              ["3 · Exploração", "Queda de uso nos últimos 30 dias apareceu como forte sinal",
               "A hipótese inicial (preço) não se sustentou nos dados"],
              ["4 · Preparação", "Criadas as variáveis \"tempo de casa\" e \"variação de uso\"",
               "Bases não batiam: mesmo cliente com 3 IDs diferentes"],
              ["5 · Solução", "Classificação. Baseline: \"quem abriu 2+ chamados\"",
               "O modelo só venceu o baseline na 3ª tentativa"],
              ["6 · Avaliação", "Priorizou recall: perder cliente custa mais que ligar à toa",
               "Acurácia alta escondia desempenho ruim nos cancelamentos"],
              ["7 · Produção", "Lista semanal dos 200 maiores riscos para o time de retenção",
               "Ninguém tinha combinado O QUE fazer com a lista"],
              ["8 · Monitoramento", "Acompanhamento mensal e retreino trimestral",
               "Após uma campanha, o padrão mudou e o modelo caiu"]],
             subtitle="Repare: nenhum dos \"quase deu errado\" é um problema de algoritmo.",
             widths=[0.16, 0.44, 0.40])
notes(s, "6 min", "ESSENCIAL, fechamento do bloco", FELIPE,
      """
Este é o slide que amarra tudo. Percorra linha a linha, mas com ritmo: 40 segundos por
linha no máximo. Foque na terceira coluna.

"Agora vamos ver as oito fases juntas, num caso realista de previsão de cancelamento.

Repara que eu coloquei uma terceira coluna: o que QUASE deu errado. Porque é aí que está
o aprendizado de verdade.

Fase 1: o pedido que chegou foi "usar IA para reter cliente". Vago. A tradução virou:
quais clientes mensais vão cancelar em 60 dias, com meta de reduzir 2 pontos de churn.

Fase 2: pegamos cadastro, uso, chamados e pagamentos. E quase entrou no modelo a coluna
"motivo do cancelamento", que só existe DEPOIS do cancelamento. Aquele vazamento que eu
mostrei há pouco. Teria dado 99% de acerto no teste e zero de utilidade.

Fase 3: a hipótese inicial era preço. O dado não sustentou. O que apareceu forte foi
queda de uso nos últimos 30 dias.

Fase 4: criamos "tempo de casa" e "variação de uso". E aí veio o problema chato de
sempre: o mesmo cliente tinha três IDs diferentes em bases diferentes.

Fase 5: classificação. Baseline: "quem abriu dois ou mais chamados". E o modelo só ganhou
do baseline na terceira tentativa. Isso é normal.

Fase 6: priorizamos recall, porque perder um cliente custa muito mais caro do que ligar
para alguém que não ia cancelar. Decisão de NEGÓCIO, não técnica.

Fase 7: virou uma lista semanal com os 200 maiores riscos, entregue para o time de
retenção. E olha o que quase matou o projeto: ninguém tinha combinado o que o time DEVIA
FAZER com a lista. Modelo pronto, lista chegando, e o time olhando sem saber o que fazer.

Fase 8: acompanhamento mensal, retreino trimestral. Depois de uma campanha de marketing o
padrão mudou e o desempenho caiu.

E agora o resumo do meu bloco inteiro: olha a coluna da direita. NENHUM desses problemas
é um problema de algoritmo. Todos são problemas de definição, de dado, de processo ou de
gente. É exatamente por isso que a gente começou o curso por aqui, e não ensinando
código."
""")

s = sl_table("Amarrando", "Quem atua em cada fase",
             ["Fase", "Papel principal", "Também participa"],
             [["1 · Entender o problema", "Analista de Dados / PM", "Todo mundo. Sempre."],
              ["2 · Conseguir os dados", "Engenheiro de Dados", "Governança de Dados"],
              ["3 e 4 · Explorar e preparar", "Cientista / Analista de Dados", "Engenheiro de Dados"],
              ["5 · Construir a solução", "Cientista de Dados / AI Engineer", "ML Engineer"],
              ["6 · Avaliar", "Cientista de Dados", "Negócio (define o que importa)"],
              ["7 · Colocar no ar", "ML Engineer", "Engenharia de Software"],
              ["8 · Monitorar", "ML Engineer / MLOps", "Analista de Dados"]],
             subtitle="Ninguém faz tudo sozinho. E dá para entrar nessa área por qualquer uma dessas portas.",
             widths=[0.32, 0.36, 0.32])
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Agora eu vou juntar o meu bloco com o do Edmar.

Cada fase tem um papel principal e vários que participam.

Repara na primeira linha: fase 1, "entender o problema". O papel principal é analista ou
PM, mas quem participa? Todo mundo. Sempre. Não existe projeto de dados bom em que só uma
pessoa entendeu o problema.

E repara em outra coisa: você pode entrar nessa área por QUALQUER uma dessas portas. Se
você gosta de conversar com o negócio e traduzir problema, entra pela fase 1. Se você
gosta de construir estrutura e resolver quebra-cabeça técnico, entra pela fase 2. Se
gosta de investigar e testar hipótese, fases 3, 4 e 5. Se gosta de fazer as coisas
funcionarem de verdade e não quebrarem, fases 7 e 8.

Nenhuma dessas portas é mais nobre que a outra. E ninguém faz tudo sozinho."
""")

s = sl_interaction("Interação", "Antes de encerrarmos",
                   "Na sua opinião, em qual fase a maioria dos projetos de IA trava?",
                   ["1 Entender o problema   ·   2 Dados   ·   3 e 4 Explorar e preparar",
                    "5 Construir   ·   6 Avaliar   ·   7 Colocar no ar   ·   8 Monitorar",
                    "Responda na enquete, 30 segundos",
                    "Depois eu conto o que a experiência de mercado costuma mostrar"])
notes(s, "2 min", "DESCARTÁVEL", FELIPE,
      """
"Última interação da noite. Na opinião de vocês, em qual dessas fases a maioria dos
projetos de IA trava?"

[aguarde 30 a 45 s]

Depois comente:
"Na prática, as duas campeãs são a fase 1 e a fase 7. A fase 1 porque o problema estava
mal definido desde o começo, e aí tudo depois vira desperdício. E a fase 7 porque o
protótipo funcionou e nunca virou algo que alguém usasse de verdade.

Repara: as duas pontas. O começo e o fim. E nenhuma das duas é a parte de treinar modelo,
que é onde quase todo mundo acha que está a dificuldade."
""")

# ==========================================================================
# BLOCO D: Encerramento (21h45 às 22h00)
# ==========================================================================
s = sl_section("05", "Encerramento", "O que você leva de hoje e o que vem na quinta",
               "21h45 às 22h00  ·  15 minutos")
notes(s, "21h45 às 22h00 (15 min)", "ESSENCIAL", FELIPE,
      """
DISTRIBUIÇÃO DOS 15 MIN:
  Recapitulação           3 min
  O que vem na quinta     3 min
  Como se preparar        2 min
  Q&A                     6 min  (elástico: é aqui que você absorve atraso)
  Fechamento              1 min

Se a aula estiver atrasada, o Q&A encolhe primeiro, mas NUNCA passe das 22h00.
Terminar no horário na aula 1 é uma promessa implícita para as outras 7 semanas.
""")

s = sl_bullets("Recapitulando", "As 6 ideias que a gente quer que você leve hoje",
               [("IA é um guarda-chuva", "ML aprende com exemplos; GenAI cria conteúdo; agentes executam tarefas"),
                ("O que mudou não foi a inteligência da máquina", "foi o acesso: hoje qualquer pessoa consegue usar"),
                ("A IA não entende, não é neutra e não decide por você", "ela reduz o caminho até a decisão"),
                ("A pergunta certa não é \"como uso IA?\"", "é \"que decisão precisa melhorar, e o que esse problema pede?\""),
                ("Treinar modelo é a menor parte do trabalho", "problema, dado e produção é onde os projetos vivem ou morrem"),
                ("Existe uma porta de entrada para o seu perfil", "técnico ou não, analítico ou de negócio: todas são válidas")],
               subtitle="Se você levar só essas seis frases desta noite, a aula cumpriu o objetivo dela.",
               numbered=True)
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
Leia as seis com calma. É a última chance de fixar.

"Antes de a gente encerrar, seis frases. Se vocês esquecerem tudo desta noite e lembrarem
só destas seis, a aula cumpriu o objetivo.

Um: IA é um guarda-chuva. Machine learning aprende com exemplos, GenAI cria conteúdo,
agentes executam tarefas.

Dois: o que mudou nos últimos anos não foi a inteligência da máquina. Foi o acesso.

Três: a IA não entende, não é neutra e não decide por você. Ela reduz o caminho até a
decisão, e a decisão continua sendo humana.

Quatro: a pergunta certa nunca é "como eu uso IA aqui?". É "que decisão precisa melhorar,
e o que esse problema pede?".

Cinco: treinar modelo é a menor parte do trabalho. O projeto vive ou morre no problema,
no dado e na produção.

E seis, que é a mais importante para vocês hoje: existe uma porta de entrada para o SEU
perfil. Técnico ou não, analítico ou de negócio. Todas são válidas, e a gente vai mostrar
todas elas nas próximas sete semanas."
""")

s = sl_two_col("Próximo encontro", "Quinta-feira, 19h00 às 21h00",
               "O QUE VAMOS FAZER",
               ["Primeiro laboratório do programa",
                "Como transformar um problema de negócio em problema analítico, na prática",
                "Apresentação do Canvas do Problema, sua primeira ferramenta de trabalho",
                "Um caso real para vocês estruturarem junto com a gente",
                "Espaço aberto para dúvidas desta aula"],
               "O QUE VOCÊ PRECISA LEVAR",
               ["Nada instalado: a quinta ainda é sem código",
                "Uma conta Google (vamos usar Google Colab a partir da semana 2)",
                "Papel e caneta, ou um documento em branco",
                "As dúvidas que ficaram de hoje",
                "Estar no Discord, o material será postado lá antes da aula"],
               subtitle="As quintas são mais curtas e muito mais práticas. Não perca esta.",
               lcolor=NAVY, rcolor=NAVY_SOFT)
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
"Quinta-feira, 19h às 21h. Duas horas, e é bem diferente de hoje.

Hoje foi panorama. Quinta é laboratório: a gente vai pegar um caso real e transformar
junto com vocês um problema de negócio vago numa pergunta analítica de verdade, aquilo
que eu mostrei há pouco, mas fazendo com vocês.

E a gente vai apresentar o Canvas do Problema, que é a primeira ferramenta de trabalho de
vocês no programa. É simples, cabe numa página, e vocês vão usar ela até o final do curso.

Do lado direito, o que você precisa levar: nada instalado. Quinta ainda é sem código. Só
uma conta Google, porque a partir da semana 2 a gente entra no Google Colab, papel e
caneta, e as dúvidas que ficaram de hoje.

E por favor: entrem no Discord ainda esta noite. O material da quinta vai ser postado lá
antes da aula."
""")

s = sl_cards("Até quinta", "Como aproveitar melhor os próximos 3 dias",
             [("Entre no Discord hoje",
               "É onde o material, os avisos e as dúvidas vão viver nas próximas 8 semanas.\n\nLink no chat e no e-mail que você vai receber."),
              ("Um exercício de 10 minutos",
               "Pense em UM problema real do seu trabalho, faculdade ou dia a dia que você acha que dados poderiam resolver.\n\nTraga ele na quinta. Vamos usar."),
              ("Se quiser ir além (opcional)",
               "Reveja a gravação da aula com calma, ou anote as 3 palavras de hoje que você não conhecia.\n\nNão tem leitura obrigatória. Descanse também.")],
             subtitle="Nada aqui é obrigatório. Mas quem faz, chega na quinta em outro nível.",
             cols=3)
notes(s, "2 min", "ESSENCIAL (o 3º card é DESCARTÁVEL)", FELIPE,
      """
"Três coisas para os próximos dias.

Primeira: entrem no Discord HOJE. É o canal oficial.

Segunda, e essa é a que mais vale a pena: pensem em UM problema real, do trabalho, da
faculdade, do dia a dia, que vocês acham que dados poderiam resolver. Não precisa ser
sofisticado. Pode ser "por que a fila do meu setor sempre trava na sexta". Tragam esse
problema na quinta, porque a gente vai usar de verdade.

Terceira, opcional: revejam a gravação com calma ou anotem as três palavras de hoje que
vocês não conheciam. E descansem também: são 8 semanas, isso é maratona, não é tiro
curto."
""")

s = sl_statement("Agora é com vocês", "Perguntas?",
                 "Escreva no chat. Vamos responder o máximo que o tempo permitir.\nO que não der tempo, respondemos no Discord ainda esta semana.")
notes(s, "6 min (elástico)", "ESSENCIAL", f"{FELIPE} + {EU}",
      """
Q&A com 190 pessoas exige método:

1. O MODERADOR seleciona as perguntas. Não leiam o chat cru ao vivo.
2. Priorizem perguntas REPETIDAS (se 5 pessoas perguntaram, responda em voz alta).
3. Respondam em até 60 segundos cada. Se precisar de mais, diga: "essa merece mais
   tempo, vou responder no Discord ainda hoje".
4. Os dois respondem. Alternem, não deixem uma pessoa sozinha.
5. Encerrem prometendo o que não deu tempo: "as perguntas que ficaram vão para o Discord
   ainda esta semana." E CUMPRAM.

PERGUNTAS QUE VÃO APARECER, respostas prontas:

• "Preciso saber programar?"
  Não para acompanhar. E no mini-desafio existe uma trilha que não exige código.

• "Quantas vagas de trainee tem?"
  Isso vai depender do desempenho da turma. Nosso interesse é levar o máximo de gente
  engajada para a Etapa 2. (NÃO informar o número.)

• "Todo mundo passa para a Etapa 2?"
  A Etapa 2 é para quem mostrar desempenho no mini-desafio da semana 4. Os critérios
  completos a gente apresenta com antecedência, na semana 3.

• "Vai ter certificado?"
  [ALINHAR ESTA RESPOSTA COM A DIRETORIA ANTES DA AULA.]

• "A aula fica gravada?"
  Sim, o link chega em até 24 horas.

• "Posso fazer só as segundas?"
  Pode, mas a quinta é onde a prática acontece, e a avaliação olha as entregas.

• "Qual linguagem vamos usar?"
  Python, no Google Colab, a partir da semana 2. Gratuito e sem instalar nada.

• "Preciso pagar por ChatGPT ou API?"
  Não. Nas aulas práticas usamos APIs gratuitas para modelos de LLM.
""")

s = sl_closing()
notes(s, "1 min", "ESSENCIAL", FELIPE,
      """
FECHAMENTO (30 segundos, com energia, a última frase é a que fica):

"Pessoal, muito obrigado pela noite de hoje. Sério: 190 pessoas numa segunda à noite,
até às 22h, é um compromisso e a gente reconhece isso.

Entrem no Discord, pensem naquele problema que a gente pediu, e nos vemos na quinta às
19h.

E fica com isso: hoje vocês estavam do lado de fora olhando esse mundo de dados e IA.
Daqui a sete semanas, vocês vão ter construído alguma coisa dentro dele. Boa noite!"

DEPOIS DE ENCERRAR:
- Pare a gravação.
- Poste no chat, uma última vez: link do Discord.
- Vocês dois: 10 minutos de retrospectiva ainda hoje (o que funcionou, o que cortar).
- Envie o e-mail de pós-aula no dia seguinte, de manhã.
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

out = ROOT / "docs" / "aula-01"
out.mkdir(parents=True, exist_ok=True)
dest = out / "AI-Talent-Academy-Aula01.pptx"
prs.save(dest)
print(f"OK: {dest}  ({_n['i']} slides)  Roboto, sem travessões, tamanho único por bloco.")
