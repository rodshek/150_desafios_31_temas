class Cozinha:
    def __init__(self):
        self.pedidos_cozinha = []

    def adicionar_pedido(self, pedido):
        self.pedidos_cozinha.append(pedido)

    def listar_pedidos(self):
        return [f"{pedido.cliente}: {pedido.produto} x{pedido.quantidade} (Status: {pedido.status})" for pedido in self.pedidos_cozinha]

    def despachar_pedido(self, index):
        if 0 <= index < len(self.pedidos_cozinha):
            return self.pedidos_cozinha.pop(index)
        else:
            raise IndexError("Pedido não encontrado.")
