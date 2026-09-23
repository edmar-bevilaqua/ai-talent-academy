# -*- coding: utf-8 -*-
"""
Gerador do deck da Aula 13 (Semana 7, segunda-feira) do AI Talent Academy.

Tema: Agentes de IA. Escopo pedido explicitamente pelo usuario, em seis perguntas:
quando agentes surgiram, o que sao, como se diferenciam de uma chamada unica de LLM,
como se controla um agente, quais sao as principais solucoes do mercado para criar
um, e qual e o estado da arte hoje. Ao contrario da Aula 11 (que cresceu de 34 para
70 slides em cinco rodadas de "sem se apegar ao tempo"), aqui o pedido explicito
inicial foi o oposto: uma aula potencialmente mais curta que o padrao de 3h+ das
segundas.

Isso mudou de novo depois: o usuario pediu para trazer a pratica (construir um agente
de verdade, com pelo menos uma ferramenta, servida por um MCP server simples) para
dentro desta propria aula de segunda, quebrando de proposito a regra padrao de "sem
mao na massa nas segundas", para que a quinta-feira (Aula 14) fique inteira livre
para mentoria de squad, com a Semana 8 e o Demo Day se aproximando. O Bloco 04
("Mao na massa: seu primeiro agente") entrega isso: um agente de uma ferramenta so,
com um servidor MCP de verdade (biblioteca FastMCP, cliente em memoria, sem
subprocesso nem rede) e um loop ReAct escrito a mao usando a API da NVIDIA (OpenAI
compatible, gratuita). O deck cresceu de 3h35 para pouco mais de 4h por causa disso,
e isso foi uma troca consciente, nao um erro de escopo.

Ponto de partida importante: a Aula 1 e a Aula 3 ja plantaram a base. A Aula 1 definiu
agente numa frase ("uma GenAI que nao so responde: planeja, usa ferramentas e executa
tarefas") e colocou "agentes" como o ultimo marco da linha do tempo historica, logo
apos o ChatGPT. A Aula 3 prometeu explicitamente, no proprio roadmap do curso, que a
Semana 7 seria sobre agentes ("da resposta a acao"), e ja cobriu Transformer, janela de
contexto, prompt engineering e RAG em profundidade. Este script nao repete nada disso:
abre com um recap de uma frase e vai direto para o que ainda nao foi dito.

Todos os fatos historicos (datas do ReAct, AutoGPT, function calling, MCP) e os dados
de adocao de mercado (LangGraph, CrewAI, Claude Agent SDK) foram verificados via busca
antes de escrever, no mesmo padrao ja usado nas Aulas 9 e 11 para Spark/Databricks e
Netflix Prize/CART.

Identidade visual: padrao White Cube (Roboto, azul 28347B, fundos e logo do template
oficial em assets/whitecube/).

Uso:  python scripts/gerar_slides_aula13.py
Saida: docs/aula-13/AI-Talent-Academy-Aula13.pptx

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

assert min(S_SUB, S_BULLET, S_CARD_T, S_CARD_B, S_TABLE_H, S_TABLE_C, S_BIG, S_SRC,
           S_TIMELINE, S_PIPELINE_B) >= S_MIN, \
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
          "Semana 7  ·  Agentes de IA", 25, INK, space=0)
    shape(s, ML, Inches(5.75), Inches(2.4), Pt(5), fill=RED)
    block(s, ML, Inches(8.15), Inches(13), Inches(1.0),
          ["Aula 13  ·  Segunda-feira, 19h00 às 23h05  ·  Online",
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
    """Bloco de codigo/roteiro em destaque, com bullets de explicacao embaixo."""
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
    block(s, ML, Inches(5.85), Inches(14), Inches(0.7), "Voltamos às 21h20 em ponto.", 28,
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
# RECEPÇÃO (19h00 às 19h10)
# --------------------------------------------------------------------------
s = sl_cover()
notes(s, "19h00 às 19h10 (slide de espera)", "ESSENCIAL", EU,
      """
Slide projetado desde 18h55. Fale a cada 2 ou 3 minutos enquanto a sala enche.

"Boa noite! Semana 7, e hoje é o assunto que a gente prometeu lá na Aula 3: agentes
de IA. Enquanto a sala enche, uma pergunta pro chat: você já usou alguma ferramenta
de IA que fez mais do que só responder, tipo pesquisar na internet, mexer num
arquivo ou executar alguma coisa sozinha?"

Não comece antes de 19h08.
""",
      """
- Microfones em mudo, câmeras opcionais.
- Confirmar gravação ligada antes de 19h10.
- Moderador com o link do Discord pronto para colar.
- Aula desenhada para ficar mais enxuta que o padrão das segundas, por pedido
  explícito do usuário. Edmar e Felipe controlam o ritmo ao vivo: cortem à vontade
  o que já estiver claro para a sala.
""")

s = sl_bullets("Enquanto todo mundo entra", "Hoje a gente cumpre a promessa da Aula 3",
               [("Áudio e câmera", "microfone no mudo, câmera fica a seu critério"),
                ("Dúvidas", "escreva no chat a qualquer momento, temos moderação acompanhando"),
                ("Gravação", "a aula é gravada e o link chega em até 24h"),
                ("Hoje tem prática de verdade, no meio da aula", "vocês vão construir um agente com a própria mão, no Bloco 04"),
                ("Aqueça o teclado", "escreva no chat: que ferramenta de IA já fez mais do que só responder, para você?")],
               subtitle="Semana 7, Agentes de IA: quando surgiram, o que são, e como se controlam.")
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Bem-vindos à Aula 13. Rapidinho: microfone no mudo, câmera à vontade, dúvida no
chat a qualquer momento, aula gravada com link em até 24h.

Aviso importante, diferente do padrão das outras segundas: hoje tem prática de
verdade, no meio da aula, não só teoria. Lá pelo Bloco 04 vocês vão construir um
agente com a própria mão. Por isso a quinta desta semana muda de formato, mais
sobre isso no fim da noite.

Enquanto isso, escreve no chat: que ferramenta de IA já fez mais do que só
responder, para você? Já pesquisou sozinha, já mexeu num arquivo, já executou
alguma coisa? Vou puxar algumas respostas daqui a pouco."
""")

