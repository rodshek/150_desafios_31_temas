from datetime import datetime

import pandas as pd

# Dados fictícios dos pedidos
dados_pedidos = {
    'ID do Pedido': [101, 102, 103, 104, 105],
    'Nome do Cliente': ['Ana Silva', 'Carlos Souza', 'Maria Oliveira', 'João Santos', 'Pedro Costa'],
    'Data do Pedido': ['2024-07-01', '2024-07-02', '2024-07-02', '2024-07-03', '2024-07-04'],
    'Produto': ['Sofá', 'Mesa', 'Cadeira', 'Estante', 'Cama'],
    'Quantidade': [1, 2, 3, 1, 2],
    'Preço Total': [500.00, 300.00, 225.00, 200.00, 1200.00]
}

# Converter as datas para o formato datetime
dados_pedidos['Data do Pedido'] = pd.to_datetime(
    dados_pedidos['Data do Pedido'])

# Criar um DataFrame com os dados dos pedidos
pedidos_df = pd.DataFrame(dados_pedidos)

# Exibir o DataFrame
print("Relatório de Pedidos de Clientes:")
print(pedidos_df)

# Salvar o DataFrame em um arquivo Excel
pedidos_df.to_excel('relatorio_pedidos_clientes.xlsx',
                    index=False, engine='openpyxl')

print("\nO arquivo 'relatorio_pedidos_clientes.xlsx' foi criado com sucesso!")
