import sqlite3


def conectar_banco():
    conn = sqlite3.connect('plantao.db')
    return conn


def criar_tabelas():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS pacientes (id INTEGER PRIMARY KEY, nome TEXT, historico TEXT)''')
    conn.commit()
    conn.close()


def buscar_historico_paciente(paciente_id):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT historico FROM pacientes WHERE id=?", (paciente_id,))
    historico = cursor.fetchone()
    conn.close()
    if historico:
        return historico[0]
    else:
        return "Paciente não encontrado."
