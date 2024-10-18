import pandas as pd
import requests


def obter_dados_api(url):
    """Obtém dados JSON de uma API e retorna o conteúdo."""
    resposta = requests.get(url)
    resposta.raise_for_status()  # Levanta um erro para códigos de status HTTP ruins
    return resposta.json()


def analisar_dados(dados):
    """Realiza análises básicas sobre os dados JSON."""
    # Converte os dados JSON em um DataFrame do pandas
    df = pd.DataFrame(dados)

    # Exemplo de análises básicas
    analises = {
        'total_usuarios': len(df),
        'primeiro_usuario': df.iloc[0]['login'] if not df.empty else 'N/A',
        'colunas': list(df.columns)
    }

    return analises


def salvar_csv(dados, arquivo_csv):
    """Salva os dados em um arquivo CSV."""
    df = pd.DataFrame(dados)
    df.to_csv(arquivo_csv, index=False)


# URL da API
url = 'https://api.github.com/users'

# Obtém e analisa os dados
dados_api = obter_dados_api(url)
analises = analisar_dados(dados_api)

# Exibe as análises
print("Análises dos dados:")
print(analises)

# Salva os dados em um arquivo CSV
salvar_csv(dados_api, 'dados_usuarios_github.csv')

print("Dados dos usuários salvos em 'dados_usuarios_github.csv'.")
