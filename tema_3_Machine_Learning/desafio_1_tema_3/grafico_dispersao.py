import matplotlib.pyplot as plt

# Dados fictícios
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Criar o gráfico de dispersão
plt.scatter(x, y, color='blue', marker='o')

# Adicionar título e rótulos aos eixos
plt.title('Gráfico de Dispersão de Dados Fictícios')
plt.xlabel('Valor de X')
plt.ylabel('Valor de Y')

# Exibir o gráfico
plt.show()
