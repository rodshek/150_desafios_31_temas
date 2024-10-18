class Estoque:
    def __init__(self):
        self.produtos = {
            "Dog": 50,
            "Lanche": 50,
            "Pizza": 50
        }

    def reduzir_estoque(self, produto, quantidade):
        if produto in self.produtos and self.produtos[produto] >= quantidade:
            self.produtos[produto] -= quantidade
        else:
            raise ValueError("Estoque insuficiente.")

    def adicionar_estoque(self, produto, quantidade):
        if produto in self.produtos:
            self.produtos[produto] += quantidade

    def listar_estoque(self):
        return self.produtos
