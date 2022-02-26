from tkinter import *

from pint import test


janela = Tk()
janela.title('--TELA DE LOGIN--')
janela["bg"] = "#BA55D3"

l1 = Label(janela, text="LOGIN: ", bg="#BA55D3")
l2 = Label(janela, text="SENHA: ", bg="#BA55D3")

ed1 = Entry(janela, bg="#00FFFF")
ed2 = Entry(janela, bg="#00FFFF")

bt = Button(janela, text="CONFIRMAR", bg="green")

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)
bt.grid(row=2, column=1)




janela.geometry('200x200+100+100')
janela.mainloop()