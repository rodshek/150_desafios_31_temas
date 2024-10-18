import numpy as np


# Função para calcular o impacto ambiental
def calcular_impacto_ambiental(distancia, tipo_transporte):
    # Fatores de emissão para diferentes tipos de transporte (kg CO2/km)
    fatores_emissao = {
        'carro': 0.2,
        'avião': 0.25,
        'ônibus': 0.05,
        'trem': 0.03
    }

    # Verificar se o tipo de transporte está no dicionário
    if tipo_transporte not in fatores_emissao:
        raise ValueError(f"Tipo de transporte inválido: {tipo_transporte}")

    fator_emissao = fatores_emissao[tipo_transporte]
    return distancia * fator_emissao


# Distâncias percorridas (em km)
distancias = np.array([100, 200, 300, 400, 500])  # Exemplo de distâncias
tipos_transporte = ['carro', 'avião', 'ônibus', 'trem']

# Calcular o impacto ambiental para cada tipo de transporte e distância
for tipo in tipos_transporte:
    impactos = np.array([calcular_impacto_ambiental(
        distancia, tipo) for distancia in distancias])
    print(f"Impacto ambiental para transporte {tipo}:")
    for distancia, impacto in zip(distancias, impactos):
        print(f"Distância: {distancia} km -> Impacto: {impacto:.2f} kg CO2")
    print()

"""
set FATOR_CARRO=0.25
set FATOR_AVIAO=0.30
set FATOR_ONIBUS=0.04
set FATOR_TREM=0.02
"""
