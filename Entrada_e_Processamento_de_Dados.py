from tkinter import *

def click():
    print('foi clicado com sucesso!')
    if str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric():
        n1 = int(ed1.get())
        n2 = int(ed2.get())
        lb2["text"] = n1 + n2
    else:
        lb2["text"] = "Os valores digitados não sao aceitos :( "

janela = Tk()
janela.title('--SOMADOR DE NUMEROS--')

lb1 = Label(janela, text="DIGITE VALORES NUMERICOS PARA SOMAR:", font="Arial")
lb1.place(x=15, y=40)

lb3 = Label(janela, text="VALOR 1")
lb3.place(x=100, y=100)

lb4 = Label(janela, text='VALOR 2')
lb4.place(x=100, y=130)

ed1 = Entry(janela)
ed1.place(x=150, y=100)

ed2 = Entry(janela)
ed2.place(x=150, y=130)

bt = Button(janela, width=17, text="SOMAR", command=click)
bt.place(x=150, y=170)

lb2 = Label(janela, text="Nenhum valor digita!", font="Arial")
lb2.place(x=150, y=250)

lb5 = Label(janela, text="A soma deu: ", font="Arial")
lb5.place(x=50, y=250)

janela.geometry("400x400+300+300")
janela.mainloop()