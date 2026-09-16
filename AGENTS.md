# Agentes do AI Talent Academy

Este repositório dispõe de agentes especializados para manter a qualidade instrucional, a consistência visual e o rigor técnico de todo o material produzido.

---

## Agentes disponíveis

### `criador-de-aulas`

Especialista em planejar, redigir e gerar os pacotes completos de aula do AI Talent Academy.

- **Localização**: `.github/agents/criador-de-aulas.agent.md` e `.claude/agents/criador-de-aulas.md`
- **Invocação no Copilot CLI**: `/agent criador-de-aulas`
- **Escopo**:
  - Geração de apresentações `.pptx` executáveis via script Python (`python-pptx`), sem edição manual direta.
  - Redação de notas completas de apresentador com roteiro de fala verbatim em primeira pessoa e marcações operacionais (`ESSENCIAL` ou `DESCARTÁVEL`).
  - Criação do pacote de apoio (`01-plano-da-aula.md`, `02-roteiro-do-apresentador.md`, `03-material-de-apoio-participante.md`, planos de interação e e-mails).
  - Aplicação estrita da identidade visual White Cube (tamanho 20 × 11,25 polegadas, fonte Roboto 100%, piso de 17pt, um tamanho por caixa de texto, fundos oficiais).
  - Eliminação de travessões (em dash U+2014 e en dash U+2013).
  - Eliminação rigorosa dos vícios de escrita de IA (regra 3.5 do `CLAUDE.md`), com auditoria obrigatória via `python scripts/auditar_vicios.py`.

---

## Como acionar o agente

No GitHub Copilot CLI:
```bash
/agent criador-de-aulas
```

Exemplos de pedidos para o agente:
- *"Crie o pacote completo da Aula 12 (Semana 6, quinta-feira) sobre treinamento prático de modelos com Scikit-Learn no Google Colab."*
- *"Revise os slides da Aula 03 incorporando o feedback da turma e regere o roteiro."*
- *"Audite os textos da Aula 11 contra os vícios de escrita de IA e corrija as ocorrências."*
