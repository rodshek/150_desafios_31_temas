class Relatorio:
    def __init__(self, pedido_manager):
        self.pedido_manager = pedido_manager

    def gerar_relatorio_pedidos(self):
        return self.pedido_manager.relatorio_pedidos_dia()

    def exportar_para_excel(self, caminho):
        with open(caminho, "w") as arquivo:
            pedidos = self.pedido_manager.relatorio_pedidos_dia()
            for pedido in pedidos:
                arquivo.write(f"{pedido}\n")
        print(f"Relatório exportado para {caminho}")

    def gerar_relatorio_faturamento(self, caixa):
        relatorio = caixa.relatorio_faturamento()
        return relatorio
