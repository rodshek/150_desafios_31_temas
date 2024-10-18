import pandas as pd
import requests
from bs4 import BeautifulSoup


def extrair_dados_tabela(url, seletores):
    """Extrai dados de uma tabela de um site e retorna uma lista de dicionários."""
    resposta = requests.get(url)
    resposta.raise_for_status()  # Levanta um erro para códigos de status HTTP ruins

    soup = BeautifulSoup(resposta.text, 'html.parser')
    tabela = soup.select_one(seletores['tabela'])  # Seleciona a tabela
    linhas = tabela.find_all('tr')  # Encontra todas as linhas da tabela

    dados = []
    for linha in linhas:
        colunas = linha.find_all('td')
        dados.append([coluna.get_text(strip=True) for coluna in colunas])

    return dados


def salvar_csv(dados, arquivo_csv):
    """Salva os dados em um arquivo CSV."""
    df = pd.DataFrame(dados[1:], columns=dados[0])
    df.to_csv(arquivo_csv, index=False)


# URL da página e seletores para a tabela
url = 'https://example.com/tabela'  # Substitua pela URL do site com a tabela
seletores = {
    'tabela': 'table'  # Seletor CSS para a tabela (ajuste conforme necessário)
}

# Extrai dados e salva em um arquivo CSV
dados_tabela = extrair_dados_tabela(url, seletores)
salvar_csv(dados_tabela, 'dados_tabela.csv')

print("Dados da tabela salvos em 'dados_tabela.csv'.")
