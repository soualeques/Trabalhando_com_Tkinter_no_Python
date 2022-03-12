from tkinter import *

janela = Tk()

#cria uma barra de slide
slide = Scale(janela, from_=0, to=100, orient=HORIZONTAL)
slide.pack()

janela.geometry('300x200')
janela.mainloop()