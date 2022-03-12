from tkinter import *

janela = Tk()

#outra forma de mostra texto na interface, para formatar necessita usar width
msg = Message(janela, text='este é um texto do widget message', width=200)
msg.pack()

janela.mainloop()