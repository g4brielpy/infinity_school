import tkinter as tk


def somar():
    global num1_input
    global num2_input

    try: 
        resultado = float(num1_input.get()) + float(num2_input.get())
    except ValueError:
        resultado = 'Valores inválido!'
        
    resultado_label.config(text=resultado)


# Config. root
root = tk.Tk()
root.title('Calculadora')
root.geometry('400x500')


# Widgets
titulo = tk.Label(root, text='Calculadora', font=('Arial', 26))

num1_label = tk.Label(root, text='Numero 1:', font=('Arial', 16))
num1_input = tk.Entry(root, font=('Arial', 16))

operador_mais_label = tk.Label(root, text='+', font=('Arial', 20))

num2_label = tk.Label(root, text='Numero 2:', font=('Arial', 16))
num2_input = tk.Entry(root, font=('Arial', 16))

resultado_label = tk.Label(root, text='', font=('Arial', 16))

somar_button = tk.Button(root, text='Fazer Soma',
                         font=('Arial', 14), command=somar)


# Posicionamentos
titulo.pack(pady=25)

num1_label.pack()
num1_input.pack()

operador_mais_label.pack(pady=5)

num2_label.pack()
num2_input.pack()

somar_button.pack(pady=25)
resultado_label.pack()


# Exibir janela root
root.mainloop()
