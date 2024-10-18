import pandas as pd

# Dados fictícios de vendas diárias
dados_vendas = {
    'Data': ['2024-07-01', '2024-07-02', '2024-07-03', '2024-07-04', '2024-07-05'],
    'Vendas': [1500, 1700, 1800, 1600, 2000],
    'Número de Clientes': [25, 30, 28, 22, 35]
}

# Criar DataFrame com os dados de vendas
vendas_df = pd.DataFrame(dados_vendas)

# Salvar DataFrame em um arquivo Excel
arquivo_excel = 'relatorio_vendas_diarias.xlsx'
vendas_df.to_excel(arquivo_excel, index=False, engine='openpyxl')

print(f"Relatório de vendas diárias foi salvo como '{arquivo_excel}'.")
