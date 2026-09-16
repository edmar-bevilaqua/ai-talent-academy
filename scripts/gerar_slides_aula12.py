# -*- coding: utf-8 -*-
"""
Gerador do deck da Aula 12 (Semana 6, quinta-feira) do AI Talent Academy.

Tema: Aplicação de Machine Learning: Treinando o Primeiro Modelo.
Aula inteiramente prática no Google Colab com scikit-learn.
Reaproveita a base de transações e fraude das Aulas 2, 5, 6, 7, 8 e 10.

Identidade visual: padrao White Cube (Roboto, azul 28347B, fundos e logo do template
oficial em assets/whitecube/).

Uso:  python scripts/gerar_slides_aula12.py
Saida: docs/aula-12/AI-Talent-Academy-Aula12.pptx

Regras de estilo aplicadas em todo o deck:
  1. Fonte Roboto em 100% dos textos.
  2. Um unico tamanho de fonte por caixa de texto (nunca alterna tamanho no mesmo bloco).
  3. Zero travessoes (nem em dash nem en dash). Ha assert no final que garante isso.
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
S_FOOT = 13          # rodape (mobilia da pagina)
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
        if isinstance(ln, tuple):
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
        r = p.add_run()
        r.text = mk
        r.font.size = Pt(size)
        r.font.bold = True
        r.font.color.rgb = bullet_color
        r.font.name = FONT
        r = p.add_run()
        r.text = head
        r.font.size = Pt(size)
        r.font.bold = tail is not None
        r.font.color.rgb = head_color
        r.font.name = FONT
        if tail:
            r = p.add_run()
            r.text = "  " + tail
            r.font.size = Pt(size)
            r.font.bold = False
            r.font.color.rgb = tail_color
            r.font.name = FONT
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
    """Rodape do template White Cube sem numero impresso nos shapes."""
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
          "Semana 6  ·  Aplicação de Machine Learning: Treinando o Primeiro Modelo", 25, INK, space=0)
    shape(s, ML, Inches(5.75), Inches(2.4), Pt(5), fill=RED)
    block(s, ML, Inches(8.15), Inches(13), Inches(1.0),
          ["Aula 12  ·  Quinta-feira, 19h00 às 21h00  ·  Online",
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
    """Bloco de declaração com assert de comprimento máximo de linha."""
    s = new_slide(BG_NAVY)
    linhas = big.split("\n")
    for ln in linhas:
        assert len(ln) <= MAX_LINHA_BIG, f"linha longa demais no statement: {ln!r}"
    top = Inches(3.85)
    lh = Inches(0.62)
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


def sl_pipeline(kicker, title, steps, subtitle=None, per_row=3):
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
            next_center = yy + ch + vgap + int(ch / 2)
            shape(s, ML - Inches(0.52), next_center - Inches(0.17), Inches(0.42),
                  Inches(0.34), fill=LINE, kind=MSO_SHAPE.CHEVRON)
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


def sl_code(kicker, title, codigo, items, subtitle=None):
    """Bloco de codigo em destaque com bullets explicativos embaixo."""
    s = new_slide(BG_WHITE)
    y = chrome(s, kicker, title, subtitle)
    linhas = codigo if isinstance(codigo, list) else codigo.split("\n")
    alt_linha = Inches(0.38)
    qh = alt_linha * len(linhas) + Inches(0.45)
    shape(s, ML, y, CW, qh, fill=RGBColor(0xF2, 0xF3, 0xF6), border=NAVY, border_w=1.0)
    shape(s, ML, y, Pt(6), qh, fill=NAVY)
    block(s, ML + Inches(0.45), y + Inches(0.22), CW - Inches(0.9), qh - Inches(0.3),
          linhas, S_MIN, NAVY, bold=True, space=2, line=1.28)
    y2 = y + qh + Inches(0.4)
    rich_block(s, ML, y2, CW, BOTTOM - y2, items, S_BULLET)
    footer(s)
    return s


def sl_timeline(kicker, title, steps, subtitle=None):
    """Linha do tempo horizontal com marcos cronologicos."""
    s = new_slide(BG_WHITE)
    y = chrome(s, kicker, title, subtitle)
    n = len(steps)
    gap = Inches(0.4)
    cw = int((CW - gap * (n - 1)) / n)
    line_y = y + Inches(0.9)
    shape(s, ML, line_y, CW, Pt(4), fill=LINE)
    for i, (tempo, texto) in enumerate(steps):
        x = ML + i * (cw + gap)
        cx = x + int(cw / 2)
        shape(s, cx - Inches(0.25), line_y - Inches(0.23), Inches(0.5), Inches(0.5),
              fill=NAVY, kind=MSO_SHAPE.OVAL)
        shape(s, cx - Inches(0.12), line_y - Inches(0.1), Inches(0.24), Inches(0.24),
              fill=RED, kind=MSO_SHAPE.OVAL)
        block(s, x, y, cw, Inches(0.6), tempo, S_CARD_T, NAVY, bold=True,
              align=PP_ALIGN.CENTER, space=0)
        shape(s, x, line_y + Inches(0.5), cw, BOTTOM - line_y - Inches(0.7), fill=LIGHT, border=LINE)
        block(s, x + Inches(0.25), line_y + Inches(0.75), cw - Inches(0.5),
              BOTTOM - line_y - Inches(1.1), texto.split("\n"), S_TIMELINE, INK,
              space=6, line=1.18)
    footer(s)
    return s


def sl_closing():
    s = new_slide(BG_NAVY)
    block(s, ML, Inches(3.6), Inches(15), Inches(1.7), "Obrigado!", 66, WHITE, bold=True,
          space=0, line=1.0)
    block(s, ML, Inches(5.5), Inches(15), Inches(0.8), "Nos vemos na segunda-feira, 19h00.",
          30, NAVY_TXT_SOFT, space=0)
    shape(s, ML, Inches(6.85), Inches(2.4), Pt(5), fill=RED)
    block(s, ML, Inches(7.4), Inches(15), Inches(1.4),
          ["Discord do AI Talent Academy: canal de dúvidas e material aberto.",
           "Gravação e notebooks desta aula chegam em até 24 horas."], 18, NAVY_TXT_SOFT, space=8)
    footer(s, dark=True)
    return s


# ==========================================================================
# CONTEÚDO DOS SLIDES
# ==========================================================================
EDMAR = "Edmar Bevilaqua"
FELIPE = "Felipe André Bach Alves"

# Slide 1: Capa
s = sl_cover()
notes(s, "19h00 às 19h05 (5 min)", "ESSENCIAL", EDMAR,
      """
