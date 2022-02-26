from tkinter import *

janela = Tk()
janela.title('propriedade expand')

l1 = Label(janela, text="1", bg="Blue")
l2 = Label(janela, text="2", bg="red")
l3 = Label(janela, text="3", bg="Green")

l1.pack(side=TOP, fill=BOTH, expand=1)
l2.pack(side=TOP, fill=BOTH, expand=1)
l3.pack(side=TOP, fill=BOTH, expand=1)






janela.geometry("300x300+300+300")
janela.mainloop()