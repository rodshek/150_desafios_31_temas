import os
import subprocess
import sys


def analisar_codigo(diretorio):
    """Executa a análise de código e gera um relatório."""

    # Comando para obter a complexidade ciclomática e outras métricas
    comando = ['radon', 'cc', '-s', diretorio]

    try:
        resultado = subprocess.run(
            comando, capture_output=True, text=True, check=True)
        return resultado.stdout
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar radon: {e}")
        sys.exit(1)


def contar_linhas_codigo(diretorio):
    """Conta o número de linhas de código no diretório especificado."""
    total_linhas = 0
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if file.endswith('.py'):
                caminho_arquivo = os.path.join(root, file)
                with open(caminho_arquivo, 'r') as f:
                    total_linhas += len(f.readlines())
    return total_linhas


# Defina o diretório do projeto aqui
diretorio_projeto = '.'  # Atualize com o diretório do seu projeto

# Gera o relatório de complexidade ciclomática
relatorio_complexidade = analisar_codigo(diretorio_projeto)

# Conta o número de linhas de código
numero_linhas_codigo = contar_linhas_codigo(diretorio_projeto)

# Exibe o relatório
print("Relatório de Qualidade do Código:")
print("------------------------------")
print(f"Número total de linhas de código: {numero_linhas_codigo}")
print("\nComplexidade Ciclomática e Outras Métricas:")
print(relatorio_complexidade)
