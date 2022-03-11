'''Frames são componentes que podem agregar outros widgets'''

from tkinter import *



#----------GUI--------------------#
janela = Tk()
janela.title('sobre frames')

#-----------WIDGETS----------------#
frames_login = Frame(janela)

lab_usuario = Label(frames_login, text='Usuario: ')
lab_password = Label(frames_login, text='Senha: ')
texto_usuario = Entry(frames_login)
texto_password = Entry(frames_login)
bt = Button(frames_login, text='Confirmar')

#------------LAYOUT-----------------#
lab_usuario.grid(row=0, column=0)
lab_password.grid(row=1, column=0)
texto_usuario.grid(row=0, column=1)
texto_password.grid(row=1, column=1)
bt.grid(row=2, column=1)
frames_login.grid()

#-----------------------------------#
janela.mainloop()