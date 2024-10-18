import plotly.graph_objects as go

# Dados para visualização
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criar o gráfico
fig = go.Figure()

# Adicionar a linha de dados
fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', name='Dados'))

# Adicionar título e rótulos
fig.update_layout(
    title='Exemplo de Gráfico com Plotly',
    xaxis_title='Eixo X',
    yaxis_title='Eixo Y'
)

# Exibir o gráfico
fig.show()
