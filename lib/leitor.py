from pathlib import Path
import pandas as pd
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def ler_planilha(nome_arquivo: str):
    pasta_entrada = Path("data/entrada")
    caminho_arquivo = pasta_entrada / nome_arquivo
    if not caminho_arquivo.exists():
        raise FileNotFoundError(f"\033[31m\nArquivo {caminho_arquivo} não encontrado.\033[0m")
    df = pd.read_excel(caminho_arquivo)
    return df


def ler_dados():
    while True:
        try:
            nome_arquivo = input("Nome da planilha: ")
            if not nome_arquivo:    
                print("\033[31m\nNenhum nome de arquivo fornecido.\033[0m")
                input("Pressione ENTER para tentar novamente...")
                limpar_tela()
                continue
            df = ler_planilha(nome_arquivo)
            print("\033[32mPlanilha carregada com sucesso!\n\033[0m")
            print(df.head())
            return df
        except FileNotFoundError as e:
            print(e)
            input("Pressione ENTER para tentar novamente...")
            limpar_tela()
        except KeyboardInterrupt:
            print("\033[33mProcesso interrompido pelo usuário.\033[0m")
            exit()
        except EOFError:
            print("\033[33m\nEntrada finalizada pelo usuário.\033[0m")
            exit()
        except Exception as e:
            print(f"\033[31mErro ao ler a planilha: {e}\033[0m")
            input("Pressione ENTER para tentar novamente...")
            limpar_tela()