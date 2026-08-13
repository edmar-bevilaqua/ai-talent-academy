# Aula 1: Semana 1, segunda-feira

Pacote completo da primeira aula do **AI Talent Academy**, no padrão visual White Cube.
19h00 às 22h00 · online · ~190 participantes
Condução: Edmar Bevilaqua + Felipe André Bach Alves

---

## O que tem aqui

| Arquivo | O que é | Para quem |
|---|---|---|
| **`AI-Talent-Academy-Aula01.pptx`** | O deck: 64 slides, com roteiro de fala nas notas de cada slide | Vocês dois |
| [`01-plano-da-aula.md`](01-plano-da-aula.md) | Cronômetro, marcos de controle, mapa essencial × descartável, checklists e riscos | Vocês dois |
| [`02-roteiro-do-apresentador.md`](02-roteiro-do-apresentador.md) | Todas as notas do deck em markdown imprimível | Vocês dois |
| [`03-material-de-apoio-participante.md`](03-material-de-apoio-participante.md) | Resumo + glossário + tarefas até quinta | Participantes (pós-aula) |
| [`04-plano-de-interacao-ao-vivo.md`](04-plano-de-interacao-ao-vivo.md) | As 2 enquetes, micro-interações e moderação do chat | Vocês + moderador |
| [`05-emails-convite-e-lembrete.md`](05-emails-convite-e-lembrete.md) | 4 e-mails prontos: convite, lembrete, pós-aula e quinta | Quem dispara a comunicação |

---

## Estrutura da aula

| Horário | Bloco | Quem | Slides |
|---|---|---|---|
| 19h00 às 19h10 | Recepção | Edmar + moderador | 1 e 2 |
| 19h10 às 19h30 | Quem é a White Cube? | Ale e Márcio | 3 |
| 19h30 às 19h45 | Cronograma e metodologia | Edmar | 4 a 11 |
| 19h45 às 20h30 | Introdução ao universo de Dados e IA | Edmar | 12 a 38 |
| 20h30 às 20h45 | Intervalo | (os dois) | 39 |
| 20h45 às 21h45 | Ciclo de vida de soluções de dados e IA | Felipe | 40 a 58 |
| 21h45 às 22h00 | Encerramento e Q&A | Felipe + Edmar | 59 a 64 |

---

## Identidade visual

O deck segue o template oficial da White Cube. Os fundos e o logo são os arquivos reais
extraídos de `Apresentação_Template_WhiteCube.pptx`, guardados em [`assets/whitecube/`](../../assets/whitecube/).

| Elemento | Valor |
|---|---|
| Formato | 20 × 11,25 pol (16:9, mesma medida do template) |
| Fonte | **Roboto** em 100% dos textos, sem exceção |
| Tamanho mínimo | 17pt em todo texto de leitura (rodapé e rótulos do diagrama de círculos são a única exceção) |
| Azul institucional | `#28347B` |
| Azul do logo | `#3C5DAA` |
| Vermelho do logo | `#E23635` |
| Texto | `#404148` (corpo) e `#767880` (secundário) |
| Fundo claro | `#EAEBEB` |
| Margem lateral | 1,059 pol (mesma do template) |
| Rodapé | `whitecube.com.br` à esquerda, número do slide à direita |

**Fundos usados:** capa com cubos (`image1`), cinza claro com marca d'água (`image3`),
branco com régua azul (`image5`) e azul institucional para seções e declarações (`image6`).

### Regras de estilo aplicadas

1. **Roboto em tudo.**
2. **Tamanho mínimo de 17pt em todo texto de leitura.** Exceções documentadas: rodapé
   (13pt, é mobília da página) e os rótulos internos do diagrama de círculos concêntricos
   (o espaço físico dos anéis não comporta 17pt).
3. **Um único tamanho de fonte por caixa de texto.** Título e corpo de um card ficam em
   caixas separadas justamente para nunca misturar tamanhos num mesmo bloco.
4. **Zero travessões.** Nem em dash nem en dash, nos slides e nas notas.
5. **Zero vícios de escrita que soam a IA.** Nada de "insight", "crucial", "fundamental",
   contraste raso "não é X. É Y.", pergunta retórica em série. Lista completa em `CLAUDE.md`.

As quatro primeiras regras são verificadas por asserção no gerador: se alguma for violada,
o script falha e não gera o arquivo. A quinta depende de revisão manual do texto.

---

## ⚠️ Instale a fonte Roboto

Roboto não está instalada nesta máquina. O `.pptx` referencia a fonte corretamente, mas o
PowerPoint vai substituir por outra ao abrir, e o espaçamento das linhas muda.

- **Se for apresentar pelo Canva:** não precisa fazer nada, o Canva já tem Roboto.
- **Se for apresentar pelo PowerPoint:** baixe Roboto em fonts.google.com/specimen/Roboto
  e instale em quem for apresentar, antes do ensaio.

---

## Levando para o Canva

O `.pptx` foi construído com formas e caixas de texto posicionadas manualmente (sem
placeholders de template), justamente para sobreviver ao import.

1. No Canva: **Criar design → Importar arquivo** e selecione o `.pptx`.
2. O tamanho já bate com o template White Cube, então não haverá reescala.
3. Confira se a fonte ficou como Roboto. Se o Canva trocar, selecione tudo e reaplique.
4. **As notas do apresentador não sobrevivem ao import.** Use o
   [`02-roteiro-do-apresentador.md`](02-roteiro-do-apresentador.md) num segundo monitor
   ou impresso.

---

## Regerando o deck

O deck é gerado por script, então dá para editar conteúdo e refazer tudo em segundos:

```bash
python scripts/gerar_slides_aula01.py     # regera o .pptx
python scripts/exportar_roteiro.py        # regera o roteiro em markdown
```

Rode os dois em sequência sempre que mexer no conteúdo, senão o roteiro fica defasado.

---

## Pendências antes da aula

**Preencher:**
- [ ] Slide 5: a linha “[1 linha sobre o que você faz no dia a dia]” do Edmar

**Decidir e alinhar:**
- [ ] Plataforma da aula e ferramenta de enquete. Ver [`04`](04-plano-de-interacao-ao-vivo.md)
- [ ] Criar o Discord e gerar o link de convite
- [ ] Quem será o moderador do chat (papel dedicado, não acumula com apresentar)
- [ ] Resposta oficial sobre **certificado**. A pergunta vai aparecer no Q&A
- [ ] Confirmar com Ale e Márcio: 20 min e quem passa a palavra para quem
- [ ] Instalar a fonte Roboto em quem for apresentar pelo PowerPoint

**Conferir:**
- [ ] Se for citar algum número de mercado, confirme a fonte atualizada. Os casos usados no
      deck (Netflix Prize 2009, Justiça Federal de Londrina 2025, reconhecimento facial em
      Aracaju 2024 com o estudo DPU/CESeC 2025, recrutamento da Amazon 2018) são fatos
      públicos e estáveis. Qualquer estatística de “% de projetos de IA que falham”
      precisa de fonte conferida ou deve ficar qualitativa.

**Restrição de conteúdo, combinar com o moderador:**
- [ ] 🚫 **Não mencionar o número de vagas de trainee em nenhum momento.** Resposta pronta
      para o Q&A está nas notas do slide 63.