# --------------------------------------------------------------------------
# BLOCO 01: De volta à promessa da Semana 2 (19h10 às 19h25)
# --------------------------------------------------------------------------
s = sl_section("01", "De volta à promessa da Semana 2",
               "A Aula 3 já disse que hoje seria este dia",
               "19h10 às 19h25  ·  15 minutos")
notes(s, "19h10 às 19h25 (15 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Recap de uma frase por conceito    7 min
  Panorama de hoje                   8 min

Bloco deliberadamente curto. Toda a base já foi plantada nas Aulas 1 e 3, o trabalho
aqui é só reconectar o que já foi dito.
""")

s = sl_bullets("Lembrando", "O que as Aulas 1 e 3 já deixaram plantado",
               [("A Aula 1 já definiu agente numa frase", "\"uma GenAI que não só responde: planeja, usa ferramentas e executa tarefas\""),
                ("A Aula 1 colocou agentes como o marco mais recente da história da IA", "logo depois do ChatGPT, na linha do tempo"),
                ("A Aula 3 prometeu este dia, no próprio roteiro do curso", "\"Semana 7: Agentes de IA, da resposta à ação\""),
                ("A Aula 3 já cobriu Transformer, janela de contexto e prompt", "a base técnica que um agente usa por baixo já é conhecida"),
                ("A Aula 3 já cobriu RAG", "buscar informação externa antes de responder, uma das ferramentas que um agente pode ter")],
               subtitle="Nada disso será reexplicado hoje. A base já está posta.")
notes(s, "7 min", "ESSENCIAL", EU,
      """
"Cinco coisas que vocês já ouviram, rapidinho.

A Aula 1 já definiu agente numa frase: uma GenAI que não só responde, planeja, usa
ferramentas e executa tarefas.

A Aula 1 colocou agentes como o marco mais recente da história da IA, logo depois do
ChatGPT.

A Aula 3 prometeu este dia, no próprio roteiro do curso: "Semana 7, Agentes de IA,
da resposta à ação".

A Aula 3 já cobriu Transformer, janela de contexto e prompt, a base técnica que um
agente usa por baixo.

E a Aula 3 já cobriu RAG, buscar informação externa antes de responder, que é
literalmente uma das ferramentas que um agente pode ter na caixa.

Hoje a gente não reexplica nada disso. A gente vai direto para o que ainda não foi
dito."
""")

s = sl_bullets("O panorama de hoje", "Seis perguntas, na ordem que vocês pediram",
               [("Quando isso surgiu", "a história real, com data e nome, não só \"é recente\""),
                ("O que é um agente, de verdade", "a definição técnica por trás da frase da Aula 1"),
                ("O que muda em relação a uma chamada única de LLM", "onde exatamente a diferença mora"),
                ("Como controlamos um agente", "para não perder o controle que a Aula 1 já avisou que se perde"),
                ("Quais são as principais soluções para criar um", "o cardápio de ferramentas do mercado hoje"),
                ("Qual é o estado da arte agora", "quem usa, em que escala, e onde ainda trava")],
               subtitle="Seis blocos, cada um respondendo uma pergunta só.",
               numbered=True)
notes(s, "8 min", "ESSENCIAL", EU,
      """
"O panorama de hoje, em seis perguntas, exatamente na ordem que faz sentido
responder: quando isso surgiu, o que é de verdade, o que muda em relação a uma
chamada única de LLM, como controlamos, quais são as principais soluções, e qual é
o estado da arte agora.

Cada bloco responde uma pergunta só. Vamos."
""")

# --------------------------------------------------------------------------
# BLOCO 02: Quando isso surgiu (19h25 às 19h50)
# --------------------------------------------------------------------------
s = sl_section("02", "Quando isso surgiu",
               "Mais antigo do que parece, com data exata",
               "19h25 às 19h50  ·  25 minutos")
notes(s, "19h25 às 19h50 (25 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Linha do tempo, parte 1 (2022 a 2023)     8 min
  AutoGPT, a febre viral                    9 min
  Linha do tempo, parte 2 (2023 a hoje)     8 min
""")

s = sl_timeline("A virada", "De um paper acadêmico a um repositório viral, em 5 meses",
                [("Out 2022", "ReAct\nGoogle Research e Princeton publicam o paper que junta raciocínio e ação num loop só"),
                 ("Nov 2022", "ChatGPT\nJá visto na Aula 1. O momento em que o mundo conheceu a IA generativa"),
                 ("Fev 2023", "Toolformer\nA Meta publica um modelo que aprende sozinho quando vale a pena chamar uma ferramenta"),
                 ("Mar 2023", "AutoGPT\nUm goal, e o modelo se prompta sozinho, sem parar, até terminar")])
notes(s, "8 min", "ESSENCIAL", EU,
      """
"A história começa antes do que a maioria imagina.

Outubro de 2022, um mês antes do ChatGPT: pesquisadores do Google Research e da
Princeton publicam o paper ReAct, Reasoning and Acting. A ideia central: em vez de o
modelo só responder, ele intercala pensar e agir, num loop só. Essa é literalmente a
arquitetura que quase todo agente usa até hoje.

Novembro de 2022, ChatGPT, já visto na Aula 1.

Fevereiro de 2023, a Meta publica o Toolformer: um modelo treinado para decidir
sozinho quando vale a pena chamar uma calculadora, um buscador, um tradutor. Uso de
ferramenta deixou de ser truque de prompt e virou capacidade aprendida.

Março de 2023, um desenvolvedor independente chamado Toran Bruce Richards publica o
AutoGPT: você dá um objetivo, e o modelo gera suas próprias tarefas, executa,
avalia, gera mais tarefas, sem parar. Vamos ver o que aconteceu com isso."
""")

s = sl_statement("Uma febre real",
                 "Mais de 185 mil estrelas no GitHub.\nUm dos projetos que mais\ncresceu na história da plataforma.",
                 "AutoGPT, repositório criado em 16 de março de 2023")
