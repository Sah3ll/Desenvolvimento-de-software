import tkinter as tk

janela = tk.Tk()
janela.title("Meu primeiro aplicativo!")
janela.geometry("400x300")

titulo = tk.Label(
    janela,
    text="Cadastro de Alunos",
    font=("Arial", 16)
)

titulo.pack()
campo_nome = tk.Entry(janela)
campo_nome.pack()
nome = campo_nome.get()
print(nome)
campo_nome.delete(0, tk.END)

def cadastrar():
    nome = campo_nome.get()
    print("Botão clicado!")

botao = tk.Button(
    janela,
    text="Cadastrar"
)

botao.pack()


# O mainloop deve ser SEMPRE a última linha da interface gráfica
janela.mainloop()
