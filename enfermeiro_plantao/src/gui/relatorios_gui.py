import tkinter as tk

from services.excel_exporter import gerar_relatorio_pacientes


class RelatoriosGUI:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Gerar Relatórios")

        tk.Button(self.window, text="Gerar Relatório de Pacientes",
                  command=self.gerar_relatorio).pack(pady=10)

    def gerar_relatorio(self):
        gerar_relatorio_pacientes()
        tk.messagebox.showinfo("Sucesso", "Relatório gerado com sucesso!")

    def run(self):
        self.window.mainloop()
