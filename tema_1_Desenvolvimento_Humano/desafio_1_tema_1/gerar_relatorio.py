import pandas as pd


# Função para gerar relatório a partir de um arquivo CSV
def gerar_relatorio(csv_path):
    # Ler o arquivo CSV
    df = pd.read_csv(csv_path)

    # Exibir as primeiras linhas do DataFrame
    print("Primeiras linhas do arquivo CSV:")
    print(df.head())

    # Calcular estatísticas básicas
    estatisticas = df.describe()

    # Exibir estatísticas básicas
    print("\nEstatísticas básicas do DataFrame:")
    print(estatisticas)

    # Salvar o relatório em um novo arquivo Excel
    estatisticas.to_excel('relatorio_estatisticas.xlsx', engine='openpyxl')
    print("\nRelatório de estatísticas salvo como 'relatorio_estatisticas.xlsx'.")


# Caminho para o arquivo CSV
csv_path = 'dados_clientes.csv'

# Gerar o relatório
gerar_relatorio(csv_path)
