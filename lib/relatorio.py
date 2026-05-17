from fpdf import FPDF
from lib import analise

def gerar_relatorio(df, saida_pdf="data/saida/relatorio.pdf"):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', size=20)
    pdf.cell(0, 10, 'RELATÓRIO DE VENDAS', ln=True, align="C")
    pdf.ln(3)
    pdf.line(25, pdf.get_y(), 185, pdf.get_y())
    pdf.ln(10)
    pdf.cell(0, 10, "", ln=True)

    pdf.set_font('Arial', 'B', size=16)
    pdf.cell(0, 10, "Análise completa: ", ln=True)
    pdf.set_font('Arial', size=16)
    pdf.cell(0, 10, f"Total de vendas: R${float(analise.total_vendas(df)):.2f}", ln=True)
    pdf.cell(0, 10, f"Número de clientes únicos: {analise.clientes_unicos(df)}", ln=True)
    pdf.cell(0, 10, f"Número de transações: {analise.numero_transacoes(df)}", ln=True)
    pdf.cell(0, 10, f"Ticket médio: R${float(analise.ticket_medio(df)):.2f}", ln=True)
    pdf.cell(0, 10, "", ln=True)

    pdf.set_font('Arial', 'B', size=16)
    pdf.cell(0, 10, "Vendas por vendedor: ", ln=True)
    pdf.set_font('Arial', size=16)
    vendas = analise.vendas_por_vendedor(df)
    for vendedor, valor in vendas.items():
        valor_limpo = str(valor).replace("R$", "").strip()
        pdf.cell(0, 10, f"{vendedor}: R${float(valor_limpo):.2f}", ln=True)
    pdf.cell(0, 10, "", ln=True)

    pdf.set_font('Arial', 'B', size=16)
    pdf.cell(0, 10, "Ranking de vendedores: ", ln=True)
    pdf.set_font('Arial', size=16)
    ranking = analise.ranking_vendedores(df)
    for vendedor, valor in ranking.items():
        valor_limpo = str(valor).replace("R$", "").strip()
        pdf.cell(0, 10, f"{vendedor}: R${float(valor_limpo):.2f}", ln=True)
    pdf.cell(0, 10, '', ln=True)

    pdf.add_page()
    pdf.ln(10)

    pdf.set_font('Arial', 'B', size=16)
    pdf.cell(0, 10, "Vendas por produto: ", ln=True)
    pdf.set_font('Arial', size=16)
    vendas_produto = analise.vendas_por_produto(df)
    for produto, valor in vendas_produto.items():
        valor_limpo = str(valor).replace("R$", "").strip()
        pdf.cell(0, 10, f"{produto}: R${float(valor_limpo):.2f}", ln=True)
    pdf.cell(0, 10, "", ln=True)

    pdf.output(saida_pdf)
    print(f"Relatório gerado com sucesso em: {saida_pdf}")