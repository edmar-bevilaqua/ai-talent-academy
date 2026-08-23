# Aula 5: Semana 3, segunda-feira

Pacote da quinta aula do **AI Talent Academy**, no padrão visual White Cube.
Tema: **Análise de Dados com SQL** · 19h00 às ~22h05 · online · aula expositiva
Condução: Edmar Bevilaqua (aula inteira)

Primeira aula técnica de verdade do programa. Segue a regra das segundas: sem código ao
vivo, sem mão na massa. Toda consulta aparece como slide, com o texto da query num bloco
destacado e a explicação em bullets logo abaixo. A prática com banco real fica para a
Aula 6 (quinta), que ainda não foi produzida.

---

## O que tem aqui

| Arquivo | O que é | Para quem |
|---|---|---|
| **`AI-Talent-Academy-Aula05.pptx`** | O deck: 34 slides, com roteiro de fala nas notas | Edmar |
| [`02-roteiro-do-apresentador.md`](02-roteiro-do-apresentador.md) | Todas as notas do deck em markdown imprimível | Edmar |

---

## Estrutura da aula

| Horário | Bloco | Slides |
|---|---|---|
| 19h00 às 19h10 | Recepção | 1 e 2 |
| 19h10 às 19h25 | Por que SQL, e por que agora | 3 a 6 |
| 19h25 às 20h00 | Anatomia de uma consulta (SELECT, FROM, WHERE, ORDER BY, LIMIT, ordem de execução) | 7 a 14 |
| 20h00 às 20h25 | Filtrando e refinando (comparação, faixa, OR, IN, LIKE, NULL) | 15 a 18 |
| 20h25 às 20h40 | Intervalo | — |
| 20h40 às 21h15 | Agregações (COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING) | 19 a 23 |
| 21h15 às 21h45 | Juntando tabelas (chave primária, chave estrangeira, JOIN, INNER x LEFT) | 24 a 29 |
| 21h45 às 22h05 | Encerramento | 30 a 34 |

Total sincrono de ~3h05, cinco minutos além do padrão de 3h. É folga natural do
cronograma, não uma decisão de esticar como na Aula 3.

---

## Decisões de conteúdo desta aula

| Decisão | O que foi combinado |
|---|---|
| **Profundidade** | Só fundamentos: SELECT, WHERE, GROUP BY, HAVING, JOIN. Sem subquery, sem CTE, sem window function. A grade não reserva uma semana de SQL avançado depois desta |
| **Caso de exemplo** | Reaproveita o caso de fraude em cartão da Aula 2 (tabelas `transacoes`, `clientes`, `lojistas`), para não gastar tempo de aula explicando um cenário novo |
| **Mão na massa** | Zero, mantém a regra das segundas. Toda consulta aparece só como slide |
| **Condução** | Edmar sozinho, aula inteira. Não há bloco dividido com o Felipe |

### Ganchos com as aulas anteriores

- O caso de fraude em cartão retoma o Canvas do Problema preenchido na Aula 2
- O slide "Onde estamos" é o mesmo formato usado na Aula 3, com a linha da semana 3
  marcada
- O bloco F aponta direto para a Aula 6 (quinta) e para a Aula 7 (Python, semana 4)

---

## Layout novo nesta aula

Esta aula introduziu o `sl_query`, que mostra uma consulta SQL num bloco destacado
(fundo cinza claro, borda azul, texto em negrito) com bullets de explicação logo abaixo.
Reutilizado em praticamente toda a aula, sempre com o mesmo padrão visual, para a turma
aprender a reconhecer rápido "isto é uma consulta" assim que o slide aparece.

---

## Regerando o deck

```bash
python scripts/gerar_slides_aula05.py     # regera o .pptx
python scripts/exportar_roteiro_aula05.py # regera o roteiro em markdown
python scripts/auditar_vicios.py scripts/gerar_slides_aula05.py   # passo obrigatório
```

---

## Pendências antes da aula

**Conteúdo:**
- [ ] Confirmar se a Aula 6 (quinta desta semana) vai usar exatamente as mesmas três
      tabelas e o mesmo caso de fraude, como este deck promete no encerramento
- [ ] Validar que o exemplo de JOIN (`transacoes` com `clientes`) funciona sem ajuste
      quando a Aula 6 definir o banco real que os participantes vão usar

**Ensaio:**
- [ ] Ensaiar o bloco de agregação (GROUP BY e HAVING) em voz alta. É o ponto onde mais
      gente costuma travar numa primeira aula de SQL
- [ ] Praticar a transição entre "a ordem que você escreve" e "a ordem real de
      execução", porque é o gancho que sustenta o HAVING mais à frente

**Operacional:**
- [ ] Criar as 2 enquetes com antecedência (slides 14 e 29)
- [ ] Instalar a fonte Roboto em quem for apresentar pelo PowerPoint
