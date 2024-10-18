import matplotlib.pyplot as plt
import pandas as pd


def carregar_dados(caminho_arquivo):
    """Carrega os dados do arquivo CSV em um DataFrame do pandas."""
    return pd.read_csv(caminho_arquivo)


def analise_exploratoria(df):
    """Realiza uma análise exploratória básica dos dados."""
    print("Informações gerais sobre o DataFrame:")
    print(df.info())
    print("\nEstatísticas descritivas das variáveis numéricas:")
    print(df.describe())


def visualizar_distribuicoes(df):
    """Plota gráficos de distribuição para variáveis numéricas no DataFrame."""
    num_vars = df.select_dtypes(include=['number']).columns
    plt.figure(figsize=(12, 10))

    for i, var in enumerate(num_vars, 1):
        plt.subplot(len(num_vars), 1, i)
        plt.hist(df[var].dropna(), bins=30, edgecolor='black')
        plt.title(f'Distribuição de {var}')
        plt.xlabel(var)
        plt.ylabel('Frequência')

    plt.tight_layout()
    plt.show()


def main():
    """Função principal para executar o script."""
    caminho_arquivo = 'dados.csv'  # Substitua pelo caminho do seu arquivo CSV
    df = carregar_dados(caminho_arquivo)
    analise_exploratoria(df)
    visualizar_distribuicoes(df)


if __name__ == '__main__':
    main()
