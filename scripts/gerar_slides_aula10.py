# -*- coding: utf-8 -*-
"""
Gerador do deck da Aula 10 (Semana 5, quinta-feira) do AI Talent Academy.

Tema: Aplicação de Engenharia de Dados. Aula quase inteiramente prática, no mesmo
formato das outras quintas (Aulas 2, 4, 6, 8): demonstração curta, e o resto e mão
na massa. Dois cenários combinados: Apache Airflow rodando na máquina do instrutor
(so demonstração, ninguem mais mexe) e PySpark no Google Colab (toda a turma, com um
pipeline de seis passos: extract, transform com quarentena, unify, bifurcação por
regra de negócio, load em múltiplos destinos e reconciliação final). Reaproveita o
caso de fraude em cartão das Aulas 2, 5, 6, 7, 8 e 9.

Identidade visual: padrao White Cube (Roboto, azul 28347B, fundos e logo do template
oficial em assets/whitecube/).

Uso:  python scripts/gerar_slides_aula10.py
Saida: docs/aula-10/AI-Talent-Academy-Aula10.pptx

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
# As DUAS excecoes documentadas, que a propria versao final aprovada do usuario mantem
# abaixo de 17pt, sao S_FOOT (rodape, e mobilia da pagina, ninguem precisa le-lo de
# longe) e os rotulos internos dos circulos concentricos do sl_nested (o espaco fisico
# dentro dos aneis mais internos nao comporta 17pt sem quebrar o desenho).
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
          "Semana 5  ·  Aplicação de Engenharia de Dados", 25, INK, space=0)
    shape(s, ML, Inches(5.75), Inches(2.4), Pt(5), fill=RED)
    block(s, ML, Inches(8.15), Inches(13), Inches(1.0),
          ["Aula 10  ·  Quinta-feira, 19h00 às 21h00  ·  Online",
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


def sl_closing():
    s = new_slide(BG_NAVY)
    block(s, ML, Inches(3.6), Inches(15), Inches(1.7), "Obrigado!", 66, WHITE, bold=True,
          space=0, line=1.0)
    block(s, ML, Inches(5.5), Inches(15), Inches(0.8), "Nos vemos na segunda-feira, 19h00.",
          30, NAVY_TXT_SOFT, space=0)
    shape(s, ML, Inches(6.85), Inches(2.4), Pt(5), fill=RED)
    block(s, ML, Inches(7.4), Inches(15), Inches(1.4),
          ["Discord do AI Talent Academy: link fixado no chat e enviado por e-mail.",
           "Gravação e slides desta aula chegam em até 24h."], 18, NAVY_TXT_SOFT, space=8)
    footer(s, dark=True)
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

# --------------------------------------------------------------------------
# RECEPÇÃO (19h00 às 19h10)
# --------------------------------------------------------------------------
s = sl_cover()
notes(s, "19h00 às 19h10 (slide de espera)", "ESSENCIAL", EU,
      """
Slide projetado desde 18h55. Fale a cada 2 ou 3 minutos enquanto a sala enche.

"Boa noite! Hoje é o dia que a Aula 9 prometeu: pipeline de verdade, rodando de
verdade, com vocês no teclado. Enquanto a sala enche, escreve no chat: alguém aqui
já instalou alguma coisa parecida com Airflow ou Spark antes?"

Não comece antes de 19h08.
""",
      """
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- Moderador com o link do Discord e do notebook prontos para colar no chat.
- Confirmar ANTES da aula: containers do Airflow de pé (docker compose ps) e a DAG
  aula10_pipeline_fraude aparecendo sem erro de import. Ver docs/aula-10/00-guia-de-
  preparacao.md, secao 2.