Abertura da noite e recepção da turma.

"Boa noite, pessoal! Sejam bem-vindos à nossa Aula 12 do AI Talent Academy.
Hoje é a nossa quinta-feira de laboratório da Semana 6, e esta noite marca um ponto
muito especial no nosso programa.

Na segunda-feira nós cobrimos toda a base conceitual de Machine Learning: o que significa
aprender, função de perda, gradiente descendente, matriz de confusão e o cardápio de
modelos. Hoje nós vamos sentar na frente do computador e treinar o primeiro modelo de
vocês, do zero, no Google Colab, usando a biblioteca scikit-learn.

Abram o Colab pelo link fixado no chat e vamos começar."
""",
      "Conferir gravação ligada e link do notebook fixado no chat do Zoom e no canal do Discord.")

# Slide 2: Espera
s = sl_statement("Enquanto todo mundo entra",
                 "Abram o Google Colab pelo link fixado no chat.\nHoje vamos treinar o primeiro modelo de verdade.",
                 "19h00 às 19h10  ·  Recepção, áudio e tela compartilhada")
notes(s, "19h05 às 19h10 (5 min)", "DESCARTÁVEL", FELIPE,
      """
Slide de apoio nos dez minutos iniciais para acolher quem está entrando na sala.

"Quem acabou de chegar: o link do notebook de hoje já está fixado no topo do chat e
também lá no Discord.

