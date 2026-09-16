# -*- coding: utf-8 -*-
"""
Gerador do deck da Aula 11 (Semana 6, segunda-feira) do AI Talent Academy.

Tema: Machine Learning, do baseline ao primeiro modelo. Aula expositiva, sem mao na
massa (a pratica de treinar de verdade fica para a Aula 12, na quinta).

Ponto de partida importante: a Aula 1 ja cobriu, na visao geral das 8 fases, varios
conceitos que um brainstorm ingenuo repetiria aqui: baseline (com a frase "amanha vai
vender o mesmo que hoje"), overfitting (metafora do aluno que decorou a prova), a
armadilha da acuracia (o exemplo de deteccao de fraude com 1 a cada 100 transacoes,
sempre respondendo "nao e fraude", 99% de acuracia e zero fraude detectada), e ate os
nomes precisao/recall/F1, tudo isso na Fase 5 e Fase 6 do pipeline. Este script NAO
repete essas explicacoes. Ele abre com um recap de uma frase e vai direto para o que a
Aula 1 nao teve tempo de cobrir: a matriz de confusao formal com numeros, um algoritmo
de verdade (arvore de decisao, com historia real), metricas de regressao (a Aula 1 nao
cobriu nenhuma), e uma releitura do caso de vies da Aula 1 pela lente de classificador.

Segunda versao deste script, apos feedback do usuario de que a primeira versao estava
rasa demais em fundamentos. Acrescentado o Bloco 03 inteiro, "Como uma maquina aprende
de verdade": o que significa aprender, parametro, funcao de perda (MSE), otimizacao,
gradiente descendente (com a metafora da montanha na neblina e taxa de aprendizado),
treino x inferencia, parametro x hiperparametro, e uma ponte honesta explicando que a
arvore de decisao de hoje NAO usa gradiente descendente (ela decide por escolha gulosa),
enquanto regressao e redes neurais (incluindo os LLMs da Aula 3) usam. A numeracao dos
blocos tambem mudou de letras (A, B, C...) para numeros de dois digitos (01, 02, 03...),
para bater com o padrao ja usado nos scripts anteriores (ver Aula 9).

Identidade visual: padrao White Cube (Roboto, azul 28347B, fundos e logo do template
oficial em assets/whitecube/).

Uso:  python scripts/gerar_slides_aula11.py
Saida: docs/aula-11/AI-Talent-Academy-Aula11.pptx

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
          "Semana 6  ·  Machine Learning", 25, INK, space=0)
    shape(s, ML, Inches(5.75), Inches(2.4), Pt(5), fill=RED)
    block(s, ML, Inches(8.15), Inches(13), Inches(1.0),
          ["Aula 11  ·  Segunda-feira, 19h00 às 00h15  ·  Online",
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
    block(s, ML, Inches(5.85), Inches(14), Inches(0.7), "Voltamos às 22h45 em ponto.", 28,
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

# --------------------------------------------------------------------------
# RECEPÇÃO (19h00 às 19h10)
# --------------------------------------------------------------------------
s = sl_cover()
notes(s, "19h00 às 19h10 (slide de espera)", "ESSENCIAL", EU,
      """
Slide projetado desde 18h55. Fale a cada 2 ou 3 minutos enquanto a sala enche.

"Boa noite! Semana 6, Machine Learning. Enquanto a sala enche, uma pergunta: você já
recebeu uma recomendação de filme, série ou produto que pareceu ler sua mente? Hoje a
gente desmonta como isso funciona por dentro."

Não comece antes de 19h08.
""",
      """
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- Moderador com o link do Discord pronto para colar.
- Sem código ao vivo hoje. A prática de treinar um modelo de verdade é na Aula 12.
""")

s = sl_bullets("Enquanto todo mundo entra", "Hoje a gente desmonta a recomendação que parece ler sua mente",
               [("Áudio e câmera", "microfone no mudo, câmera fica a seu critério"),
                ("Dúvidas", "escreva no chat a qualquer momento, temos moderação acompanhando"),
                ("Gravação", "a aula é gravada e o link chega em até 24h"),
                ("Ainda sem código ao vivo hoje", "os exemplos aparecem no slide, a prática é na quinta"),
                ("Aqueça o teclado", "escreva no chat: que serviço já te recomendou algo certeiro demais?")],
               subtitle="Semana 6, Machine Learning: do baseline ao primeiro modelo.")
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Bem-vindos à Aula 11. Rapidinho: microfone no mudo, câmera à vontade, dúvida no chat
a qualquer momento, aula gravada com link em até 24h.

Hoje é só teoria, igual toda segunda. A prática de treinar um modelo de verdade fica
para quinta-feira.

Enquanto isso, escreve no chat: que serviço já te recomendou um filme, uma música ou
um produto de um jeito que pareceu ler sua mente? Vou usar algumas respostas daqui a
pouco."
""")

# --------------------------------------------------------------------------
# BLOCO 01: Duas fases, de novo, agora a fundo (19h10 às 19h20)
# --------------------------------------------------------------------------
s = sl_section("01", "Duas fases, de novo, agora a fundo",
               "O que a Aula 1 só teve tempo de tocar",
               "19h10 às 19h20  ·  10 minutos")
notes(s, "19h10 às 19h20 (10 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Recap de uma frase por conceito    5 min
  Panorama de hoje                   5 min

Este bloco é deliberadamente curto. Baseline, treino e teste, overfitting e a
armadilha da acurácia já foram ensinados na Aula 1, Fase 5 e Fase 6, com o exemplo do
cancelamento de cliente. Não repita a explicação inteira, só toque o nome e siga.
""")

s = sl_bullets("Lembrando da Aula 1", "Cinco conceitos que vocês já ouviram, numa frase cada",
               [("Baseline", "a solução mais simples que funciona, a régua honesta antes de qualquer modelo"),
                ("Treino e teste", "o modelo aprende com uma parte dos dados e é avaliado numa parte que nunca viu"),
                ("Overfitting", "o aluno que decorou a prova antiga, vai bem no que já viu e mal no que é novo"),
                ("A armadilha da acurácia", "1 fraude a cada 100 transações, sempre dizer \"não é fraude\" acerta 99% e pega zero"),
                ("Precisão, recall, F1", "os nomes que resolvem essa armadilha, ditos na Aula 1 sem entrar na conta")],
               subtitle="Se algum desses cinco soa novo, vale revisar o roteiro da Aula 1 antes de seguir.")
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Rapidíssimo, cinco coisas que vocês já ouviram na Aula 1.

Baseline: a solução mais simples que funciona.

Treino e teste: o modelo é avaliado numa parte dos dados que nunca viu.

Overfitting: o aluno que decorou a prova, vai bem no que já viu e mal no que é novo.

A armadilha da acurácia: o exemplo de detectar fraude, sempre dizer "não é fraude" e
acertar 99% sem pegar nenhuma.

E os nomes precisão, recall e F1, que resolvem essa armadilha.

Hoje a gente não reexplica nada disso. A gente vai direto para o que a Aula 1 não
teve tempo de fazer: a conta de verdade, um algoritmo de verdade, e as métricas para
quando a resposta vira um número em vez de uma categoria."
""")

s = sl_bullets("O panorama de hoje", "Seis coisas novas, em cima do que vocês já sabem",
               [("Como uma máquina aprende de verdade", "função de perda, otimização, gradiente descendente, treino e inferência"),
                ("A matemática da armadilha", "matriz de confusão, com números de verdade, não só os nomes"),
                ("Seu primeiro algoritmo", "árvore de decisão: como ela decide, e por que tem uma história de 1984"),
                ("O cardápio de modelos de hoje", "regressão linear e logística, Naive Bayes, SVM, Random Forest, XGBoost, Stacking"),
                ("Quando a resposta é um número", "métricas de regressão, e o caso do Netflix Prize"),
                ("Quando o modelo aprende o preconceito", "o caso de viés da Aula 1, agora pela lente de um classificador")],
               subtitle="Tudo aplicado ao caso de fraude que vocês já conhecem de cor.")
notes(s, "5 min", "ESSENCIAL", EU,
      """
"O panorama de hoje, em seis blocos: como uma máquina aprende de verdade por
dentro, a matemática por trás da armadilha da acurácia, o primeiro algoritmo de
verdade, um cardápio com os principais modelos que o mercado usa hoje, o que muda
quando a resposta é um número, e o que acontece quando o modelo aprende o
preconceito dos dados.

Tudo usando o caso de fraude em cartão que vocês já conhecem desde a Aula 2. Nada de
exemplo hipotético novo."
""")

# --------------------------------------------------------------------------
# BLOCO 02: Que tipo de problema é esse (19h20 às 19h35)
# --------------------------------------------------------------------------
s = sl_section("02", "Que tipo de problema é esse",
               "Classificação, regressão e clusterização, agora com o caso de fraude",
               "19h20 às 19h35  ·  15 minutos")