""")

s = sl_bullets("Enquanto todo mundo entra", "Hoje é o dia que a Aula 9 prometeu",
               [("Áudio e câmera", "microfone no mudo, câmera fica a seu critério"),
                ("Dúvidas", "escreva no chat a qualquer momento, temos moderação acompanhando"),
                ("Gravação", "a aula é gravada e o link chega em até 24h"),
                ("O formato de hoje", "uma demonstração curta, e o resto é vocês com a mão no teclado"),
                ("Aqueça o teclado", "escreva no chat: você já instalou algo parecido com Airflow ou Spark antes?")],
               subtitle="Segunda foi teoria. Hoje o pipeline roda de verdade.")
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Bem-vindos à Aula 10. Rapidinho, antes de começar:

Microfone sempre no mudo, câmera é opcional. Dúvida a qualquer momento, escreve no
chat, a gente tem moderação acompanhando o tempo todo. A aula fica gravada e o link
chega em até 24 horas.

O formato de hoje é diferente da segunda: eu mostro uma coisa rodando ao vivo, vocês
ganham uns 15 minutos de mecânica, e o resto da noite é vocês de mão na massa, com a
gente e os mentores circulando para ajudar.

Enquanto isso, escreve no chat: alguém aqui já instalou algo parecido com Airflow ou
Spark antes? Quero ver quantas mãos virtuais eu tenho na sala."
""")

# --------------------------------------------------------------------------
# BLOCO A: De volta à segunda (19h10 às 19h25)
# --------------------------------------------------------------------------
s = sl_section("A", "De volta à segunda",
               "O que ficou combinado na Aula 9, e o que muda hoje",
               "19h10 às 19h25  ·  15 minutos")
notes(s, "19h10 às 19h25 (15 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Recapitulação rápida da Aula 9    5 min
  Os dois cenários de hoje          5 min
  Mecânica da noite                 5 min
""")

s = sl_bullets("Recapitulando", "Três nomes que a Aula 9 só descreveu, e hoje executam",
               [("DAG", "o grafo de tarefas que decide em que ordem cada passo do pipeline roda"),
                ("Airflow", "o orquestrador que dispara, agenda e reexecuta cada tarefa da DAG"),
                ("Spark", "o motor que divide um processamento grande entre várias máquinas ao mesmo tempo")],
               subtitle="Na segunda, vocês viram o que cada um faz. Hoje, cada um roda de verdade.")
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Relembrando rapidinho três nomes da Aula 9.

DAG é o grafo que decide a ordem das tarefas: extrair antes de transformar, transformar
antes de carregar.

Airflow é o orquestrador que dispara, agenda e reexecuta essas tarefas sem intervenção
manual.

Spark é o motor que divide um processamento grande entre várias máquinas ao mesmo
tempo, em vez de uma máquina só suando sozinha.

Na segunda, vocês viram a explicação. Hoje, os três rodam de verdade, na frente de
vocês."
""")

s = sl_cards("Os dois cenários de hoje", "Uma demonstração, e uma prática",
             [("Cenário 1: Apache Airflow",
               "Instalado e rodando na minha máquina. Eu mostro ao vivo, ninguém mais "
               "precisa instalar nada. O que importa é ver o grafo, disparar a execução e "
               "acompanhar o log."),
              ("Cenário 2: PySpark no Colab",
               "Cada um de vocês roda no próprio notebook, no navegador, sem instalar nada "
               "no computador. É onde a prática de verdade acontece, com o pipeline "
               "completo do início ao fim.")],
             cols=2, card_h=2.6,
             subtitle="O primeiro vocês assistem. O segundo, vocês constroem.")
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Hoje tem dois cenários.

O primeiro é o Apache Airflow, já instalado e rodando na minha máquina. Isso aqui
ninguém mais precisa instalar: eu mostro funcionando, vocês acompanham o grafo, o
disparo e o log.

O segundo é PySpark, dentro do Google Colab, no navegador de cada um. Aqui é onde
vocês colocam a mão: o pipeline inteiro, do início ao fim, com o mesmo caso de fraude
que a gente usa desde a Aula 2."
""")

s = sl_bullets("Mecânica da noite", "Como vai funcionar a partir daqui",
               [("O notebook", "link fixado no Discord, chama-se Aula_10_Alunos_Engenharia_de_Dados_com_PySpark"),
                ("Onde travou, pede ajuda", "escreva no chat com o número do passo, os mentores estão de olho"),
                ("Os TODO no notebook", "cada célula incompleta tem uma dica ao lado, não é para adivinhar sozinho"),
                ("Sem problema errar", "o pipeline foi pensado para você bater num erro de propósito, e aprender com ele")],
               subtitle="Guarde o link do notebook antes de sair deste bloco.")
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Antes da demonstração, a mecânica rápida.

O notebook de vocês já está no Discord, chamado Aula_10_Alunos_Engenharia_de_Dados_com_
PySpark. Onde aparecer TODO, tem uma dica do lado, não é para adivinhar do nada.

Travou, escreve no chat com o número do passo. A gente e os mentores estão de olho.

E um aviso: uma das etapas foi pensada para dar erro de propósito. Quando isso
acontecer, não é bug de vocês, é o próprio exercício."
""",
      """
Felipe: fixar o link do notebook no Discord ANTES deste slide entrar no ar.
""")