Abram o link no navegador. Não precisa instalar nada no computador: tudo roda nos
servidores do Google Colab. Hoje vamos usar Python, pandas e a biblioteca scikit-learn.
Aproveitem estes minutos para salvar uma cópia do notebook no Drive de vocês."
""")

# Slide 3: Seção 01
s = sl_section("01", "Bloco A · Da teoria ao código",
               "O retorno da Aula 11 e o plano da noite",
               "19h10 às 19h25  ·  15 minutos")
notes(s, "19h10 às 19h13 (3 min)", "ESSENCIAL", EDMAR,
      """
Abertura do primeiro bloco expositivo da noite.

"Começamos o Bloco A fazendo a ponte direta com o que vimos na segunda-feira.
Na segunda nós passamos mais de quatro horas discutindo conceitos, fórmulas e intuição.
Hoje a regra é outra: código executável, visualização gráfica e decisões de negócio."
""")

# Slide 4: Cards recap Aula 11 x Aula 12
s = sl_cards("De volta à segunda", "O que a teoria ensinou e o que a prática constrói",
             [("Na segunda: os conceitos",
               "Aprendizado como ajuste de números para errar menos.\nMatriz de confusão com VP, FP, FN e VN.\nA armadilha clássica da acurácia.\nOito famílias de algoritmos apresentadas."),
              ("Hoje: código executável",
               "Ambiente real no Google Colab com Python.\nTreinamento com scikit-learn.\nDesenho visual da árvore de decisão com plot_tree.\nMedição de impacto em reais."),
              ("A mesma base de dados",
               "O mesmo caso de fraude em cartão das Aulas 2, 5, 6, 7, 8 e 10.\nVariáveis temporais, valores e categorias que vocês já conhecem e exploraram.")],
             subtitle="Tudo que vimos na teoria ganha forma em células de código hoje.")
notes(s, "4 min", "ESSENCIAL", EDMAR,
      """
"Reparem na continuidade do programa.
Na segunda a gente discutiu como a máquina aprende: ajustando parâmetros matemáticos até errar menos.
Vimos a matriz de confusão e por que acurácia engana.

Hoje nós vamos pegar esses mesmos conceitos e colocar para rodar.
E o melhor: sobre a mesma base de transações de cartão que vocês vêm acompanhando desde
a modelagem do canvas na Aula 2, as consultas em SQL na Aula 5 e o pipeline na Aula 10.
Vocês já conhecem o negócio por trás desses números."
""")

# Slide 5: Statement sobre a armadilha do 99%
s = sl_statement("A armadilha do 99%",
                 "Em dados desbalanceados,\nacurácia alta é a forma mais fácil de mentir.",
                 "Um modelo que responde sempre 'não é fraude' acerta 98% e não pega uma fraude sequer.")
notes(s, "3 min", "ESSENCIAL", FELIPE,
      """
Provocação central do laboratório.

"Gravem esta frase antes de encostar no teclado: em dados desbalanceados, acurácia alta
é a forma mais fácil de mentir.

Se noventa e oito por cento das transações de um banco são legítimas e duas são fraude,
um modelo preguiçoso que carimba 'aprovada' em todas as compras terá noventa e oito por cento
de acurácia. A diretoria comemora a métrica e o banco quebra no final do mês porque
nenhuma fraude foi interceptada.

O nosso primeiro passo prático no Colab vai ser justamente programar esse modelo ingênuo
para ver esse número feio na tela."
""")

# Slide 6: Pipeline do laboratório (6 passos)
s = sl_pipeline("Roteiro prático", "Os seis passos do laboratório no Colab",
                [(1, "Preparação", "Importação dos módulos e carga da base com coluna alvo."),
                 (2, "Baseline ingênuo", "DummyClassifier provando acurácia alta com recall zero."),
                 (3, "Split de dados", "Separação estratificada entre 70% treino e 30% teste."),
                 (4, "Árvore de decisão", "Treino no scikit-learn e desenho visual dos nós."),
                 (5, "Matriz e finanças", "Cálculo de precisão, recall e economia líquida em reais."),
                 (6, "Poda e overfitting", "Ajuste de max_depth para generalizar sem decorar.")],
                subtitle="Um fluxo completo de Machine Learning executado em duas horas.")
notes(s, "5 min", "ESSENCIAL", FELIPE,
      """