notes(s, "19h20 às 19h35 (15 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Recap rápido dos três tipos    4 min
  Mapeando no caso de fraude     6 min
  Interação                      5 min
""")

s = sl_bullets("Recap rápido", "Os três tipos que a Fase 5 da Aula 1 já nomeou",
               [("Classificação", "a resposta é uma categoria: fraude ou não, contestada ou não"),
                ("Regressão", "a resposta é um número: preço, tempo, valor"),
                ("Clusterização", "não existe rótulo, o objetivo é achar grupos parecidos sozinho")],
               subtitle="Supervisionado tem rótulo conhecido (classificação e regressão). Clusterização não.")
notes(s, "4 min", "ESSENCIAL", EU,
      """
"A Fase 5 da Aula 1 já deu os três nomes. Classificação: resposta é categoria.
Regressão: resposta é número. Clusterização: não tem rótulo, é achar grupo sozinho.

Hoje a gente não fica na definição. A gente aplica isso no caso de fraude."
""")

s = sl_cards("Aplicando no caso de fraude", "A mesma base, três perguntas diferentes",
             [("Classificação",
               "\"Esta transação vai ser contestada?\"\n\nRótulo conhecido: cada transação já tem um status, aprovada, recusada ou contestada."),
              ("Regressão",
               "\"Quanto este cliente vai gastar no próximo mês?\"\n\nAqui a resposta é sempre um número, um valor em reais."),
              ("Clusterização",
               "\"Que grupos de cliente existem, sem eu definir antes?\"\n\nNão supervisionado: ninguém rotulou os grupos com antecedência.")],
             cols=3, card_h=4.2)
notes(s, "6 min", "ESSENCIAL", EU,
      """
"A mesma base de fraude serve para os três tipos, dependendo da pergunta.

Classificação: esta transação vai ser contestada? O rótulo já existe na coluna
status.

Regressão: quanto este cliente vai gastar no próximo mês? Aqui a resposta é um
número.

Clusterização: que grupos de cliente existem, sem eu ter definido antes? Aqui
ninguém rotulou nada, o algoritmo tem que achar sozinho.

Hoje a gente fica principalmente em classificação, porque é o problema do caso de
fraude, mas os três merecem estar no seu vocabulário."
""")

s = sl_interaction("Interação rápida", "Classificação, regressão ou clusterização?",
                    "No chat: para cada cenário, escreva C, R ou CL",
                    ["\"Esta imagem tem um gato ou um cachorro?\"",
                     "\"Quantos graus vai fazer amanhã?\"",
                     "\"Quais desses clientes se parecem entre si, sem eu saber por quê?\"",
                     "\"Este e-mail é spam?\""])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"No chat: para cada cenário que eu vou ler, escreva C de classificação, R de
regressão ou CL de clusterização.

Gato ou cachorro? Classificação.
Quantos graus vai fazer amanhã? Regressão.
Quais clientes se parecem, sem eu saber por quê? Clusterização.
Este e-mail é spam? Classificação.

Reparem: "gato ou cachorro" e "spam ou não" são o mesmo tipo de problema, mesmo
sendo de áreas completamente diferentes. Isso é o poder de pensar em tipos de
problema, não em domínios."
""")

# --------------------------------------------------------------------------
# BLOCO 03: Como uma máquina aprende de verdade (19h35 às 20h10)
# --------------------------------------------------------------------------
s = sl_section("03", "Como uma máquina aprende de verdade",
               "Parâmetro, perda, otimização e gradiente descendente, sem fórmula assustadora",
               "19h35 às 20h10  ·  35 minutos")
notes(s, "19h35 às 20h10 (35 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  O que significa aprender, e o exemplo mínimo    6 min
  Função de perda                                 6 min
  Otimização e gradiente descendente             12 min
  Treino, inferência, parâmetro e hiperparâmetro   7 min
  Ponte para a árvore de decisão de hoje           4 min

Este é o bloco que a turma pediu de volta: sem ele, "Machine Learning" vira um nome
para "escolher a métrica certa", sem explicar o mecanismo por trás do aprendizado.
Vá devagar aqui, é o bloco mais denso tecnicamente da aula inteira.
""")

s = sl_statement("O que significa aprender, para uma máquina",
                 "Aprender não é entender.\nÉ ajustar números até errar menos.",
                 "Isso vale para árvore de decisão, regressão e até para os LLMs da Aula 3.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Até agora falamos de classificação, regressão, precisão, recall. Mas ninguém
explicou o que significa, por dentro, uma máquina "aprender". É isso que fecha
hoje.

Para uma máquina, aprender significa só uma coisa: ajustar um conjunto de números
repetidamente, até o modelo errar menos nos exemplos que ele já viu. Nenhuma
compreensão envolvida. Vamos ver com um exemplo mínimo."
""")

s = sl_code("Um exemplo mínimo", "Prever o valor de uma transação, a partir de uma variável só",
            ["valor_previsto = a × horário_da_transação + b",
             "",
             "# \"aprender\" = encontrar os melhores valores de a e b,",
             "# os que erram menos nos dados que o modelo já viu"],
            [("a e b são os parâmetros do modelo", "os únicos números que o treino vai mexer"),
             ("Antes do treino, a e b começam em qualquer valor", "geralmente aleatório, o modelo começa \"burro\" de propósito"),
             ("Depois do treino, a e b ficam fixos", "e essa reta passa a ser o modelo inteiro")])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Exemplo mínimo, de propósito simples demais para a base de fraude real, só para
mostrar o mecanismo.

Quero prever o valor de uma transação a partir do horário. A fórmula é uma reta:
valor previsto igual a "a" vezes horário, mais "b".

"a" e "b" são os parâmetros. São os únicos números que o treino vai mexer. Antes de
treinar, eles começam em qualquer valor, geralmente aleatório, o modelo começa
"burro" de propósito. Depois do treino, "a" e "b" ficam fixos, e essa reta vira o
modelo inteiro."
""")

s = sl_bullets("Como medir o erro", "A função de perda",
               [("Para cada exemplo, compare o valor previsto com o valor real", "a diferença entre os dois é o erro daquele exemplo"),
                ("Eleve essa diferença ao quadrado", "erro grande pesa muito mais que erro pequeno, de propósito"),
                ("Tire a média de todos os exemplos", "isso tem nome: MSE, erro quadrático médio"),
                ("Quanto menor a perda, melhor o modelo está indo", "e o objetivo do treino inteiro é só isso: diminuir esse número")],
               subtitle="A raiz do MSE é exatamente o RMSE que vocês vão ver daqui a pouco, no bloco de regressão.")
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Como saber se "a" e "b" estão bons? Precisa de um número que resuma o quão errado
o modelo está. Isso é a função de perda.

Para cada exemplo, compare o valor previsto com o valor real, isso dá o erro daquele
exemplo. Eleve ao quadrado, de propósito: um erro de 100 pesa muito mais que dez
erros de 10 cada. Tire a média de todos os exemplos. Isso tem nome, MSE, erro
quadrático médio.

Quanto menor a perda, melhor o modelo. E aqui está a ideia central do bloco inteiro:
treinar um modelo é, do início ao fim, só isso: encontrar os parâmetros que deixam
essa perda a mais baixa possível.

E reparem no nome: a raiz quadrada do MSE é exatamente o RMSE que vocês vão ver daqui
a pouco. Mesma conta, dois nomes diferentes."
""")

s = sl_bullets("Da pergunta ao processo", "Otimização: buscar os parâmetros que erram menos",
               [("Não é tentar valores de \"a\" e \"b\" ao acaso", "com milhões de combinações possíveis, tentativa aleatória nunca converge a tempo"),
                ("Existe um jeito inteligente de buscar", "a própria função de perda aponta para qual direção cada parâmetro deveria mudar"),
                ("Esse processo de busca inteligente tem nome", "gradiente descendente, o algoritmo por trás da maioria dos modelos que aprendem com dados")])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Encontrar os melhores "a" e "b" é um problema de busca. E não dá para tentar ao
acaso, são infinitas combinações possíveis.

A boa notícia: a função de perda não é só um número, ela também aponta uma direção.
Para cada parâmetro, dá para calcular "se eu aumentar um pouquinho, a perda sobe ou
desce?". Isso guia a busca. Esse processo tem nome: gradiente descendente."
""")

s = sl_statement("O algoritmo por trás do ajuste",
                 "Você está numa montanha, na neblina.\nSó sente, com os pés, para que lado\no chão desce mais rápido.",
                 "A cada passo, ande nessa direção. Repita até não conseguir descer mais.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"A metáfora que fica: você está numa montanha coberta de neblina. Não enxerga o
vale lá embaixo. A única informação que você tem é o chão debaixo dos seus pés: para
que lado ele desce mais rápido agora.

Você dá um passo nessa direção. Sente de novo. Dá outro passo. Repete isso centenas,
milhares de vezes, até chegar a um ponto onde qualquer passo te faz subir, não
descer mais. Você chegou perto do fundo do vale.

Gradiente descendente é exatamente isso, só que o "vale" é a função de perda, e os
"seus pés" são a derivada dela em cada parâmetro."
""")

s = sl_bullets("Gradiente descendente, sem neblina", "O que a máquina faz de verdade, passo a passo",
               [("A cada passo, calcula a direção que mais reduz a perda", "para cada parâmetro, isso é o \"gradiente\""),
                ("Ajusta cada parâmetro um pouco, nessa direção", "não tudo de uma vez, só um passo pequeno"),
                ("Repete isso milhares de vezes", "até a perda parar de cair de forma relevante"),
                ("Taxa de aprendizado: o tamanho de cada passo", "passo grande demais pula o vale e nunca estabiliza. Passo pequeno demais, o treino demora uma eternidade")],
               subtitle="Taxa de aprendizado é o primeiro hiperparâmetro que vocês acabaram de conhecer.")
notes(s, "6 min", "ESSENCIAL, o coração técnico do bloco", EU,
      """
Vá devagar aqui, é o ponto mais denso da aula inteira.

"Passo a passo, sem neblina agora.

A cada passo, o algoritmo calcula, para cada parâmetro, em que direção mudá-lo
reduz a perda. Isso é o gradiente.

Ajusta cada parâmetro um pouquinho nessa direção. Não tudo de uma vez, um passo
pequeno.

Repete isso milhares de vezes, recalculando a cada rodada, até a perda parar de cair
de um jeito que valha a pena continuar.

E o tamanho de cada passo tem nome: taxa de aprendizado. Se o passo é grande demais,
o modelo pula o fundo do vale e fica oscilando, nunca estabiliza. Se o passo é
pequeno demais, o treino converge, mas demora uma eternidade, às vezes mais tempo do
que alguém tem paciência de esperar."
""")

s = sl_two_col("Duas fases muito diferentes", "Treinamento e inferência",
               "TREINAMENTO",
               ["Repetir o gradiente descendente sobre os dados de treino",
                "Ajustar os parâmetros a cada passo",
                "É a parte lenta e cara, pode levar horas ou dias",
                "Acontece uma vez, ou de tempos em tempos, no retreino"],
               "INFERÊNCIA",
               ["Usar o modelo já treinado, com os parâmetros fixos",
                "Nenhum parâmetro muda nesse momento",
                "É rápido, é só aplicar a fórmula já pronta",
                "Acontece toda vez que alguém usa o modelo"],
               subtitle="Todo modelo em produção vive fazendo inferência a maior parte do tempo. Treinar é raro.")
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Duas fases bem diferentes, e é comum confundir os nomes.

