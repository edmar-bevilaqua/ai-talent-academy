# Aula 2: Semana 1, quinta-feira

Primeiro laboratório do **AI Talent Academy**, no padrão visual White Cube.
19h00 às 21h00 · online · ~190 participantes
Condução: Edmar Bevilaqua + Felipe André Bach Alves

---

## O que tem aqui

| Arquivo | O que é | Para quem |
|---|---|---|
| **`AI-Talent-Academy-Aula02.pptx`** | O deck: 29 slides, com roteiro de fala nas notas | Vocês dois |
| [`01-plano-da-aula.md`](01-plano-da-aula.md) | Cronômetro, marcos, checklist pré-aula, como circular nas salas | Vocês dois |
| [`02-roteiro-do-apresentador.md`](02-roteiro-do-apresentador.md) | Todas as notas do deck em markdown imprimível | Vocês dois |
| [`03-canvas-do-problema.md`](03-canvas-do-problema.md) | O canvas em branco, para os grupos preencherem | Participantes |

---

## Estrutura da aula

| Horário | Bloco | Quem | Slides |
|---|---|---|---|
| 19h00 às 19h10 | Recepção | Edmar + moderador | 1 e 2 |
| 19h10 às 19h20 | Explicar as quintas-feiras | Edmar | 3 a 6 |
| 19h20 às 19h45 | Canvas do Problema + demonstração | Felipe | 7 a 19 |
| 19h45 às 20h00 | Quebra em grupos | Edmar | 20 a 23 |
| 20h00 às 20h45 | Atividade em grupo | os dois circulando | 24 |
| 20h45 às 21h00 | Encerramento e Q&A | Felipe + Edmar | 25 a 29 |

Só **35 minutos** são de apresentação. O resto da noite é da turma.

---

## O caso da demonstração

**Fraude em cartão de crédito.** O pedido vago que abre a demonstração é
*"queremos usar IA para reduzir as perdas com fraude no cartão"*, e os 8 campos são
preenchidos ao vivo até virar um problema resolvível.

### Por que este caso

Ele **já apareceu duas vezes na Aula 1**, então a turma chega com contexto:

| Onde apareceu | O que foi dito |
|---|---|
| Slide 15, "IA que você já usa" | "A compra bloqueada pelo banco: detecção de fraude em tempo real" |
| Slide 52, "A armadilha das métricas" | O modelo que responde sempre "não é fraude", acerta 99% e não pega fraude nenhuma |

O arco fecha no **campo 8**, quando o Felipe retoma o exemplo do 99% para justificar por
que acurácia ficou de fora da lista de métricas. Guarde energia para esse item.

### O que o caso rende bem

- **Campo 2:** o usuário não é uma pessoa só. São três (o sistema de autorização, o
  analista de prevenção e o cliente afetado), cada um com uma necessidade diferente
- **Campo 3:** o rótulo de fraude vem do chargeback e demora de 30 a 90 dias, então o
  modelo treina com o mundo de três meses atrás enquanto o fraudador já mudou de tática
- **Campo 5:** o modelo aprende CEP como substituto de renda, mesmo sem receber renda.
  Conecta direto com os dois casos de viés da Aula 1
- **Campo 6:** devolver *score* em vez de sim ou não permite três ações, e a faixa do meio
  (pedir confirmação) salva o cliente legítimo do constrangimento

### Os dados

O caso é **hipotético e realista**, sem dataset público atrelado. Base de fraude real não é
pública, por sigilo bancário e proteção de dados. Se alguém perguntar onde baixar, essa é
a resposta honesta.

---

## Os três casos da atividade em grupo

| Caso | Tema | Dados públicos |
|---|---|---|
| **A** | Evasão escolar numa rede de ensino | Censo Escolar do INEP |
| **B** | Fila de pronto-socorro num hospital | Genérico, sem dataset atrelado |
| **C** | Problema real trazido por alguém do grupo | Depende do caso |

O caso C é o recomendado quando alguém do grupo tem um problema de verdade: a pessoa
consegue responder as perguntas difíceis do campo 2.

---

## ⚠️ O que precisa existir antes das 19h00

A atividade em grupo depende de coisas que precisam existir **antes** da aula começar:

- [ ] Salas de grupo criadas, com os participantes já distribuídos
- [ ] Lista de grupos em texto, para o moderador colar no chat às 19h45
- [ ] Uma cópia do canvas por grupo, em documento compartilhado
- [ ] Links dos documentos organizados por grupo
- [ ] Canvas em branco (PDF) no Discord
- [ ] Teste de mover 2 pessoas para uma sala e trazer de volta

Com 190 pessoas e grupos de 8, são 24 salas. **Grupos de 10 caem para 19 salas**, o que é
bem mais viável de circular em 45 minutos com duas pessoas.

---

## Regerando o deck

```bash
python scripts/gerar_slides_aula02.py        # regera o .pptx
python scripts/exportar_roteiro_aula02.py    # regera o roteiro em markdown
```

Rode os dois em sequência sempre que mexer no conteúdo.

---

## Pendências

- [ ] **Confirmar o tema da semana 2** antes de anunciar no slide 27. O cronograma novo
      indica IA Generativa, mas isso ainda não foi fechado
- [ ] Definir se os grupos serão de 8 ou 10 pessoas
- [ ] Decidir se os canvas preenchidos vão para o Discord depois da aula
- [ ] Converter [`03-canvas-do-problema.md`](03-canvas-do-problema.md) para PDF antes de postar
