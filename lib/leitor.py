from pathlib import Path
import pandas as pd

def ler_planilha(nome_arquivo: str):
    pasta_entrada = Path("data/entrada")
    caminho_arquivo = pasta_entrada / nome_arquivo
    if not caminho_arquivo.exists():
        raise FileNotFoundError(f"Arquivo {caminho_arquivo} não encontrado.")
    df = pd.read_excel(caminho_arquivo)
    return df


def ler_dados():
    nome_arquivo = input("Digite o nome da planilha: ")
    df = ler_planilha(nome_arquivo)
    print("Planilha carregada com sucesso!")
    print(df.head())
    return df