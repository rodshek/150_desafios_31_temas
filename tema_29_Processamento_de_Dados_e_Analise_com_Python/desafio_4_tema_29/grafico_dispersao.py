import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Criação de um DataFrame de exemplo
dados = {
    'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'y': [2.3, 3.5, 4.7, 5.1, 6.8, 7.4, 8.2, 9.5, 10.1, 11.2],
    'categoria': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
}
df = pd.DataFrame(dados)

# Geração do gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='x', y='y', hue='categoria',
                style='categoria', palette='deep')

# Adicionando título e rótulos
plt.title('Gráfico de Dispersão Exemplo')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Exibindo o gráfico
plt.legend(title='Categoria')
plt.show()
