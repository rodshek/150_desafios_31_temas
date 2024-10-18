import matplotlib.pyplot as plt
import pandas as pd

# Dados fictícios de idades
dados_idades = {
    'Nome': ['Ana', 'Carlos', 'Beatriz', 'Daniel', 'Eva', 'Fernando', 'Gabriela', 'Hugo', 'Isabela', 'João'],
    'Idade': [23, 45, 34, 29, 52, 30, 41, 27, 35, 50]
}

# Criar DataFrame com os dados de idades
idades_df = pd.DataFrame(dados_idades)

# Criar histograma
plt.figure(figsize=(8, 6))
plt.hist(idades_df['Idade'], bins=5, color='green', edgecolor='black')

# Adicionar título e rótulos aos eixos
plt.title('Distribuição de Idades')
plt.xlabel('Idade')
plt.ylabel('Número de Pessoas')

# Mostrar o gráfico
plt.grid(True)
plt.savefig('histograma_idades.png')
plt.show()

# Exibir DataFrame
print("Dados de Idades:")
print(idades_df)
print("\nO histograma foi salvo como 'histograma_idades.png'.")
