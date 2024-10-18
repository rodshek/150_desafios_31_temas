import pandas as pd

# Dados fictícios de produtos e promoções
dados_produtos = {
    'ID do Produto': [201, 202, 203, 204],
    'Nome do Produto': ['Arroz', 'Feijão', 'Macarrão', 'Óleo'],
    'Preço Original': [10.00, 8.00, 12.00, 6.00],
    'Desconto (%)': [5, 10, 0, 15]
}

# Criar DataFrame com os dados dos produtos
produtos_df = pd.DataFrame(dados_produtos)

# Calcular o preço com desconto
produtos_df['Preço com Desconto'] = produtos_df['Preço Original'] * \
    (1 - produtos_df['Desconto (%)'] / 100)

# Gerar relatórios
relatorio_produtos = produtos_df[[
    'ID do Produto', 'Nome do Produto', 'Preço Original', 'Desconto (%)', 'Preço com Desconto']]

# Salvar o relatório em um arquivo Excel
relatorio_produtos.to_excel('relatorio_promocoes.xlsx', index=False)

# Exibir o relatório
print("Relatório de Promoções e Descontos:")
print(relatorio_produtos)
print("\nO relatório foi salvo como 'relatorio_promocoes.xlsx'.")
