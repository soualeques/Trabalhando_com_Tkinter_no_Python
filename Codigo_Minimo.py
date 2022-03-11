import tkinter as tk


#Cria uma janela para o programa.
janela = tk.Tk()

#Cria um titulo (aquele que fica no topo) para a janela. 
janela.title("Programa do Alex")

#Podemos mudar a cor do fundo da janela com essas duas opções de comandos.
janela["bg"] = "pink"
janela["background"] = "pink"
lb = tk.Label(janela, text="Olá! sou o Alex e estou aprendendo a usar a biblioteca tkinter.").pack()

#Modifica o tamanho da janela e onde ela ira aparecer.
#LARGURA X ALTURA + ONDE APARECE A ESQUERDA DA TELA + ONDE APARECE NO TOPO DA TELA
#EX: 300 X 300 + 100 + 100
janela.geometry("800x600+200+50")

#deixa a janela aberta com loop ate fechar.
janela.mainloop()