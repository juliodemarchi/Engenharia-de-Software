import tkinter as tk

def saudacao():
    print("Olá! Você clicou no botão.")

# 1. Criar a janela principal
janela = tk.Tk()
janela.title("Meu App em Python")
janela.geometry("300x200")

# 2. Adicionar um rótulo (texto)
texto = tk.Label(janela, text="Bem-vindo ao Tkinter!", fg="black")
texto.pack(pady=10) # pady adiciona um espaçamento vertical

# 3. Adicionar um botão
botao = tk.Button(janela, text="Clique aqui", command=saudacao)
botao.pack()

# 4. Rodar o programa
janela.mainloop()