# --------------------------------------------------------------------------
# BLOCO B: Apache Airflow, demonstração ao vivo (19h25 às 19h45)
# --------------------------------------------------------------------------
s = sl_section("B", "Apache Airflow",
               "Orquestrando um pipeline de verdade, ao vivo",
               "19h25 às 19h45  ·  20 minutos")
notes(s, "19h25 às 19h45 (20 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  O que a DAG de hoje faz     5 min
  Demonstração ao vivo       12 min
  Perguntas rápidas           3 min

Antes de começar: já com http://localhost:8080 aberto e logado numa aba, DAG
aula10_pipeline_fraude visível na lista. Ver o roteiro completo em docs/aula-10/00-
guia-de-preparacao.md, seção 2.5.
""")

s = sl_pipeline("A DAG de hoje", "Três tarefas, a mesma ordem que a Aula 9 ensinou",
                [(1, "extract", "Lê o CSV de transações e grava em formato Parquet."),
                 (2, "transform", "Remove nulo, duplicado e valor inválido. Registra quantas linhas entraram e saíram."),
                 (3, "load", "Agrupa por lojista, soma o valor, ordena do maior para o menor e grava o resultado.")],
                per_row=3,
                subtitle="Extract, transform, load: a mesma sigla da Aula 9, agora em código que roda")
notes(s, "5 min", "ESSENCIAL", EU,
      """
"A DAG de hoje tem três tarefas encadeadas: extract, transform, load. A mesma sigla
que vocês viram na segunda, só que agora cada quadrado desse grafo é uma função Python
que realmente executa.

Extract lê o CSV de transações. Transform limpa: tira nulo, duplicado e valor
inválido, e registra no log quantas linhas entraram e quantas sobraram. Load agrupa
por lojista, soma o valor e grava o resultado final.

Vamos ver isso rodando."
""")

s = sl_statement("Ao vivo", "Vamos abrir o Airflow\ne disparar essa DAG",
                 "http://localhost:8080  ·  usuário airflow, senha airflow")
notes(s, "12 min", "ESSENCIAL", EU,
      """
ROTEIRO DA DEMONSTRAÇÃO (ver docs/aula-10/00-guia-de-preparacao.md, seção 2.5):

1. Mostrar a lista de DAGs, apontar aula10_pipeline_fraude.
   "Isso aqui é uma DAG, o grafo de dependência que vimos na semana passada. Cada
   quadrado é uma tarefa."

2. Clicar na DAG, abrir a visão de grafo. Mostrar extract -> transform -> load
   visualmente.

3. Disparar a execução manual (botão de play, "Trigger DAG").

4. Acompanhar as três tarefas mudando de cor conforme rodam (fila, execução,
   sucesso), narrando o que está acontecendo por trás.

5. Abrir os logs da tarefa transform, mostrar a linha com a contagem de linhas antes
   e depois da limpeza. Conectar com o bloco de qualidade de dados da Aula 9.

6. Encerrar mostrando o CSV de saída gerado, com os lojistas ordenados por valor
   total.

"Reparem: eu não rodei nenhum desses três passos na mão. Eu só disparei a DAG, e o
Airflow decidiu a ordem, executou cada tarefa, e guardou o log de cada uma. Se a
transform falhasse, o load nem começaria. É isso que separa um pipeline de produção
de um notebook rodado célula por célula."
""",
      """
Se algo falhar ao vivo: usar o vídeo de backup gravado com antecedência (seção 2.7 do
guia). Não gastar mais que 2 minutos tentando debugar em tempo real.
""")

s = sl_cards("O que prestar atenção", "Quatro coisas que a demonstração mostra, além do resultado",
             [("O grafo", "a ordem das tarefas é visual, não é preciso ler código para entender a sequência"),
              ("O disparo manual", "hoje foi um clique, mas a mesma DAG pode rodar sozinha todo dia, numa hora marcada"),
              ("O log de cada tarefa", "cada passo grava sua própria evidência, útil quando algo dá errado às 3 da manhã"),
              ("A reexecução", "se uma tarefa falhar, o Airflow sabe reexecutar só ela, não o pipeline inteiro de novo")],
             cols=2, card_h=2.4)
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Quatro coisas para levar dessa demonstração, além do resultado final: o grafo mostra
a ordem sem precisar ler código, o disparo manual de hoje podia ser automático numa
hora marcada, cada tarefa deixa seu próprio log, e se uma falhar, o Airflow reexecuta
só ela, não o pipeline inteiro de novo. Isso é o que separa orquestração de só rodar
um script."

Perguntas rápidas antes de seguir para o Spark.
""")

