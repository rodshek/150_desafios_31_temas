# desafio_24_3.py

import requests


def obter_dados_api(url):
    try:
        # Faz uma requisição GET à URL fornecida
        resposta = requests.get(url)

        # Verifica se a resposta foi bem-sucedida
        if resposta.status_code == 200:
            # Converte a resposta para JSON
            dados = resposta.json()

            # Exibe os primeiros dados da resposta
            print("Dados recebidos da API:")
            print(dados)

            # Exemplo de processamento adicional: contar itens
            if isinstance(dados, list):
                print(f"\nNúmero de itens recebidos: {len(dados)}")
            elif isinstance(dados, dict):
                print(f"\nChaves dos dados recebidos: {list(dados.keys())}")
            else:
                print("\nFormato de dados não esperado.")
        else:
            print(f"Falha na requisição: Status code {resposta.status_code}")

    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")


if __name__ == "__main__":
    url = "https://api.exemplo.com/dados"  # Substitua pela URL da sua API
    obter_dados_api(url)
