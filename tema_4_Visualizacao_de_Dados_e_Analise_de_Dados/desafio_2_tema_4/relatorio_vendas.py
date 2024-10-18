from datetime import datetime

import pandas as pd

# Dados fictícios de vendas diárias
dados = {
    'Data': ['2024-07-01', '2024-07-02', '2024-07-03', '2024-07-04', '2024-07-05'],
    'Produto': ['Sofá', 'Mesa', 'Cadeira', 'Estante', 'Cama'],
    'Quantidade Vendida': [5, 3, 7, 2, 4],
    'Preço Unitário': [500.00, 150.00, 75.00, 200.00, 600.00]
}

# Converter as datas para o formato datetime
dados['Data'] = pd.to_datetime(dados['Data'])

# Criar um DataFrame com os dados
vendas_diarias = pd.DataFrame(dados)

# Calcular o valor total das vendas
vendas_diarias['Valor Total'] = vendas_diarias['Quantidade Vendida'] * \
    vendas_diarias['Preço Unitário']

# Exibir o DataFrame
print("Relatório de Vendas Diárias:")
print(vendas_diarias)

# Salvar o DataFrame em um arquivo Excel
vendas_diarias.to_excel('relatorio_vendas_diarias.xlsx',
                        index=False, engine='openpyxl')

print("\nO arquivo 'relatorio_vendas_diarias.xlsx' foi criado com sucesso!")
