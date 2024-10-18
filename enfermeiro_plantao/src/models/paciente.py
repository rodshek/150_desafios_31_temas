class Paciente:
    def __init__(self, id, nome, historico):
        self.id = id
        self.nome = nome
        self.historico = historico

    def adicionar_evento_historico(self, evento):
        self.historico.append(evento)
