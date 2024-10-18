import pandas as pd

# Dados fictícios do estoque
dados = {
    'ID': [1, 2, 3, 4, 5],
    'Nome do Móvel': ['Sofá', 'Mesa', 'Cadeira', 'Estante', 'Cama'],
    'Quantidade': [10, 5, 15, 7, 3],
    'Preço Unitário': [500.00, 150.00, 75.00, 200.00, 600.00]
}

# Criar um DataFrame com os dados
estoque = pd.DataFrame(dados)

# Exibir o DataFrame
print("Estoque de Móveis:")
print(estoque)

# Salvar o DataFrame em um arquivo Excel
estoque.to_excel('estoque_moveis.xlsx', index=False, engine='openpyxl')

print("\nO arquivo 'estoque_moveis.xlsx' foi criado com sucesso!")
