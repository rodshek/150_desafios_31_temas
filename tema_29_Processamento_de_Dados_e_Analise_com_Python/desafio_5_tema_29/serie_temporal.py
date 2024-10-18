import matplotlib.pyplot as plt
import pandas as pd

# Criação de uma série temporal de exemplo
data = {
    'data': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'valor': [100, 110, 105, 120, 115, 130, 125, 140, 135, 150, 145, 160]
}
df = pd.DataFrame(data)

# Configuração do gráfico
plt.figure(figsize=(12, 6))
plt.plot(df['data'], df['valor'], marker='o', linestyle='-', color='b')

# Adicionando título e rótulos
plt.title('Série Temporal de Exemplo')
plt.xlabel('Data')
plt.ylabel('Valor')

# Exibindo o gráfico
plt.grid(True)
plt.show()
