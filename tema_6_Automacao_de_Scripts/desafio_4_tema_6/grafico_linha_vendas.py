import matplotlib.pyplot as plt
import pandas as pd

# Dados fictícios de vendas ao longo dos meses
dados_vendas_mensais = {
    'Mês': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Vendas': [1200, 1500, 1700, 1800, 2000, 2200, 2100, 2300, 2400, 2500, 2600, 2700]
}

# Criar DataFrame com os dados de vendas mensais
vendas_mensais_df = pd.DataFrame(dados_vendas_mensais)

# Criar gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(vendas_mensais_df['Mês'], vendas_mensais_df['Vendas'],
         marker='o', color='red', linestyle='-', linewidth=2)

# Adicionar título e rótulos aos eixos
plt.title('Evolução das Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Vendas (em R$)')

# Mostrar o gráfico
plt.grid(True)
plt.savefig('grafico_linha_vendas.png')
plt.show()

# Exibir DataFrame
print("Dados de Vendas Mensais:")
print(vendas_mensais_df)
print("\nO gráfico de linha foi salvo como 'grafico_linha_vendas.png'.")
