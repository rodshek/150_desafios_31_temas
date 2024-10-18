import time

import pandas as pd
import psutil


def coletar_dados():
    """Coleta dados de uso de CPU, memória e disco."""
    uso_cpu = psutil.cpu_percent(interval=1)  # Percentual de uso da CPU
    memoria = psutil.virtual_memory()
    uso_memoria = memoria.percent  # Percentual de uso da memória
    disco = psutil.disk_usage('/')
    uso_disco = disco.percent  # Percentual de uso do disco

    return {
        'uso_cpu': uso_cpu,
        'uso_memoria': uso_memoria,
        'uso_disco': uso_disco
    }


def monitorar_recurso(duracao, intervalo):
    """Monitora os recursos do sistema por uma duração específica e salva os dados em um DataFrame."""
    dados = []

    for _ in range(int(duracao / intervalo)):
        dados.append(coletar_dados())
        time.sleep(intervalo)

    return pd.DataFrame(dados)


def salvar_csv(df, arquivo_csv):
    """Salva os dados em um arquivo CSV."""
    df.to_csv(arquivo_csv, index=False)


# Configurações
duracao = 60  # Duração da monitoração em segundos
intervalo = 5  # Intervalo entre coletas em segundos

# Monitora os recursos e salva os dados
df_recurso = monitorar_recurso(duracao, intervalo)
salvar_csv(df_recurso, 'relatorio_recurso_sistema.csv')

print("Relatório de uso dos recursos do sistema salvo em 'relatorio_recurso_sistema.csv'.")
