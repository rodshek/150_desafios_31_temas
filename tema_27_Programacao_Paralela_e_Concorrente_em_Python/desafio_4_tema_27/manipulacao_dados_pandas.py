import pandas as pd

# Criar um DataFrame a partir de um dicionário
data = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Idade': [28, 34, 45, 23],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
}

df = pd.DataFrame(data)

# Mostrar o DataFrame
print("DataFrame Original:")
print(df)

# Adicionar uma nova coluna
df['Profissão'] = ['Engenheira', 'Médico', 'Professor', 'Designer']

# Filtrar linhas onde a idade é maior que 30
df_maior_30 = df[df['Idade'] > 30]

# Mostrar o DataFrame modificado
print("\nDataFrame com nova coluna e filtro:")
print(df_maior_30)
