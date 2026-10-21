
import tkinter as tk
from tkinter import messagebox


# Classe para representar o aluno
class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if valor <= 0:
            raise ValueError("A idade deve ser maior que zero!")
        self._idade = valor


# Classe da janela
class Janela:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cadastro de Alunos")
        self.janela.geometry("400x400")

        self.alunos = []

        tk.Label(janela, text="Nome:").pack()
        self.nome = tk.Entry(janela)
        self.nome.pack()

        tk.Label(janela, text="Idade:").pack()
        self.idade = tk.Entry(janela)
        self.idade.pack()

        tk.Label(janela, text="Nota:").pack()
        self.nota = tk.Entry(janela)
        self.nota.pack()

        tk.Button(
            janela, text="Cadastrar",
            command=self.cadastrar
        ).pack(pady=10)

        self.lista = tk.Listbox(janela, width=45)
        self.lista.pack()

    def cadastrar(self):
        try:
            nome = self.nome.get().strip()
            idade = int(self.idade.get())
            nota = float(self.nota.get().replace(",", "."))

            if nome == "":
                raise ValueError("Digite o nome do aluno!")

            if nota < 0 or nota > 10:
                raise ValueError("A nota deve ser de 0 a 10!")

            aluno = Aluno(nome, idade, nota)
            self.alunos.append(aluno)

            self.lista.insert(
                tk.END,
                f"{aluno.nome} - {aluno.idade} anos - Nota: {aluno.nota}"
            )

            messagebox.showinfo(
                "Sucesso", "Aluno cadastrado!"
            )

            self.nome.delete(0, tk.END)
            self.idade.delete(0, tk.END)
            self.nota.delete(0, tk.END)

        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))


# Executar o programa
janela = tk.Tk()
app = Janela(janela)
janela.mainloop()
