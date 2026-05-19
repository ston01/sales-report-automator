from lib.executor import executar

if __name__ == "__main__":
    executar()
try:
    input("\nPressione ENTER para sair...")
except KeyboardInterrupt:
    print("\033[313\nPrograma encerrado pelo usuário.\033[0m")