# --------------------------------------------------------------------------
# BLOCO C: PySpark no Colab, mecânica da prática (19h45 às 20h00)
# --------------------------------------------------------------------------
s = sl_section("C", "PySpark no Colab",
               "Agora é a vez de vocês",
               "19h45 às 20h00  ·  15 minutos")
notes(s, "19h45 às 20h00 (15 min)", "ESSENCIAL", FELIPE,
      """
DISTRIBUIÇÃO:
  Uma correção antes de começar   4 min
  O pipeline de hoje, em visão geral   6 min
  Como abrir e navegar no notebook   5 min
""")

s = sl_bullets("Antes de começar", "Uma correção: o Colab não vem com Spark pronto",
               [("O que o Colab já tem", "Python e um conjunto grande de bibliotecas, mas não Java nem PySpark"),
                ("Por que Java importa", "o motor do Spark é escrito em Scala, que roda sobre a máquina virtual do Java"),
                ("A solução", "duas linhas de comando, na primeira célula do notebook, resolvem isso em menos de 2 minutos"),
                ("Roda uma vez por sessão", "se o Colab desconectar, é só rodar a célula de novo desde o início")],
               subtitle="Se alguém leu por aí que o Colab já vem pronto para Spark, essa parte não é exata.")
notes(s, "4 min", "ESSENCIAL", FELIPE,
      """
"Uma correção rápida antes de começar. O Colab não vem com Spark instalado de fábrica,
só com Python e um conjunto grande de bibliotecas. Falta especificamente Java, que é
o que o motor do Spark precisa para rodar por baixo.

A primeira célula do notebook resolve isso: instala o Java e o PySpark, e leva menos
de 2 minutos. Vocês rodam essa célula uma vez por sessão. Se o Colab cair no meio da
aula, é só rodar de novo desde o início."
""")

s = sl_pipeline("O pipeline de hoje", "Seis passos, do dado bruto ao resultado auditável",
                [(1, "extract", "Lê as seis tabelas do caso de fraude, direto do CSV."),
                 (2, "transform", "Separa transações válidas de rejeitadas, com o motivo de cada rejeição, em vez de só descartar."),
                 (3, "unify", "Junta as seis tabelas numa só, resolvendo colunas com o mesmo nome em tabelas diferentes."),
                 (4, "bifurcação", "Separa transações normais de transações que precisam de atenção, por regra de negócio."),
                 (5, "load", "Grava cada trilha num destino diferente: uma partição de dados, um CSV de risco, um resumo."),
                 (6, "reconciliação", "Confere que nenhuma linha sumiu sem explicação em nenhuma etapa.")],
                per_row=3,
                subtitle="Extract e transform vocês já conhecem. Os outros quatro são novos.")
notes(s, "6 min", "ESSENCIAL", FELIPE,
      """
"O pipeline de hoje tem seis passos. Extract e transform seguem o mesmo espírito da
Aula 9: ler os dados, e garantir qualidade antes de seguir adiante. A diferença é que,
em vez de só descartar linha ruim, hoje vocês vão separar e guardar o motivo, isso se
chama quarentena de dados.

Depois vem unify, juntando as seis tabelas. Depois, um passo novo: bifurcação, separando
transações normais de transações que merecem atenção, cada uma seguindo para um destino
diferente. E fecha com reconciliação: provar que nenhuma linha sumiu sem explicação em
nenhuma etapa.

Isso é engenharia de dados de verdade: transformar importa, mas provar que a
transformação funcionou importa tanto quanto."
""")