Treinamento é repetir o gradiente descendente sobre os dados que o modelo tem
disponível, ajustando os parâmetros a cada passo. É lento e caro, pode levar de
minutos a dias, dependendo do modelo. E não acontece toda hora: acontece uma vez, ou
de tempos em tempos, quando alguém decide retreinar.

Inferência é usar o modelo já treinado, com os parâmetros já fixos, para prever um
caso novo. Nenhum parâmetro muda nesse momento, é só aplicar a fórmula pronta. É
rápido, e acontece toda vez que alguém usa o modelo.

Quando vocês usam qualquer app com IA no dia a dia, é inferência que está
acontecendo. O treinamento já aconteceu bem antes, em algum servidor, uma vez."
""")

s = sl_bullets("Duas categorias de número, fáceis de confundir", "Parâmetro e hiperparâmetro",
               [("Parâmetro", "o que o modelo aprende sozinho, durante o treino: \"a\", \"b\", os pesos de uma rede neural"),
                ("Hiperparâmetro", "escolha humana, feita ANTES do treino começar: taxa de aprendizado, quantos passos dar, profundidade máxima de uma árvore"),
                ("Ninguém treina um modelo sem escolher hiperparâmetro primeiro", "e escolher mal pode fazer o treino nunca convergir")])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Uma distinção que vocês vão ouvir o resto do programa: parâmetro e hiperparâmetro.

Parâmetro é o que o modelo aprende sozinho, durante o treino. "a" e "b" do nosso
exemplo, ou os pesos de uma rede neural.

Hiperparâmetro é escolha humana, feita antes do treino começar. Taxa de
aprendizado é um hiperparâmetro. Quantos passos dar é outro. Profundidade máxima de
uma árvore, que vocês vão ver daqui a pouco, também é.

Ninguém treina um modelo sem escolher hiperparâmetro primeiro. E escolher mal pode
fazer o treino nunca convergir, ou convergir devagar demais para ser útil."
""")

s = sl_bullets("E a árvore de decisão de hoje?", "Ela não usa nada disso",
               [("A árvore de decisão não tem função de perda contínua", "e não usa gradiente descendente"),
                ("Ela decide de outro jeito: escolha gulosa", "a cada pergunta, escolhe a que melhor separa os dados, sem calcular direção nenhuma"),
                ("Gradiente descendente fica para outra família de modelo", "regressão linear, regressão logística, e redes neurais, incluindo os LLMs da Aula 3"),
                ("Existe mais de um jeito de aprender", "vocês acabaram de ver dois: o guloso, de hoje, e o gradual, que vai reaparecer o resto do programa")],
               subtitle="Guardem essa distinção: nem todo modelo aprende do mesmo jeito.")
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Um aviso importante antes de ver a árvore de decisão: tudo que vimos agora, função
de perda, gradiente descendente, taxa de aprendizado, NÃO é como uma árvore de
decisão aprende.

A árvore decide de outro jeito, chamado escolha gulosa: a cada pergunta, ela testa
várias divisões possíveis dos dados e escolhe a que separa melhor fraude de não
fraude, sem calcular gradiente nenhum, sem função de perda contínua.

Gradiente descendente é o mecanismo por trás de outra família de modelo: regressão
linear, regressão logística, e redes neurais, incluindo os LLMs que vocês viram na
Aula 3.

Vocês acabaram de conhecer os dois grandes jeitos de uma máquina aprender. A árvore
de hoje usa um. O resto do programa vai reencontrar o outro."
""")

# --------------------------------------------------------------------------
# BLOCO 04: A matemática por trás da armadilha (20h10 às 20h40)
# --------------------------------------------------------------------------
s = sl_section("04", "A matemática por trás da armadilha",
               "A Aula 1 deu o exemplo. Hoje a gente faz a conta",
               "20h10 às 20h40  ·  30 minutos")
notes(s, "20h10 às 20h40 (30 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Recap de uma frase                 2 min
  Matriz de confusão                 8 min
  Precisão e recall, com a conta    10 min
  F1                                  5 min
  Interação                          5 min

Este é o bloco mais denso da aula. Reserve o tempo e não deixe a interação do final
ser cortada, ela é o gancho para o trade-off de negócio.
""")

s = sl_statement("Lembrando",
                 "1 em 100 é fraude. Dizer \"nunca é fraude\"\nacerta 99% e não pega nenhuma.",
                 "Exemplo da Aula 1, Fase 6. Hoje a gente vê a máquina por trás disso.")
notes(s, "2 min", "ESSENCIAL", EU,
      """
"Vocês já ouviram isso na Aula 1. Hoje a gente vê a máquina por trás desse número."
""")

s = sl_table("A matriz de confusão", "Quatro números que substituem um só",
             ["", "Modelo disse fraude", "Modelo disse não é fraude"],
             [["Era fraude de verdade", "Verdadeiro positivo (VP)", "Falso negativo (FN)"],
              ["Não era fraude", "Falso positivo (FP)", "Verdadeiro negativo (VN)"]],
             subtitle="Toda avaliação de classificação começa preenchendo esta tabela.",
             widths=[0.34, 0.33, 0.33])
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Isto aqui é a matriz de confusão. Quatro números, não um só.

Verdadeiro positivo: era fraude, o modelo disse fraude. Acertou.

Falso negativo: era fraude, o modelo disse que não era. Errou, e esse erro é caro:
uma fraude passou.

Falso positivo: não era fraude, o modelo disse que era. Errou, e esse erro incomoda
um cliente honesto.

Verdadeiro negativo: não era fraude, o modelo disse que não era. Acertou.

Acurácia junta os quatro números numa conta só, e é exatamente por isso que ela
engana: ela não separa qual tipo de erro está acontecendo."
""")

s = sl_bullets("Um exemplo com números", "1.000 transações testadas, 20 são fraude de verdade",
               [("Verdadeiro positivo: 12", "fraudes que o modelo pegou"),
                ("Falso negativo: 8", "fraudes que passaram batido"),
                ("Falso positivo: 30", "transações normais que o modelo assustou"),
                ("Verdadeiro negativo: 950", "transações normais que o modelo deixou passar, corretamente")],
               subtitle="Acurácia deste modelo: (12 + 950) dividido por 1.000, ou seja, 96,2%.")
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Exemplo ilustrativo, com números redondos, não é resultado real, isso vocês vão
medir de verdade na quinta.

1.000 transações, 20 são fraude de verdade. O modelo pegou 12 (verdadeiro positivo),
deixou passar 8 (falso negativo), assustou 30 clientes honestos (falso positivo), e
acertou 950 transações normais (verdadeiro negativo).

Acurácia: 962 dividido por 1.000, 96,2%. Parece ótimo. Vamos ver o que precisão e
recall dizem sobre o mesmo modelo."
""")

s = sl_bullets("Precisão e recall, com a conta", "As duas perguntas que a acurácia não responde",
               [("Precisão: 12 dividido por 42", "das vezes que eu disse fraude (12 + 30 = 42), quantas eram mesmo? 28,6%"),
                ("Recall: 12 dividido por 20", "das fraudes reais (12 + 8 = 20), quantas eu peguei? 60%")],
               subtitle="96,2% de acurácia, 28,6% de precisão, 60% de recall. Três fotos do mesmo modelo.")
notes(s, "10 min", "ESSENCIAL", EU,
      """
"Precisão: das vezes que o modelo gritou fraude, quantas eram mesmo? 12 acertos
dividido por 42 alarmes totais (12 verdadeiros mais 30 falsos), 28,6%. Ou seja, mais
de 7 em cada 10 alarmes deste modelo são falsos.

Recall: das 20 fraudes que existiam de verdade, quantas o modelo pegou? 12 dividido
por 20, 60%. Ou seja, 4 em cada 10 fraudes passam batido.

Reparem: acurácia de 96,2% escondeu os dois problemas. Um modelo que parecia ótimo
tem quase três quartos de alarme falso, e ainda deixa passar 40% das fraudes."
""")

s = sl_bullets("F1, o equilíbrio entre os dois", "Uma métrica só, quando você precisa de um número",
               [("F1 é a média harmônica de precisão e recall", "não a média simples, ela pune mais quando um dos dois é muito baixo"),
                ("Neste exemplo, F1 fica perto de 38,7%", "bem mais baixo que a acurácia de 96,2%, e mais honesto sobre o modelo"),
                ("F1 serve para comparar modelos", "quando você não quer escolher entre olhar só precisão ou só recall")],
               subtitle="F1 não substitui a decisão de negócio. Só resume duas métricas numa.")
notes(s, "5 min", "ESSENCIAL", EU,
      """
"F1 junta precisão e recall numa métrica só, mas não pela média simples. É a média
harmônica dos dois, que pune mais forte quando um deles está muito baixo.

Neste exemplo, F1 fica perto de 38,7%. Muito mais honesto que os 96,2% de acurácia
sobre o mesmo modelo.

F1 é útil quando você precisa de um número só para comparar modelos. Mas ele não
decide sozinho o que importa mais para o seu negócio, precisão ou recall. Isso é a
próxima pergunta."
""")

s = sl_interaction("Trade-off de negócio", "Precisão ou recall: o que dói mais para um banco?",
                    "No chat: escolha um lado e diga por quê",
                    ["Errar bloqueando uma compra honesta (perde precisão)",
                     "Errar deixando passar uma fraude de verdade (perde recall)",
                     "A resposta muda se o produto for cartão de crédito ou empréstimo?",
                     "Não existe resposta certa única, é decisão de negócio"])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Pergunta para o chat: o que dói mais para um banco, bloquear uma compra honesta por
engano, ou deixar passar uma fraude de verdade?

