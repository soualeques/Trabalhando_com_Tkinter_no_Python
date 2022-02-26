from tkinter import *

#Usando o gerenciador de interface PACK
janela = Tk()
janela.title("GERENCIADO DE LAYOUT PACK")

l1 = Label(janela, text="1", bg="red")
l2 = Label(janela, text="2", bg="green")
l3 = Label(janela, text="3", bg="pink")
l4 = Label(janela, text="4", bg="orange")

#Mostra na janela conforme a posiçao da variavel no codigo
l1.pack()
l2.pack()
l3.pack()
l4.pack(side=BOTTOM)


janela.geometry("300x300+300+300")
janela.mainloop()