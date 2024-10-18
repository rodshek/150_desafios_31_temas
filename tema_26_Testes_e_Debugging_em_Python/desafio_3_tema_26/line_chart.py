import matplotlib.pyplot as plt
import pandas as pd


# Carregar os dados de um arquivo CSV
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Criar um gráfico de linhas


def create_line_chart(data):
    plt.figure(figsize=(10, 6))
    for category in data['category'].unique():
        subset = data[data['category'] == category]
        plt.plot(subset['x'], subset['y'], marker='o', label=category)

    plt.title('Gráfico de Linhas')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.legend(title='Categoria')
    plt.grid(True)
    plt.savefig('line_chart.png')
    plt.show()


if __name__ == '__main__':
    file_path = 'data.csv'  # Altere para o caminho do seu arquivo CSV
    data = load_data(file_path)
    create_line_chart(data)
