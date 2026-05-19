from pathlib import Path
import pandas as pd
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def ler_planilha(nome_arquivo: str):
    pasta_entrada = Path("data/entrada")
    caminho_arquivo = pasta_entrada / nome_arquivo
    if not caminho_arquivo.exists():
        raise FileNotFoundError(f"\nArquivo {caminho_arquivo} não encontrado.")
    df = pd.read_excel(caminho_arquivo)
    return df


def ler_dados():
    while True:
        try:
            nome_arquivo = input("Nome da planilha: ")
            df = ler_planilha(nome_arquivo)
            print("\nPlanilha carregada com sucesso!\n")
            print(df.head())
            return df
        except FileNotFoundError as e:
            print(e)
            input("Pressione ENTER para tentar novamente...")
            limpar_tela()
        except KeyboardInterrupt:
            print("\nProcesso interrompido pelo usuário.")
            exit()
        except EOFError:
            print("\nEntrada finalizada pelo usuário.")
            exit()
        except Exception as e:
            print(f"Erro ao ler a planilha: {e}")
            input("Pressione ENTER para tentar novamente...")
            limpar_tela()