Não existe resposta certa universal. Um banco de cartão pré-pago, com cliente
sensível a fricção, pode preferir menos bloqueio (mais recall, menos precisão). Uma
operação de empréstimo, com prejuízo alto por fraude confirmada, pode preferir o
contrário.

Essa decisão nunca é só técnica. É decisão de negócio, e quem escolhe a métrica
está, na prática, escolhendo essa resposta."
""")

# --------------------------------------------------------------------------
# BLOCO 05: Seu primeiro modelo (20h40 às 21h10)
# --------------------------------------------------------------------------
s = sl_section("05", "Seu primeiro modelo",
               "A árvore de decisão, o algoritmo que vocês vão treinar na quinta",
               "20h40 às 21h10  ·  30 minutos")
notes(s, "20h40 às 21h10 (30 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  História, CART e ID3       6 min
  Como ela decide            10 min
  Por que é fácil de explicar 6 min
  Feature engineering         8 min
""")

s = sl_timeline("Uma ferramenta com história", "A árvore de decisão não nasceu ontem",
                [("1984", "CART\nLeo Breiman e colegas publicam o livro que formaliza a árvore de decisão"),
                 ("1986", "ID3\nRoss Quinlan publica outro algoritmo de árvore, de uma vertente diferente"),
                 ("Hoje", "Random Forest, XGBoost\nJuntam centenas de árvores para decidir em conjunto, ainda mais fortes")])
notes(s, "6 min", "ESSENCIAL", EU,
      """
"A árvore de decisão tem quatro décadas. Em 1984, o estatístico Leo Breiman e
colegas publicaram o livro que formalizou o CART, Classification And Regression
Trees, o nome já entrega os dois usos: classificação e regressão.

Em 1986, Ross Quinlan publicou o ID3, outra família de árvore, de uma linha de
pesquisa diferente.

E hoje, os algoritmos mais fortes do mercado, Random Forest e XGBoost, não abandonam
a árvore: eles juntam centenas delas para decidir em conjunto. Entender uma árvore
sozinha é a porta de entrada para entender os dois."
""")

s = sl_pipeline("Como ela decide", "Um caminho possível, sobre o caso de fraude",
                [(1, "O valor passa de R$500?", "Se não, aprovada. Se sim, segue para a próxima pergunta."),
                 (2, "O horário é de madrugada?", "Entre 1h e 5h. Se não, aprovada. Se sim, segue adiante."),
                 (3, "O país é diferente do Brasil?", "Se não, aprovada. Se sim, marca como suspeita.")],
                per_row=3,
                subtitle="A árvore de verdade testa várias perguntas ao mesmo tempo. Isto é só um caminho, para entender a ideia.")
notes(s, "10 min", "ESSENCIAL", EU,
      """
"Uma árvore de decisão é uma sequência de perguntas sim ou não, aprendidas a partir
dos dados, não escritas por uma pessoa.

Valor passa de R$500? Se não, aprovada. Se sim, próxima pergunta.

Horário de madrugada, entre 1h e 5h? Se não, aprovada. Se sim, próxima.

País diferente do Brasil? Se sim, marca como suspeita.

Importante: isto é só UM caminho, para dar a intuição. Uma árvore de verdade tem
várias perguntas em cada ponto, e vários caminhos possíveis, formando de fato uma
árvore que se ramifica. O algoritmo escolhe sozinho quais perguntas fazer, e em qual
ordem, testando qual pergunta separa melhor fraude de não fraude nos dados de
treino."
""")

s = sl_bullets("Por que é fácil de explicar", "A vantagem que nem todo modelo tem",
               [("Cada decisão é auditável", "dá para mostrar exatamente quais perguntas levaram a uma transação ser marcada"),
                ("Não é uma caixa preta", "um analista de risco consegue ler e questionar o caminho, pergunta por pergunta"),
                ("Isso importa legalmente", "decisões automatizadas que afetam pessoas muitas vezes precisam ser explicáveis"),
                ("O custo: sozinha, uma árvore erra mais", "por isso o mercado combina centenas delas em Random Forest e XGBoost")],
               subtitle="Em crédito, seguro e saúde, explicabilidade costuma ser exigência legal.")
notes(s, "6 min", "ESSENCIAL", EU,
      """
"A grande vantagem da árvore: cada decisão é auditável. Dá para mostrar exatamente
qual sequência de perguntas levou a uma transação ser marcada como suspeita. Não é
caixa preta.

Isso não é só elegância técnica. Em crédito, seguro e saúde, decisão automatizada que
afeta uma pessoa muitas vezes precisa ser explicável, às vezes por exigência legal.

O custo: uma árvore sozinha erra mais do que os modelos mais sofisticados de hoje.
Por isso o mercado combina centenas delas, Random Forest, XGBoost, trocando um pouco
de explicabilidade por mais acerto."
""")

s = sl_cards("Feature engineering", "Transformar coluna bruta em pergunta boa",
             [("Data e hora crua",
               "Vira \"é madrugada?\", \"é fim de semana?\"\n\nA árvore decide melhor com perguntas binárias do que com um timestamp inteiro."),
              ("Valor da transação",
               "Vira faixas: até R$50, R$50 a R$500, acima de R$500.\n\nMesma técnica que a Aula 7 já ensinou em pandas, agora alimentando um modelo."),
              ("País da transação",
               "Vira \"é Brasil?\" (sim ou não)\n\nUma coluna de texto com cinco valores possíveis vira uma pergunta binária simples.")],
             cols=3, card_h=4.2)
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Feature engineering é transformar a coluna bruta numa pergunta que o modelo
consegue usar bem.

Data e hora inteira não ajuda muito. "É madrugada?" ajuda demais.

Valor contínuo funciona, mas faixas (até R$50, R$50 a R$500, acima de R$500) às
vezes revelam um padrão mais claro para a árvore encontrar.

País com cinco valores possíveis vira uma pergunta binária, "é Brasil?", que é
exatamente o tipo de pergunta que uma árvore faz.

Reparem: isso é a mesma técnica de transformação de coluna que a Aula 7 já ensinou
em pandas. O que muda agora é só o destino: essa coluna vai alimentar um modelo."
""")

# --------------------------------------------------------------------------
# BLOCO 06: O cardápio de modelos de hoje (21h10 às 21h35)
# --------------------------------------------------------------------------
s = sl_section("06", "O cardápio de modelos de hoje",
               "Oito nomes que vocês vão ouvir o resto da carreira, cada um com a própria história",
               "21h10 às 22h30  ·  80 minutos")
notes(s, "21h10 às 22h30 (80 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Por que tantos nomes           2 min
  Regressão Linear                6 min
  Regressão Logística             6 min
  Naive Bayes                     6 min
  SVM                             6 min
  Árvore de Decisão, recap        2 min
  Random Forest                   6 min
  XGBoost                         6 min
  Stacking                        5 min
  Redes Neurais                  19 min
  Duas tabelas de resumo          6 min
  De volta ao Bloco 03            9 min

Bloco muito acrescentado a pedido do usuário, para a aula não ficar só em métrica e
árvore, e depois aprofundado de novo para incluir Redes Neurais. Tempo aproximado,
não cronometrado com rigor desta vez.
""")

s = sl_bullets("Antes de começar", "Pensem em Machine Learning como uma caixa de ferramentas",
               [("Cada modelo nasceu resolvendo um problema, numa década diferente", "estatística do século 19, guerra fria, crescimento de e-commerce, competição de dados"),
                ("Nenhum modelo vence em tudo", "o que muda é o formato do dado, o tamanho da base, e se explicar a decisão importa"),
                ("Oito nomes a seguir, cada um com a própria história", "todos cabem no mesmo cardápio, nenhum é mais avançado que o outro por definição")])
notes(s, "2 min", "ESSENCIAL", EU,
      """
"Antes de entrar nos oito nomes: pensem em Machine Learning como uma caixa de
ferramentas cheia de algoritmos diferentes. Cada modelo que vocês vão ver nasceu
resolvendo um problema, numa década diferente, às vezes num contexto bem distante
de dados.

Nenhum vence em tudo. O que muda é o formato do dado, o tamanho da base, e se
explicar a decisão importa tanto quanto acertar."
""")

s = sl_timeline("Uma ferramenta com história", "Regressão Linear: dois séculos de disputa e batismo",
                [("1805", "Legendre\nPublica o método dos mínimos quadrados, e dá esse nome"),
                 ("1809", "Gauss\nReivindica ter usado o mesmo método desde 1795, os dois brigam pela prioridade"),
                 ("1886", "Galton\nEstuda altura de pais e filhos, e batiza o fenômeno de \"regressão\"")])
notes(s, "3 min", "DESCARTÁVEL, corte primeiro se faltar tempo", EU,
      """
"Regressão Linear é o modelo mais antigo da lista, e tem uma história com direito
a briga.

Em 1805, o matemático francês Legendre publica o método dos mínimos quadrados, e dá
esse nome a ele.

Em 1809, Gauss publica um livro reivindicando ter usado o mesmo método desde 1795,
antes de Legendre. Os dois brigaram pela prioridade da descoberta.

E em 1886, Francis Galton, estudando a altura de pais e filhos, percebe um padrão
(filhos de pais muito altos tendem a ser um pouco mais baixos que o pai, filhos de
pais baixos tendem a ser um pouco mais altos) e batiza esse fenômeno de "regressão".
É de onde vem o nome que a gente usa até hoje."
""")

