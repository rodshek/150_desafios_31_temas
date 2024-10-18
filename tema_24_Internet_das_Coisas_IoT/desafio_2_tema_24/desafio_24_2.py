# desafio_24_2.py

import pandas as pd


def processar_csv(caminho_arquivo):
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(caminho_arquivo)

        # Exibe as primeiras linhas do DataFrame
        print("Primeiras linhas do DataFrame:")
        print(df.head())

        # Calcula e exibe estatísticas descritivas
        print("\nEstatísticas descritivas:")
        print(df.describe())

        # Calcula e exibe a soma de uma coluna específica
        if 'valor' in df.columns:
            soma_valor = df['valor'].sum()
            print(f"\nSoma da coluna 'valor': {soma_valor}")
        else:
            print("\nColuna 'valor' não encontrada.")

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except pd.errors.EmptyDataError:
        print("O arquivo está vazio.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")


if __name__ == "__main__":
    caminho_arquivo = "dados.csv"  # Substitua pelo caminho do seu arquivo CSV
    processar_csv(caminho_arquivo)
