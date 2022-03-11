from tkinter import *

#cria um widget atravez da classe que pode usar qualquer hora so mudar os parametros
class FrameNome(Frame):
    def __init__(self, janela, msg):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['border'] = 2
        self['relief'] = SOLID
        
        label_nome = Label(self, text=msg)
        text_nome = Entry(self)
        label_nome.grid(row=0, column=0)
        text_nome.grid(row=0, column=1)
        
janela = Tk()
janela.title('nome')

frame1 = FrameNome(janela, 'nome')
frame1.grid()
frame2 = FrameNome(janela, 'idade')
frame2.grid()

janela.mainloop()