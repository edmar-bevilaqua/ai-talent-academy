# -*- coding: utf-8 -*-
"""
Exporta as notas do apresentador do PPTX para um markdown imprimivel.

Uso: python scripts/exportar_roteiro_aula04.py
Saida: docs/aula-04/02-roteiro-do-apresentador.md

Rode isto SEMPRE que regerar o deck, para o roteiro nao ficar defasado.
"""
from pathlib import Path
from pptx import Presentation

root = Path(__file__).resolve().parents[1]
src = root / "docs" / "aula-04" / "AI-Talent-Academy-Aula04.pptx"
dest = root / "docs" / "aula-04" / "02-roteiro-do-apresentador.md"

prs = Presentation(src)

linhas = [
    "# Roteiro do apresentador: Aula 4 (Semana 2, quinta-feira)",
    "",
    "> Gerado automaticamente a partir das notas do deck.",
    "> Não edite este arquivo à mão: edite `scripts/gerar_slides_aula04.py` e rode",
    "> `python scripts/gerar_slides_aula04.py && python scripts/exportar_roteiro_aula04.py`.",
    "",
    "**Como usar:** imprima ou deixe aberto num segundo monitor. O texto entre aspas é",
    "fala sugerida. Adapte para a sua voz, não decore: o que importa é a sequência de ideias.",
    "",
    "---",
    "",
]

for i, slide in enumerate(prs.slides, 1):
    titulo = ""
    for sh in slide.shapes:
        if sh.has_text_frame and sh.text_frame.text.strip():
            t = sh.text_frame.text.strip().split("\n")[0]
            if len(t) > 3 and not t.isdigit():
                titulo = t
                break
    linhas.append(f"## Slide {i} · {titulo}")
    linhas.append("")
    if slide.has_notes_slide:
        nota = slide.notes_slide.notes_text_frame.text.strip()
        if nota:
            linhas.append("```")
            linhas.append(nota)
            linhas.append("```")
    linhas.append("")

dest.write_text("\n".join(linhas), encoding="utf-8")
print(f"OK: {dest}  ({len(prs.slides)} slides)")
