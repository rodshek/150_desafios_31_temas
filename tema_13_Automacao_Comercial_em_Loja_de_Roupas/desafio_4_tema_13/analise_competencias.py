from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup


# Função para obter o HTML do perfil
def obter_html_perfil(url):
    resposta = requests.get(url)
    resposta.raise_for_status()
    return resposta.text

# Função para extrair competências do HTML


def extrair_competencias(html):
    soup = BeautifulSoup(html, 'html.parser')
    competencias = []

    # Exemplo de extração fictícia de competências
    for tag in soup.find_all('span', class_='competencia'):
        competencias.append(tag.get_text())

    return competencias

# Função para contar as competências


def contar_competencias(competencias):
    return Counter(competencias)


# URL fictícia do perfil (substitua por uma URL real se aplicável)
url = 'https://www.exemplo.com/perfil'

# Obter e analisar o perfil
html = obter_html_perfil(url)
competencias = extrair_competencias(html)
competencias_contadas = contar_competencias(competencias)

# Criar DataFrame das competências

competencias_df = pd.DataFrame(competencias_contadas.items(), columns=[
                               'Competência', 'Quantidade'])
competencias_df = competencias_df.sort_values(by='Quantidade', ascending=False)

# Gerar gráfico
plt.figure(figsize=(10, 6))
plt.bar(competencias_df['Competência'],
        competencias_df['Quantidade'], color='skyblue')
plt.xlabel('Competências')
plt.ylabel('Quantidade')
plt.title('Competências mais Alinhadas com as Tendências do Mercado')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Salvar o gráfico
plt.savefig('competencias_tendencias.png')
plt.show()

# Gerar relatório em formato CSV
competencias_df.to_csv('competencias_tendencias.csv', index=False)

print("Relatório gerado com sucesso: competencias_tendencias.csv")
print("Gráfico salvo como: competencias_tendencias.png")

"""
set URL_PERFIL=https://www.exemplo.com/perfil

"""
