import pandas as pd
import plotly.express as px


# Carregar os dados de um arquivo CSV
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Criar um gráfico de dispersão interativo


def create_scatter_plot(data):
    fig = px.scatter(data, x='x', y='y', color='category',
                     title='Gráfico de Dispersão Interativo',
                     labels={'x': 'Eixo X', 'y': 'Eixo Y'},
                     hover_name='category')

    fig.update_layout(legend_title_text='Categoria')
    fig.write_html('scatter_plot.html')
    fig.show()


if __name__ == '__main__':
    file_path = 'data.csv'  # Altere para o caminho do seu arquivo CSV
    data = load_data(file_path)
    create_scatter_plot(data)
