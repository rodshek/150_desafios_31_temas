from datetime import datetime


def obter_data_atual():
    return datetime.now().strftime("%d/%m/%Y")


def obter_hora_atual():
    return datetime.now().strftime("%H:%M:%S")
