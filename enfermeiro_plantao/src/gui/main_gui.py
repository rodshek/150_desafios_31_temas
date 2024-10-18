import tkinter as tk

from historico_gui import HistoricoGUI
from plantao_gui import PlantaoGUI
from relatorios_gui import RelatoriosGUI
from services.estoque import EstoqueGUI


class MainGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Painel Principal - Enfermeiro")

        tk.Button(self.window, text="Plantão",
                  command=self.open_plantao).pack(pady=10)
        tk.Button(self.window, text="Histórico de Pacientes",
                  command=self.open_historico).pack(pady=10)
        tk.Button(self.window, text="Gerar Relatórios",
                  command=self.open_relatorios).pack(pady=10)
        tk.Button(self.window, text="Controle de Estoque",
                  command=self.open_estoque).pack(pady=10)
        tk.Button(self.window, text="Sair",
                  command=self.window.quit).pack(pady=10)

    def open_plantao(self):
        self.window.destroy()
        PlantaoGUI().run()

    def open_historico(self):
        HistoricoGUI().run()

    def open_relatorios(self):
        RelatoriosGUI().run()

    def open_estoque(self):
        EstoqueGUI().run()

    def run(self):
        self.window.mainloop()
