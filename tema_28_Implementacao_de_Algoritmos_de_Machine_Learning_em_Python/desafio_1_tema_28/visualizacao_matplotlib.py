import matplotlib.pyplot as plt

# Dados para visualização
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criar o gráfico
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Dados')

# Adicionar título e rótulos
plt.title('Exemplo de Gráfico com Matplotlib')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionar uma legenda
plt.legend()

# Exibir o gráfico
plt.show()
