import pandas as pd

# Dados fictícios do estoque
dados_estoque = {
    'ID do Produto': [201, 202, 203, 204, 205],
    'Nome do Produto': ['Sofá', 'Mesa', 'Cadeira', 'Estante', 'Cama'],
    'Categoria': ['Móveis', 'Móveis', 'Móveis', 'Móveis', 'Móveis'],
    'Quantidade em Estoque': [10, 20, 15, 5, 8],
    'Preço Unitário': [500.00, 150.00, 75.00, 200.00, 600.00]
}

# Criar um DataFrame com os dados do estoque
estoque_df = pd.DataFrame(dados_estoque)

# Calcular o valor total em estoque para cada produto
estoque_df['Valor Total'] = estoque_df['Quantidade em Estoque'] * \
    estoque_df['Preço Unitário']

# Exibir o DataFrame
print("Relatório de Estoque:")
print(estoque_df)

# Salvar o DataFrame em um arquivo Excel
estoque_df.to_excel('relatorio_estoque.xlsx', index=False, engine='openpyxl')

print("\nO arquivo 'relatorio_estoque.xlsx' foi criado com sucesso!")
