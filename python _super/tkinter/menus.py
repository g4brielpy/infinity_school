import tkinter as tk


def funcao_abrir():
    print("Abrir")


def funcao_salvar():
    print("Salvar")


root = tk.Tk()
root.title("Exemplo de Menu")
root.geometry("400x300")

menuP = tk.Menu(root)

# Adicionando opções diretamente ao menu
menuP.add_command(label="Novo", command=lambda: print("Novo"))
menuP.add_command(label="Fechar", command=root.destroy)
menuP.add_command(label='Teste', command=lambda: print('Teste'))

# Criando um submenu     definir onde vai ser exibido o submenu 'menuP'
submenu_arquivo = tk.Menu(menuP, tearoff=0)
submenu_arquivo.add_command(label="Abrir", command=funcao_abrir)
submenu_arquivo.add_command(label="Salvar", command=funcao_salvar)

# Adicionando o submenu ao menu principal         definir qual menu deve ser exibido
menuP.add_cascade(label="Acessar submenu", menu=submenu_arquivo)

# associar o menu criado (menu) à janela principal
root.config(menu=menuP)

root.mainloop()