notes(s, "5 min", "ESSENCIAL", EU,
      """
"O AutoGPT não foi um projeto de pesquisa discreto. Foi uma febre. Em poucas
semanas, virou um dos repositórios de crescimento mais rápido da história do
GitHub, hoje com mais de 185 mil estrelas.

A promessa era gigante: dá um objetivo qualquer para o modelo, e ele se vira
sozinho, sem supervisão, até terminar."
""")

s = sl_bullets("O que aconteceu na prática", "A promessa era maior do que a entrega",
               [("Loops que não terminavam", "o modelo gerava tarefa atrás de tarefa, sem convergir para o objetivo real"),
                ("Custo alto e imprevisível", "cada passo do loop é uma chamada de API, e ninguém sabia quantos passos viriam"),
                ("Nenhum controle sobre o que ele fazia", "e é exatamente esse o risco que a Aula 1 já tinha avisado: \"perder controle e rastreabilidade\""),
                ("O hype esfriou, mas a pergunta ficou", "como dar autonomia a um modelo sem perder o controle sobre ele")],
               subtitle="Essa pergunta puxa o fio de quase tudo que vem no resto da aula de hoje.")
notes(s, "4 min", "ESSENCIAL", EU,
      """
"E na prática? A entrega não acompanhou a promessa. Loops que não terminavam,
gerando tarefa atrás de tarefa sem convergir. Custo alto e imprevisível, porque cada
passo do loop custa uma chamada de API nova. E nenhum controle real sobre o que o
modelo estava fazendo, exatamente o risco que a Fase 5 da Aula 1 já tinha avisado:
"perder controle e rastreabilidade".

O hype esfriou. Mas a pergunta que ficou, como dar autonomia sem perder controle, é
o fio que puxa quase tudo que vem no resto de hoje."
""")

s = sl_timeline("Da bagunça à padronização", "2023 em diante: a indústria resolve o problema de encanamento",
                [("Meados 2023", "Function calling\nA OpenAI lança chamada de função estruturada: o modelo escolhe QUAL ferramenta chamar"),
                 ("Nov 2024", "MCP\nA Anthropic lança um protocolo aberto para conectar qualquer modelo a qualquer ferramenta"),
                 ("2025 a 2026", "SDKs de agente\nOpenAI, Google e Anthropic lançam kits oficiais para construir agentes de produção")])
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Depois da fase de bagunça criativa, a indústria passou a resolver o problema de
encanamento.

Em meados de 2023, a OpenAI lança function calling: o modelo passa a poder escolher,
de forma estruturada, qual função chamar e com quais parâmetros. É a peça técnica
que transforma "o modelo decide algo" em "o código de fora consegue confiar
nessa decisão e executar".

Em novembro de 2024, a Anthropic lança o MCP, Model Context Protocol: um jeito
aberto e padronizado de conectar qualquer modelo a qualquer ferramenta ou fonte de
dado, resolvendo um problema que a indústria chamava de N vezes M, ou seja, antes
disso, cada combinação de modelo e ferramenta precisava de uma integração própria.
Hoje já existem mais de 16 mil servidores MCP publicados.

E de 2025 para cá, os três grandes, OpenAI, Google e Anthropic, lançaram kits
oficiais de desenvolvimento para construir agente de produção, não mais só
experimento. A gente volta nisso no bloco de soluções."
""")

# --------------------------------------------------------------------------
# BLOCO 03: O que é um agente, de verdade (19h50 às 20h15)
# --------------------------------------------------------------------------
s = sl_section("03", "O que é um agente, de verdade",
               "A definição técnica por trás da frase da Aula 1",
               "19h50 às 20h15  ·  25 minutos")
notes(s, "19h50 às 20h15 (25 min)", "ESSENCIAL", FELIPE,
      """
DISTRIBUIÇÃO:
  Definição formal              6 min
  O loop ReAct, passo a passo   12 min
  O que é "ferramenta", tecnicamente   7 min
""")

s = sl_bullets("Definição formal", "Quatro peças, juntas",
               [("Um modelo de linguagem", "o \"cérebro\" que decide o que fazer a seguir"),
                ("Um loop de raciocínio", "pensa, age, observa o resultado, pensa de novo, repete"),
                ("Ferramentas reais", "funções que o modelo pode chamar para agir no mundo, não só falar sobre ele"),
                ("Estado que persiste entre os passos", "o agente lembra o que já tentou e o que já descobriu, passo a passo")],
               subtitle="Um agente é essas quatro peças trabalhando juntas, rumo a um objetivo.")
notes(s, "6 min", "ESSENCIAL", FELIPE,
      """
"Vamos destrinchar a frase da Aula 1. Um agente tem quatro peças.

Um modelo de linguagem, que decide o que fazer a seguir.

Um loop de raciocínio: pensa, age, observa o resultado dessa ação, pensa de novo, e
repete, quantas vezes for preciso.

Ferramentas reais: funções que o modelo pode chamar para agir no mundo de verdade,
não só descrever o que faria.

E estado que persiste entre os passos: o agente lembra o que já tentou e o que já
descobriu, ao longo de toda a tarefa, não só numa resposta isolada.

Um agente é essas quatro peças trabalhando juntas, rumo a um objetivo."
""")

s = sl_code("O loop ReAct, na prática", "Um exemplo: \"qual lojista teve mais contestação este mês?\"",
            ["PENSA: preciso consultar o banco de dados para responder isso",
             "AGE: chama a ferramenta de SQL, com uma query de contagem por lojista",
             "OBSERVA: a ferramenta devolve uma tabela com os resultados",
             "PENSA: já tenho a resposta, não preciso agir de novo",
             "RESPONDE: \"o lojista X, com 47 contestações este mês\""],
            [("Cada linha é um passo real de execução", "o modelo genuinamente para, decide, e só continua depois de ver o resultado"),
             ("A ferramenta de SQL não é o modelo", "é código escrito por gente, o modelo só decide QUANDO chamar e COM QUE parâmetro"),
             ("Se o resultado vier estranho, o loop pode continuar", "o modelo pode pensar de novo e tentar uma query diferente, sem intervenção humana")])
notes(s, "12 min", "ESSENCIAL", FELIPE,
      """
