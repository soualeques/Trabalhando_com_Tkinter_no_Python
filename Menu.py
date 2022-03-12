from tkinter import *

#funçao para opçao new do menu
def click():
    print('novo arquivo criado')



janela = Tk()
janela.title('menu')

#cria o menu
meu_menu = Menu(janela)


#cria um parent do meu menu
file_menu = Menu(meu_menu, tearoff=0)
edit_menu = Menu(meu_menu, tearoff=0)

#cria as opçoes dentro da seção file
file_menu.add_command(label="new", command=click)
file_menu.add_command(label="open")
file_menu.add_command(label="save")
#adicionar linha separadora
file_menu.add_separator()
file_menu.add_command(label="quit")


#cria as opçoes dentro da seção edit
edit_menu.add_command(label="copy")
edit_menu.add_command(label="paste")
edit_menu.add_command(label="cut")

#adiciona uma seçao ao menu
meu_menu.add_cascade(label='file', menu=file_menu)
meu_menu.add_cascade(label='edit', menu=edit_menu)

#fazer um tipo de pack() para o menu
janela.config(menu=meu_menu)



janela.geometry('300x200')
janela.mainloop()