import os
import time

import psutil


def monitorar_memoria(duracao, intervalo, processo_id):
    """Monitora o uso de memória de um processo e gera um relatório."""

    # Obtém o processo pelo ID
    try:
        processo = psutil.Process(processo_id)
    except psutil.NoSuchProcess:
        print(f"Processo com ID {processo_id} não encontrado.")
        return

    # Relatório
    relatorio = []
    inicio = time.time()

    while (time.time() - inicio) < duracao:
        memoria_info = processo.memory_info()
        uso_memoria = memoria_info.rss / (1024 ** 2)  # Convertido para MB
        tempo_atual = time.strftime('%Y-%m-%d %H:%M:%S')
        relatorio.append(f"{tempo_atual}: {uso_memoria:.2f} MB")
        time.sleep(intervalo)

    return relatorio


def salvar_relatorio(relatorio, arquivo):
    """Salva o relatório de uso de memória em um arquivo."""
    with open(arquivo, 'w') as f:
        f.write("\n".join(relatorio))


# Defina o ID do processo, a duração da monitoria e o intervalo
processo_id = int(input("Digite o ID do processo a ser monitorado: "))
duracao = 60  # Duração da monitoria em segundos
intervalo = 5  # Intervalo entre leituras em segundos

# Monitora o uso de memória
relatorio_memoria = monitorar_memoria(duracao, intervalo, processo_id)

# Salva o relatório em um arquivo
salvar_relatorio(relatorio_memoria, 'relatorio_memoria.txt')

print("Relatório de uso de memória salvo em 'relatorio_memoria.txt'.")
