import matplotlib.pyplot as plt

# Dados fictícios
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [23, 17, 35, 29, 12]

# Criar o gráfico de barras
plt.bar(categorias, valores, color='green')

# Adicionar título e rótulos aos eixos
plt.title('Gráfico de Barras de Dados Fictícios')
plt.xlabel('Categoria')
plt.ylabel('Valor')

# Exibir o gráfico
plt.show()
