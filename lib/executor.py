from lib.leitor import ler_dados
from lib.tratamento import tratar_dados
from lib.analise import analise_completa
from lib.relatorio import gerar_relatorio

def executar():
    try:
        df = ler_dados()
        df_tratado = tratar_dados(df)
        analise_completa(df_tratado)
        gerar_relatorio(df_tratado)
    except Exception as e:
        print(f"\033[31mErro inesperado na execução: {e}\033[0m")