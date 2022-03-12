from tkinter import *

janela = Tk()

#cria varias opçoes para ser selecionado
r1 = Radiobutton(janela, text='opçao 1', value=1)
r2 = Radiobutton(janela, text='opçao 2', value=2)
r3 = Radiobutton(janela, text='opçao 3', value=3)

r1.pack()
r2.pack()
r3.pack()

r1.select()


janela.geometry('300x200')
janela.mainloop()