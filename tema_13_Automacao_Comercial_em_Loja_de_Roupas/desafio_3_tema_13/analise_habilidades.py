import re
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd

# Dados simulados sobre cargos e habilidades
dados = {
    'Cargo': ['Analista de Dados', 'Desenvolvedor Python', 'Gerente de Projeto', 'Analista de Sistemas', 'Desenvolvedor Frontend'],
    'Habilidades': [
        'Python, SQL, Excel',
        'Python, Django, SQL, Git',
        'Gerenciamento de Projetos, Scrum, Excel',
        'Python, SQL, Análise de Sistemas',
        'JavaScript, React, HTML, CSS'
    ]
}

# Criar um DataFrame
df = pd.DataFrame(dados)

# Contar as habilidades


# Função para contar as habilidades
def contar_habilidades(habilidades):
    habilidades_list = ' '.join(habilidades).split(', ')
    return Counter(habilidades_list)


# Contar as habilidades
habilidades_contadas = contar_habilidades(df['Habilidades'])

# Criar DataFrame das habilidades
habilidades_df = pd.DataFrame(habilidades_contadas.items(), columns=[
                              'Habilidade', 'Quantidade'])
habilidades_df = habilidades_df.sort_values(by='Quantidade', ascending=False)

# Gerar gráfico
plt.figure(figsize=(10, 6))
plt.bar(habilidades_df['Habilidade'],
        habilidades_df['Quantidade'], color='skyblue')
plt.xlabel('Habilidades')
plt.ylabel('Quantidade')
plt.title('Habilidades mais Comuns Necessárias para Cargos Futuros')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Salvar o gráfico
plt.savefig('habilidades_comuns.png')
plt.show()

# Gerar relatório em formato CSV
habilidades_df.to_csv('habilidades_comuns.csv', index=False)

print("Relatório gerado com sucesso: habilidades_comuns.csv")
print("Gráfico salvo como: habilidades_comuns.png")

"""
set CARGOS=Analista de Dados, Desenvolvedor Python, Gerente de Projeto, Analista de Sistemas, Desenvolvedor Frontend
set HABILIDADES=Python, SQL, Excel, Python, Django, SQL, Git, Gerenciamento de Projetos, Scrum, Excel, Python, SQL, Análise de Sistemas, JavaScript, React, HTML, CSS

"""