"Isso aqui é o loop ReAct, do paper de outubro de 2022, na prática, usando o caso de
fraude que vocês já conhecem de cor.

Pergunta: qual lojista teve mais contestação este mês?

Pensa: preciso consultar o banco de dados para responder isso. Age: chama a
ferramenta de SQL, passando uma query de contagem por lojista. Observa: a ferramenta
devolve uma tabela de resultado. Pensa de novo: já tenho a resposta, não preciso
agir mais. Responde com o dado real.

Três coisas para prestar atenção. Primeira: cada linha dessas é um passo real de
execução, o modelo genuinamente para e espera o resultado antes de continuar,
isso não é uma metáfora de apresentação.

Segunda: a ferramenta de SQL é código escrito por uma pessoa, separado do modelo. O
modelo só decide quando chamar essa ferramenta e com qual parâmetro. Quem executa a
query de verdade é o banco de dados.

Terceira: se o resultado voltasse estranho, tipo vazio ou com erro, o modelo poderia
pensar de novo e tentar uma query diferente, sozinho, sem ninguém pedir. É isso que
separa um agente de um script fixo."
""")

s = sl_bullets("O que é \"ferramenta\", tecnicamente", "A peça que faz o agente sair do texto",
               [("Uma ferramenta é uma função comum, com nome e parâmetros descritos", "o modelo lê essa descrição e decide se e quando usá-la"),
                ("O modelo nunca executa a ferramenta sozinho", "ele só devolve \"quero chamar tal função, com tais parâmetros\""),
                ("Quem executa de verdade é o código em volta do modelo", "e é exatamente aí que mora todo o controle possível, tema do Bloco 06"),
                ("Consultar um banco, chamar uma API, editar um arquivo, mandar um e-mail", "tudo isso já foi usado como ferramenta de agente")],
               subtitle="Sem essa separação entre \"decidir\" e \"executar\", não existe controle possível.")
notes(s, "7 min", "ESSENCIAL", FELIPE,
      """
"Última peça deste bloco: o que é uma ferramenta, tecnicamente.

É uma função comum, de código comum, com um nome e uma descrição dos parâmetros que
ela espera. O modelo lê essa descrição, junto com o pedido do usuário, e decide se e
quando vale a pena chamar.

Ponto crucial: o modelo NUNCA executa a ferramenta sozinho. Ele só devolve um pedido
estruturado, "quero chamar tal função, com tais parâmetros". Quem executa de
verdade é o código em volta do modelo, escrito por uma pessoa.

É exatamente essa separação, entre decidir e executar, que abre espaço para todo o
controle que existe hoje sobre agente. A gente aprofunda isso no Bloco 06, depois do
intervalo.

Consultar banco, chamar API, ler e escrever arquivo, mandar mensagem: tudo isso já
foi usado como ferramenta de agente, em algum produto real."
""")

# --------------------------------------------------------------------------
# BLOCO 04: Mão na massa, seu primeiro agente (20h15 às 20h45)
# --------------------------------------------------------------------------
s = sl_section("04", "Mão na massa: seu primeiro agente",
               "A mesma pergunta do Bloco 03, agora rodando de verdade",
               "20h15 às 20h45  ·  30 minutos")
notes(s, "20h15 às 20h45 (30 min)", "ESSENCIAL", FELIPE,
      """
DISTRIBUIÇÃO:
  Mecânica e abertura do notebook    8 min
  Prática guiada                    22 min

Mudança de plano do curso: esta prática entrou na segunda de propósito, para a
quinta-feira (Aula 14) ficar inteira livre para mentoria individual de squad, com a
Semana 8 e o Demo Day se aproximando. Isso quebra a regra padrão das segundas (zero
código ao vivo), de forma deliberada.
""")

s = sl_bullets("Como vai funcionar", "Vocês vão construir o exato exemplo do Bloco 03",
               [("O notebook", "link fixado no Discord, chama-se Aula_13_Alunos_Construindo_Primeiro_Agente"),
                ("Uma chave gratuita da NVIDIA", "o notebook explica em duas linhas como gerar, no próprio build.nvidia.com"),
                ("Leitura guiada, código já pronto", "sem lacuna para preencher, o foco de hoje é ver o loop pensa, age, observa rodando de verdade"),
                ("A ferramenta é um servidor MCP de verdade", "o mesmo protocolo do Bloco 02 e do Bloco 06, rodando dentro do próprio notebook")],
               subtitle="Ao final, vocês terão construído, sozinhos, exatamente o loop do slide anterior.")
notes(s, "8 min", "ESSENCIAL", FELIPE,
      """
"Mecânica rápida antes de começar. O notebook está no Discord, chamado
Aula_13_Alunos_Construindo_Primeiro_Agente. Vocês vão precisar de uma chave gratuita
da NVIDIA, o próprio notebook explica como gerar em menos de um minuto.

O código já vem pronto, é leitura guiada, sem lacuna para preencher: hoje o foco é
ver o loop pensa, age, observa, responde rodando de verdade, não decorar sintaxe de
Python.

E a ferramenta que o agente vai usar não é simulada: é um servidor MCP de verdade,
rodando dentro do próprio notebook, com uma única ferramenta que consulta a taxa de
contestação de um lojista, na mesma base que vocês já conhecem."
""")

s = sl_statement("Agora é com vocês", "22 minutos.\nO mesmo agente do Bloco 03, na sua tela.",
                 "Travou? Chat, com o número do passo. Edmar e Felipe estão de olho o tempo todo.")
notes(s, "22 min (projetado o tempo todo)", "ESSENCIAL", "Edmar + Felipe",
      """
Este slide fica projetado durante toda a prática, sem narração contínua. Circular
pelo chat, responder dúvida por dúvida.

Checklist do mentor:
- Quem travar gerando a chave da NVIDIA: confirmar que copiou a chave inteira,
  incluindo o prefixo nvapi-.
- Quem terminar antes do tempo: sugerir testar com um id_lojista diferente, ou
  perguntar algo que não precise da ferramenta, para ver o agente decidir sozinho.
