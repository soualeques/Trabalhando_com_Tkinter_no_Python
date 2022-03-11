from email.mime import image
from tkinter import *


janela = Tk()
janela.title('criando fundo')
janela.geometry('380x253')

#criando fundo
img = PhotoImage(file="img/fundo.png")
lb_imagem = Label(janela, image=img).grid()

janela.mainloop()