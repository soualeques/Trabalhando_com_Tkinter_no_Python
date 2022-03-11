from tkinter import *

def ola():
    print(ed.get())
    #usa o metodo get() para poder acessar conteudo do entry
    lb2['text'] = (f'ola mundo\nSeja bem vindo {ed.get()}')



janela = Tk()
janela.title('<<Boas vindas>>')
#muda o icone da janela
janela.iconbitmap('img/coding_computer_pc_screen_code_icon_193925.ico')

#mudando a cor da letra, fonte, tamanho, etc.
lb1 = Label(janela, text='digite seu nome: ', fg='green', font="Arial 15 bold")
lb1.grid(row=0, column=0)

#entrada de dados
ed = Entry(janela, textvariable="", justify='center')
ed.grid(row=0, column=1)


bt= Button(janela, text='Confirmar', bg='green',fg='White', font='Arial 12 bold', width=13, height=1,activebackground='pink', command=ola)
bt.grid(row=1, column=1)

#adicionar borda ao redor da label sendo: SOLID, GROOVE, FLAT, RAISED, SUNKEN e RIDGE.
lb2 = Label(janela,
            text=':)',
            bd=1,
            relief="solid",
            font='Arial 14 bold italic',
            width=35)
lb2.grid(columnspan=4)



#define o tamanho da tela e onde ela vai aparecer na tela
janela.geometry('400x300+400+200')
#define se a janela pode ou nao ser redimensionada manualmente
janela.resizable(0,0)
janela.mainloop()