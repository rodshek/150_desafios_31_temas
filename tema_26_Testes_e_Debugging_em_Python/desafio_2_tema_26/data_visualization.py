import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Carregar os dados de um arquivo CSV
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Criar um gráfico de dispersão


def create_scatter_plot(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='x', y='y', hue='category', palette='viridis')
    plt.title('Gráfico de Dispersão')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.grid(True)
    plt.savefig('scatter_plot.png')
    plt.show()


if __name__ == '__main__':
    file_path = 'data.csv'  # Altere para o caminho do seu arquivo CSV
    data = load_data(file_path)
    create_scatter_plot(data)