s = sl_bullets("Como vai funcionar", "Abrindo o notebook",
               [("Passo 0", "abrir o notebook pelo link do Discord, e fazer uma cópia para o seu próprio Drive"),
                ("Rode em ordem", "uma célula de cada vez, de cima para baixo, sem pular"),
                ("Os TODO", "aparecem exatamente onde é preciso decidir alguma coisa, com uma dica ao lado"),
                ("Um erro é esperado", "no passo de unificação, uma célula vai dar erro de propósito, leia a explicação antes de corrigir")],
               subtitle="A partir daqui, 50 minutos são só de vocês.")
notes(s, "5 min", "ESSENCIAL", FELIPE,
      """
"Para abrir: link no Discord, e a primeira coisa é fazer uma cópia para o próprio
Drive, Arquivo, Salvar uma cópia no Drive. Depois disso, o notebook é só seu.

Rodem uma célula de cada vez, em ordem, sem pular. Onde tiver TODO, tem uma dica do
lado. E um aviso: no passo 3, uma célula vai dar erro de propósito. Leiam o texto logo
depois da célula antes de tentar corrigir, ele explica exatamente por quê.

A partir do próximo slide, são 50 minutos só de prática. A gente e os mentores vamos
circular pelo chat o tempo todo."
""")

# --------------------------------------------------------------------------
# BLOCO D: Mão na massa (20h00 às 20h50)
# --------------------------------------------------------------------------
s = sl_section("D", "Mão na massa",
               "O pipeline inteiro, do seu teclado até o resultado final",
               "20h00 às 20h50  ·  50 minutos")
notes(s, "20h00 às 20h50 (50 min)", "ESSENCIAL", "Edmar + Felipe",
      """
CHECKLIST DO MENTOR DURANTE A PRÁTICA:

- Circular pelo chat a cada 5 minutos, não esperar pergunta chegar sozinha.
- Quem travar no passo 3 (erro de referência ambígua): confirmar que leu o texto
  explicativo antes de dar a resposta pronta.
- Quem terminar antes do tempo: sugerir revisar as duas perguntas de conferência do
  final do notebook, ou conferir se a reconciliação do passo 6 realmente bateu.
- Aos 20h40, avisar no chat: "10 minutos para o fechamento, garantam que rodaram até
  a reconciliação."
""")

s = sl_statement("Agora é com vocês", "50 minutos.\nO notebook, do passo 0 ao 6.",
                 "Travou? Chat, com o número do passo. A gente está de olho o tempo todo.")
notes(s, "50 min (projetado o tempo todo)", "ESSENCIAL", "Edmar + Felipe",
      """
Este slide fica projetado durante toda a prática, sem narração contínua. Circular
pelo chat, responder dúvida por dúvida.

Aos 20h40 (10 minutos do fim): avisar no chat pedindo para todo mundo garantir que
chegou pelo menos até o passo 6 (reconciliação), mesmo que as duas perguntas finais
ainda não estejam respondidas.
""")

# --------------------------------------------------------------------------
# BLOCO E: Encerramento (20h50 às 21h00)
# --------------------------------------------------------------------------
s = sl_section("E", "Encerramento",
               "O que vocês levam de hoje e o que vem na semana 6",
               "20h50 às 21h00  ·  10 minutos")
