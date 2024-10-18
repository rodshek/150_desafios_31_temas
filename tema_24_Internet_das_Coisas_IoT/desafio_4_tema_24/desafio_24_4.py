# desafio_24_4.py

import pandas as pd


def processar_csv(caminho_arquivo):
    try:
        # Lê o arquivo CSV usando pandas
        dados = pd.read_csv(caminho_arquivo)

        # Exibe as primeiras linhas dos dados
        print("Primeiras linhas dos dados:")
        print(dados.head())

        # Mostra algumas informações gerais sobre os dados
        print("\nInformações gerais sobre os dados:")
        print(dados.info())

        # Calcula e exibe estatísticas descritivas
        print("\nEstatísticas descritivas:")
        print(dados.describe())

        # Exemplo de operação: Contar o número de valores nulos em cada coluna
        print("\nNúmero de valores nulos em cada coluna:")
        print(dados.isnull().sum())

    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")


if __name__ == "__main__":
    caminho_arquivo = "dados.csv"  # Substitua pelo caminho para o seu arquivo CSV
    processar_csv(caminho_arquivo)
