import tkinter as tk
from tkinter import ttk

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo de Treeview")

# Criação do Treeview
tree = ttk.Treeview(root, columns=('Nome', 'Idade', 'Cidade'), show='headings')

# Configuração dos cabeçalhos das colunas
tree.heading('Nome', text='Nome')
tree.heading('Idade', text='Idade')
tree.heading('Cidade', text='Cidade')

# Inserção manual de dados
dados_estaticos = [
    ('João', 25, 'São Paulo'),
    ('Maria', 30, 'Rio de Janeiro'),
    ('Carlos', 28, 'Brasília'),
    ('Ana', 22, 'Salvador')
]

for dados in dados_estaticos:
    tree.insert('', 'end', values=dados)
    # tree.insert('', 'end', values=('João', 25, 'São Paulo'))

# Posiciona o Treeview na janela
tree.pack(pady=10)

root.mainloop()
