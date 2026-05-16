import pandas as pd

def limpar_nulos(df):
    return df.dropna()


def limpar_duplicados(df):
    return df.drop_duplicates()