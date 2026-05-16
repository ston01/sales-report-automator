import pandas as pd

def limpar_nulos(df):
    return df.dropna()


def limpar_duplicados(df):
    return df.drop_duplicates()


def tratar_planilha(df):
    df = limpar_nulos(df)
    df = limpar_duplicados(df)
    return df


def tratar_dados(df):
    df = limpar_nulos(df)
    df = limpar_duplicados(df)
    print("Dados limpos com sucesso!")
    df.to_excel("data/saida/planilha_tratada.xlsx", index=False)
    print("Planilha tratada salva em data/saida/planilha_tratada.xlsx")
    return df