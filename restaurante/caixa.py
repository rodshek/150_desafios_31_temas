class Caixa:
    def __init__(self):
        self.pedidos_faturados = []

    def faturar_todos_pedidos(self):
        self.pedidos_faturados.clear()

    def listar_pedidos(self):
        return self.pedidos_faturados
