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
    return df.groupby('vendedor')['valor'].sum().sort_values(ascending=False)


def ranking_vendedores(df, top=5):
    return vendas_por_vendedor(df).head(top)


def vendas_por_produto(df):
    return df.groupby('produto')['valor'].sum().sort_values(ascending=False)


def ranking_produtos(df, top=5):
    return vendas_por_produto(df).head(top)


def vendas_por_mes(df):
    df['data'] = pd.to_datetime(df['data'])
    return df.groupby(df['data'].dt.to_period('M'))['valor'].sum()


def crescimento_mensal(df):
    vendas_mensais = vendas_por_mes(df)
    return vendas_mensais.pct_change().fillna(0) * 100


def participacao_vendedores(df):
    total = df['valor'].sum()
    return (df.groupby('vendedor')['valor'].sum() / total * 100).sort_values(ascending=False)


def participacao_produtos(df):
    total = df['valor'].sum()
    resultado = (df.groupby('produto')['valor'].sum() / total * 100).round(2).sort_values(ascending=False)
    return resultado.astype(str) + " %"


def analise_completa(df):
    print('=== ANÁLISE COMPLETA ===')
    print(f"Total de vendas: R$ {total_vendas(df):,.2f}")
    print(f"Número de clientes únicos: {clientes_unicos(df)}")
    print(f"Número de transações: {numero_transacoes(df)}")
    print(f"Ticket médio: R$ {ticket_medio(df):,.2f}\n")

    print('=== VENDAS POR VENDEDOR ===')
    print(vendas_por_vendedor(df), "\n")

    print('=== RANKING DE VENDEDORES ===')
    print(ranking_vendedores(df), "\n")

    print('=== VENDAS POR PRODUTO ===')
    print(vendas_por_produto(df), "\n")

    print('=== RANKING DE PRODUTOS ===')
    print(ranking_produtos(df), "\n")

    print('=== VENDAS POR MÊS ===')
    print(vendas_por_mes(df), "\n")

    print('=== CRESCIMENTO MENSAL (%) ===')
    print(crescimento_mensal(df), "\n")

    print('=== PARTICIPAÇÃO DOS VENDEDORES (%) ===')
    print(participacao_vendedores(df), "\n")

    print('=== PARTICIPAÇÃO DOS PRODUTOS (%) ===')
    print(participacao_produtos(df), "\n")