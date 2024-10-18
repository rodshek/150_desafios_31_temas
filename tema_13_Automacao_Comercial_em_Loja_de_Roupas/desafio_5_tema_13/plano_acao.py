from datetime import datetime, timedelta

import pandas as pd


# Função para gerar o plano de ação
def gerar_plano_acao(objetivos, tarefas_por_objetivo, prazo_inicial):
    plano = []
    prazo_atual = prazo_inicial

    for objetivo in objetivos:
        for tarefa in range(tarefas_por_objetivo):
            plano.append({
                'Objetivo': objetivo,
                'Tarefa': f'Tarefa {tarefa + 1}',
                'Data de Início': prazo_atual.strftime('%Y-%m-%d'),
                'Data de Conclusão': (prazo_atual + timedelta(days=7)).strftime('%Y-%m-%d')
            })
            # Ajusta a data para a próxima tarefa
            prazo_atual += timedelta(days=7)

    return pd.DataFrame(plano)


# Definições do plano de ação
objetivos = [
    'Desenvolver habilidades em Python',
    'Aprimorar técnicas de análise de dados',
    'Construir um portfólio profissional'
]
tarefas_por_objetivo = 3  # Número de tarefas para cada objetivo
prazo_inicial = datetime(2024, 8, 1)  # Data de início do plano

# Gerar o plano de ação
plano_acao_df = gerar_plano_acao(
    objetivos, tarefas_por_objetivo, prazo_inicial)

# Salvar o plano de ação em um arquivo CSV
plano_acao_df.to_csv('plano_acao.csv', index=False)

print("Plano de ação gerado com sucesso: plano_acao.csv")
