from tkinter import *

#---------PROGRAMA-------#
def conversor():
    f = ((9 * float(temp.get()))/5) + 32
    lb2['text'] = f'A temperatura ficou: {f}ºF'


#---------GUI------------#
janela = Tk()
janela.title('CONVERSOR TEMPERATURA')
janela.geometry('400x300+300+100')
#-------------------------#
#---------WIDGETS----------#
frame_conversor = Frame(janela)
lb = Label(frame_conversor,
           text='Digite a temperatura em celcius\npara converter em fahrenheit:',
           justify=CENTER,
           font='arial 12 bold',
           bd=1,
           relief="solid",
           width=40)
temp = Entry(frame_conversor)
conversor = Button(frame_conversor,
                   text='Converter',
                   bg = '#76b5c5',
                   font='Times 12 bold',
                   command=conversor)
lb2 = Label(frame_conversor,
            text='nenhuma temperatura digitada.',
            height=7,
            width=40,
            font='Arial 12 italic',
            border=2,
            relief='groove')
#--------------------------------------#
#---------------LAYOUT-----------------#
lb.grid(row=0, column=0)
temp.grid(row=1, column=0)
conversor.grid(row=2,column=0)
lb2.grid(row=3,column=0)
frame_conversor.grid()









janela.mainloop()