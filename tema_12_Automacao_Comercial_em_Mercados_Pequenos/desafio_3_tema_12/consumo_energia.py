import pandas as pd

# Dados dos eletrodomésticos
dados = {
    'Eletrodoméstico': ['Geladeira', 'Máquina de Lavar', 'Ar Condicionado', 'Micro-ondas'],
    'Consumo (kWh)': [1.2, 0.8, 2.5, 1.0],  # Consumo por hora
    'Custo por kWh (R$)': [0.6, 0.6, 0.6, 0.6]  # Custo por kWh em reais
}

# Criar um DataFrame
df = pd.DataFrame(dados)

# Tempo de uso em horas
tempo_uso = {
    'Geladeira': 24,          # Exemplo: uso contínuo por 24 horas
    'Máquina de Lavar': 1,    # Exemplo: uso de 1 hora por semana
    'Ar Condicionado': 5,     # Exemplo: uso de 5 horas por dia
    'Micro-ondas': 0.5        # Exemplo: uso de 30 minutos por dia
}

# Adicionar coluna de custo total
df['Tempo de Uso (horas)'] = df['Eletrodoméstico'].map(tempo_uso)
df['Custo Total (R$)'] = df['Consumo (kWh)'] * \
    df['Custo por kWh (R$)'] * df['Tempo de Uso (horas)']

# Exibir o DataFrame
print("Custo Total de Energia dos Eletrodomésticos:")
print(df)
