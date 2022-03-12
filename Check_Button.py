from tkinter import *

def click():
    #se o botao for selecionado o valor booleano muda para 1(true)
    #senao muda para 0(false)
    print(valorcheck.get())


janela = Tk()
janela.title('Check button')

#cria um botao para selecionar ou nao
valorcheck = IntVar()
bt = Checkbutton(janela,
                 text='Aceita os termos?',
                 variable= valorcheck,
                 command=click)
bt.pack()




janela.mainloop()