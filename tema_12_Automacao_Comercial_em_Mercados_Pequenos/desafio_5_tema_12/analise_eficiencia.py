import pandas as pd

# Dados simulados sobre a eficiência energética dos aparelhos
dados = {
    'Aparelho': ['Lâmpada LED', 'Aparelho de Ar-Condicionado', 'Geladeira', 'Micro-ondas', 'Televisão'],
    'Consumo (kWh/ano)': [50, 1200, 350, 100, 200],
    'Horas de Uso Diário': [5, 8, 24, 0.5, 4],
    'Eficiência (kWh/hora)': [50/5/365, 1200/(8*365), 350/(24*365), 100/(0.5*365), 200/(4*365)]
}

# Criar um DataFrame
df = pd.DataFrame(dados)

# Gerar o relatório em formato CSV
df.to_csv('relatorio_eficiencia_energetica.csv', index=False)

print("Relatório gerado com sucesso: relatorio_eficiencia_energetica.csv")

"""
export CONSUMO_0=50
export CONSUMO_1=1200
export CONSUMO_2=350
export CONSUMO_3=100
export CONSUMO_4=200
export HORAS_USO_0=5
export HORAS_USO_1=8
export HORAS_USO_2=24
export HORAS_USO_3=0.5
export HORAS_USO_4=4

"""
