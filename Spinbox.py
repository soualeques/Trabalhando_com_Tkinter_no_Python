from tkinter import *

janela = Tk()
janela.title('SPINBOX')

#cria uma caixa onde pode ser alterado valores atravz de uma seta

#neste caso ira de 0 ate 10
#por padrao ele trava na ultima opçao, pode mudar isso com parametro wrap=True
s1 = Spinbox(janela, from_=0, to=10, wrap=True)
s1.pack()

#neste caso ira de acordo com os valores passados
s2 = Spinbox(janela, values=(10,20,30,40,50,60,70,80,90,100))
s2.pack()

#neste caso os valores serao strings
s3 = Spinbox(janela, values=('alex', 'fabio', 'soeli', 'ana'))
s3.pack()

janela.geometry('300x200')
janela.mainloop()