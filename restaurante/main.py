import tkinter as tk
from tkinter import messagebox, ttk

from caixa import Caixa
from estoque import Estoque
from pedidos import PedidoManager
from produtos import Produtos


class RestauranteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Delivery de Restaurante")

        self.caixa = Caixa()
        self.estoque = Estoque()
        self.pedido_manager = PedidoManager(self.estoque, self.caixa)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        self.setup_pedido_tab()
        self.setup_cozinha_tab()
        self.setup_caixa_tab()
        self.setup_estoque_tab()
        self.setup_relatorios_tab()

    def setup_pedido_tab(self):
        self.pedido_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.pedido_tab, text="Fazer Pedido")

        label_cliente = tk.Label(self.pedido_tab, text="Nome do Cliente:")
        label_cliente.pack(pady=5)
        self.entry_cliente = tk.Entry(self.pedido_tab)
        self.entry_cliente.pack(pady=5)

        label_produto = tk.Label(self.pedido_tab, text="Selecione o Produto:")
        label_produto.pack(pady=5)

        self.produto_var = tk.StringVar(value="Dog")
        self.spinbox_produto = ttk.Spinbox(self.pedido_tab, values=(
            "Dog", "Lanche", "Pizza"), textvariable=self.produto_var)
        self.spinbox_produto.pack(pady=5)

        label_quantidade = tk.Label(self.pedido_tab, text="Quantidade:")
        label_quantidade.pack(pady=5)
        self.entry_quantidade = tk.Spinbox(self.pedido_tab, from_=1, to=6)
        self.entry_quantidade.pack(pady=5)

        btn_fazer_pedido = tk.Button(
            self.pedido_tab, text="Fazer Pedido", command=self.fazer_pedido)
        btn_fazer_pedido.pack(pady=5)

    def setup_cozinha_tab(self):
        self.cozinha_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.cozinha_tab, text="Cozinha")

        self.listbox_cozinha = tk.Listbox(self.cozinha_tab)
        self.listbox_cozinha.pack(padx=10, pady=10, fill='both', expand=True)

        btn_despachar = tk.Button(
            self.cozinha_tab, text="Despachar Pedido", command=self.despachar_pedido)
        btn_despachar.pack(pady=5)

    def setup_caixa_tab(self):
        self.caixa_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.caixa_tab, text="Caixa")

        self.listbox_caixa = tk.Listbox(self.caixa_tab)
        self.listbox_caixa.pack(padx=10, pady=10, fill='both', expand=True)

        btn_faturar = tk.Button(
            self.caixa_tab, text="Faturar", command=self.faturar_pedido)
        btn_faturar.pack(pady=5)

    def setup_estoque_tab(self):
        self.estoque_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.estoque_tab, text="Estoque")

        label_produto = tk.Label(self.estoque_tab, text="Produto:")
        label_produto.pack(pady=5)

        self.produto_estoque_var = tk.StringVar(value="Dog")
        self.spinbox_produto_estoque = ttk.Spinbox(self.estoque_tab, values=(
            "Dog", "Lanche", "Pizza"), textvariable=self.produto_estoque_var)
        self.spinbox_produto_estoque.pack(pady=5)

        label_quantidade_estoque = tk.Label(
            self.estoque_tab, text="Quantidade a adicionar:")
        label_quantidade_estoque.pack(pady=5)

        self.entry_quantidade_estoque = tk.Spinbox(
            self.estoque_tab, from_=1, to=100)
        self.entry_quantidade_estoque.pack(pady=5)

        btn_atualizar_estoque = tk.Button(
            self.estoque_tab, text="Adicionar ao Estoque", command=self.atualizar_estoque)
        btn_atualizar_estoque.pack(pady=5)

    def setup_relatorios_tab(self):
        self.relatorio_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.relatorio_tab, text="Relatórios")

        self.listbox_relatorios = tk.Listbox(self.relatorio_tab)
        self.listbox_relatorios.pack(
            padx=10, pady=10, fill='both', expand=True)

        btn_gerar_relatorio = tk.Button(
            self.relatorio_tab, text="Gerar Relatório", command=self.mostrar_relatorio_pedidos)
        btn_gerar_relatorio.pack(pady=5)

    def fazer_pedido(self):
        cliente = self.entry_cliente.get()
        produto = self.produto_var.get()
        quantidade = int(self.entry_quantidade.get())

        if cliente and produto and quantidade > 0:
            self.pedido_manager.novo_pedido(cliente, produto, quantidade)
            self.mostrar_pedidos_cozinha()
            messagebox.showinfo(
                "Pedido", f"Pedido de {produto} para {cliente} adicionado à cozinha!")
        else:
            messagebox.showerror(
                "Erro", "Preencha todos os campos corretamente.")

    def mostrar_pedidos_cozinha(self):
        self.listbox_cozinha.delete(0, tk.END)
        pedidos = self.pedido_manager.listar_pedidos_cozinha()
        for pedido in pedidos:
            self.listbox_cozinha.insert(tk.END, pedido)

    def despachar_pedido(self):
        pedido = self.pedido_manager.despachar_pedido()
        if pedido:
            messagebox.showinfo(
                "Despacho", f"Pedido de {pedido['produto']} para {pedido['cliente']} despachado!")
            self.mostrar_pedidos_cozinha()
            self.mostrar_pedidos_caixa()
        else:
            messagebox.showerror("Erro", "Não há pedidos para despachar.")

    def mostrar_pedidos_caixa(self):
        self.listbox_caixa.delete(0, tk.END)
        pedidos = self.pedido_manager.listar_pedidos_faturados()
        for pedido in pedidos:
            self.listbox_caixa.insert(tk.END, pedido)

    def faturar_pedido(self):
        if self.listbox_caixa.size() == 0:
            messagebox.showerror("Erro", "Não há pedidos para faturar.")
        else:
            messagebox.showinfo(
                "Faturamento", "Todos os pedidos foram faturados.")
            self.caixa.faturar_todos_pedidos()
            self.mostrar_pedidos_caixa()

    def atualizar_estoque(self):
        produto = self.produto_estoque_var.get()
        quantidade = int(self.entry_quantidade_estoque.get())

        if produto and quantidade > 0:
            self.estoque.adicionar_estoque(produto, quantidade)
            messagebox.showinfo(
                "Estoque", f"{quantidade} unidades de {produto} adicionadas ao estoque!")
        else:
            messagebox.showerror("Erro", "Preencha os campos corretamente.")

    def mostrar_relatorio_pedidos(self):
        pedidos_faturados = self.pedido_manager.relatorio_pedidos_dia()
        self.listbox_relatorios.delete(0, tk.END)
        for pedido in pedidos_faturados:
            self.listbox_relatorios.insert(tk.END, pedido)


if __name__ == "__main__":
    root = tk.Tk()
    app = RestauranteApp(root)
    root.mainloop()
