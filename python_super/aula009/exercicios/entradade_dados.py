import tkinter as tk

# Config. root
root = tk.Tk()
root.title('Login')
root.geometry('400x500')


# Contêiner
user_div = tk.Frame(root, relief=tk. RAISED, borderwidth=2)
senha_div = tk.Frame(root, relief=tk. RAISED, borderwidth=2)


# Widgets
titulo = tk.Label(root, text='Fazer Login', font=('Arial', 32))

user_label = tk.Label(user_div, text='Nome:', font=('Arial', 16))
user_input = tk.Entry(user_div, font=('Arial', 16))

senha_label = tk.Label(senha_div, text='Senha:', font=('Arial', 16))
senha_input = tk.Entry(senha_div, font=('Arial', 16))

login_button = tk.Button(root, text='Entrar', font=(
    'Arial', 14), width=15, command=lambda: print('Fui clicado!'))


# Posicionamentos
titulo.pack(pady=(25, 45))

user_div.pack(pady=(0, 10))
user_label.grid(row=0, column=0, padx=5)
user_input.grid(row=0, column=1, padx=(0, 5))

senha_div.pack()
senha_label.grid(row=0, column=0, padx=5)
senha_input.grid(row=0, column=1, padx=(0, 5))

login_button.pack(pady=(25, 0))

root.mainloop()
