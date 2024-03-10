# Import do módulo customtkinter
import customtkinter as ctk


# Função para validar entradas do usuário
def fazer_login() -> None:
    user: str = user_input.get()
    senha: str = senha_input.get()

    user_valido: bool = False
    senha_valida: bool = False

    if '@' in user:
        user_valido: bool = True
    if len(senha) >= 4:
        senha_valida: bool = True

    if user_valido and senha_valida:
        fazer_login_label.configure(text='Login Realizado!')
    else:
        fazer_login_label.configure(text='Login Inválido!')


# Configurações
root = ctk.CTk()
root.title('Login')
root.geometry('400x500+500+200')
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


# CTkFrame
div_user = ctk.CTkFrame(master=root)
div_senha = ctk.CTkFrame(master=root)


# Widgets CTk
titulo_label = ctk.CTkLabel(
    master=root, text='Fazer Login', font=('System', 40))

user_label = ctk.CTkLabel(master=div_user, text='User', font=('Arial', 18))
user_input = ctk.CTkEntry(master=div_user)

senha_label = ctk.CTkLabel(master=div_senha, text='Senha', font=('Arial', 18))
senha_input = ctk.CTkEntry(master=div_senha,show='*')

fazer_login_button = ctk.CTkButton(
    master=root, text='Fazer Login', font=('Arial', 20),
    command=fazer_login,
    width=170, height=50, anchor="center",
)

fazer_login_label = ctk.CTkLabel(
    master=root,
    text='',
    font=('Arial', 20)
)


# Posicionamentos
titulo_label.pack(pady=(50, 30))

div_user.pack(pady=(0, 20))
user_label.pack()
user_input.pack()

div_senha.pack()
senha_label.pack()
senha_input.pack()

fazer_login_button.pack(pady=(50, 30))
fazer_login_label.pack()


# Loop da Root
root.mainloop()