- Aos 20h40 (5 minutos do fim): avisar no chat pedindo para todo mundo garantir que
  rodou pelo menos até o Passo 4 (a ferramenta funcionando), mesmo que o Passo 6 (o
  loop completo) ainda não tenha terminado.
""")

# --------------------------------------------------------------------------
# BLOCO 05: O que muda em relação a uma chamada única (20h45 às 21h05)
# --------------------------------------------------------------------------
s = sl_section("05", "O que muda em relação a uma chamada única",
               "Onde exatamente a diferença mora",
               "20h45 às 21h05  ·  20 minutos")
notes(s, "20h45 às 21h05 (20 min)", "ESSENCIAL", FELIPE,
      """
DISTRIBUIÇÃO:
  Comparação lado a lado    7 min
  Exemplo concreto           7 min
  Interação                  6 min
""")

s = sl_two_col("Comparando", "Chamada única de LLM x Agente",
               "CHAMADA ÚNICA",
               ["Um prompt entra, uma resposta sai",
                "Não guarda estado entre uma chamada e outra",
                "Não age no mundo, só descreve o que faria",
                "Se a resposta vier errada, a conversa acaba ali"],
               "AGENTE",
               ["Um objetivo entra, vários passos acontecem até a resposta",
                "Guarda estado ao longo de toda a tarefa",
                "Age de verdade, através de ferramentas reais",
                "Se um passo falhar, pode tentar de novo, sozinho"],
               subtitle="A diferença não está no modelo. Está no que existe em volta dele.")
notes(s, "7 min", "ESSENCIAL", FELIPE,
      """
"Lado a lado. Chamada única: um prompt entra, uma resposta sai, e acabou. Não guarda
nada entre uma chamada e outra, não age no mundo de verdade, só descreve o que
faria. E se a resposta vier errada, a conversa simplesmente acaba ali, sem
correção automática.

Agente: um objetivo entra, e vários passos acontecem até chegar numa resposta.
Guarda estado ao longo de toda a tarefa. Age de verdade, através de ferramentas.
E se um passo falhar, pode tentar de novo sozinho, sem ninguém pedir.

A frase que fecha isso: a diferença não está no modelo, o mesmo modelo pode fazer
as duas coisas. Está no que existe em volta dele, o loop, as ferramentas, o
estado."
""")

s = sl_cards("Um exemplo concreto", "\"Qual o clima em Curitiba agora?\"",
             [("Só o LLM",
               "Sem acesso a dado em tempo real, o modelo só conhece o que estava nos dados de treino.\n\nOu inventa uma resposta plausível, ou admite que não sabe."),
              ("O mesmo modelo, como agente",
               "Reconhece que precisa de um dado atual, chama uma ferramenta de clima de verdade, lê o resultado, e responde com o número real de agora.")],
             cols=2, card_h=3.0)
notes(s, "7 min", "ESSENCIAL", FELIPE,
      """
"Exemplo simples, de propósito, para ficar bem claro. Pergunta: qual o clima em
Curitiba agora?

Só o LLM, sem ferramenta nenhuma: ele não tem acesso a dado em tempo real, só
conhece o que estava nos dados de treino. Duas saídas possíveis, e nenhuma boa:
inventa uma resposta plausível, ou admite que não sabe.

O mesmo modelo, agora como agente: ele reconhece que precisa de um dado atual, chama
uma ferramenta de clima de verdade, lê o resultado real, e responde com o número
certo de agora.

O modelo é o mesmo. A diferença inteira está em ter, ou não ter, uma ferramenta e um
loop em volta dele."
""")

s = sl_interaction("Interação rápida", "Isso é uma chamada única, ou um agente?",
                    "No chat: para cada cenário, escreva \"única\" ou \"agente\"",
                    ["Você pede um resumo de um texto que colou na conversa",
                     "Você pede para reservar o hotel mais barato disponível numa data",
                     "Você pede a tradução de uma frase para o inglês",
                     "Você pede para investigar por que as vendas caíram, e ele consulta o banco sozinho"])
notes(s, "6 min", "ESSENCIAL", FELIPE,
      """
"No chat: para cada cenário, escreva única ou agente.

Resumir um texto que já está na conversa? Única, não precisa de ferramenta nem de
ação no mundo.

Reservar o hotel mais barato numa data? Agente, precisa buscar preços reais e
executar uma reserva de verdade.

Traduzir uma frase? Única.

Investigar por que as vendas caíram, consultando o banco sozinho? Agente, na
veia: loop, ferramenta, e provavelmente mais de um passo até achar a causa."
""")

# --------------------------------------------------------------------------
# INTERVALO (21h05 às 21h20)
# --------------------------------------------------------------------------
s = sl_break()
notes(s, "15 min", "ESSENCIAL", EU, "Intervalo. Sem apresentação.")

# --------------------------------------------------------------------------
# BLOCO 06: Como controlamos um agente (21h20 às 21h50)
# --------------------------------------------------------------------------
s = sl_section("06", "Como controlamos um agente",
               "A resposta ao risco que a Aula 1 já tinha avisado",
               "21h20 às 21h50  ·  30 minutos")
notes(s, "21h20 às 21h50 (30 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Callback ao risco da Aula 1    3 min
  Mecanismos de controle        14 min
  Observabilidade e avaliação    8 min
  MCP como parte do controle     5 min
""")

