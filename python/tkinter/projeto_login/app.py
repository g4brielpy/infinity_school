'''
Projeto de criação de tela de login utilizando Tkinter GUI em python
'''

from tkinter import *
from tkinter.ttk import *
from login import fazer_login

# Configurações da janela principal
root = Tk()
root.title('Fazer Login')
root.config(padx=10, pady=20)
root.geometry('400x500+250+200')

# temas e estilos
style = Style()
root.style = Style(root)
root.style.theme_use('clam')
# TEMAS: 'clam', 'alt', 'default', 'classic', etc.

# Containers
frame_email = Frame(root, relief='groove', borderwidth=2)
frame_senha = Frame(root, relief='groove', borderwidth=2)

# Configuração dos widgets
titulo_label = Label(root, text='Login', font=('Arial', 20))

email_entrada = StringVar()
email_label = Label(frame_email, text='E-mail:', font=('Arial', 15))
email_input = Entry(
    frame_email, textvariable=email_entrada, font=('Arial', 12))

senha_entrada = StringVar()
senha_label = Label(frame_senha, text='Senha:', font=('Arial', 15))
senha_input = Entry(frame_senha, textvariable=senha_entrada,
                    show='*', font=('Arial', 12))

style.configure('TButton', font=('Arial', 12))
botao_login = Button(root, text='Fazer Login', style='TButton',
                     command=lambda: fazer_login(email_entrada, senha_entrada))

# Exibição dos elementos
titulo_label.pack(pady=(0, 50))

frame_email.pack(pady=(0, 20))
email_label.grid(row=0, column=0, pady=5, padx=(10))
email_input.grid(row=0, column=1, pady=5, padx=(0, 15))

frame_senha.pack(pady=(0, 20))
senha_label.grid(row=0, column=0, pady=5, padx=(10))
senha_input.grid(row=0, column=1, pady=5, padx=(0, 15))

botao_login.pack()

# Loop principal da aplicação
root.mainloop()
