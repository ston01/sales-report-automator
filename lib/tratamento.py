import pandas as pd
from pathlib import Path

COLUNAS_OBRIGATORIAS = ['data', 'vendedor', 'produto', 'valor', 'comprador']

def validar_colunas(df: pd.DataFrame):
    colunas_faltando = [c for c in COLUNAS_OBRIGATORIAS if c not in df.columns]
    if colunas_faltando:
        raise ValueError(f"Colunas obrigatórias ausentes: {', '.join(colunas_faltando)}")


def normalizar_texto(df: pd.DataFrame):
    for coluna in ["vendedor", "produto", "comprador"]:
        if coluna in df.columns:
            df[coluna] = (
                df[coluna]
                .astype(str)
                .str.strip()
                .replace({"nan": None})
            )
    return df


def converter_tipos(df: pd.DataFrame):
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    return df


def limpar_nulos(df: pd.DataFrame):
    return df.dropna(subset=COLUNAS_OBRIGATORIAS)


def limpar_duplicados(df: pd.DataFrame):
    return df.drop_duplicates(subset=COLUNAS_OBRIGATORIAS)


def tratar_planilha(df: pd.DataFrame):
    validar_colunas(df)
    df = normalizar_texto(df)
    df = converter_tipos(df)
    df = limpar_nulos(df)
    df = limpar_duplicados(df)
    return df


def tratar_dados(df: pd.DataFrame):
    validar_colunas(df)

    linhas_antes = len(df)
    df = normalizar_texto(df)
    df = converter_tipos(df)

    df = limpar_nulos(df)
    df = limpar_duplicados(df)

    linhas_depois = len(df)
    removidas = linhas_antes - linhas_depois

    print("\033[032m\nDados limpos com sucesso!\033[0m\n")
    print(f"Linhas antes: {linhas_antes}")
    print(f"Linhas depois: {linhas_depois}")
    print(f"Linhas removidas: {removidas}\n")

    pasta_saida = Path("data/saida")
    pasta_saida.mkdir(parents=True, exist_ok=True)

    caminho_saida = pasta_saida / "planilha_tratada.xlsx"
    df.to_excel(caminho_saida, index=False)

    print(f"Planilha tratada salva em {caminho_saida}\n")
    return df