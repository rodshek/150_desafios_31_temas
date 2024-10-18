import tkinter as tk
from tkinter import messagebox

from main_gui import MainGUI


class LoginGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login Enfermeiro")

        tk.Label(self.window, text="Usuário").pack(pady=5)
        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack(pady=5)

        tk.Label(self.window, text="Senha").pack(pady=5)
        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.window, text="Entrar",
                  command=self.validate_login).pack(pady=10)

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "enfermeiro" and password == "1234":
            self.window.destroy()
            MainGUI().run()
        else:
            messagebox.showerror("Erro", "Credenciais inválidas!")

    def run(self):
        self.window.mainloop()
