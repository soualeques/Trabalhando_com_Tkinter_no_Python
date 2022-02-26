from tkinter import *
#GERENCIADORES DE LAYOUT:
#gerenciador de layout PLACE - os widgets sao dispostos conforme suas cordenadas X e Y
#gerenciador de layout PACK - empacota os widgets na horizontal ou vertical
#gerenciador de layout GRID - os widgets são inseridos num sistema de celulas de uma tabela

janela = Tk()

lb = Label(janela, text="Ola Mundo!")

#configura onde vai aparecer o texto usando as coordenadas X e Y
lb.place(x=100, y=100)

janela.geometry("300x300+200+200")

janela.mainloop()