s = sl_statement("Lembrando",
                 "\"Perder controle e rastreabilidade.\"",
                 "O risco que a Fase 5 da Aula 1 já apontou para agentes de IA.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Vocês já ouviram esse risco na Aula 1. Hoje a gente aprende, de verdade, como
evitar que ele aconteça."
""")

s = sl_cards("Mecanismos de controle", "Quatro camadas, uma em cima da outra",
             [("Permissão e escopo",
               "O agente só enxerga as ferramentas que alguém deu para ele.\n\nUm agente de atendimento não deveria nem saber que existe uma ferramenta de apagar dado."),
              ("Humano no loop",
               "Ações irreversíveis (mandar dinheiro, apagar registro, publicar algo) esperam aprovação de uma pessoa antes de executar."),
              ("Sandbox",
               "O agente roda num ambiente isolado, sem acesso direto ao sistema real, até provar que se comporta bem."),
              ("Limite de custo e de passos",
               "Um teto de quantas chamadas de ferramenta e quanto tempo o agente pode gastar numa tarefa, para nunca repetir o loop infinito do AutoGPT.")],
             cols=2, card_h=3.3)
notes(s, "14 min", "ESSENCIAL", EU,
      """
"Quatro camadas de controle, cada uma resolvendo um pedaço do problema.

Permissão e escopo: o agente só enxerga as ferramentas que alguém deu para ele. Um
agente de atendimento ao cliente não deveria nem saber que existe uma ferramenta de
apagar registro do banco.

Humano no loop: ações irreversíveis, mandar dinheiro, apagar dado, publicar
conteúdo, esperam aprovação explícita de uma pessoa antes de executar de verdade.

Sandbox: o agente roda num ambiente isolado, sem acesso direto ao sistema de
produção, até provar que se comporta de forma confiável.

Limite de custo e de passos: um teto de quantas ferramentas ele pode chamar e quanto
tempo pode gastar numa única tarefa. Isso, sozinho, já evita o loop infinito que
matou a credibilidade do AutoGPT."
""")

s = sl_bullets("Observabilidade e avaliação", "Controlar também é conseguir enxergar",
               [("Tracing: um log de cada passo do loop", "toda decisão, toda chamada de ferramenta, todo resultado, guardado e revisável depois"),
                ("Isso é o que resolve \"rastreabilidade\"", "sem log passo a passo, ninguém consegue explicar por que o agente fez o que fez"),
                ("Avaliação automatizada, não só \"parece que funcionou\"", "testar o agente contra casos conhecidos, com resposta certa esperada, antes de confiar nele"),
                ("Sem isso, cada atualização de prompt vira uma aposta", "com tracing e avaliação, vira um experimento medido")],
               subtitle="Um agente sem log é um agente em que ninguém confia, mesmo quando funciona.")
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Controlar também é conseguir enxergar. Tracing é um log de cada passo do loop:
toda decisão, toda chamada de ferramenta, todo resultado, guardado e revisável
depois.

Isso é literalmente o que resolve a palavra "rastreabilidade" do risco da Aula 1.
Sem log passo a passo, ninguém consegue explicar por que o agente fez o que fez,
mesmo quando ele acerta.

E avaliação automatizada: testar o agente contra casos conhecidos, com resposta
certa já sabida, antes de confiar nele em produção. Sem isso, toda atualização de
prompt vira uma aposta às cegas. Com isso, vira um experimento medido, igual ao que
vocês já viram com treino e teste, lá na Aula 11."
""")

s = sl_bullets("O MCP também é controle", "Padronizar o que um agente pode tocar",
               [("O MCP, visto no Bloco 02, não é só conveniência técnica", "é também um jeito de padronizar e auditar quais ferramentas um agente tem acesso"),
                ("Um servidor MCP declara exatamente o que oferece", "fica explícito, documentado, e revisável, em vez de escondido dentro do código de cada integração"),
                ("Isso facilita a permissão e o escopo do primeiro card deste bloco", "é mais fácil dizer \"sim\" ou \"não\" para um servidor inteiro do que auditar função por função")])
notes(s, "5 min", "ESSENCIAL", EU,
      """
"Uma última conexão antes de seguir: o MCP, que vocês viram no Bloco 02 como marco
histórico, também é uma peça de controle.

Um servidor MCP declara exatamente o que oferece, de forma explícita e documentada.
Isso facilita demais a permissão e o escopo: em vez de auditar função por função
escondida dentro do código, dá para decidir "sim" ou "não" para um servidor MCP
inteiro, sabendo exatamente o que ele expõe."
""")

# --------------------------------------------------------------------------
# BLOCO 07: Principais soluções para criar um agente (21h50 às 22h20)
# --------------------------------------------------------------------------
s = sl_section("07", "Principais soluções para criar um agente",
               "O cardápio de ferramentas do mercado hoje",
               "21h50 às 22h20  ·  30 minutos")
notes(s, "21h50 às 22h20 (30 min)", "ESSENCIAL", FELIPE,
      """
DISTRIBUIÇÃO:
  Framework landscape          12 min
  MCP como padrão comum         8 min
  Caminho sem programar        10 min
""")

s = sl_table("O cardápio de hoje", "Seis nomes que vocês vão ouvir no mercado",
             ["Solução", "Quem mantém", "Forte em"],
             [["LangGraph", "LangChain", "Produção com estado, com o maior número de clientes empresariais grandes"],
              ["CrewAI", "Comunidade CrewAI", "Prototipagem rápida, forte adoção em experimentos e provas de conceito"],
              ["AutoGen / AG2", "Microsoft e comunidade", "Múltiplos agentes conversando entre si para dividir uma tarefa"],
              ["OpenAI Agents SDK", "OpenAI", "Kit oficial integrado ao ecossistema de modelos da própria OpenAI"],
              ["Google ADK", "Google", "Kit oficial integrado ao ecossistema Google Cloud e Gemini"],
              ["Claude Agent SDK", "Anthropic", "Integração mais profunda com MCP, forte em agente de codificação"]],
             widths=[0.25, 0.25, 0.50])
notes(s, "12 min", "ESSENCIAL", FELIPE,
      """
"Seis nomes que vocês vão ouvir bastante no mercado, cada um com uma força
diferente.

LangGraph, da LangChain: hoje é quem mais tem cliente grande de verdade, nomes como
Uber, LinkedIn, JPMorgan, porque foi desenhado para produção, com estado bem
controlado e trilha de auditoria.

CrewAI: mais leve para prototipar rápido. Teve mais de 2 bilhões de execuções de
agente registradas em doze meses, e aparece em quase metade das empresas da Fortune
500 em algum experimento.

AutoGen, hoje também chamado AG2, da Microsoft: forte em múltiplos agentes
conversando entre si, cada um especialista numa parte da tarefa.

E os três kits oficiais dos grandes laboratórios: OpenAI Agents SDK, Google ADK, e
Claude Agent SDK da Anthropic, este último com a integração mais profunda com MCP e
foco forte em agente de codificação, o tipo de agente que, aliás, ajudou a montar
o material desta própria aula."
""")