s = sl_bullets("Regressão Linear, na prática", "O exemplo mínimo do Bloco 03, com nome",
               [("O mecanismo já é familiar", "ajusta uma reta, ou um plano com mais variáveis, que minimiza o erro, por gradiente descendente"),
                ("No caso de fraude", "prever quanto uma próxima transação vai valer, a partir do histórico do cliente"),
                ("Quando usar", "quando a relação entre variável e resposta é aproximadamente uma linha reta"),
                ("Limitação", "assume linearidade, e é sensível a valores extremos puxando a reta para o lado errado")],
               subtitle="É o modelo mais simples da lista, e ainda assim um dos mais usados no mercado.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Na prática, Regressão Linear é o exemplo mínimo que vocês já viram no Bloco 03, só
que agora com o nome certo.

No caso de fraude, um uso real seria prever quanto a próxima transação de um
cliente vai valer, a partir do histórico dele.

Usa quando a relação é aproximadamente uma linha reta. E cuidado com valores
extremos: um outlier pode puxar a reta inteira para o lado errado."
""")

s = sl_statement("Uma ferramenta com história",
                 "Uma curva desenhada em 1838\npara crescimento populacional\nhoje decide se é fraude",
                 "A curva logística, de Pierre François Verhulst. Repaginada pela estatística no século 20.")
notes(s, "3 min", "DESCARTÁVEL, corte primeiro se faltar tempo", EU,
      """
"Regressão Logística usa uma curva que não nasceu para classificação nenhuma. Em
1838, o matemático belga Pierre François Verhulst desenhou essa curva para
descrever crescimento populacional, o jeito como uma população cresce rápido no
início e desacelera quando se aproxima de um limite.

Só no século 20 a estatística pegou essa mesma curva emprestada para outro
problema: transformar qualquer número numa probabilidade entre 0 e 1. E o nome
"regressão logística" ficou, mesmo o uso sendo classificação, não regressão."
""")

s = sl_bullets("Regressão Logística, na prática", "Regressão no nome, classificação na prática",
               [("Mesma lógica da linear, com uma curva no final", "o resultado passa pela função sigmoide, e vira um número entre 0 e 1"),
                ("Esse número é uma probabilidade", "acima de um ponto de corte, geralmente 0,5, a resposta vira \"sim\""),
                ("No caso de fraude", "a probabilidade de uma transação ser contestada, não só um \"sim\" ou \"não\" seco"),
                ("Quando usar", "quando a probabilidade importa tanto quanto a categoria final")])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Na prática, Regressão Logística parte do mesmo mecanismo da linear, ajuste de
parâmetro por gradiente descendente, só que o resultado passa por uma curva
(sigmoide) que vira uma probabilidade entre 0 e 1.

No caso de fraude, em vez de só dizer "fraude" ou "não fraude", ela devolve, por
exemplo, "82% de chance de ser contestada". Isso é mais útil quando alguém no time
de risco precisa decidir com que confiança agir."
""")

s = sl_statement("Uma ferramenta com história",
                 "Um teorema publicado em 1763,\ndois anos depois da morte\nde quem o descobriu",
                 "Thomas Bayes. Seu amigo Richard Price publicou o trabalho, postumamente.")
notes(s, "2 min", "DESCARTÁVEL, corte primeiro se faltar tempo", EU,
      """
"Naive Bayes carrega o nome de Thomas Bayes, o reverendo e matemático inglês que
descreveu o teorema que leva o nome dele. Ele nunca publicou esse trabalho em vida:
morreu em 1761, e foi um amigo, Richard Price, quem organizou e publicou o teorema,
em 1763."
""")

s = sl_bullets("Naive Bayes, na prática", "Por que \"ingênuo\"",
               [("Calcula a probabilidade de cada classe pelo Teorema de Bayes", "usando a frequência de cada variável já vista nos dados de treino"),
                ("É \"ingênuo\" porque assume que as variáveis são independentes entre si", "na prática quase nunca são, mas o modelo funciona bem mesmo assim"),
                ("No caso de fraude", "estimar a chance de fraude a partir de canal, horário e faixa de valor, combinados"),
                ("Quando usar", "classificação de texto, como filtro de spam, poucos dados, e quando velocidade de treino importa")])
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Naive Bayes calcula a probabilidade de cada classe usando o teorema de Bayes,
combinando a frequência de cada variável nos dados de treino.

O apelido "ingênuo" vem de uma simplificação: o modelo assume que as variáveis são
independentes entre si, canal, horário e valor não teriam relação nenhuma uns com
os outros. Na vida real quase nunca é bem assim, mas o modelo continua funcionando
surpreendentemente bem, e é muito mais rápido de treinar do que assumir todas as
relações reais entre variáveis."
""")

s = sl_timeline("Uma ferramenta com história", "SVM: da União Soviética ao mainstream",
                [("Anos 1960", "Vapnik\nLança as primeiras ideias ainda na União Soviética, na tese de doutorado"),
                 ("1992", "Kernel trick\nBoser, Guyon e Vapnik ensinam o SVM a separar classes que não formam uma linha reta"),
                 ("1995", "Margem suave\nCortes e Vapnik publicam a versão que o mercado usa até hoje")])
notes(s, "3 min", "DESCARTÁVEL, corte primeiro se faltar tempo", EU,
      """
"SVM, Máquinas de Vetores de Suporte, tem raiz na Guerra Fria. Vladimir Vapnik
lançou as primeiras ideias ainda na União Soviética, nos anos 1960, na própria tese
de doutorado.

Em 1992, já nos Estados Unidos, Boser, Guyon e Vapnik publicam o "kernel trick",
uma forma de o SVM separar classes que não formam uma linha reta.

E em 1995, Cortes e Vapnik publicam a versão de margem suave, mais tolerante a
ruído, que é essencialmente a versão que o mercado usa até hoje."
""")

s = sl_bullets("SVM, na prática", "A fronteira com a maior margem possível",
               [("Busca a linha, ou plano, que separa as classes", "e escolhe, entre as infinitas linhas possíveis, a que fica mais longe dos pontos mais próximos de cada lado"),
                ("Esses pontos mais próximos têm nome", "vetores de suporte, são eles que definem a fronteira, o resto dos pontos nem entra na conta"),
                ("Quando usar", "bases pequenas ou médias, com muitas colunas"),
                ("Limitação para o caso de fraude", "não é a primeira escolha para 1 milhão de linhas, o treino fica pesado nessa escala")])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Na prática, SVM busca a fronteira com a maior margem possível entre as classes.
Os pontos mais próximos da fronteira de cada lado se chamam vetores de suporte, e
são só eles que definem onde a linha fica, o resto dos pontos é irrelevante para a
conta.

Funciona muito bem em bases pequenas ou médias, com muitas colunas. Para a base de
fraude de vocês, com 1 milhão de linhas, não seria a primeira escolha: o treino
fica pesado nessa escala."
""")

s = sl_statement("Recapitulando",
                 "Árvore de Decisão, vocês já viram\nno Bloco 05: decide por perguntas,\nsem gradiente nenhum",
                 "Perguntas sucessivas, escolha gulosa, auditável. Segue no cardápio.")
notes(s, "2 min", "ESSENCIAL", EU,
      """
"Árvore de Decisão já teve um bloco inteiro só dela, o Bloco 05. Ela entra no
cardápio de hoje pelo mesmo motivo dos outros seis: decide por perguntas
sucessivas, sem gradiente nenhum, e é a base dos dois próximos modelos."
""")

s = sl_statement("Uma ferramenta com história",
                 "O mesmo Leo Breiman do CART\nvoltou, 17 anos depois,\ncom uma ideia melhor",
                 "Random Forest, Leo Breiman, 2001. Uma árvore sozinha erra mais que um monte delas.")
notes(s, "3 min", "DESCARTÁVEL, corte primeiro se faltar tempo", EU,
      """
"Random Forest tem uma conexão direta com a árvore de decisão que vocês já
conhecem: o mesmo Leo Breiman que ajudou a formalizar o CART em 1984 publicou, em
2001, o artigo do Random Forest. Dezessete anos depois, ele próprio resolveu o
maior problema da própria criação: uma árvore sozinha erra mais do que um monte
delas votando juntas."
""")

s = sl_bullets("Random Forest, na prática", "Muitas árvores, uma votação",
               [("Treina várias árvores, cada uma com uma amostra diferente dos dados", "sorteada com reposição, então cada árvore vê uma versão levemente diferente da base"),
                ("Cada árvore vota", "classificação: vence a categoria mais votada. Regressão: tira a média das previsões"),
                ("Por que isso reduz overfitting", "o erro de uma árvore que decorou demais tende a se cancelar quando muitas árvores votam juntas"),
                ("Custo", "perde parte da explicabilidade que uma árvore sozinha tinha")])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Na prática, Random Forest treina várias árvores, cada uma vendo uma amostra
diferente dos dados, sorteada com reposição. Na hora de decidir, as árvores votam:
em classificação, vence a categoria mais votada, em regressão, tira a média.

Isso reduz overfitting porque o erro de uma árvore que decorou demais tende a se
cancelar quando muitas árvores, cada uma com seu próprio exagero, votam juntas. O
custo é a explicabilidade: seguir o caminho de uma árvore é fácil, seguir o caminho
de quinhentas e depois somar os votos, nem tanto."
""")

s = sl_statement("Uma ferramenta com história",
                 "2016: um algoritmo novo\ncomeça a vencer quase toda\ncompetição de dados em tabela",
                 "XGBoost, Tianqi Chen e Carlos Guestrin, publicado na conferência KDD.")
notes(s, "3 min", "DESCARTÁVEL, corte primeiro se faltar tempo", EU,
      """
"XGBoost é o mais recente da lista. Tianqi Chen e Carlos Guestrin publicaram o
artigo em 2016, na conferência KDD, uma das principais da área. Rapidamente virou
um dos algoritmos mais usados em competição de dados com tabela, tipo Kaggle,
porque combina bom desempenho com tempo de treino administrável."
""")

s = sl_bullets("XGBoost, na prática", "Árvores em sequência, corrigindo o erro uma da outra",
               [("Treina árvores uma de cada vez, não todas juntas", "diferente do Random Forest, aqui a ordem importa"),
                ("Cada árvore nova mira no erro que sobrou", "o gradiente aponta exatamente o que a próxima árvore precisa corrigir"),
                ("Isso se chama boosting", "\"impulsionar\": cada árvore é fraca sozinha, juntas ficam fortes"),
                ("Quando usar", "dados em tabela, hoje um dos algoritmos mais usados em competição de dados")])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Na prática, XGBoost treina árvores em sequência, não ao mesmo tempo como o Random
Forest. Cada árvore nova entra mirando especificamente no erro que sobrou das
anteriores, usando o gradiente da perda para saber exatamente o que corrigir. Isso
se chama boosting: cada árvore sozinha é fraca, mas a sequência inteira fica forte."
""")

