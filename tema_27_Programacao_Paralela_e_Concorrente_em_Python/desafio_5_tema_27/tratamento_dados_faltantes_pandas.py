import numpy as np
import pandas as pd

# Criar um DataFrame com dados faltantes
data = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', np.nan],
    'Idade': [28, np.nan, 45, 23, 34],
    'Cidade': ['São Paulo', 'Rio de Janeiro', np.nan, 'Curitiba', 'São Paulo']
}

df = pd.DataFrame(data)

# Mostrar o DataFrame original
print("DataFrame Original com Dados Faltantes:")
print(df)

# Tratar dados faltantes
# Preencher dados faltantes com valores específicos
df['Nome'].fillna('Desconhecido', inplace=True)
# Preencher com a média da idade
df['Idade'].fillna(df['Idade'].mean(), inplace=True)
df['Cidade'].fillna('Não Informado', inplace=True)

# Remover linhas com dados faltantes
# df.dropna(inplace=True)  # Caso queira remover linhas com qualquer dado faltante

# Mostrar o DataFrame após tratamento
print("\nDataFrame após Tratamento dos Dados Faltantes:")
print(df)
