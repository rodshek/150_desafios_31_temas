# desafio_24_1.py

import requests


def obter_dados(url):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        return resposta.json()      # Retorna a resposta no formato JSON
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None


if __name__ == "__main__":
    url = "https://api.exemplo.com/dados"
    dados = obter_dados(url)
    if dados:
        print("Dados obtidos com sucesso:")
        print(dados)
    else:
        print("Não foi possível obter os dados.")
