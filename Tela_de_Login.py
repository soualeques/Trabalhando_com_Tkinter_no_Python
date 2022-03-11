from tkinter import *


janela = Tk()
janela.title('--TELA DE LOGIN--')
janela["bg"] = "black"

l1 = Label(janela, text="LOGIN: ", bg='black', fg='white')
l2 = Label(janela, text="SENHA: ",bg='black', fg='white')

ed1 = Entry(janela, bg="#00FFFF")
ed2 = Entry(janela, bg="#00FFFF")

bt = Button(janela, text="CONFIRMAR", bg="green", fg='white')


l1.grid(row=1, column=0)
l2.grid(row=2, column=0)
ed1.grid(row=1, column=1)
ed2.grid(row=2, column=1)
bt.grid(row=3, column=1)

#focus para focar no widget que vai usar primeiro
ed1.focus()

janela.resizable(0,0)
janela.geometry('380x253+100+100')
janela.mainloop()