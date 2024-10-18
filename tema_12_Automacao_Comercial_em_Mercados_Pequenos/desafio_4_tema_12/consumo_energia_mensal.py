import matplotlib.pyplot as plt
import pandas as pd

# Dados simulados de consumo de energia mensal (em kWh)
dados = {
    'Mês': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Consumo (kWh)': [120, 115, 130, 125, 140, 150, 160, 155, 145, 135, 125, 110]
}

# Criar um DataFrame
df = pd.DataFrame(dados)

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(df['Mês'], df['Consumo (kWh)'], marker='o', linestyle='-', color='b')

# Adicionar título e rótulos
plt.title('Consumo de Energia Mensal')
plt.xlabel('Mês')
plt.ylabel('Consumo (kWh)')

# Adicionar grades
plt.grid(True)

# Mostrar o gráfico
plt.show()

"""
set CONSUMO_JAN=120
set CONSUMO_FEB=115
set CONSUMO_MAR=130
set CONSUMO_APR=125
set CONSUMO_MAY=140
set CONSUMO_JUN=150
set CONSUMO_JUL=160
set CONSUMO_AUG=155
set CONSUMO_SEP=145
set CONSUMO_OCT=135
set CONSUMO_NOV=125
set CONSUMO_DEC=110

"""
