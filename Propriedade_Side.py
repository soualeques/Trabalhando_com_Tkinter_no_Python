from tkinter import *

janela = Tk()
janela.title('Propriedade Side')

lb1 = Label(janela, text="TOP", bg="white")
lb2 = Label(janela, text="RIGHT", bg="white")
lb3 = Label(janela, text="LEFT", bg="white")
lb4 = Label(janela, text="BOTTON", bg="white")

janela["bg"] = "black"

lb1.pack(side=TOP)
lb2.pack(side=RIGHT)
lb3.pack(side=LEFT)
lb4.pack(side=BOTTOM)






janela.geometry("300x300+300+300")
janela.mainloop()