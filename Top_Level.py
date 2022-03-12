from tkinter import *
#função para criar nova janela atraves do botão
def abrir_novo():
    #como se fosse criar uma interface normal, porem utilizando a funçao TopLevel()
    #pode criar qualquer widget normalmente
    top = Toplevel()
    top.title('Nova janela criada')
    top.geometry('300x200')
    lb = Label(top, text='Essa janela foi criada atravez do botao da primeira')
    lb.pack()

janela = Tk()
janela.title('Top level')

#botão para criar nova janela
bt = Button(janela, text="abrir nova janela", command=abrir_novo)
bt.pack()

janela.geometry('300x200')
janela.mainloop()