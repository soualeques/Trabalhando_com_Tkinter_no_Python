from functools import partial
from tkinter import *

def bt_click(botao, cor=""):
    print(botao["text"])
    cor["bg"] = "green"
    
    
def bt_click2(botao):
    botao["text"] = "mudou o fundo"
    janela["bg"] = "pink"


janela = Tk()

botao1 = Button(janela, width=20, text="Clique no botão 1")
#usa esse geito (usando o "partial") para usar diferentes parametros.
botao1["command"] = partial(bt_click, botao1, botao1)
botao1.place(x=100, y=100)

botao2 = Button(janela, width=20, text="Clique no botão 2")
botao2["command"] = partial(bt_click2, botao2)
botao2.place(x=100, y=130)


janela.geometry("300x300+200+200")
janela.mainloop()