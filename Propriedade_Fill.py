from tkinter import *

janela = Tk()
janela.title('Propriedade fill')

lb1 = Label(janela, text="TOP", bg="green")
lb2 = Label(janela, text="RIGHT", bg="red")
lb3 = Label(janela, text="LEFT", bg="red")
lb4 = Label(janela, text="BOTTON", bg="green")

janela["bg"] = "black"

lb1.pack(side=TOP, fill=X)
lb2.pack(side=RIGHT, fill=Y)
lb3.pack(side=LEFT, fill=Y)
lb4.pack(side=BOTTOM, fill=X)






janela.geometry("300x300+300+300")
janela.mainloop()