s = sl_bullets("MCP como padrão comum", "A peça que atravessa quase todas as soluções acima",
               [("Praticamente todo framework da tabela anterior já fala MCP", "não é mais recurso de um fornecedor só, virou linguagem comum"),
                ("Isso resolve o problema antigo do N vezes M", "antes, cada par modelo mais ferramenta precisava de uma integração própria"),
                ("Hoje já são mais de 16 mil servidores MCP publicados", "banco de dados, planilha, sistema interno, quase tudo já tem um")],
               subtitle="Escolher framework virou menos importante do que escolher bem as ferramentas MCP.")
notes(s, "8 min", "ESSENCIAL", FELIPE,
      """
"O MCP atravessa quase toda a tabela anterior. Praticamente todo framework grande
já fala esse protocolo, não é mais recurso exclusivo de um fornecedor.

Isso resolve o problema antigo do N vezes M: antes, cada combinação de modelo e
ferramenta precisava da própria integração feita à mão. Hoje já são mais de 16 mil
servidores MCP publicados, cobrindo banco de dados, planilha, sistema interno, quase
tudo.

Consequência prática: escolher o framework virou menos decisivo do que escolher bem
quais ferramentas MCP conectar."
""")

s = sl_cards("E quem não programa", "Também dá para montar agente sem escrever código",
             [("Ferramentas no-code",
               "Plataformas visuais de automação (o tipo n8n, Zapier) já oferecem blocos de \"agente de IA\" prontos, ligando gatilho, modelo e ferramenta sem escrever linha de código."),
              ("O trade-off",
               "Menos controle fino e menos flexibilidade do que os frameworks da tabela anterior, mas caminho real para quem está começando ou prototipando rápido.")],
             cols=2, card_h=3.2)
notes(s, "10 min", "ESSENCIAL", FELIPE,
      """
"Última coisa deste bloco, importante para a turma mista que vocês são: não precisa
programar para montar um agente simples.

Plataformas visuais de automação já oferecem bloco pronto de "agente de IA",
ligando gatilho, modelo e ferramenta sem escrever uma linha de código.

O trade-off é real: menos controle fino, menos flexibilidade do que os frameworks
que vimos. Mas é um caminho de verdade para quem está começando, ou só quer testar
uma ideia rápido antes de investir em código."
""")

# --------------------------------------------------------------------------
# BLOCO 08: O estado da arte hoje (22h20 às 22h45)
# --------------------------------------------------------------------------
s = sl_section("08", "O estado da arte hoje",
               "Quem usa, em que escala, e onde ainda trava",
               "22h20 às 22h45  ·  25 minutos")
notes(s, "22h20 às 22h45 (25 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Agentes de codificação    8 min
  Adoção empresarial real   8 min
  Onde ainda trava          9 min
""")

s = sl_statement("O exemplo mais próximo de vocês",
                 "Este material foi construído\ncom a ajuda de um agente de codificação.",
                 "Slides, roteiro e documentos de apoio, com um agente escrevendo, testando e corrigindo.")
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Vou dar o exemplo mais próximo que existe: este material, os slides que vocês
estão vendo agora, o roteiro que estamos seguindo, foi construído com a ajuda de um
agente de codificação.

Isso é a categoria de agente que mais amadureceu nos últimos dois anos: ferramentas
como Claude Code, Cursor, e o modo agente do GitHub Copilot leem um repositório
inteiro, escrevem código, rodam testes de verdade, leem o resultado, e corrigem
sozinhas o que deu errado, tudo dentro do mesmo loop que a gente viu no Bloco 03.
É ferramenta real de trabalho, usada todo dia por quem programa profissionalmente."
""")

s = sl_table("Adoção real, com número", "Não é mais só experimento de laboratório",
             ["Quem", "O que mostra"],
             [["LangGraph", "Cliente grande e real em produção: Uber, LinkedIn, JPMorgan, Klarna, Cisco, entre outros"],
              ["CrewAI", "Mais de 2 bilhões de execuções de agente em doze meses, presente em quase metade da Fortune 500"],
              ["Claude Agent SDK", "Lançado em 2025, com adoção concentrada em ferramenta de desenvolvedor e agente de codificação"]],
             widths=[0.28, 0.72])
notes(s, "8 min", "ESSENCIAL", EU,
      """
"Números reais, não projeção. LangGraph tem cliente grande de verdade rodando em
produção: Uber, LinkedIn, JPMorgan, Klarna, Cisco.

CrewAI passou de 2 bilhões de execuções de agente em doze meses, e está presente em
quase metade das empresas da Fortune 500, mesmo que em fase de experimento em
muitas delas.

E o Claude Agent SDK, lançado em 2025, cresceu com adoção concentrada em ferramenta
de desenvolvedor, o tipo de agente de codificação que citei no slide anterior.

Isso não é mais hype de 2023. É ferramenta rodando em empresa grande, hoje."
""")

s = sl_bullets("Onde ainda trava", "O estado da arte também tem limite conhecido",
               [("Tarefa muito longa ainda acumula erro", "quanto mais passos no loop, maior a chance de um erro cedo contaminar tudo que vem depois"),
                ("Custo ainda é imprevisível em tarefa complexa", "mais passos significam mais chamadas de modelo, e a conta cresce junto"),
                ("Avaliar um agente continua mais difícil que avaliar um modelo simples", "não existe só uma resposta certa, existe um caminho inteiro para julgar"),
                ("Viés e erro do modelo se multiplicam dentro do loop", "um erro pequeno numa decisão early pode se propagar por vários passos seguintes")],
               subtitle="Quem promete agente perfeito, sem limite, ainda está vendendo o hype de 2023.")
