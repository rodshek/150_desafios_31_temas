# desafio_24_5.py

import matplotlib.pyplot as plt
import pandas as pd


def plotar_grafico(caminho_arquivo):
    try:
        # Lê o arquivo CSV usando pandas
        dados = pd.read_csv(caminho_arquivo)

        # Supondo que o CSV tem colunas 'Data' e 'Valor'
        if 'Data' not in dados.columns or 'Valor' not in dados.columns:
            raise ValueError(
                "O arquivo CSV deve conter as colunas 'Data' e 'Valor'.")

        # Converte a coluna 'Data' para datetime
        dados['Data'] = pd.to_datetime(dados['Data'])

        # Cria o gráfico de linha
        plt.figure(figsize=(10, 6))
        plt.plot(dados['Data'], dados['Valor'],
                 marker='o', linestyle='-', color='b')
        plt.title('Gráfico de Linha de Valores ao Longo do Tempo')
        plt.xlabel('Data')
        plt.ylabel('Valor')
        plt.grid(True)
        plt.xticks(rotation=45)

        # Exibe o gráfico
        plt.tight_layout()  # Ajusta o layout para não cortar os rótulos
        plt.show()

    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")


if __name__ == "__main__":
    caminho_arquivo = "dados.csv"  # Substitua pelo caminho para o seu arquivo CSV
    plotar_grafico(caminho_arquivo)
