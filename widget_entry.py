from tkinter import *

def clique():
    print(ed.get())
    lb["text"] = ed.get()
    

janela = Tk()
janela.title('Interação com usuario')

#Criando campo para entrada de dados
ed = Entry(janela)
ed.place(x=100, y=100)

bt = Button(janela, width=20, text="OK", command=clique)
bt.place(x=100, y=145)

lb = Label(janela, text="Não foi digitado nada :(")
lb.place(x=100, y=200)


janela.geometry("300x300+300+300")
janela.mainloop()