notes(s, "20h50 às 21h00 (10 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Recapitulação            3 min
  O que vem pela frente    2 min
  Q&A                      4 min  (elástico, absorve atraso)
  Fechamento               1 min
""")

s = sl_bullets("Encerramento", "Cinco ideias para levar de hoje",
               [("Orquestração não é rodar célula por célula", "o Airflow decide ordem, agenda, registra log e reexecuta sozinho quando algo falha"),
                ("Quarentena vale mais que descartar em silêncio", "guardar o motivo da rejeição é o que permite explicar depois por que uma linha sumiu"),
                ("Nem todo dado segue o mesmo caminho", "separar por regra de negócio, e mandar cada trilha para o destino certo, é decisão de projeto"),
                ("Um pipeline só está pronto quando reconcilia", "contar de novo, em cada etapa, e provar que nada se perdeu sem explicação"),
                ("Vocês rodaram um pipeline real, ponta a ponta", "extract, transform, unify, bifurcação, load e reconciliação, sozinhos")],
               subtitle="Se você levar só essas cinco frases, a noite cumpriu o objetivo.",
               numbered=True)
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Cinco ideias para levar de hoje.

Orquestração não é rodar célula por célula: o Airflow decide a ordem, agenda,
registra log de cada passo e reexecuta sozinho quando algo falha.

Quarentena vale mais que descartar em silêncio: guardar o motivo é o que permite
explicar depois por que uma linha sumiu.

Nem todo dado segue o mesmo caminho: separar por regra de negócio, e mandar cada
trilha para o destino certo, é decisão de projeto deliberada.

Um pipeline só está pronto quando reconcilia: contar de novo em cada etapa, e provar
que nada se perdeu sem explicação.

E a mais importante: vocês rodaram, sozinhos, um pipeline real, do extract até a
reconciliação. Isso sai direto da teoria da Aula 9 e vira prática nas suas mãos."
""")

s = sl_two_col("Próximos encontros", "O que vem pela frente",
               "SEGUNDA · Semana 6",
               ["Machine Learning",
                "Do baseline ao primeiro modelo",
                "Volta o formato conceitual das segundas",
                "Prever com dados, não só descrever"],
               "QUINTA · Semana 6",
               ["Primeiro laboratório de Machine Learning",
                "Mesmo formato de hoje: demonstração curta e mão na massa",
                "A base de fraude em cartão continua sendo a referência"],
               subtitle="A partir da semana 6, o foco muda de preparar dados para prever com eles.")
notes(s, "2 min", "ESSENCIAL", EU,
      """
"O que vem pela frente.

Semana 6, segunda-feira: Machine Learning, do baseline ao primeiro modelo. Volta o
formato conceitual das segundas.

Quinta da mesma semana: primeiro laboratório de Machine Learning, no mesmo formato de
hoje, demonstração curta e o resto é prática. A mesma base de fraude em cartão continua
sendo a referência."
""")

s = sl_statement("Antes de ir", "Perguntas?",
                 "Escreva no chat. O que não der tempo, respondemos no Discord ainda hoje.")
notes(s, "4 min", "ESSENCIAL", EU,
      """
PERGUNTAS PREVISÍVEIS DE HOJE:

- "Preciso decorar a sintaxe do PySpark?"
  Não. O que importa é reconhecer o padrão (extract, transform, unify, load) e saber
  quando cada peça entra. A sintaxe exata está sempre a uma busca de distância.

- "Por que minha trilha de atenção veio vazia, ou minha quarentena veio vazia?"
  Depende da base do dia. Base limpa gera quarentena vazia, o pipeline está
  confirmando que não havia nada para descartar hoje, e isso é sinal de dado bom.

- "Preciso instalar Airflow na minha máquina também?"
  Não. Só quem for demonstrar precisa. Para a atividade de vocês, o Colab com PySpark
  é suficiente.

- "Isso cai no projeto final?"
  Cai direto. Squads que lidam com dados de fontes diferentes vão precisar de um
  pipeline parecido com esse, ainda que mais simples.
""")

s = sl_closing()
notes(s, "1 min", "ESSENCIAL", EU,
      """
FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. Vocês saem daqui tendo rodado um pipeline real, não só
lido sobre ele. Revisem o notebook com calma até a próxima segunda, principalmente o
passo da bifurcação. Nos vemos lá. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Anotar quais passos do notebook geraram mais pergunta no chat, para calibrar o
  roteiro de mentoria da próxima turma.
- Derrubar o ambiente Airflow só depois de confirmar que ninguém mais precisa dele
  hoje (docker compose down, opcional, pode deixar rodando).
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

out = ROOT / "docs" / "aula-10"
out.mkdir(parents=True, exist_ok=True)
dest = out / "AI-Talent-Academy-Aula10.pptx"
prs.save(dest)
print(f"OK: {dest}  ({len(prs.slides._sldIdLst)} slides)  "
      f"Roboto, sem travessões, tamanho único por bloco.")