notes(s, "9 min", "ESSENCIAL", EU,
      """
"E para fechar com os pés no chão: o estado da arte também tem limite conhecido.

Tarefa muito longa ainda acumula erro: quanto mais passos no loop, maior a chance de
um erro no início contaminar tudo que vem depois.

Custo ainda é imprevisível em tarefa complexa, porque mais passos significam mais
chamadas de modelo.

Avaliar um agente continua mais difícil que avaliar um modelo simples, porque não
existe uma resposta certa só, existe um caminho inteiro de decisões para julgar.

E viés e erro do modelo se multiplicam dentro do loop, um erro pequeno cedo pode se
propagar.

Quem promete hoje um agente perfeito, sem limite nenhum, ainda está vendendo o hype
de 2023, não o estado da arte real de agora."
""")

# --------------------------------------------------------------------------
# BLOCO 09: Encerramento (22h45 às 23h05)
# --------------------------------------------------------------------------
s = sl_section("09", "Encerramento",
               "O que vocês levam de hoje e o que vem na quinta",
               "22h45 às 23h05  ·  20 minutos")
notes(s, "22h45 às 23h05 (20 min)", "ESSENCIAL", EU,
      """
DISTRIBUIÇÃO:
  Recapitulação             4 min
  O que vem pela frente     3 min
  Q&A                       10 min  (elástico, absorve atraso)
  Fechamento                3 min
""")

s = sl_bullets("Encerramento", "Sete ideias para levar de hoje",
               [("Agente não nasceu com o hype de 2023", "o paper que deu origem ao loop é de outubro de 2022, um mês antes do próprio ChatGPT"),
                ("Um agente é modelo mais loop mais ferramenta mais estado", "as quatro peças juntas, não o modelo sozinho"),
                ("Vocês construíram isso com a própria mão, hoje", "um agente real, com uma ferramenta servida por MCP de verdade, não uma simulação"),
                ("A diferença de uma chamada única mora no que existe em volta do modelo", "o loop, a ferramenta, o estado entre os passos"),
                ("Controlar um agente é possível, com camada em cima de camada", "permissão, humano no loop, sandbox, limite, tracing e avaliação"),
                ("O mercado já tem seis ou mais soluções consolidadas", "de framework de produção a plataforma sem código, passando pelo padrão comum MCP"),
                ("O estado da arte é real, mas tem limite conhecido", "tarefa longa, custo e avaliação continuam sendo o desafio em aberto")],
               subtitle="Se você levar só essas sete frases, a noite cumpriu o objetivo.",
               numbered=True)
notes(s, "4 min", "ESSENCIAL", EU,
      """
"Sete ideias para levar de hoje.

Agente não nasceu com o hype de 2023: o paper do loop é de outubro de 2022.

Um agente é modelo mais loop mais ferramenta mais estado, as quatro peças juntas.

E vocês construíram isso com a própria mão, hoje: um agente real, com uma
ferramenta servida por MCP de verdade.

A diferença de uma chamada única mora no que existe em volta do modelo.

Controlar um agente é possível, camada em cima de camada.

O mercado já tem várias soluções consolidadas, de framework robusto a plataforma sem código.

E o estado da arte é real, mas tem limite conhecido: tarefa longa, custo e avaliação
continuam sendo o desafio em aberto."
""")

s = sl_two_col("Próximos encontros", "O que vem pela frente",
               "QUINTA · Semana 7",
               ["Sem laboratório novo: a prática de agente já foi hoje",
                "A noite inteira fica livre para mentoria com Edmar e Felipe",
                "Traga dúvida de squad, de projeto, ou do próprio agente de hoje"],
               "SEGUNDA · Semana 8",
               ["Demo Day se aproximando",
                "Formato e tema a confirmar"],
               subtitle="Mudança de formato: quinta vira mentoria aberta, não laboratório guiado.")
notes(s, "3 min", "ESSENCIAL", EU,
      """
"Reparem que a quinta desta semana muda de formato. Vocês já construíram o agente
hoje, então não tem laboratório novo guiado na quinta. A noite inteira vira mentoria
aberta, com Edmar e Felipe disponíveis para dúvida de squad, de projeto, ou de
qualquer coisa que sobrou de hoje.

E a Semana 8 já é a reta final da Etapa 1, com o Demo Day se aproximando."
""")

s = sl_statement("Antes de ir", "Perguntas?",
                 "Escreva no chat. O que não der tempo, respondemos no Discord ainda hoje.")
notes(s, "10 min", "ESSENCIAL", EU,
      """
PERGUNTAS PREVISÍVEIS DE HOJE:

- "Preciso escolher um framework para aprender já?"
  Não. O importante hoje é reconhecer os nomes e saber o que cada um resolve melhor.
  A escolha de ferramenta vem depois, quando o problema real estiver na mesa.

- "Agente substitui programador?"
  Não do jeito que a pergunta sugere. Ele muda o trabalho de quem programa, mas
  ainda precisa de alguém definindo objetivo, revisando resultado e decidindo o que
  aprovar. O próprio material desta aula teve revisão humana o tempo todo.

- "Dá para usar agente sem saber programar?"
  Sim, com as plataformas sem código do Bloco 07, embora com menos controle fino do
  que os frameworks de produção. E vocês acabaram de ver que mesmo com código, um
  agente de uma ferramenta só cabe em um notebook curto, no Bloco 04.

- "Isso cai no projeto final?"
  Cai direto, principalmente para quem escolher a trilha de GenAI ou Programação na
  Etapa 2.
""")

s = sl_closing()
notes(s, "3 min", "ESSENCIAL", EU,
      """
FECHAMENTO (30 segundos):

"Obrigado pela noite de hoje. Vocês saem daqui sabendo, de verdade, o que é um
agente por dentro, não só o nome bonito. Revisem os slides antes de quinta,
principalmente o loop do Bloco 03. Nos vemos lá. Boa noite!"

DEPOIS DE ENCERRAR:
- Parar a gravação.
- Anotar quais dos seis blocos geraram mais pergunta no chat, para calibrar o corte
  se uma próxima turma precisar de uma versão ainda mais curta.
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

out = ROOT / "docs" / "aula-13"
out.mkdir(parents=True, exist_ok=True)
dest = out / "AI-Talent-Academy-Aula13.pptx"
prs.save(dest)
print(f"OK: {dest}  ({len(prs.slides._sldIdLst)} slides)  "
      f"Roboto, sem travessões, tamanho único por bloco.")