Apresentação da trilha do aluno.

"Aqui está o mapa da nossa noite. São seis passos lógicos e bem delimitados.
Começamos preparando os dados. Em seguida, criamos o baseline ingênuo para comprovar a falha.
No passo três, fazemos a divisão em treino e teste com estratificação.
No passo quatro, treinamos nossa primeira árvore de decisão e desenhamos os ramos na tela.
No passo cinco, calculamos a matriz de confusão e convertemos erros em reais.
E fechamos no passo seis testando o overfitting ao mudar a profundidade da árvore.

Cada passo tem explicações no notebook e células marcadas com TODO para vocês preencherem."
""")

# Slide 7: Seção 02
s = sl_section("02", "Bloco B · Demonstração ao vivo",
               "Os professores treinam o primeiro modelo na tela",
               "19h25 às 19h45  ·  20 minutos")
notes(s, "19h25 às 19h27 (2 min)", "ESSENCIAL", FELIPE,
      """
Abertura da demonstração ao vivo. Felipe assume a tela e compartilha o notebook do professor.

"Agora nós vamos para os vinte minutos de demonstração.
Ninguém precisa digitar nada agora: olhem para a minha tela.
Vou percorrer o notebook, executar célula por célula e mostrar o comportamento do código."
""")

# Slide 8: Código scikit-learn
s = sl_code("scikit-learn na prática", "A anatomia de um treino em quatro passos",
            ["from sklearn.tree import DecisionTreeClassifier",
             "modelo = DecisionTreeClassifier(max_depth=3, random_state=42)",
             "modelo.fit(X_train, y_train)",
             "y_pred = modelo.predict(X_test)"],
            [("1. Instanciação", "escolhemos a classe do modelo e seus hiperparâmetros iniciais."),
             ("2. Ajuste com .fit()", "o algoritmo calcula as melhores divisões gulosas nos dados de treino."),
             ("3. Inferência com .predict()", "o modelo aplica as regras e gera previsões para o conjunto de teste."),
             ("4. Padrão universal", "a mesma interface serve para árvore, regressão logística, random forest e SVM.")],
            subtitle="Toda biblioteca moderna de dados segue essa estrutura em três métodos.")
notes(s, "6 min", "ESSENCIAL", FELIPE,
      """
Explicar a simplicidade da API do scikit-learn.

"Reparem nestas quatro linhas de código. Elas resumem o coração do scikit-learn.
Primeiro você importa o modelo desejado.
Depois você instancia o estimador, definindo opções como profundidade máxima.
Em seguida você chama fit passando X e y de treino. É aqui que o computador trabalha.
E por fim você chama predict para gerar previsões no conjunto de teste.

O fascinante da biblioteca é que quando vocês forem treinar uma regressão logística ou
um random forest, o código será praticamente idêntico. O método é sempre fit e predict."
""")

# Slide 9: Anatomia de um nó da árvore
s = sl_cards("Por dentro da árvore", "O que cada caixa do plot_tree revela",
             [("Pergunta de corte",
               "Exemplo: valor <= 312.50.\nUma regra binária simples que divide o fluxo.\nSe for verdadeiro vai para a esquerda; se falso, vai para a direita."),
              ("Índice de impureza",
               "Mede o grau de mistura de classes naquele nó.\nValor zero indica um nó totalmente puro onde todas as transações pertencem à mesma classe."),
              ("Distribuição de classes",
               "Mostra quantas transações legítimas e quantas fraudes chegaram até aquele ponto da decisão lógica.")],
             subtitle="A explicabilidade é a maior força de uma árvore de decisão.")
notes(s, "6 min", "ESSENCIAL", EDMAR,
      """
Explicar a leitura visual da árvore.

