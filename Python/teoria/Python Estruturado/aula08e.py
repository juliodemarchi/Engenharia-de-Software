# tkinter
from tkinter import*

def funcClicar():
    print("Botão pressionado")

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
janelaPrincipal.geometry("300x200")
texto.pack()

botao = Button(master = janelaPrincipal, text = 'Clicar', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()
