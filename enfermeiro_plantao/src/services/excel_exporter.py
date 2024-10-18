import pandas as pd


def gerar_relatorio_pacientes():
    dados = {
        "ID": [1, 2, 3],
        "Nome": ["Paciente 1", "Paciente 2", "Paciente 3"],
        "Histórico": ["Evento A", "Evento B", "Evento C"]
    }

    df = pd.DataFrame(dados) df.to_excel("relatorio_pacientes.xlsx", index=False)
