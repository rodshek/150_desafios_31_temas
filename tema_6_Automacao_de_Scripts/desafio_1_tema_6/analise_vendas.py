import matplotlib.pyplot as plt
import pandas as pd

# Dados fictícios de vendas
dados_vendas = {
    'Data': ['2024-07-01', '2024-07-02', '2024-07-03', '2024-07-04', '2024-07-05'],
    'Produto': ['Arroz', 'Feijão', 'Macarrão', 'Óleo', 'Açúcar'],
    'Quantidade': [30, 45, 20, 50, 40],
    'Valor Total': [300, 360, 240, 300, 200]
}

# Criar DataFrame com os dados de vendas
vendas_df = pd.DataFrame(dados_vendas)

# Converter a coluna 'Data' para o tipo datetime
vendas_df['Data'] = pd.to_datetime(vendas_df['Data'])

# Análise de dados
vendas_diarias = vendas_df.groupby('Data').sum()

# Visualização de dados
plt.figure(figsize=(12, 6))

# Gráfico de barras para valor total das vendas
plt.subplot(2, 1, 1)
plt.bar(vendas_diarias.index, vendas_diarias['Valor Total'], color='skyblue')
plt.title('Valor Total das Vendas Diárias')
plt.xlabel('Data')
plt.ylabel('Valor Total')

# Gráfico de linhas para quantidade vendida
plt.subplot(2, 1, 2)
plt.plot(vendas_df['Data'], vendas_df['Quantidade'],
         marker='o', color='orange')
plt.title('Quantidade Vendida por Dia')
plt.xlabel('Data')
plt.ylabel('Quantidade')

# Ajustar layout e salvar gráfico
plt.tight_layout()
plt.savefig('analise_vendas.png')

# Exibir DataFrame e gráfico
print("Análise de Vendas Diárias:")
print(vendas_diarias)
print("\nO gráfico foi salvo como 'analise_vendas.png'.")
