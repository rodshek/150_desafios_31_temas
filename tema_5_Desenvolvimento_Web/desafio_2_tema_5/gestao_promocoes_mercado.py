import pandas as pd

# Dados fictícios de produtos e preços
dados_produtos = {
    'ID do Produto': [201, 202, 203],
    'Nome do Produto': ['Maçã', 'Banana', 'Laranja'],
    'Preço Unitário': [3.00, 2.00, 4.00]
}

# Dados fictícios de promoções
dados_promocoes = {
    'ID da Promoção': [1, 2],
    'Nome da Promoção': ['Desconto de 10%', 'Desconto de 15%'],
    'Desconto (%)': [10, 15],
    'Produtos Incluídos': [[201, 203], [202]]
}

# Dados fictícios de vendas
dados_vendas = {
    'ID da Venda': [1, 2, 3],
    'ID do Produto': [201, 202, 203],
    'Quantidade Vendida': [3, 5, 2],
    'Data da Venda': ['2024-07-10', '2024-07-10', '2024-07-11']
}

# Criar DataFrames com os dados
produtos_df = pd.DataFrame(dados_produtos)
promocoes_df = pd.DataFrame(dados_promocoes)
vendas_df = pd.DataFrame(dados_vendas)

# Converter as datas para o formato datetime
vendas_df['Data da Venda'] = pd.to_datetime(vendas_df['Data da Venda'])

# Calcular o valor total das vendas antes do desconto
vendas_df['Preço Unitário'] = vendas_df['ID do Produto'].map(
    produtos_df.set_index('ID do Produto')['Preço Unitário'])
vendas_df['Valor Total'] = vendas_df['Quantidade Vendida'] * \
    vendas_df['Preço Unitário']

# Aplicar descontos


def aplicar_desconto(row):
    desconto = 0
    for _, promocao in promocoes_df.iterrows():
        if row['ID do Produto'] in promocao['Produtos Incluídos']:
            desconto = promocao['Desconto (%)']
            break
    return row['Valor Total'] * (1 - desconto / 100)


vendas_df['Valor Total com Desconto'] = vendas_df.apply(
    aplicar_desconto, axis=1)

# Relatório de vendas por dia com e sem desconto
relatorio_diario = vendas_df.groupby('Data da Venda').agg(
    Valor_Total=('Valor Total', 'sum'),
    Valor_Total_Com_Desconto=('Valor Total com Desconto', 'sum')
).reset_index()

# Exibir os DataFrames
print("Produtos Disponíveis:")
print(produtos_df)
print("\nPromoções Ativas:")
print(promocoes_df)
print("\nRelatório Diário de Vendas:")
print(relatorio_diario)

# Salvar os DataFrames em arquivos Excel
produtos_df.to_excel('produtos_disponiveis.xlsx',
                     index=False, engine='openpyxl')
promocoes_df.to_excel('promocoes_ativas.xlsx', index=False, engine='openpyxl')
relatorio_diario.to_excel(
    'relatorio_vendas_com_desconto.xlsx', index=False, engine='openpyxl')

print("\nOs arquivos 'produtos_disponiveis.xlsx', 'promocoes_ativas.xlsx' e 'relatorio_vendas_com_desconto.xlsx' foram criados com sucesso!")
