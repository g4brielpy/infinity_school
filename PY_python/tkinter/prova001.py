'''
Crie uma janela usando a biblioteca TKINTER em Python que tenha um título "Sistema de Cadastro". 
Nesta janela, crie um campo de entrada de texto para o usuário digitar seu nome e um botão "Enviar" que, ao ser clicado, exiba uma mensagem de boas-vindas com o nome do usuário em uma nova janela.
'''

import tkinter as tk
from tkinter import messagebox


def mensagem_boas_vindas():
    nome_user = nome.get()
    mensagem = f'Bem-vindo, {nome_user}!'
    messagebox.showwarning("Boas-vindas", mensagem)


root = tk.Tk()
root.title('Cadastro')
root.config(padx=10, pady=20)
root.geometry('400x500+250+200')

div_nome = tk.Frame(root, relief='groove', borderwidth=2)

titulo_label = tk.Label(root, text='Sistema de Cadastro', font=('Arial', 24))

nome = tk.StringVar()
nome_label = tk.Label(div_nome, text='Nome:', font=('Arial', 14))
nome_input = tk.Entry(div_nome, textvariable=nome, font=('Arial', 12))

botao_login = tk.Button(root, text='Enviar',
                        command=mensagem_boas_vindas, font=('Arial', 14))

# exibir wb
titulo_label.pack(pady=(0, 50))

div_nome.pack(pady=20)
nome_label.grid(row=0, column=1, pady=5, padx=(10))
nome_input.grid(row=0, column=2, pady=5, padx=(0, 15))

botao_login.pack()

root.mainloop()
