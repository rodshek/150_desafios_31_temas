import pandas as pd

# Dados fictícios do estoque
dados_estoque = {
    'ID do Produto': [101, 102, 103],
    'Nome do Produto': ['Arroz', 'Feijão', 'Açúcar'],
    'Quantidade em Estoque': [50, 30, 20],
    'Preço Unitário': [5.00, 4.00, 3.00]
}

# Dados fictícios das vendas
dados_vendas = {
    'ID da Venda': [1, 2, 3],
    'ID do Produto': [101, 102, 103],
    'Quantidade Vendida': [2, 1, 5],
    'Data da Venda': ['2024-07-10', '2024-07-10', '2024-07-11']
}

# Criar DataFrames com os dados
estoque_df = pd.DataFrame(dados_estoque)
vendas_df = pd.DataFrame(dados_vendas)

# Converter as datas para o formato datetime
vendas_df['Data da Venda'] = pd.to_datetime(vendas_df['Data da Venda'])

# Calcular o valor total da venda para cada linha
vendas_df['Valor Total'] = vendas_df['Quantidade Vendida'] * \
    vendas_df['ID do Produto'].map(
        estoque_df.set_index('ID do Produto')['Preço Unitário'])

# Atualizar o estoque
for index, row in vendas_df.iterrows():
    produto_id = row['ID do Produto']
    quantidade_vendida = row['Quantidade Vendida']
    estoque_df.loc[estoque_df['ID do Produto'] == produto_id,
                   'Quantidade em Estoque'] -= quantidade_vendida

# Relatório de vendas por dia
relatorio_diario = vendas_df.groupby('Data da Venda')[
    'Valor Total'].sum().reset_index()

# Exibir os DataFrames
print("Estoque Atual:")
print(estoque_df)
print("\nRelatório Diário de Vendas:")
print(relatorio_diario)

# Salvar os DataFrames em arquivos Excel
estoque_df.to_excel('estoque_atual.xlsx', index=False, engine='openpyxl')
relatorio_diario.to_excel('relatorio_vendas_diarias.xlsx',
                          index=False, engine='openpyxl')

print("\nOs arquivos 'estoque_atual.xlsx' e 'relatorio_vendas_diarias.xlsx' foram criados com sucesso!")
