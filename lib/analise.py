import pandas as pd

def total_vendas(df):
    return df['valor'].sum()


def clientes_unicos(df):
    return df['comprador'].nunique()


def numero_transacoes(df):
    return len(df)


def ticket_medio(df):
    return df['valor'].sum() / df['comprador'].nunique()


def vendas_por_vendedor(df):
    resultado = df.groupby('vendedor')['valor'].sum().sort_values(ascending=False)
    return resultado.apply(lambda x: f"R$ {x:.2f}")


def ranking_vendedores(df, top=5):
    resultado = vendas_por_vendedor(df).head(top)
    return resultado.round(2)


def vendas_por_produto(df):
    resultado = df.groupby('produto')['valor'].sum().sort_values(ascending=False)
    return resultado.apply(lambda x: f"R$ {x:,.2f}")


def ranking_produtos(df, top=5):
    return vendas_por_produto(df).head(top).round(2)


def vendas_por_mes(df):
    df['data'] = pd.to_datetime(df['data'])
    resultado = df.groupby(df['data'].dt.to_period('M'))['valor'].sum().round(2)
    resultado = resultado.apply(lambda x: f"R$ {x:.2f}")
    resultado.index = resultado.index.astype(str)  # <-- adicione isso
    return resultado


def crescimento_mensal(df):
    vendas_mensais = vendas_por_mes(df)
    resultado = vendas_mensais.pct_change().fillna(0) * 100
    return resultado.round(2).astype(str) + " %"


def participacao_vendedores(df):
    total = df['valor'].sum()
    resultado = (df.groupby('vendedor')['valor'].sum() / total * 100).round(2).sort_values(ascending=False)
    return resultado.astype(str) + " %"


def participacao_produtos(df):
    total = df['valor'].sum()
    resultado = (df.groupby('produto')['valor'].sum() / total * 100).round(2).sort_values(ascending=False)
    return resultado.astype(str) + " %"


def analise_completa(df):
    print('\033[032m\nAnálise feita com sucesso!\033[0m\n')
    print('=== ANÁLISE COMPLETA ===')
    print(f"Total de vendas: R$ {total_vendas(df):,.2f}")
    print(f"Número de clientes únicos: {clientes_unicos(df)}")
    print(f"Número de transações: {numero_transacoes(df)}")
    print(f"Ticket médio: R$ {ticket_medio(df):,.2f}\n")

    print('=== VENDAS POR VENDEDOR ===')
    print(vendas_por_vendedor(df).to_string(), "\n")

    print('=== RANKING DE VENDEDORES ===')
    print(ranking_vendedores(df).to_string(), "\n")

    print('=== VENDAS POR PRODUTO ===')
    print(vendas_por_produto(df).to_string(), "\n")

    print('=== RANKING DE PRODUTOS ===')
    print(ranking_produtos(df).to_string(), "\n")

    print('=== VENDAS POR MÊS ===')
    print(vendas_por_mes(df).to_string(), "\n")

    print('=== CRESCIMENTO MENSAL (%) ===')
    print(crescimento_mensal(df).to_string(), "\n")

    print('=== PARTICIPAÇÃO DOS VENDEDORES (%) ===')
    print(participacao_vendedores(df).to_string(), "\n")

    print('=== PARTICIPAÇÃO DOS PRODUTOS (%) ===')
    print(participacao_produtos(df).to_string(), "\n")