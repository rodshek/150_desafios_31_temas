import tkinter as tk

from services.database import buscar_historico_paciente


class HistoricoGUI:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Histórico de Pacientes")

        tk.Label(self.window, text="ID do Paciente").pack(pady=5)
        self.id_entry = tk.Entry(self.window)
        self.id_entry.pack(pady=5)

        self.result_text = tk.Text(self.window, height=10, width=50)
        self.result_text.pack(pady=5)

        tk.Button(self.window, text="Buscar Histórico",
                  command=self.buscar_historico).pack(pady=10)

    def buscar_historico(self):
        paciente_id = self.id_entry.get()
        historico = buscar_historico_paciente(paciente_id)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, historico)

    def run(self):
        self.window.mainloop()
