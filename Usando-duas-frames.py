from tkinter import *

#------------GUI----------------#
janela = Tk()
janela.title('Cadastro')
janela.geometry('300x200')

#------------WIDGETS-------------#
frames_nomes = Frame(janela)
frames_morada = Frame(janela)

lb_nome = Label(frames_nomes, text='NOME: ')
lb_apelido = Label(frames_nomes, text='APELIDO: ')
lb_cidade = Label(frames_morada, text='CIDADE: ')
lb_estado = Label(frames_morada, text='ESTADO: ')
tx_nome = Entry(frames_nomes)
tx_apelido = Entry(frames_nomes)
tx_cidade = Entry(frames_morada)
tx_estado = Entry(frames_morada)
bt = Button(janela, text='SALVAR')

#------------LAYOUT----------------#
lb_nome.grid(row=0, column=0)
lb_apelido.grid(row=1, column=0)
tx_nome.grid(row=0, column=1)
tx_apelido.grid(row=1, column=1)

lb_cidade.grid(row=0, column=0)
lb_estado.grid(row=1, column=0)
tx_cidade.grid(row=0, column=1)
tx_estado.grid(row=1, column=1)

frames_nomes.grid()
frames_morada.grid()

bt.grid()

janela.mainloop()