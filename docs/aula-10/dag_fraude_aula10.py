"""DAG de demonstracao da Aula 10.

Extract, transform e load sobre a base de fraude em cartao (a mesma das
Aulas 2, 5, 6, 7 e 8), para mostrar o Airflow orquestrando exatamente as
fases de ETL ensinadas na Aula 9. Ver docs/aula-10/00-guia-de-preparacao.md
para o passo a passo de instalacao e o roteiro de demonstracao.
"""
from __future__ import annotations

import pendulum
import pandas as pd

from airflow.sdk import dag, task

CAMINHO_ENTRADA = "/opt/airflow/dags/data/transacoes.csv"
CAMINHO_BRUTO = "/opt/airflow/dags/data/_bruto.parquet"
CAMINHO_LIMPO = "/opt/airflow/dags/data/_limpo.parquet"
CAMINHO_SAIDA = "/opt/airflow/dags/data/resumo_por_lojista.csv"


@dag(
    dag_id="aula10_pipeline_fraude",
    schedule=None,
    start_date=pendulum.datetime(2026, 1, 1, tz="America/Sao_Paulo"),
    catchup=False,
    tags=["aula-10", "demonstracao"],
)
def pipeline_fraude():

    @task()
    def extract() -> str:
        df = pd.read_csv(CAMINHO_ENTRADA)
        df.to_parquet(CAMINHO_BRUTO)
        return CAMINHO_BRUTO

    @task()
    def transform(caminho_bruto: str) -> str:
        df = pd.read_parquet(caminho_bruto)
        antes = len(df)
        df = df.dropna(subset=["id_transacao", "id_cartao", "id_lojista", "valor"])
        df = df.drop_duplicates(subset=["id_transacao"])
        df = df[df["valor"] > 0]
        print(f"Linhas antes da limpeza: {antes}. Depois: {len(df)}.")
        df.to_parquet(CAMINHO_LIMPO)
        return CAMINHO_LIMPO

    @task()
    def load(caminho_limpo: str) -> None:
        df = pd.read_parquet(caminho_limpo)
        resumo = (
            df.groupby("id_lojista")["valor"]
            .sum()
            .reset_index()
            .sort_values("valor", ascending=False)
        )
        resumo.to_csv(CAMINHO_SAIDA, index=False)
        print(f"Resumo gravado em {CAMINHO_SAIDA}, com {len(resumo)} lojistas.")

    load(transform(extract()))


pipeline_fraude()