"Quando rodamos a função plot_tree no notebook, surge um diagrama em forma de árvore.
Cada caixa representa um nó de decisão.
No topo da caixa tem a pergunta de corte: por exemplo, valor menor ou igual a trezentos reais.
Se for sim, o dado desce para a esquerda. Se for não, desce para a direita.

Logo abaixo tem o índice de Gini, que mede a impureza. Se tiver zero, significa que todas
as transações ali são de uma classe só.
E embaixo tem a contagem exata de quantas compras legítimas e quantas fraudes caíram ali.
É por isso que equipes de auditoria adoram árvores: você consegue justificar cada decisão."
""")

# Slide 10: Tabela da matriz traduzida em finanças
s = sl_table("Matriz de confusão", "Traduzindo métricas em impacto financeiro real",
             ["Resultado do Modelo", "Situação Real", "O que acontece na prática", "Impacto em Reais"],
             [["Verdadeiro Positivo (VP)", "Fraude Real", "Transação bloqueada a tempo", "Economia do valor da fraude"],
              ["Falso Positivo (FP)", "Compra Legítima", "Cliente bom barrado no caixa", "Custo de SAC e atrito comercial"],
              ["Falso Negativo (FN)", "Fraude Real", "Fraude aprovada sem barreira", "Prejuízo financeiro direto"],
              ["Verdadeiro Negativo (VN)", "Compra Legítima", "Compra aprovada sem fricção", "Receita saudável garantida"]],
             widths=[0.24, 0.20, 0.30, 0.26],
             subtitle="No comitê de diretoria, ninguém pergunta pelo F1: perguntam pelo saldo líquido.")
notes(s, "6 min", "ESSENCIAL", FELIPE,
      """
Ligação direta com finanças e negócio.

"Na segunda-feira nós aprendemos os quatro quadrantes da matriz de confusão.
Hoje nós vamos colocar preço neles.
O Verdadeiro Positivo economiza o dinheiro da fraude roubada.
O Falso Positivo custa caro: gera ligação furiosa no atendimento, retrabalho e risco de
perder o cliente para a concorrência.
O Falso Negativo é o prejuízo puro: a fraude aconteceu e o banco assume a perda.
E o Verdadeiro Negativo é o negócio funcionando em paz.

No notebook, criamos uma fórmula simples que calcula o ganho líquido em reais.
É esse número que vende o projeto internamente."
""")

# Slide 11: Seção 03
s = sl_section("03", "Bloco C · Mecânica da prática",
               "Como vamos trabalhar nos próximos 45 minutos",
               "19h45 às 20h00  ·  15 minutos")
notes(s, "19h45 às 19h48 (3 min)", "ESSENCIAL", FELIPE,
      """
Abertura das instruções práticas antes da mão na massa.

"Agora é a vez de vocês. Vamos explicar como a atividade vai funcionar para ninguém
ficar perdido nos próximos quarenta e cinco minutos."
""")

# Slide 12: Instruções de acesso Colab
s = sl_cards("Instruções de acesso", "Tudo pronto no navegador, sem instalar nada",
             [("1. Abra o link fixado",
               "Acesse o link do Google Colab que está fixado no chat e no Discord.\nO notebook já vem com o texto e o esqueleto de código."),
              ("2. Salve uma cópia",
               "Clique em 'Arquivo' no menu superior do Colab e selecione 'Salvar uma cópia no Drive'.\nAssim você edita a sua versão pessoal."),
              ("3. Rode o Passo 0",
               "Execute a primeira célula para importar as bibliotecas e carregar os dados.\nSe o download falhar, o script gera dados sintéticos.")],
             subtitle="Certifique-se de salvar sua cópia antes de começar a editar.")
notes(s, "4 min", "ESSENCIAL", FELIPE,
      """
Passo a passo operacional para salvar a cópia.