s = sl_bullets("Stacking, na prática", "O último andar: um modelo que aprende a combinar outros",
               [("Proposto por David Wolpert em 1992, com o nome \"stacked generalization\"", "a ideia de empilhar modelos, não só somar votos"),
                ("Treina vários modelos diferentes ao mesmo tempo", "por exemplo árvore, regressão logística e SVM, todos sobre o mesmo problema"),
                ("As previsões de todos viram entrada de um último modelo", "o meta-modelo, que aprende a combinar essas previsões da melhor forma"),
                ("Trade-off", "ganha desempenho, perde simplicidade, velocidade de treino e facilidade de manutenção")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Stacking é o mais flexível dos modelos vistos até aqui. Foi proposto por David
Wolpert em 1992, com o nome "stacked generalization", empilhar generalizações.

A ideia: treinar vários modelos diferentes ao mesmo tempo, por exemplo árvore,
regressão logística e SVM, todos tentando resolver o mesmo problema. As previsões
de todos eles viram a entrada de um último modelo, o meta-modelo, que aprende a
combinar essas previsões da melhor forma possível.

O trade-off é real: ganha desempenho, perde simplicidade, velocidade de treino e
facilidade de manutenção. Ninguém sobe pra Stacking no primeiro projeto."
""")

s = sl_timeline("Uma ferramenta com história", "Redes Neurais: seis décadas até virar mainstream",
                [("1943", "McCulloch e Pitts\nDescrevem o primeiro modelo matemático de um neurônio"),
                 ("1958", "Rosenblatt\nCria o Perceptron, o primeiro modelo neural que aprende sozinho, ajustando os próprios pesos"),
                 ("1969", "Minsky e Papert\nPublicam um livro mostrando o limite do Perceptron, e o campo esfria por mais de uma década"),
                 ("1986", "Rumelhart, Hinton e Williams\nReintroduzem o backpropagation, e redes com várias camadas passam a treinar de verdade")])
notes(s, "4 min", "DESCARTÁVEL, corte primeiro se faltar tempo", EU,
      """
"Redes Neurais fecham o cardápio, e são as que têm a história mais longa e mais
acidentada.

Em 1943, McCulloch e Pitts descrevem o primeiro modelo matemático de um neurônio,
ainda sem nenhuma forma de aprender sozinho.

Em 1958, Rosenblatt cria o Perceptron, o primeiro modelo que ajusta os próprios
pesos a partir de exemplos. É o nascimento de "aprender com dado" nas redes
neurais.

Em 1969, Minsky e Papert publicam um livro mostrando matematicamente o limite de um
Perceptron de uma camada só. A prova estava certa, mas foi lida como "redes neurais
não funcionam", e o campo praticamente parou por mais de uma década, um episódio
que ficou conhecido como inverno da IA.

Só em 1986, Rumelhart, Hinton e Williams reintroduzem o backpropagation, o
algoritmo que permite treinar redes com várias camadas de verdade. É a partir daí
que o campo se recupera, até chegar no marco de 2012 que vocês já viram na Aula 1:
o salto do deep learning."
""")

s = sl_bullets("O conceito", "Vocês já construíram um neurônio, no Bloco 03",
               [("Um neurônio artificial é a mesma conta do Bloco 03", "peso vezes entrada, mais um viés, exatamente o \"a\" e o \"b\" da regressão linear"),
                ("A diferença é uma função de ativação no final", "ela decide o quanto o neurônio \"dispara\", e é o que permite capturar padrões que não são uma linha reta"),
                ("Uma rede é um monte desses neurônios, organizados em camadas", "camada de entrada, uma ou mais camadas ocultas, camada de saída"),
                ("Cada neurônio de uma camada se conecta a todos da próxima", "cada conexão tem o próprio peso, e é isso que o treino ajusta")],
               subtitle="\"Deep\" em deep learning só quer dizer: várias camadas ocultas, não uma só.")
notes(s, "4 min", "ESSENCIAL", EU,
      """
"O conceito de rede neural não é tão distante quanto parece: vocês já construíram
um neurônio, no Bloco 03, sem saber. Peso vezes entrada, mais um viés, é
exatamente o "a" e o "b" da regressão linear.

A diferença é uma função de ativação no final, que decide o quanto aquele neurônio
"dispara". É essa função que permite à rede capturar padrões que não são uma linha
reta, coisa que a regressão linear sozinha não consegue.

Uma rede neural é um monte desses neurônios, organizados em camadas: uma camada de
entrada, uma ou mais camadas ocultas, e uma camada de saída. Cada neurônio se
conecta a todos os da próxima camada, cada conexão com o próprio peso.

E "deep" em deep learning quer dizer só isso: várias camadas ocultas, não uma só."
""")

s = sl_pipeline("A arquitetura, no caso de fraude", "Três camadas, um exemplo simplificado",
                [(1, "Camada de entrada", "Recebe as variáveis da transação: valor, horário, país, canal, uma por neurônio."),
                 (2, "Camada oculta", "Combina essas variáveis de formas que nenhum humano escreveu à mão, buscando padrões."),
                 (3, "Camada de saída", "Devolve a probabilidade de a transação ser fraude, um número entre 0 e 1.")],
                per_row=3,
                subtitle="Uma rede real teria mais neurônios e mais camadas ocultas. Isto é a ideia, em miniatura.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Um exemplo simplificado, com o caso de fraude. Camada de entrada recebe as
variáveis da transação, uma por neurônio: valor, horário, país, canal.

Camada oculta combina essas variáveis de formas que ninguém escreveu à mão,
buscando padrões que separem fraude de não fraude.

Camada de saída devolve um número entre 0 e 1: a probabilidade de fraude, igual à
Regressão Logística que vocês já viram, só que chegando lá por um caminho bem mais
longo."
""")

s = sl_bullets("Como aprende", "O mesmo gradiente descendente, com um problema novo",
               [("Passo 1, forward pass", "os dados atravessam a rede, camada por camada, até uma previsão sair do outro lado"),
                ("Passo 2, função de perda", "compara a previsão com a resposta certa, o mesmo MSE do Bloco 03"),
                ("O problema novo: milhares de pesos, espalhados em várias camadas", "gradiente descendente sozinho não diz quanto cada peso, de cada camada, contribuiu para o erro"),
                ("A solução tem nome: backpropagation", "calcula o gradiente de trás para frente, da camada de saída até a de entrada, distribuindo a cada peso sua parcela de responsabilidade pelo erro")],
               subtitle="Backpropagation é gradiente descendente aplicado a uma rede inteira, camada por camada.")
notes(s, "5 min", "ESSENCIAL, o coração técnico deste modelo", EU,
      """
Vá devagar aqui, é o ponto mais denso da parte de redes neurais.

""Como aprende" tem dois passos que já são conhecidos, e um problema novo.

Passo 1, forward pass: os dados atravessam a rede, camada por camada, até uma
previsão sair do outro lado.

Passo 2, função de perda: compara a previsão com a resposta certa, o mesmo MSE do
Bloco 03.

O problema novo: uma rede tem milhares de pesos, espalhados em várias camadas.
Gradiente descendente, sozinho, sabe reduzir a perda, mas não diz automaticamente
quanto cada peso individual, em cada camada, contribuiu para o erro final.

A solução tem nome, backpropagation: calcula o gradiente de trás para frente, da
camada de saída até a de entrada, distribuindo a cada peso sua parcela de
responsabilidade pelo erro. Depois disso, é o gradiente descendente de sempre:
ajusta cada peso um pouquinho, na direção que reduz a perda, repete milhares de
vezes."
""")

s = sl_bullets("Quando usar, e a ponte com a Aula 3", "Poder, ao custo de explicabilidade",
               [("Forte quando o padrão é complexo demais para uma reta ou uma árvore", "imagem, áudio, texto, é exatamente aí que \"deep\" em deep learning entra"),
                ("Custo real: explicar uma decisão fica muito mais difícil", "diferente da árvore do Bloco 05, não dá para apontar uma sequência de perguntas"),
                ("Precisa de muito mais dado para compensar tantos pesos", "milhares ou milhões de parâmetros para ajustar"),
                ("É a base dos LLMs da Aula 3", "um modelo de linguagem é uma rede neural gigante, treinada com o mesmo gradiente descendente, só que em escala muito maior")])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Quando usar rede neural: quando o padrão é complexo demais para uma reta ou uma
árvore capturarem, imagem, áudio, texto.

O custo é real: explicar uma decisão fica muito mais difícil. Diferente da árvore
do Bloco 05, não dá para apontar uma sequência de perguntas que levou à resposta.
E precisa de muito mais dado, para compensar a quantidade de pesos.

E aqui fecha um ciclo do programa inteiro: um modelo de linguagem, os LLMs da Aula
3, é uma rede neural gigante, treinada com o mesmo gradiente descendente que vocês
aprenderam hoje, só que em uma escala muito maior."
""")

s = sl_table("Resumo rápido, modelos individuais", "Seis famílias, seis jeitos de decidir",
             ["Modelo", "Como decide", "Bom para"],
             [["Regressão Linear",
               "Ajusta uma reta que minimiza o erro, por gradiente descendente",
               "Prever um número, quando a relação é aproximadamente linear"],
              ["Regressão Logística",
               "Mesma ideia da linear, mas passa o resultado por uma curva que vira probabilidade",
               "Classificação, quando a probabilidade importa tanto quanto a categoria"],
              ["Naive Bayes",
               "Calcula a probabilidade de cada classe pelo Teorema de Bayes, assumindo variáveis independentes",
               "Classificação de texto, como filtro de spam, rápido de treinar"],
              ["SVM, Máquinas de Vetores de Suporte",
               "Busca a fronteira com a maior margem possível entre as classes",
               "Bases pequenas ou médias, com muitas colunas"],
              ["Árvore de Decisão",
               "Decide por perguntas sucessivas, escolhendo a divisão que separa melhor a cada passo",
               "Quando explicar a decisão importa tanto quanto acertar"],
              ["Redes Neurais",
               "Camadas de neurônios, treinadas por gradiente descendente e backpropagation",
               "Padrão complexo demais para reta ou árvore: imagem, áudio, texto"]],
             widths=[0.22, 0.44, 0.34])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Cola rápida dos seis modelos individuais que acabamos de ver, para revisar antes
da prova ou antes de escolher um modelo num projeto de verdade."
""")

