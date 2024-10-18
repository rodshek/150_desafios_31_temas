import matplotlib.pyplot as plt
import pandas as pd


def ler_dados(arquivo_csv):
    """Lê os dados do arquivo CSV."""
    return pd.read_csv(arquivo_csv)


def gerar_grafico(dados):
    """Gera um gráfico de barras a partir dos dados fornecidos."""
    atividades = dados['Atividade']
    tempo = dados['Tempo']

    plt.figure(figsize=(10, 6))
    plt.bar(atividades, tempo, color='skyblue')
    plt.xlabel('Atividade')
    plt.ylabel('Tempo (horas)')
    plt.title('Tempo Dedicado a Diferentes Atividades Diárias')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def main():
    """Função principal para executar o script."""
    arquivo_csv = 'dados_atividades.csv'
    dados = ler_dados(arquivo_csv)
    gerar_grafico(dados)


if __name__ == '__main__':
    main()