"Primeiro passo operacional: abram o link do Google Colab.
Segundo passo: cliquem em Arquivo e depois em Salvar uma cópia no Drive.
Se vocês tentarem editar direto no link compartilhado, o Colab vai avisar que o arquivo
está protegido para edição.
Depois de salvar sua cópia, rodem o Passo 0."
""")

# Slide 13: Regras e apoio
s = sl_two_col("Regras da prática", "Como aproveitar os 45 minutos de código",
               "O QUE FAZER HOJE",
               ["Executar as células na ordem numérica estrita",
                "Ler os comentários e orientações em cada seção",
                "Completar as linhas marcadas com # TODO",
                "Olhar a matriz de confusão gerada no seu teste",
                "Compartilhar dúvidas pontuais no chat da sala"],
               "ONDE BUSCAR SUPORTE",
               ["Chat do Zoom para dúvidas rápidas com o número do passo",
                "Canal da Aula 12 no Discord para colar prints de erro",
                "Mentores da White Cube monitorando as mensagens",
                "Se travar num erro de sintaxe, chame imediatamente",
                "Não tenha medo de errar: faz parte do laboratório"],
               subtitle="Erros de execução são naturais e fazem parte do aprendizado.")
notes(s, "5 min", "ESSENCIAL", EDMAR,
      """
Orientações de suporte e atitude.

"Algumas regras para o nosso laboratório render bem.
Rode sempre as células de cima para baixo. Se você pular para o Passo 3 sem ter rodado
o Passo 2, o Python vai reclamar que X_train não existe.
Onde tiver a marcação TODO, complete o código antes de rodar.
E se aparecer alguma mensagem em vermelho na tela: mantenha a calma. Leia a última linha
do erro. Se não entender, mande no chat dizendo: 'travei no Passo 4 com tal mensagem'.
Os mentores e nós dois estaremos atentos para destravar todo mundo."
""")

# Slide 14: Seção 04
s = sl_section("04", "Bloco D · Mão na massa",
               "45 minutos de código guiado no Google Colab",
               "20h00 às 20h45  ·  45 minutos")
notes(s, "20h00 às 20h02 (2 min)", "ESSENCIAL", FELIPE,
      """
Liberação da turma para a prática. Cronômetro iniciado na tela.

"Valendo, pessoal! Quarenta e cinco minutos de código no Colab.
Nós vamos colocar um cronômetro na tela e acompanhar vocês pelo chat."
""")

# Slide 15: Timeline de marcos de progresso
s = sl_timeline("Marcos de progresso", "Acompanhe seu ritmo durante a prática",
                [("20h15 · 15 min", "Passos 1 e 2 concluídos.\nBaseline ingênuo rodando e split estratificado pronto."),
                 ("20h30 · 30 min", "Passos 3 e 4 concluídos.\nÁrvore treinada, nós desenhados e matriz gerada."),
                 ("20h45 · 45 min", "Passos 5 e 6 concluídos.\nCurva de overfitting plotada e teste de profundidade.")],
                subtitle="Use esses três marcos para calibrar o seu ritmo.")
notes(s, "45 min", "ESSENCIAL", FELIPE,
      """
Roteiro de acompanhamento durante os 45 minutos.

Minuto 0 a 10:  conferir se todo mundo salvou a cópia e rodou o Passo 0 sem problemas.
Minuto 10 a 20: circular nas dúvidas do chat. Focar em quem teve problema com imports.
Minuto 20 a 30: avisar no microfone: "quem já gerou a matriz de confusão, olhe o valor de recall".
Minuto 30 a 40: avisar que faltam 15 minutos e pedir para avançarem para o Passo 5 (overfitting).
Minuto 40 a 45: aviso final de 5 minutos e preparação para a interação no chat.
""")

# Slide 16: Interação no chat
s = sl_interaction("Interação ao vivo", "Compartilhe o primeiro corte da sua árvore",
                   "Qual variável apareceu no nó raiz da sua árvore de decisão?",
                   ["Abra o diagrama gerado na célula do Passo 3",
                    "Olhe a primeira linha dentro da caixa superior (o nó raiz)",
                    "Digite no chat do Zoom o nome da variável (ex: valor ou hora) e o valor de corte",
                    "Veja se o corte que o seu modelo encontrou coincide com o dos colegas"])
notes(s, "5 min", "ESSENCIAL", FELIPE,
      """
