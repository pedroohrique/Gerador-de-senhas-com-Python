import tkinter as tk
import random
import string
from tkinter import messagebox

class GeradorDeSenhas:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerador de Senhas")
        self.master.configure(bg="white")

        largura_janela = 300
        altura_janela = 400

        largura_tela = self.master.winfo_screenwidth()
        altura_tela = self.master.winfo_screenheight()

        posicao_x = (largura_tela // 2) - (largura_janela // 2)
        posicao_y = (altura_tela // 2) - (altura_janela // 2)

        self.master.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

        self.criar_widgets()

    def criar_widgets(self):
        frame_opcoes = tk.LabelFrame(self.master, text="Opções de Caracteres", padx=10, pady=10, bg="white")
        frame_opcoes.pack(pady=20, padx=20, fill="both", expand="yes")

        self.var_maiusculas = tk.BooleanVar()
        self.var_minusculas = tk.BooleanVar()
        self.var_numeros = tk.BooleanVar()
        self.var_especiais = tk.BooleanVar()

        tk.Checkbutton(frame_opcoes, text="Incluir Letras Maiúsculas", variable=self.var_maiusculas, bg="white").grid(row=0, column=0, sticky="w")
        tk.Checkbutton(frame_opcoes, text="Incluir Letras Minúsculas", variable=self.var_minusculas, bg="white").grid(row=1, column=0, sticky="w")
        tk.Checkbutton(frame_opcoes, text="Incluir Números", variable=self.var_numeros, bg="white").grid(row=2, column=0, sticky="w")
        tk.Checkbutton(frame_opcoes, text="Incluir Caracteres Especiais", variable=self.var_especiais, bg="white").grid(row=3, column=0, sticky="w")

        frame_comprimento = tk.Frame(self.master, bg="white")
        frame_comprimento.pack(pady=10)

        tk.Label(frame_comprimento, text="Quantidade de Dígitos:", bg="white").pack(side="left", padx=5)
        self.entrada_comprimento = tk.Entry(frame_comprimento, width=5)
        self.entrada_comprimento.pack(side="left", padx=5)

        tk.Button(self.master, text="Gerar Senha", command=self.gerar_senha).pack(pady=20)

        frame_senha = tk.Frame(self.master, bg="white")
        frame_senha.pack(pady=10)

        tk.Label(frame_senha, text="Senha Gerada:", bg="white").pack(side="left", padx=5)
        self.entrada_senha = tk.Entry(frame_senha, width=50, font=('Helvetica', 14))
        self.entrada_senha.pack(side="left", padx=5)

    def gerar_senha(self):
        try:
            comprimento = int(self.entrada_comprimento.get())
        except ValueError:
            messagebox.showwarning("Entrada Inválida!", "Por favor, insira um número válido para a quantidade de dígitos!")
            return

        incluir_maiusculas = self.var_maiusculas.get()
        incluir_minusculas = self.var_minusculas.get()
        incluir_numeros = self.var_numeros.get()
        incluir_especiais = self.var_especiais.get()

        if not (incluir_maiusculas or incluir_minusculas or incluir_numeros or incluir_especiais):
            messagebox.showwarning("Opção Inválida!", "Selecione ao menos uma opção!")
            return

        caracteres = ""
        senha = []

        if incluir_maiusculas:
            caracteres += string.ascii_uppercase
            senha.append(random.choice(string.ascii_uppercase))
        if incluir_minusculas:
            caracteres += string.ascii_lowercase
            senha.append(random.choice(string.ascii_lowercase))
        if incluir_numeros:
            caracteres += string.digits
            senha.append(random.choice(string.digits))
        if incluir_especiais:
            caracteres += string.punctuation
            senha.append(random.choice(string.punctuation))

        if len(caracteres) == 0:
            messagebox.showwarning("Opção Inválida!", "Selecione ao menos uma opção!")
            return

        while len(senha) < comprimento:
            senha.append(random.choice(caracteres))

        random.shuffle(senha)
        senha = "".join(senha[:comprimento])
        self.entrada_senha.delete(0, tk.END)
        self.entrada_senha.insert(0, senha)

if __name__ == "__main__":
    root = tk.Tk()
    app = GeradorDeSenhas(root)
    root.mainloop()