import pandas as pd

# Dados fictícios de inventário
dados_inventario = {
    'ID do Produto': [101, 102, 103, 104],
    'Nome do Produto': ['Arroz', 'Feijão', 'Macarrão', 'Óleo'],
    'Quantidade em Estoque': [50, 20, 0, 30],
    'Quantidade Mínima': [10, 15, 5, 20]
}

# Criar DataFrame com os dados de inventário
inventario_df = pd.DataFrame(dados_inventario)

# Verificar produtos com baixo estoque
inventario_df['Necessário Reabastecimento'] = inventario_df['Quantidade em Estoque'] < inventario_df['Quantidade Mínima']

# Gerar alerta para produtos com baixo estoque
alertas = inventario_df[inventario_df['Necessário Reabastecimento']]

# Exibir os DataFrames
print("Inventário Atual:")
print(inventario_df)
print("\nAlertas de Baixo Estoque:")
print(alertas)

# Salvar os DataFrames em arquivos Excel
inventario_df.to_excel('inventario_atual.xlsx', index=False)
alertas.to_excel('alertas_baixo_estoque.xlsx', index=False)

print("\nOs arquivos 'inventario_atual.xlsx' e 'alertas_baixo_estoque.xlsx' foram criados com sucesso!")