Condução da interação no chat após a prática.

"Vamos ver o que as máquinas de vocês descobriram.
Olhem para o diagrama da árvore no Passo 3. Qual foi a variável que o algoritmo escolheu
no primeiro retângulo, lá no topo?
Escrevam no chat: foi valor ou foi hora? E qual foi o número de corte?"

LER 3 OU 4 RESPOSTAS DO CHAT:
"O algoritmo do Lucas cortou em valor menor que trezentos. A da Mariana também.
Isso mostra que mesmo rodando em máquinas separadas, o critério matemático do ganho
de informação convergiu para a mesma regra de negócio."
""")

# Slide 17: Overfitting visual
s = sl_two_col("O teste do overfitting", "O que aconteceu quando a profundidade cresceu?",
               "ÁRVORE CURTA (max_depth = 3)",
               ["Regras simples e fáceis de explicar para a equipe",
                "Desempenho consistente no treino e no teste",
                "O modelo aprende os padrões gerais do negócio",
                "Generaliza com segurança para novas transações"],
               "ÁRVORE LIVRE (max_depth = None)",
               ["Cria centenas de ramos até isolar cada linha",
                "F1 no treino chega perto de 100%",
                "Desempenho no teste despenca bruscamente",
                "O clássico estudante que decorou o gabarito anterior"],
               subtitle="Controlar a profundidade é a diferença entre aprender e apenas decorar.")
notes(s, "5 min", "ESSENCIAL", EDMAR,
      """
Conclusão do experimento de overfitting do Passo 5.

"Olhem para o gráfico de overfitting que vocês acabaram de gerar no Passo 5.
A linha azul do treino sobe até encostar em cem por cento quando a árvore é livre.
Mas a linha vermelha do teste atinge um pico na profundidade três ou quatro e depois
começa a cair.

Isso é a prova visual do que discutimos na segunda-feira: se você deixa a árvore livre,
ela decora o ruído do treino. O estudante que decora as questões da prova anterior tira
dez no simulado e zera a prova oficial quando trocam as perguntas.
Por isso a poda é obrigatória em árvores de decisão."
""")

# Slide 18: Seção 05
s = sl_section("05", "Bloco E · Síntese e encerramento",
               "O que levamos de hoje e a transição de etapa",
               "20h45 às 21h00  ·  15 minutos")
notes(s, "20h45 às 20h48 (3 min)", "ESSENCIAL", EDMAR,
      """
Abertura da síntese final da noite.

"Chegamos ao Bloco E. Vamos amarrar as principais conclusões desta noite e falar sobre
o que vem na reta final do nosso programa."
""")

# Slide 19: 5 ideias para levar
s = sl_bullets("O que a gente viu hoje", "Cinco lições práticas desta noite",
               [("Acurácia isolada não serve para classes desbalanceadas", "um modelo que acerta 98% pode ter zero de recall para fraudes."),
                ("Estratificação no split é obrigatória", "treino e teste precisam ter rigorosamente a mesma proporção da classe rara."),
                ("Árvores de decisão geram regras auditáveis", "cada nó responde a uma pergunta lógica com critérios de negócio claros."),
                ("Erros têm custos financeiros distintos", "falso positivo custa atrito de cliente; falso negativo custa dinheiro perdido."),
                ("Limitar a profundidade evita o overfitting", "podar o modelo garante generalização real para dados futuros.")],
               subtitle="Se você levar essas cinco conclusões, a noite cumpriu o seu objetivo.",
               numbered=True)
notes(s, "4 min", "ESSENCIAL", EDMAR,
      """
Recapitulação numerada em voz alta.

