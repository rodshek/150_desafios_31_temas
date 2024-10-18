import matplotlib.pyplot as plt

# Dados fictícios
anos = [2018, 2019, 2020, 2021, 2022]
valores = [50, 60, 70, 65, 80]

# Criar o gráfico de linhas
plt.plot(anos, valores, marker='o', color='red', linestyle='-', linewidth=2)

# Adicionar título e rótulos aos eixos
plt.title('Gráfico de Linhas de Dados Fictícios')
plt.xlabel('Ano')
plt.ylabel('Valor')

# Exibir o gráfico
plt.show()
