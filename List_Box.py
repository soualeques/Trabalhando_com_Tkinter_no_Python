from tkinter import *

janela = Tk()
janela.title('List Box')

#criar listbox onde pode selecionar itens
#para selecionar mais de um dado usa o parametro selectmode=Extended
lista = Listbox(janela, selectmode=EXTENDED)
lista.pack()

#pode inserir dados um de cada vez atravez do indice ou colocando END para ir ao final
lista.insert(END, 'alex')
lista.insert(END, 'fabio')
lista.insert(END, 'soeli')
lista.insert(END, 'val')

#pode inserir dados atravez de listas com o for
nomes = ['joao', 'maria', 'ana']
for nome in nomes:
    lista.insert(END, nome)

#eliminar dados de uma lista atravez do indice, nesse caso a maria
lista.delete(5)

#ver qual dado esta selecionado usando parametro active
def verselecionado():
    print(lista.get(ACTIVE))

bt = Button(janela, text='verificar', command=verselecionado).pack()



janela.mainloop()