import matplotlib.pyplot as plt

# Dados fictícios
categorias = ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D']
valores = [20, 35, 25, 20]

# Criar o gráfico de pizza
plt.pie(valores, labels=categorias, autopct='%1.1f%%', colors=[
        'gold', 'lightcoral', 'lightskyblue', 'lightgreen'])

# Adicionar título
plt.title('Gráfico de Pizza de Dados Fictícios')

# Exibir o gráfico
plt.show()
