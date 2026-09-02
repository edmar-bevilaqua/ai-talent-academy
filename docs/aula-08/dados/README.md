# Dados sintéticos da Aula 8

Mesmo esquema e o mesmo gerador da Aula 6 (`scripts/gerar_dados_aula06.py`), com três
ajustes pedidos para a Aula 8:

1. **Nome de lojista corrigido.** A versão usada na Aula 6 usava `fake.company()` do
   Faker, que no locale `pt_BR` gera nome de empresa registrada a partir de sobrenome
   ("da Costa - EI", "Farias e Filhos"), mais parecido com escritório de contabilidade
   do que com loja. Agora o nome combina um prefixo de marca fictícia (Vetor, Aurora,
   Bom Preço, Estrela, e mais 21 opções) com um sufixo coerente com a categoria do
   lojista (Eletrônicos, Farmácia, Supermercado, e assim por diante). Exemplos reais
   deste pacote: `União Transportes`, `Bom Preço Combustíveis`, `Alameda Eletrônicos`.
2. **Volume maior.** 1.000.000 de transações, contra 50 mil da Aula 6, para a Aula 8
   ter um caso real de "isso é grande demais para abrir no Excel" ao trabalhar com
   pandas.
3. **Uma fraude plantada, de propósito, para dar objetivo à análise exploratória.**
   Ver [`historia_anomalia.md`](historia_anomalia.md), que só o instrutor deve ler.

O ajuste do nome ficou no gerador compartilhado, então vale para as duas aulas dali
para frente. **Os dados já gerados da Aula 6 não foram tocados**, de propósito: eles
já têm exercícios e gabarito calibrados em cima dos números atuais, e eles ficariam
desalinhados se os dados fossem regerados por baixo.

---

## Volume gerado

| Tabela | Linhas |
|---|---|
| `categorias` | 12 |
| `clientes` | 1.500 |
| `lojistas` | 300 |
| `cartoes` | 1.931 |
| `transacoes` | 1.000.090 |
| `contestacoes` | 21.395 |

`clientes` e `lojistas` ficaram no mesmo tamanho da Aula 6, de propósito: só o volume
de transações cresceu. Se a ideia for aumentar também a variedade de clientes e
lojistas, é só rodar de novo com `--clientes` e `--lojistas` maiores.

`transacoes` passou de 1.000.000 para 1.000.090: as 90 linhas a mais são a rajada de
teste de cartão plantada (ver `historia_anomalia.md`), não um erro de arredondamento.

`csv/transacoes.csv` sozinho fica com aproximadamente 65 MB nesse volume, contra 3 MB
na Aula 6. Isso já é grande o suficiente para não abrir bem numa planilha comum, mas
ainda leve para o pandas no Colab.

Toda chave estrangeira foi conferida contra os dados reais deste pacote: nenhum
lojista aponta para categoria inexistente, nenhum cartão aponta para cliente
inexistente, nenhuma das 1.000.090 transações aponta para cartão ou lojista
inexistente, e toda transação contestada tem exatamente uma contestação
correspondente.

---

## A fraude plantada

Dois lojistas concentram taxa de contestação bem acima da média, transações de
madrugada fora do padrão, e rajadas de compra pequena típicas de teste de cartão. As
três camadas foram testadas com pandas de verdade, contra os 1.000.090 dados reais
deste pacote, e o sinal aparece limpo, sem ruído natural da base disfarçando a
conclusão.

**Leitura obrigatória para quem vai preparar a aula:**
[`historia_anomalia.md`](historia_anomalia.md). Não é para compartilhar com a turma,
é o gabarito da investigação.

---

## Como gerar de novo

```bash
python scripts/gerar_dados_aula06.py --transacoes 1000000 --saida aula-08 --anomalias
```

O parâmetro `--saida` é nome de uma pasta dentro de `docs/`, então este pacote inteiro
sai em `docs/aula-08/dados/`, sem encostar em `docs/aula-06/dados/`. `--anomalias`
planta a fraude descrita acima; sem essa flag, os dados saem limpos, sem história.
Rodar de novo com o mesmo `--seed` (o padrão é 42) reproduz exatamente os mesmos
dados, incluindo quais lojistas e cartões viram a história.

---

## Pendência

Este pacote só tem os dados. Ainda faltam o notebook de carga para o aluno (o
equivalente ao `carregar_dados_aluno.ipynb` da Aula 6) e o material da aula em si, que
ainda não foram desenhados para a Aula 8.
