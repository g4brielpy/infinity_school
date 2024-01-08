import tkinter as tk


def funcao_abrir():
    print("Abrir")


def funcao_salvar():
    print("Salvar")


root = tk.Tk()
root.title("Exemplo de Menu")

menu = tk.Menu(root)

# Adicionando opções diretamente ao menu
menu.add_command(label="Novo", command=lambda: print("Novo"))
menu.add_command(label="Fechar", command=root.destroy)

# Criando um submenu
submenu_arquivo = tk.Menu(menu, tearoff=0)
submenu_arquivo.add_command(label="Abrir", command=funcao_abrir)
submenu_arquivo.add_command(label="Salvar", command=funcao_salvar)

# Adicionando o submenu ao menu principal
menu.add_cascade(label="Arquivo", menu=submenu_arquivo)

# associar o menu criado (menu) à janela principal
root.config(menu=menu)


root.mainloop()
