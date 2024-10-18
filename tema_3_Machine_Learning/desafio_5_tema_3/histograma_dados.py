import matplotlib.pyplot as plt

# Dados fictícios
dados = [23, 45, 56, 78, 33, 44, 23, 56, 89,
         90, 12, 45, 67, 89, 45, 34, 23, 56, 78, 90]

# Criar o histograma
plt.hist(dados, bins=10, color='purple', edgecolor='black')

# Adicionar título e rótulos aos eixos
plt.title('Histograma de Dados Fictícios')
plt.xlabel('Faixa de Valores')
plt.ylabel('Frequência')

# Exibir o gráfico
plt.show()