s = sl_table("Resumo rápido, ensembles", "Quando juntar modelos rende mais que um sozinho",
             ["Modelo", "Como decide", "Bom para"],
             [["Random Forest",
               "Várias árvores treinadas com amostras diferentes dos dados, decidindo por votação",
               "Reduzir o overfitting de uma árvore sozinha, com pouco ajuste fino"],
              ["XGBoost",
               "Árvores treinadas em sequência, cada uma corrigindo o erro que as anteriores deixaram passar",
               "Dados em tabela, um dos algoritmos mais usados em competição de dados"],
              ["Stacking",
               "Junta as previsões de modelos diferentes, e um modelo final aprende a combiná-las",
               "Espremer o último ponto de desempenho, ao custo de mais complexidade"]],
             widths=[0.22, 0.44, 0.34])
notes(s, "3 min", "ESSENCIAL", EU,
      """
"E a cola rápida dos três ensembles: Random Forest, XGBoost e Stacking, quando
juntar modelos rende mais do que treinar um sozinho."
""")

s = sl_bullets("De volta à pergunta do Bloco 03", "Quem usa gradiente descendente, quem não usa",
               [("Regressão Linear, Regressão Logística e Redes Neurais", "usam gradiente descendente, ajustando parâmetro por parâmetro (as redes, com a ajuda do backpropagation)"),
                ("Árvore de Decisão e Random Forest", "decidem por escolha gulosa, sem gradiente nenhum"),
                ("XGBoost usa gradiente de um jeito diferente", "o gradiente aponta o erro que a próxima árvore precisa corrigir, mas cada árvore ainda decide por divisão gulosa"),
                ("SVM e Naive Bayes têm mecanismo próprio", "SVM busca a margem máxima entre classes, Naive Bayes calcula probabilidade direto, sem ajuste iterativo")],
               subtitle="Nem toda família aprende do mesmo jeito. Cada uma escolheu um mecanismo diferente de propósito.")
notes(s, "9 min", "ESSENCIAL", EU,
      """
"Voltando à pergunta do Bloco 03: quem usa gradiente descendente, quem não usa?

Regressão Linear, Regressão Logística e Redes Neurais usam, ajustando parâmetro
por parâmetro. Nas redes, o backpropagation é quem calcula a direção certa para
cada peso, em cada camada, mas o ajuste final continua sendo gradiente descendente.

Árvore de Decisão e Random Forest não usam, decidem por escolha gulosa.

XGBoost é o caso interessante: o próprio nome tem "gradient" dentro. Ele usa
gradiente, mas de um jeito diferente do que vimos no Bloco 03: o gradiente aponta o
erro que a próxima árvore da sequência precisa corrigir. A árvore em si, porém,
continua decidindo por divisão gulosa, não por ajuste contínuo de parâmetro.

SVM e Naive Bayes têm mecanismo próprio, nenhum dos dois se encaixa exatamente nos
outros grupos. Isso é normal: a área tem décadas, e diferentes problemas inspiraram
diferentes mecanismos de aprendizado."
""")

# --------------------------------------------------------------------------
# INTERVALO (22h30 às 22h45)
# --------------------------------------------------------------------------
s = sl_break()
notes(s, "15 min", "ESSENCIAL", EU, "Intervalo. Sem apresentação.")

# --------------------------------------------------------------------------
# BLOCO 07: Quando a resposta é um número (22h45 às 23h15)
# --------------------------------------------------------------------------
s = sl_section("07", "Quando a resposta é um número",
               "Regressão tem métricas próprias, e a Aula 1 não chegou a cobrir isso",
               "22h45 às 23h15  ·  30 minutos")
notes(s, "22h45 às 23h15 (30 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  MAE, RMSE, R2               10 min
  O caso do Netflix Prize     15 min
  Por que RMSE fazia sentido   5 min

Este bloco reaproveita o MSE que acabou de aparecer no Bloco 03: RMSE é a raiz do
MSE. A Aula 1 nunca cobriu nenhuma métrica de regressão, então o resto é inédito.
""")

s = sl_bullets("Três métricas para quando a resposta é um número", "MAE, RMSE e R quadrado",
               [("MAE, erro médio absoluto", "a distância média entre o que o modelo previu e o valor real, em reais ou na unidade original"),
                ("RMSE, raiz do erro quadrático médio", "parecido com MAE, mas eleva cada erro ao quadrado antes de tirar a média: erros grandes pesam muito mais"),
                ("R quadrado", "quanto da variação dos dados o modelo consegue explicar, de 0 a 1, quanto mais perto de 1, melhor")],
               subtitle="Não existe acurácia em regressão. Essas três métricas fazem esse papel.")
notes(s, "10 min", "ESSENCIAL", EU,
      """
"Em classificação a gente tem acurácia, precisão, recall. Em regressão, o jogo é
outro, porque não existe "acertou ou errou", existe "errou por quanto".

MAE: erro médio absoluto. Some a diferença entre previsto e real de cada exemplo, em
valor absoluto, e tire a média. Se o MAE é R$50, o modelo erra em média R$50 pra mais
ou pra menos.

RMSE: é a raiz daquele MSE do Bloco 03, a mesma função de perda que o gradiente
descendente tenta minimizar. Eleva cada erro ao quadrado antes de tirar a média, e
depois tira a raiz. Consequência prática: um erro de R$500 pesa muito mais que dez
erros de R$50 cada. RMSE pune erro grande com mais força que MAE.

R quadrado: de 0 a 1, quanto da variação dos dados o modelo explica. Perto de 1 é
bom, perto de 0 significa que o modelo não está capturando quase nada."
""")

s = sl_statement("Uma ferramenta com história",
                 "US$ 1 milhão para melhorar\numa nota de 1 a 5 estrelas em 10%",
                 "Netflix Prize, 2006 a 2009")
notes(s, "2 min", "ESSENCIAL", EU,
      """
"Vocês já ouviram falar do Netflix Prize na Aula 1, só como uma data. Hoje, a
história completa, porque ela é literalmente sobre a métrica que a gente acabou de
ver."
""")

s = sl_table("O desafio", "Como o Netflix mediu \"10% melhor\"",
             ["Item", "O que era"],
             [["A meta", "melhorar em 10% o RMSE do sistema Cinematch, que a Netflix já usava"],
              ["O RMSE de partida", "0,9525, medido em cima da nota real de 1 a 5 estrelas que cada usuário deu"],
              ["O prêmio", "US$ 1 milhão para a primeira equipe a bater a meta"],
              ["Quem venceu", "BellKor's Pragmatic Chaos, em 2009, com RMSE de 0,8567, uma melhora de 10,06%"]],
             widths=[0.28, 0.72])
notes(s, "8 min", "ESSENCIAL", EU,
      """
"O desafio era prever, para cada usuário, que nota de 1 a 5 estrelas ele daria para
um filme que ainda não tinha visto. E o critério de vitória era literalmente o RMSE
que vocês acabaram de aprender.

O sistema que a Netflix já usava, Cinematch, tinha RMSE de 0,9525. A meta era baixar
isso em 10%. Prêmio: um milhão de dólares para a primeira equipe a conseguir.

A equipe BellKor's Pragmatic Chaos venceu em 2009, com RMSE de 0,8567, uma melhora de
10,06% sobre o Cinematch."
""")

s = sl_bullets("O detalhe que ninguém esquece", "Perder um milhão de dólares por 20 minutos",
               [("Outra equipe, The Ensemble, também bateu a meta", "com um resultado empatado ou levemente melhor que o BellKor's Pragmatic Chaos"),
                ("Mas enviou a resposta 20 minutos depois", "e a regra do desafio dizia que, em caso de empate, vence quem enviou primeiro"),
                ("BellKor's Pragmatic Chaos levou o prêmio inteiro", "por ter cronometrado o envio, não só por ter o melhor modelo")],
               subtitle="Métrica define quem ganha. Regra do jogo também.")
notes(s, "5 min", "ESSENCIAL, o mais memorável do bloco", EU,
      """
Conte devagar, é o tipo de detalhe que fica na cabeça da turma.

"Um detalhe real do Netflix Prize que vale a pena guardar: outra equipe, chamada The
Ensemble, também bateu a meta de 10%, com um resultado empatado ou levemente melhor
que o time vencedor.

Só que enviou a resposta 20 minutos depois. E a regra do desafio dizia: em caso de
empate, vence quem enviou primeiro.

BellKor's Pragmatic Chaos levou o milhão de dólares inteiro. Não só por ter o modelo
mais forte, mas por ter cronometrado o envio. Lição real: a métrica decide o
resultado técnico, mas a regra do jogo decide quem ganha."
""")

s = sl_bullets("Por que RMSE fazia sentido para a Netflix", "A escolha da métrica não é neutra",
               [("Prever nota 4 quando era 5 é aceitável", "erro pequeno, o RMSE penaliza pouco"),
                ("Prever nota 5 quando era 1 é grave", "recomendar com confiança um filme que a pessoa vai odiar"),
                ("RMSE pune esse erro grande com mais força", "por isso fazia mais sentido que MAE para o objetivo do negócio"),
                ("A métrica de avaliação sempre carrega uma prioridade de negócio", "escolher métrica é escolher o que você mais quer evitar errar")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Por que RMSE, e não MAE? Porque, para a Netflix, o erro grave é recomendar com
confiança um filme que a pessoa vai odiar, bem mais grave que errar por pouco. RMSE pune erro
grande desproporcionalmente mais que erro pequeno, exatamente o comportamento que a
Netflix queria incentivar nos competidores.

Isso fecha a ideia do bloco: escolher métrica nunca é neutro. É sempre uma escolha
sobre o que você mais quer evitar errar."
""")

