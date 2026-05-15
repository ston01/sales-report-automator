from pathlib import Path
import pandas as pd

def ler_planilha(nome_arquivo: str):
    pasta_entrada = Path("projeto/entrada")
    caminho_arquivo = pasta_entrada / nome_arquivo
    if not caminho_arquivo.exists():
        raise FileNotFoundError(f"Arquivo {caminho_arquivo} não encontrado.")
    df = pd.read_excel(caminho_arquivo)
    return df