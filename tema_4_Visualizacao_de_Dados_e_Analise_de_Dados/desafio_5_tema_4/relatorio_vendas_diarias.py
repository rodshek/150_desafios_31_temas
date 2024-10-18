from datetime import datetime

import pandas as pd

# Dados fictícios das vendas
dados_vendas = {
    'ID da Venda': [301, 302, 303, 304, 305],
    'Data da Venda': ['2024-07-01', '2024-07-01', '2024-07-02', '2024-07-02', '2024-07-03'],
    'Nome do Cliente': ['Ana Silva', 'Carlos Souza', 'Maria Oliveira', 'João Santos', 'Pedro Costa'],
    'Produto': ['Sofá', 'Mesa', 'Cadeira', 'Estante', 'Cama'],
    'Quantidade Vendida': [1, 2, 1, 1, 2],
    'Preço Unitário': [500.00, 150.00, 75.00, 200.00, 600.00]
}

# Converter as datas para o formato datetime
dados_vendas['Data da Venda'] = pd.to_datetime(dados_vendas['Data da Venda'])

# Criar um DataFrame com os dados das vendas
vendas_df = pd.DataFrame(dados_vendas)

# Calcular o valor total da venda para cada linha
vendas_df['Valor Total'] = vendas_df['Quantidade Vendida'] * \
    vendas_df['Preço Unitário']

# Calcular o total de vendas por dia
relatorio_diario = vendas_df.groupby('Data da Venda')[
    'Valor Total'].sum().reset_index()

# Exibir o DataFrame
print("Relatório Diário de Vendas:")
print(relatorio_diario)

# Salvar o DataFrame em um arquivo Excel
relatorio_diario.to_excel('relatorio_vendas_diarias.xlsx',
                          index=False, engine='openpyxl')

print("\nO arquivo 'relatorio_vendas_diarias.xlsx' foi criado com sucesso!")
