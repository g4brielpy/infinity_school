'''
Usando seus conhecimentos aprendidos em sala, realize uma interface de login utilizando a biblioteca Tkinter em Python. 
O objetivo é permitir que o usuário faça login somente se a senha tiver mais de 6 dígitos e se o e-mail contiver o caractere "@", ou seja, 
realizar uma tela de login com restrições de e-mail e senha.
'''

from login import fazer_login

import tkinter as tk
from tkinter.ttk import (
    Style, Label, Entry, Button, Frame
)

# Configurações da janela principal
root = tk.Tk()
root.title('Fazer Login')
root.config(padx=10, pady=20)
root.geometry('400x500+250+200')

# temas e estilos
style = Style()
style.theme_use('clam')
# TEMAS: 'clam', 'alt', 'default', 'classic', etc.

# Containers
frame_email = Frame(root, relief='groove', borderwidth=2)
frame_senha = Frame(root, relief='groove', borderwidth=2)

# Configuração dos widgets
titulo_label = Label(root, text='Login', font=('Arial', 20))

email_entrada = tk.StringVar()
email_label = Label(frame_email, text='E-mail:', font=('Arial', 15))
email_input = Entry(
    frame_email, textvariable=email_entrada, font=('Arial', 12))

senha_entrada = tk.StringVar()
senha_label = Label(frame_senha, text='Senha:', font=('Arial', 15))
senha_input = Entry(frame_senha, textvariable=senha_entrada,
                    show='*', font=('Arial', 12))

style.configure('TButton', font=('Arial', 12))
botao_login = Button(root, text='Fazer Login', style='TButton',
                     command=lambda: fazer_login(email_entrada, senha_entrada, login))

# condição de login
login = Label(root, text='', font=('Arial', 15))

# Exibição dos elementos
titulo_label.pack(pady=(0, 50))

frame_email.pack(pady=(0, 20))
email_label.grid(row=0, column=0, pady=5, padx=(10))
email_input.grid(row=0, column=1, pady=5, padx=(0, 15))

frame_senha.pack(pady=(0, 20))
senha_label.grid(row=0, column=0, pady=5, padx=(10))
senha_input.grid(row=0, column=1, pady=5, padx=(0, 15))

botao_login.pack()

login.pack(pady=(50, 0))

# Loop principal da aplicação
root.mainloop()
