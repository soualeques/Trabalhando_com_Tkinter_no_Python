from tkinter import *


janela = Tk()
janela.title('Row e Collun')

l1 = Label(janela, text="linha 1", bg="red")
l2 = Label(janela, text="linha 2", bg="green")

#usando o GRID
l1.grid(row=1, column=1)
l2.grid(row=2, column=2)


janela.geometry("300x400+300+300")
janela.mainloop()