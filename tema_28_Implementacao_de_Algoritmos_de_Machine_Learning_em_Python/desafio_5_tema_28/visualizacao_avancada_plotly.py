import numpy as np
import plotly.graph_objects as go

# Gerar dados de exemplo
np.random.seed(42)
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)
tamanho = np.random.rand(100) * 20  # Tamanho dos pontos

# Criar o gráfico de dispersão 3D
fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=tamanho,
        color=z,               # Cor dos pontos baseada na coordenada Z
        colorscale='Viridis',  # Mapa de cores
        opacity=0.8
    )
)])

# Adicionar título e rótulos
fig.update_layout(
    title='Gráfico de Dispersão 3D Interativo com Plotly',
    scene=dict(
        xaxis_title='Eixo X',
        yaxis_title='Eixo Y',
        zaxis_title='Eixo Z'
    )
)

# Adicionar informações interativas
fig.update_traces(
    marker=dict(
        colorbar=dict(
            title='Valor de Z',  # Título da barra de cores
            tickvals=[0, 0.5, 1],  # Valores dos ticks
            ticktext=['Baixo', 'Médio', 'Alto']  # Textos dos ticks
        )
    )
)

# Exibir o gráfico
fig.show()
