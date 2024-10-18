import matplotlib.pyplot as plt
import pandas as pd

# Dados fictícios de vendas
dados_vendas = {
    'Produto': ['Arroz', 'Feijão', 'Macarrão', 'Óleo', 'Açúcar'],
    'Quantidade Vendida': [30, 45, 20, 50, 40],
    'Valor Total': [300, 360, 240, 300, 200]
}

# Criar DataFrame com os dados de vendas
vendas_df = pd.DataFrame(dados_vendas)

# Criar gráfico de dispersão
plt.figure(figsize=(8, 6))
plt.scatter(vendas_df['Quantidade Vendida'],
            vendas_df['Valor Total'], color='blue', marker='o')

# Adicionar título e rótulos aos eixos
plt.title('Gráfico de Dispersão: Quantidade Vendida vs Valor Total')
plt.xlabel('Quantidade Vendida')
plt.ylabel('Valor Total')

# Mostrar o gráfico
plt.grid(True)
plt.savefig('grafico_dispersao.png')
plt.show()

# Exibir DataFrame
print("Dados de Vendas:")
print(vendas_df)
print("\nO gráfico foi salvo como 'grafico_dispersao.png'.")
