# A história plantada: instrutor, leia antes da Aula 8

Este pacote de dados tem uma fraude escondida, plantada de propósito no gerador
(`scripts/gerar_dados_aula06.py --anomalias`), para dar um objetivo real à análise
exploratória, em vez de só calcular média e desenhar gráfico sem motivo. A ideia é a
turma seguir o mesmo caminho que um analista de dados seguiria: começar largo, estranhar
um número, e ir cavando até achar a explicação.

**Não compartilhe este arquivo com os alunos.** Ele é o gabarito da investigação.

---

## O enredo, em uma frase

Dois lojistas, escolhidos ao acaso pelo gerador, concentram uma taxa de contestação
muito acima da média, transações de madrugada fora do padrão, e rajadas de compras
minúsculas típicas de teste de cartão roubado.

Nesta geração (seed padrão, 42), os dois são:

| id_lojista | Nome | Taxa de contestação | % de transações entre 1h e 3h |
|---|---|---|---|
| 141 | Express Posto | 23,7% | 69,0% |
| 271 | Bela Vista Soluções | 22,7% | 69,9% |

Para comparação, a média geral da base é ~2% de contestação e ~12,9% das transações
entre 1h e 3h. Se você regerar os dados (mesmo com `--seed 42`, mas com `--clientes` ou
`--lojistas` diferente do padrão), os dois lojistas sorteados podem mudar de id: rode a
célula da camada 1 para achar quem são desta vez.

---

## As três camadas, na ordem em que a turma deve achar

### Camada 1: taxa de contestação por lojista

A pergunta que puxa o fio: "algum lojista se destaca por taxa de contestação?"

```python
taxa = transacoes.groupby("id_lojista")["status"].apply(
    lambda s: (s == "contestada").mean()
)
taxa.sort_values(ascending=False).head(10)
```

Dois lojistas aparecem bem acima de todo o resto, folgados: por volta de 23%, contra
2% a 3% de qualquer outro. Um `boxplot` da taxa de contestação por lojista mostra os
dois como pontos isolados, fora da caixa.

```python
import seaborn as sns
sns.boxplot(x=taxa.values)
```

### Camada 2: horário das transações do lojista suspeito

Com o `id_lojista` suspeito em mãos, a pergunta natural é "o que mais é estranho
nesse lojista?".

```python
suspeito = taxa.idxmax()
horas = transacoes.loc[transacoes["id_lojista"] == suspeito, "data_hora"].dt.hour
sns.histplot(horas, bins=24)
```

O histograma mostra um pico isolado entre 1h e 3h da manhã, bem diferente da
distribuição bem mais espalhada do resto da base. Comércio não costuma vender tanto de
madrugada.

### Camada 3: teste de cartão

A última camada exige cruzar cartão, lojista e dia, procurando rajada de compras
pequenas e parecidas, o padrão clássico de alguém testando se um cartão roubado ainda
funciona antes de usar ele para valer.

```python
pequenas = transacoes[transacoes["valor"] <= 5]
rajadas = (
    pequenas
    .assign(dia=pequenas["data_hora"].dt.date)
    .groupby(["id_cartao", "id_lojista", "dia"])
    .size()
    .reset_index(name="qtd_transacoes")
)
rajadas[rajadas["qtd_transacoes"] >= 4].sort_values("qtd_transacoes", ascending=False)
```

Aparecem exatamente 15 cartões, todos com 6 transações de R\$1 a R\$5 no mesmo dia, no
mesmo lojista, e os dois lojistas envolvidos são os mesmos das camadas 1 e 2. Fora
desses 15, não existe nenhuma outra ocorrência do padrão na base inteira: o sinal é
limpo, sem ruído para atrapalhar a conclusão.

---

## O que foi tentado e não funcionou

A ideia original incluía uma quarta camada, "viagem impossível": o mesmo cartão
aparecendo em duas cidades distantes com poucos minutos de diferença. Calibrada e
testada contra os dados reais, essa camada não sobreviveu: com 1.000.000 de transações
distribuídas de forma totalmente independente entre lojista e horário, esse tipo de
par acontece aos milhares por puro acaso, mesmo exigindo uma velocidade acima de
1.000 km/h entre as cidades. Sem nenhuma noção de "cidade de origem" do cliente na
base, não existe um comportamento normal de deslocamento para a anomalia se destacar
contra ele. Foi substituída pelo teste de cartão, que não depende de nenhuma estrutura
geográfica do resto dos dados, e por isso ficou limpa.

Guarde essa observação: é um bom exemplo, para citar em aula, de que nem toda ideia de
anomalia sobrevive ao teste contra o dado real, e o motivo do descarte também ensina
algo sobre como os dados foram construídos.

---

## Parâmetros, se quiser recalibrar

No topo de `injetar_anomalias()`, em `scripts/gerar_dados_aula06.py`:

| Constante | Valor atual | O que controla |
|---|---|---|
| `N_LOJISTAS_SUSPEITOS` | 2 | quantos lojistas recebem o padrão de fraude |
| `TAXA_CONTESTACAO_SUSPEITA` | 0.22 | fração das transações desses lojistas marcada como contestada |
| `FRACAO_HORARIO_SUSPEITO` | 0.65 | fração das transações desses lojistas movida para a madrugada |
| `N_CARTOES_TESTE` | 15 | quantos cartões ganham a rajada de teste |
| `N_TRANSACOES_POR_TESTE` | 6 | quantas transações pequenas por rajada |
