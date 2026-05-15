from lib.leitor import ler_planilha

def executar():
    nome_arquivo = input("Digite o nome da planilha: ")
    df = ler_planilha(nome_arquivo)
    print("Planilha carregada com sucesso!")
    print(df.head())