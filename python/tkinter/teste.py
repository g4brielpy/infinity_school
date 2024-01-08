import tkinter as tk


def funcao_abrir():
    print("Abrir")


def funcao_salvar():
    print("Salvar")


root = tk.Tk()
root.title("Exemplo de Menu")

menuP = tk.Menu(root)

# Adicionando opções diretamente ao menu
menuP.add_command(label="Novo", command=lambda: print("Novo"))
menuP.add_command(label="Fechar", command=root.destroy)

# Criando um submenu
submenu_arquivo = tk.Menu(menuP, tearoff=0)
submenu_arquivo.add_command(label="Abrir", command=funcao_abrir)
submenu_arquivo.add_command(label="Salvar", command=funcao_salvar)

# Adicionando o submenu ao menu principal
menuP.add_cascade(label="Arquivo", menu=submenu_arquivo)

# associar o menu criado (menu) à janela principal
root.config(menu=menuP)


root.mainloop()
