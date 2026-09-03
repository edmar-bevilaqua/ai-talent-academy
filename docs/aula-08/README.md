# Aula 8: Semana 4, quinta-feira

Pacote da oitava aula do **AI Talent Academy**, no padrão visual White Cube.
Tema: **laboratório prático de NumPy, pandas, Matplotlib e Seaborn** · 19h00 às 21h00 ·
online · aula quase inteiramente prática
Condução: Edmar Bevilaqua + Felipe André Bach Alves

> **Esta aula é deliberadamente enxuta em slide.** Por pedido explícito do usuário, o
> foco quase inteiro da noite é a prática: os alunos respondem 20 perguntas em
> `avaliacao_aluno.ipynb`, contra a base de 1 milhão de transações, e colam cada
> resposta num Google Forms. Os slides existem só para abrir a aula, explicar a
> mecânica, dar o gancho de investigação, e fechar. 15 slides no total, a maioria
> deles cabendo em menos de 20 minutos de fala.

> ⚠️ **Este deck não revela a fraude plantada nos dados.** A investigação é o próprio
> exercício. O gabarito completo está em
> [`dados/historia_anomalia.md`](dados/historia_anomalia.md), que não deve ser
> compartilhado com a turma. Leia esse arquivo antes de apresentar, e guarde a
> revelação para o encerramento, ao vivo, puxando pelo que a turma contar no chat.

---

## O que tem aqui

| Arquivo | O que é | Para quem |
|---|---|---|
| **`AI-Talent-Academy-Aula08.pptx`** | O deck: 15 slides, com roteiro de fala nas notas | Edmar + Felipe |
| [`02-roteiro-do-apresentador.md`](02-roteiro-do-apresentador.md) | Todas as notas do deck em markdown imprimível | Edmar + Felipe |
| [`avaliacao_aluno.ipynb`](avaliacao_aluno.ipynb) | As 20 perguntas, célula de código vazia, para o aluno responder | Alunos |
| [`avaliacao_professor.ipynb`](avaliacao_professor.ipynb) | As mesmas 20 perguntas, já resolvidas | Edmar + Felipe |
| [`dados/`](dados/) | O pacote de dados (1 milhão de transações) e a história da anomalia plantada | Ver aviso acima |

---

## Estrutura da aula

| Horário | Bloco | Slides |
|---|---|---|
| 19h00 às 19h10 | Recepção | 1 e 2 |
| 19h10 às 19h30 | Hoje é dia de investigar (mecânica, gancho, regras) | 3 a 8 |
| 19h30 às 20h45 | Mão na massa, 75 minutos | 9 e 10 |
| 20h45 às 21h00 | Encerramento (com a revelação, ao vivo, sem slide) | 11 a 15 |

Total síncrono de 2h, o padrão das quintas. Sem intervalo, mesmo padrão das Aulas 2, 4
e 6.

---

## Decisões de conteúdo desta aula

| Decisão | O que foi combinado |
|---|---|
| **Escopo** | Quase inteiramente prático, por pedido explícito do usuário. Sem re-ensinar NumPy, pandas, Matplotlib ou Seaborn, isso já foi coberto na Aula 7 |
| **O gancho investigativo** | A aula é apresentada como uma investigação real, sem spoiler do que está escondido nos dados. A revelação acontece ao vivo no encerramento, puxada pelo chat, não por slide |
| **Mecânica explícita** | Um slide de cards dedicado só a explicar o passo a passo (abrir notebook, carregar dados, responder, colar no Forms), porque essa é a parte com mais risco real de travar gente |
| **Cola liberada** | O notebook de demonstração da Aula 7 é citado como referência válida durante a prática, de propósito |
| **Condução** | Dupla, como nas outras quintas: um comanda o bloco de abertura, os dois circulam durante a prática |

### Ganchos com as aulas anteriores

- O bloco de abertura reforça que o notebook de demonstração da Aula 7 continua sendo
  referência válida
- As 20 perguntas usam a mesma base de fraude em cartão das Aulas 2, 5, 6 e 7, agora
  em escala de 1 milhão de transações
- O bloco F aponta para a Semana 5 (Engenharia de Dados)

---

## Regerando o deck

```bash
python scripts/gerar_slides_aula08.py     # regera o .pptx
python scripts/exportar_roteiro_aula08.py # regera o roteiro em markdown
python scripts/auditar_vicios.py scripts/gerar_slides_aula08.py   # passo obrigatório
```

---

## Pendências antes da aula

**Conteúdo:**
- [ ] Ler `dados/historia_anomalia.md` por completo antes de apresentar. É o roteiro
      da revelação do encerramento
- [ ] Decidir, entre os dois apresentadores, quem conduz a revelação ao vivo no
      encerramento, e ensaiar essa parte especificamente, já que não tem slide de apoio

**Operacional:**
- [ ] Criar o Google Forms com as 20 perguntas antes da aula, usando
      `avaliacao_professor.ipynb` como referência do que cada resposta deveria ser
- [ ] Fixar o link do notebook do aluno E o link do Forms no Discord antes de 19h00
- [ ] Confirmar que `docs/aula-08/dados/csv/` está numa pasta do Drive acessível para
      toda a turma, com o volume de 1 milhão de transações já carregado
- [ ] Combinar com os mentores que vão circular durante os 75 minutos: não confirmar
      nem negar se uma resposta da investigação está certa, só ajudar quem travou