# --------------------------------------------------------------------------
# BLOCO 08: Quando o modelo aprende o preconceito (23h15 às 23h35)
# --------------------------------------------------------------------------
s = sl_section("08", "Quando o modelo aprende o preconceito dos dados",
               "O caso de viés da Aula 1, pela lente de hoje",
               "23h15 às 23h35  ·  20 minutos")
notes(s, "23h15 às 23h35 (20 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Releitura do caso de viés    8 min
  De onde vem o viés          12 min
""")

s = sl_statement("Releitura",
                 "O sistema de reconhecimento facial da Aula 1\né um classificador. E ele errou mais\npara um grupo específico de pessoas.",
                 "Reconhecimento facial, Aracaju, abr/2024. Estudo DPU + CESeC, 7/mai/2025.")
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Lembram do caso de viés da Aula 1? Reconhecimento facial, Aracaju, o estudo da DPU
com o CESeC mapeando 24 casos entre 2019 e abril de 2025, mais da metade das
abordagens resultando em identificação equivocada.

Na Aula 1 isso foi apresentado como um caso de IA dando errado. Hoje, com o
vocabulário de hoje: aquilo é um classificador. Ele recebe uma imagem, e decide
"esta pessoa é quem o sistema busca, sim ou não". É exatamente a mesma estrutura da
árvore de decisão que vimos hoje, só que rodando dentro de uma rede neural, não numa
árvore.

E o problema real está em outro lugar: ele decidiu errado com muito mais frequência
para um grupo específico de pessoas."
""")

s = sl_bullets("De onde vem o viés", "Três origens, todas dentro dos dados, não do algoritmo",
               [("Dado de treino não representativo", "poucos exemplos de um grupo no conjunto usado para treinar, o modelo aprende menos sobre ele"),
                ("Rótulo enviesado", "quando o \"gabarito\" usado no treino já vem de uma decisão humana historicamente enviesada"),
                ("Variável usada como proxy", "um campo aparentemente neutro que, na prática, carrega informação de um grupo sensível"),
                ("A saída nunca é \"não usar dado\"", "é auditar quem está representado, como, e testar o erro separado por grupo, não só no total")],
               subtitle="Viés de modelo é viés de dado. Corrigir o algoritmo sem corrigir o dado não resolve.")
notes(s, "12 min", "ESSENCIAL", EU,
      """
"De onde vem o viés? Três origens, e nenhuma delas é o algoritmo em si.

Dado de treino não representativo: se um grupo aparece pouco nos dados de treino, o
modelo simplesmente aprende menos sobre esse grupo, e erra mais nele.

Rótulo enviesado: se o "gabarito" usado para treinar já vem de uma decisão humana
historicamente enviesada, o modelo aprende a repetir esse padrão com uma confiança
matemática que parece objetiva, mas não é.

Variável usada como proxy: um campo que parece neutro, como CEP ou nome, pode
carregar, na prática, informação que correlaciona fortemente com um grupo sensível.

A saída nunca é "não usar dado". É auditar quem está representado nos dados, e medir
o erro do modelo SEPARADO por grupo, não só no total. Um modelo com 95% de acurácia
geral pode estar errando 40% do tempo só para um grupo específico, e a métrica geral
esconde isso completamente."
""")

# --------------------------------------------------------------------------
# BLOCO 09: Encerramento (23h35 às 00h15)
# --------------------------------------------------------------------------
s = sl_section("09", "Encerramento",
               "O que vocês levam de hoje e o que vem na quinta",
               "23h35 às 00h15  ·  40 minutos")
notes(s, "23h35 às 00h15 (40 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Recapitulação             6 min
  O que vem pela frente     4 min
  Q&A                      25 min  (elástico, absorve atraso)
  Fechamento                5 min
""")

s = sl_bullets("Encerramento", "Nove ideias para levar de hoje",
               [("Aprender é ajustar números até errar menos", "função de perda, otimização e gradiente descendente, o motor por trás da maioria dos modelos"),
                ("Treino é lento e raro, inferência é rápida e constante", "todo modelo em produção vive fazendo inferência, o treino já ficou para trás"),
                ("Nem todo modelo aprende do mesmo jeito", "árvore de decisão escolhe gulosamente, sem gradiente nenhum, diferente de regressão e redes neurais"),
                ("Agora vocês têm oito nomes de modelo no vocabulário", "regressão linear e logística, Naive Bayes, SVM, árvore, Random Forest, XGBoost, Stacking e Redes Neurais"),
                ("Uma rede neural é só um monte de \"a vezes x mais b\" empilhados", "com uma função de ativação, organizados em camadas, aprendendo por backpropagation"),
                ("Acurácia sozinha não basta, e agora vocês sabem a conta", "matriz de confusão, precisão, recall e F1, com números de verdade"),
                ("Regressão tem métricas próprias", "MAE, RMSE e R quadrado, cada uma penalizando o erro de um jeito diferente"),
                ("Escolher métrica é escolher prioridade de negócio", "o Netflix Prize escolheu RMSE porque queria evitar recomendação péssima, não erro pequeno"),
                ("Viés de modelo é viés de dado", "corrigir o algoritmo sem auditar o dado que o treinou não resolve o problema")],
               subtitle="Se você levar só essas nove frases, a noite cumpriu o objetivo.",
               numbered=True)
notes(s, "6 min", "ESSENCIAL", EU,
      """
"Nove ideias para levar de hoje.

Aprender é ajustar números até errar menos: função de perda, otimização, gradiente
descendente.

Treino é lento e raro, inferência é rápida e constante.

Nem todo modelo aprende do mesmo jeito: árvore escolhe gulosamente, sem gradiente.

Vocês saem hoje com oito nomes de modelo no vocabulário: regressão linear,
regressão logística, Naive Bayes, SVM, árvore de decisão, Random Forest, XGBoost,
Stacking e Redes Neurais.

Uma rede neural é só um monte do exemplo mínimo do Bloco 03 empilhado, com uma
função de ativação, organizado em camadas, aprendendo por backpropagation.

Acurácia sozinha não basta, e agora vocês sabem a conta: matriz de confusão,
precisão, recall, F1.

Regressão tem métricas próprias: MAE, RMSE, R quadrado.

Escolher métrica é escolher prioridade de negócio, o Netflix Prize é a prova disso.

E viés de modelo nasce do dado que treinou o modelo, quase nunca do algoritmo em si.

Vocês saem hoje sabendo o suficiente para treinar o primeiro modelo de verdade. Isso
acontece quinta-feira."
""")

s = sl_two_col("Próximos encontros", "O que vem pela frente",
               "QUINTA · Semana 6",
               ["Primeiro modelo de verdade, com árvore de decisão",
                "Mesmo formato das outras quintas: demonstração curta e mão na massa",
                "A base de fraude em cartão finalmente vira um modelo"],
               "SEGUNDA · Semana 7",
               ["Tema a definir",
                "Mantém o formato conceitual das segundas"],
               subtitle="Quinta-feira fecha o ciclo: dados, engenharia, e agora modelo, tudo sobre o mesmo caso.")
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Na quinta, primeiro modelo de verdade: árvore de decisão, no Colab, sobre a base de
fraude que vocês já conhecem. Mesmo formato de sempre, demonstração curta e o resto é
prática.

Isso fecha um ciclo bonito: vocês exploraram o dado com SQL e pandas, construíram um
pipeline de engenharia de dados, e agora vão treinar um modelo em cima do mesmo caso.
Tudo conectado."
""")

s = sl_statement("Antes de ir", "Perguntas?",
                 "Escreva no chat. O que não der tempo, respondemos no Discord ainda hoje.")
notes(s, "25 min", "ESSENCIAL", EU,
      """
PERGUNTAS PREVISÍVEIS DE HOJE:

- "Preciso saber calcular gradiente descendente na mão?"
  Não. O que importa é entender o mecanismo (ajustar parâmetro na direção que reduz
  a perda, passo a passo) e reconhecer quando um modelo usa isso e quando não usa.
  A conta, na prática, quem faz é a biblioteca.

- "Preciso saber a fórmula de F1 de cabeça?"
  Não. O que importa é saber que ela existe, o que ela resume, e quando pedir para
  alguém calcular ou usar uma biblioteca que calcula sozinha.

- "Toda árvore de decisão é fácil de explicar?"
  Uma árvore sozinha, sim. Quando o mercado junta centenas delas (Random Forest,
  XGBoost), a explicabilidade cai bastante, mesmo a base ainda sendo árvore.

- "Por que não aprendemos redes neurais hoje?"
  Redes neurais entram melhor depois de já entender treino, teste, overfitting e
  métrica com um modelo simples. Árvore de decisão é a porta de entrada mais didática.

- "Isso cai no projeto final?"
  Cai direto, para quem escolher a trilha de Machine Learning na Etapa 2.
""")

s = sl_closing()
notes(s, "5 min", "ESSENCIAL", EU,
      """
FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. Vocês saem daqui sabendo fazer a conta que a maioria
das pessoas que fala de IA no dia a dia não sabe fazer. Revisem os slides antes de
quinta, principalmente a matriz de confusão. Nos vemos lá. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Anotar quais dos seis blocos geraram mais pergunta no chat, para calibrar onde
  cortar se a Aula 11 precisar ficar mais curta numa próxima turma.
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

out = ROOT / "docs" / "aula-11"
out.mkdir(parents=True, exist_ok=True)
dest = out / "AI-Talent-Academy-Aula11.pptx"
prs.save(dest)
print(f"OK: {dest}  ({len(prs.slides._sldIdLst)} slides)  "
      f"Roboto, sem travessões, tamanho único por bloco.")
