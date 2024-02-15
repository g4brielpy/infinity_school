import tkinter as tk
from tkinter import Label, ttk

# Função para calcular o resultado da operação
def calcular():
    try:
        num1 = float(numero_1.get())
        num2 = float(numero_2.get())
        operacao = operacoes.get()

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        else:
            resultado = "Operação inválida"

        # Exibindo o resultado
        resultado_label.config(text=f"Resultado: {resultado}")
    except:
        resultado_label.config(text="Erro: Insira números válidos")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora Simples")
root.config(padx=10, pady=20)
root.geometry('400x500+250+200')

titulo = Label(root, text='CALCULADORA SIMPLES', font=('Arial', 20))

quadro_operacoes = tk.Frame(root, relief='ridge', borderwidth=2)

# Criando e posicionando os elementos na root
titulo.pack()

quadro_operacoes.pack(pady=(50, 30))

numero_1 = ttk.Entry(quadro_operacoes, width=15)
numero_1.grid(row=0, column=0, padx=10, pady=10)

operacoes = ttk.Combobox(quadro_operacoes, values=["+", "-", "*", "/"], width=5)
operacoes.grid(row=0, column=1, padx=10, pady=10)

numero_2 = ttk.Entry(quadro_operacoes, width=15)
numero_2.grid(row=0, column=2, padx=10, pady=10)

botao_calcular = ttk.Button(quadro_operacoes, text="Calcular", command=calcular)
botao_calcular.grid(row=1, column=0, columnspan=3, pady=10)

resultado_label = ttk.Label(root, text="Resultado: ", font=('Arial', 16))
resultado_label.pack()

# Iniciando o loop principal da interface gráfica
root.mainloop()
