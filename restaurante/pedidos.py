class PedidoManager:
    def __init__(self, estoque, caixa):
        self.estoque = estoque
        self.caixa = caixa
        self.pedidos_cozinha = []
        self.pedidos_faturados = []

    def novo_pedido(self, cliente, produto, quantidade):
        pedido = {
            "cliente": cliente,
            "produto": produto,
            "quantidade": quantidade
        }
        self.pedidos_cozinha.append(pedido)
        self.estoque.reduzir_estoque(produto, quantidade)

    def listar_pedidos_cozinha(self):
        return [f"{pedido['cliente']} - {pedido['produto']} x{pedido['quantidade']}" for pedido in self.pedidos_cozinha]

    def despachar_pedido(self):
        if self.pedidos_cozinha:
            pedido = self.pedidos_cozinha.pop(0)
            self.pedidos_faturados.append(pedido)
            return pedido
        return None

    def listar_pedidos_faturados(self):
        return [f"{pedido['cliente']} - {pedido['produto']} x{pedido['quantidade']}" for pedido in self.pedidos_faturados]

    def relatorio_pedidos_dia(self):
        return [f"{pedido['cliente']} - {pedido['produto']} x{pedido['quantidade']}" for pedido in self.pedidos_faturados]
