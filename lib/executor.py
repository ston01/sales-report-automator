from lib.leitor import ler_planilha
from lib.tratamento import limpar_nulos, limpar_duplicados
import pandas as pd

def executar():
    try:
        nome_arquivo = input("Digite o nome da planilha: ")
        df = ler_planilha(nome_arquivo)
        print("Planilha carregada com sucesso!")
        print(df.head())

        df = limpar_nulos(df)
        df = limpar_duplicados(df)
        print("Dados limpos com sucesso!")

        df.to_excel("data/saida/planilha_tratada.xlsx", index=False)
        print("Planilha tratada salva em data/saida/planilha_tratada.xlsx")
    except Exception as e:
        print(f"Erro: {e}")