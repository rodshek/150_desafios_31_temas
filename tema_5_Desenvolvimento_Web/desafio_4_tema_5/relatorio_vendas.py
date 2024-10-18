import matplotlib.pyplot as plt
import pandas as pd

# Dados fictícios de vendas diárias
dados_vendas = {
    'Data': ['2024-07-01', '2024-07-02', '2024-07-03', '2024-07-04'],
    'Produto': ['Arroz', 'Feijão', 'Macarrão', 'Óleo'],
    'Vendas': [200, 150, 180, 220]
}

# Criar DataFrame com os dados de vendas
vendas_df = pd.DataFrame(dados_vendas)

# Converter a coluna 'Data' para o tipo datetime
vendas_df['Data'] = pd.to_datetime(vendas_df['Data'])

# Criar o relatório de vendas diárias
vendas_diarias = vendas_df.groupby('Data').sum()

# Gerar gráficos de vendas
plt.figure(figsize=(10, 6))

# Gráfico de barras de vendas diárias
plt.subplot(2, 1, 1)
plt.bar(vendas_diarias.index, vendas_diarias['Vendas'], color='skyblue')
plt.title('Vendas Diárias')
plt.xlabel('Data')
plt.ylabel('Vendas')

# Gráfico de linhas de tendências de vendas
plt.subplot(2, 1, 2)
plt.plot(vendas_df['Data'], vendas_df['Vendas'], marker='o', color='orange')
plt.title('Tendências de Vendas')
plt.xlabel('Data')
plt.ylabel('Vendas')

# Salvar gráficos
plt.tight_layout()
plt.savefig('relatorio_vendas.png')

# Exibir DataFrame e gráfico
print("Relatório de Vendas Diárias:")
print(vendas_diarias)
print("\nO gráfico de vendas diárias e a análise de tendências foram salvos como 'relatorio_vendas.png'.")
