import pandas as pd


# Função para calcular a pegada de carbono
def calcular_pegada_carbono(consumo_diario_kwh):
    # Fator de emissão de carbono (kg CO2/kWh)
    fator_emissao = 0.233  # Valor médio para a geração de energia elétrica
    return consumo_diario_kwh * fator_emissao


# Dados de consumo diário (em kWh)
data = {
    'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'],
    # Exemplo de consumo diário
    'Consumo_Diario_kWh': [12, 15, 10, 13, 14, 9, 11]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Calcular pegada de carbono
df['Pegada_Carbono_kg'] = df['Consumo_Diario_kWh'].apply(
    calcular_pegada_carbono)

# Exibir resultados
print(df)
