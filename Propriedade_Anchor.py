from tkinter import *

janela = Tk()
janela.title('Propriedade Anchor')

lb1 = Label(janela, text="side1", bg="white")
lb2 = Label(janela, text="side2", bg="red")
lb3 = Label(janela, text="anchor1", bg="white")
lb4 = Label(janela, text="anchor2", bg="red")

janela["bg"] = "black"

lb1.pack(side=RIGHT)
lb2.pack(side=RIGHT)
#exemplo da  propriedade anchor
lb3.pack(anchor=NW)
lb4.pack(anchor=SW)






janela.geometry("300x300+300+300")
janela.mainloop()