"Cinco ideias para levar da nossa noite de hoje.
A primeira: nunca avaliem problemas de fraude ou evento raro olhando apenas a acurácia.
Segunda: usem sempre amostragem estratificada para dividir treino e teste.
Terceira: a árvore de decisão é a melhor porta de entrada para Machine Learning porque
ela gera regras que qualquer pessoa de negócio consegue auditar.
Quarta: traduzam métricas em dinheiro: falsos positivos e falsos negativos têm impactos
comerciais completamente diferentes.
E quinta: controlem a profundidade para o modelo aprender a pensar, e não apenas a decorar."
""")

# Slide 20: Arco do programa
s = sl_two_col("O arco do programa", "Onde estamos e o que vem pela frente",
               "O QUE VOCÊS JÁ CONSTRUÍRAM",
               ["Mapeamento do problema e métricas no Canvas (Semana 1)",
                "Consultas relacionais e agregações com SQL (Semana 3)",
                "Tratamento e análise de dados com pandas (Semana 4)",
                "Engenharia de dados e pipelines escaláveis (Semana 5)",
                "Treinamento do primeiro modelo de Machine Learning hoje"],
               "A ETAPA 2 QUE SE APROXIMA",
               ["Semana 7: Formação de squads e trabalho em projetos reais",
                "Semana 8: Refinamento das soluções e preparação executiva",
                "Demo Day: Apresentação para a banca da White Cube",
                "Aplicação prática de tudo que vocês aprenderam até aqui"],
               subtitle="Vocês completaram todo o ciclo de fundamentos de dados e IA.")
notes(s, "4 min", "ESSENCIAL", EDMAR,
      """
Ponte institucional e motivação da turma.

"Olhem para a coluna da esquerda. Vocês começaram na Semana 1 aprendendo a estruturar
um problema de negócio sem abrir código.
Passaram por SQL, pandas, pipelines de dados e hoje treinaram o primeiro modelo preditivo.
Vocês percorreram todo o ciclo de vida de uma solução de Inteligência Artificial.

Nas próximas duas semanas, na Etapa 2, vocês vão aplicar esse conjunto de ferramentas
em squads para resolver desafios reais que serão apresentados no Demo Day."
""")

# Slide 21: Q&A Statement
s = sl_statement("Perguntas frequentes",
                 "Perguntas sobre o laboratório?",
                 "Coloque no chat. Os professores e mentores responderão agora e no Discord.")
notes(s, "3 min", "ESSENCIAL", f"{EDMAR} e {FELIPE}",
      """
Perguntas previsíveis da noite de hoje:

• "Por que a árvore escolheu 'valor' e não 'hora' no nó raiz?"
  Porque matematicamente a divisão por valor gerou uma redução maior de impureza
  (maior ganho de informação) do que a divisão por hora naquele ponto específico.

• "Posso usar essa mesma lógica para prever cancelamento de clientes (churn)?"
  Exatamente a mesma. Churn também é um problema de classificação com classes desbalanceadas.

• "Como escolher o melhor max_depth na prática corporativa?"
  Geralmente usamos validação cruzada (GridSearchCV) para testar várias profundidades
  automaticamente e escolher a que obtém o melhor F1 ou recall no conjunto de validação.

• "Os notebooks resolvidos ficarão disponíveis?"
  Sim, o notebook do professor com todos os gabaritos comentados será enviado logo após a aula.
""")

# Slide 22: Closing
s = sl_closing()
notes(s, "1 min", "ESSENCIAL", FELIPE,
      """
Fechamento da aula (30 segundos).

"Parabéns pelo trabalho de hoje! Treinar o primeiro modelo de Machine Learning é um marco
na carreira de qualquer profissional de dados.
Salvem seus notebooks, continuem praticando e nos vemos na segunda-feira.
Boa noite a todos!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Enviar o link do notebook do professor no canal do Discord.
- Realizar retrospectiva de 10 minutos entre Edmar e Felipe sobre onde os alunos mais travaram.
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

out = ROOT / "docs" / "aula-12"
out.mkdir(parents=True, exist_ok=True)
dest = out / "AI-Talent-Academy-Aula12.pptx"
prs.save(dest)
print(f"OK: {dest}  ({_n['i']} slides)  Roboto, sem travessões, tamanho único por bloco.")
