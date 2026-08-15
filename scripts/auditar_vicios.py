# -*- coding: utf-8 -*-
"""
Auditor dos vicios de escrita que soam a IA (regra 3.5 do CLAUDE.md).

Uso:
    python scripts/auditar_vicios.py                    # audita tudo
    python scripts/auditar_vicios.py scripts/gerar_slides_aula02.py

Saida: relatorio em C:/tmp/auditoria-vicios.txt (o console do Windows quebra com acento).

IMPORTANTE: este auditor tem falsos positivos de proposito. Ele aponta candidatos, e a
decisao e humana. O que ele NAO consegue julgar sozinho:
  - rotulo estrutural ("FASE 1: Traducao", "FORA DO ESCOPO: ...") nao e o vicio 3
  - marcacao operacional ESSENCIAL/DESCARTAVEL nao e o vicio 5
  - "otimizacao" como nome do degrau da escada e termo tecnico, nao adjetivo decorativo
  - repeticao em escadinha funciona melhor na FALA do que na prosa escrita

Rode isto ANTES de considerar qualquer conteudo pronto.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

# Termos que o auditor ignora por serem rotulo operacional ou nome tecnico do projeto.
ISENTOS = [
    r'\b(ESSENCIAL|DESCARTÁVEL)\b',          # marcacao de corte no roteiro
    r'mapa essencial × descartável',
    r'\botimização\b(?=[,)]|\s+de rotas|\s*\|)',  # degrau da escada, termo tecnico
]

# Rotulos de metadado seguidos de nome proprio. O artigo isenta explicitamente nome
# proprio, fala, citacao e enumeracao da regra do vicio 4.
ROTULOS_META = (
    r'(?:Apresenta|Fonte|Fontes|Caso|Autor|Autores|Relator|Grupo|Data|Quem|Local|'
    r'Exemplo|Ex|Público|Publico|Assunto|Link|Obs|Nota|Semanas?|Slide|Bloco|'
    r'FORTE EM|SAÍDA|SAIDA|Meta|Baseline|Objetivo|Condução|Conducao|Semanas?|Aula|Plano da Aula \d|Roteiro do apresentador|existem)'
)

VICIOS = [
    ("V2 pergunta retórica em série",
     r'\?\s*(Porque|Não\.|Sim\.|Parece|Cria)\b', 0),

    ("V3 título-manchete com dois-pontos",
     r'(?m)^#{1,4} [^:\n]{4,45}: [a-zà-ú]', 0),

    # Filtrado depois por `_v4_valido`: rotulo de metadado costuma preceder nome proprio,
    # e o artigo isenta nome proprio explicitamente.
    ("V4 maiúscula depois de dois-pontos",
     r'\w: [A-ZÀ-Ú][a-zà-ú]{2,}', 0),

    ("V5 vocabulário genérico de robô",
     r'\b(insight\w*|crucial|fundamental|essencia(l|is)|mergulh\w+|naveg(ar|ando)|'
     r'revolucion\w+|inspirador\w*|valios[oa]s?|significativ[oa]s?|otimiz\w+|'
     r'contínu[oa]s?|vital|em um mundo|num mundo)\b', re.I),

    ("V6 contraste raso (não é X, é Y)",
     r'[Nn]ão é [^.\n|]{2,45}[.,]\s*[ÉéEe][ .]', 0),

    ("V6 contraste raso invertido (é X, não Y)",
     r'\bé [^.\n|]{2,40}, não [^.\n|]{2,40}', 0),

    ("V8 adjetivo que enfeita sem explicar",
     r'\b(incrível|sólid[oa]|extraordinári[oa]|poderos[oa]|robust[oa]|impressionante|'
     r'fantástic[oa]|excepciona(l|is))\b', re.I),

    ("V9 fórmula Sem X. Sem Y. Só Z.",
     r'[Ss]em [^.\n|]{2,25}\.\s*[Ss]em ', 0),
]


_RE_META = re.compile(ROTULOS_META + r'\s*$')


def _v4_valido(texto: str, m: re.Match) -> bool:
    """Descarta o V4 quando os dois-pontos seguem um rotulo de metadado.

    "Apresenta: Edmar" e "Fonte: Netflix Prize" tem nome proprio depois, e o artigo
    isenta nome proprio da regra. Ja "um objetivo claro: Conquistar clientes" e o vicio.
    """
    ini_linha = texto.rfind("\n", 0, m.start()) + 1
    antes = texto[ini_linha:m.start() + 1].strip().lstrip("-*#> |")
    return not _RE_META.search(antes)


def auditar(caminho: pathlib.Path):
    texto = caminho.read_text(encoding="utf-8")
    for iso in ISENTOS:
        texto = re.sub(iso, "_", texto, flags=re.I)
    achados = []
    for nome, padrao, flags in VICIOS:
        for m in re.finditer(padrao, texto, flags):
            if nome.startswith("V4") and not _v4_valido(texto, m):
                continue
            ini = max(0, m.start() - 60)
            trecho = texto[ini:m.end() + 45].replace("\n", " ")
            achados.append(f"  [{nome}]\n    ...{trecho}...")
    return achados


def main():
    if len(sys.argv) > 1:
        alvos = [pathlib.Path(a).resolve() for a in sys.argv[1:]]
    else:
        alvos = sorted(ROOT.glob("scripts/gerar_slides_*.py"))
        alvos += sorted(ROOT.glob("docs/aula-*/*.md"))
        alvos += [ROOT / "CLAUDE.md"]

    linhas = ["AUDITORIA DE VICIOS DE ESCRITA (regra 3.5 do CLAUDE.md)",
              "=" * 70,
              "Falsos positivos sao esperados. Leia cada um e decida.",
              ""]
    total = 0
    for alvo in alvos:
        if not alvo.exists():
            continue
        achados = auditar(alvo)
        if achados:
            total += len(achados)
            try:
                rotulo = alvo.relative_to(ROOT)
            except ValueError:
                rotulo = alvo
            linhas.append(f"\n### {rotulo}  ({len(achados)} candidatos)")
            linhas.extend(achados)

    linhas.append(f"\n{'=' * 70}\nTOTAL DE CANDIDATOS: {total}")
    destino = pathlib.Path("C:/tmp/auditoria-vicios.txt")
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text("\n".join(linhas), encoding="utf-8")
    print(f"OK: {destino}  ({total} candidatos em {len(alvos)} arquivos)")


if __name__ == "__main__":
    main()
