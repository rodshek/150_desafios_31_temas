import matplotlib.pyplot as plt
import pandas as pd


# Carregar os dados de um arquivo CSV
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Criar um gráfico simples


def create_plot(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['x'], data['y'], marker='o', linestyle='-', color='b')
    plt.title('Gráfico de Linha Simples')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.grid(True)
    plt.savefig('plot.png')
    plt.show()


if __name__ == '__main__':
    file_path = 'data.csv'  # Altere para o caminho do seu arquivo CSV
    data = load_data(file_path)
    create_plot(data)
