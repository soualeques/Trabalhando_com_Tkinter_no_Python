from tkinter import *

#Função que ocorrera ao apertao o botão
def click_botao():
    print('clicou')
    #Ao clicar no botão ira trocar o texto para esse
    lb["text"] = "funcionou! voce clicou."
    #Ao clicar no botão tambem ira trocar a cor de fundo.
    janela["bg"] = "#40E0D0"

janela = Tk()
janela.title("Criando um botão")

#Cria um botao na janela
bt = Button(janela, width=20, text="Clique aqui", command=click_botao)
bt.place(x=100, y=100)

lb = Label(janela, text="Não clicou!")
lb.place(x=115, y=150)

janela.geometry("300x300+200+200")
janela.mainloop()