'''
O objetivo deste projeto é criar um sistema básico de supermercado utilizando a linguagem de programação Python e a biblioteca Tkinter para a construção da interface gráfica. Este sistema possui funcionalidades simples, que proporcionam um ambiente de aprendizado para iniciantes em programação.

Funcionalidades Principais:
    . Adicionar Produtos
    . Remover Produtos
    . Lista de Produtos
    . Atualizar Produtos

Interface Gráfica:
    . Uma interface gráfica será construída utilizando o Tkinter para proporcionar uma experiência amigável ao usuário
'''

import tkinter as tk

# config gerais do modal
root = tk.Tk()
root.title('Mercado')
root.config(padx=20, pady=20)
# root.geometry('150x300+200+200')

'''
MERCADO

MENU DE PRODUTOS
-- -- -- -- -- --
[1] - Adicionar produtos
[2] - Remover produto
[3] - Lista de produtos
[4] - Atualizar produtos
'''

# adicionar textos
titulo = tk.Label(root, text='MERCADO', font=('Arial', 25))
subtitulo = tk.Label(root, text='MENU DE PRODUTOS', font=('Arial', 18))

texto_adicionar = tk.Label(root, text='[1] - Adicionar produtos')
texto_remover = tk.Label(root, text='[2] - Remover produto')
texto_lista = tk.Label(root, text='[3] - Lista de produtos')
texto_atualizar = tk.Label(root, text='[4] - Atualizar produtos')

# opções disponíveis
botao_adicionar = tk.Button(
    root, text='Add produtos', command=lambda: print('Adicionar'))
botao_remover = tk.Button(
    root, text='Del produto', command=lambda: print('Remover'))
botao_exibir_lista = tk.Button(
    root, text='Ver produtos', command=lambda: print('Exibir produtos'))
botao_atualizar = tk.Button(
    root, text='Att produto', command=lambda: print('Atualizar'))

# exibir textos
titulo.grid(row=0, column=0, columnspan=4, pady=(0, 10), sticky="nsew")
subtitulo.grid(row=1, column=0, columnspan=4, pady=(0, 15), sticky="nsew")

botao_adicionar.grid(row=2, column=0, padx=5)
botao_remover.grid(row=2, column=1, padx=5)
botao_atualizar.grid(row=2, column=2, padx=5)
botao_exibir_lista.grid(row=2, column=3, padx=5)


root.mainloop()
