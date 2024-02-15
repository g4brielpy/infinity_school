'''
[PY-A09] Desenvolva um código utilizando seus conhecimentos de Tkinter para converter uma unidade de medida de centímetros para metros
'''

import tkinter as tk


# para converter uma unidade de medida de centímetros para metros
def centimetros_para_metros():
    centimetros = float(cm_valor.get())
    metros = centimetros / 100
    resultado.config(text=f'{centimetros:.2f}cm = {metros:.2f}m')


# config geral
root = tk.Tk()
root.title('Converte valores')
root.config(padx=15, pady=15)

# config de widgets
titulo_label = tk.Label(
    root, text='Converter centímetros para metros', font=('Arial', 18))

cm_frame = tk.Frame(root, relief='groove', borderwidth=2)
cm_valor = tk.StringVar()
cm_lebel = tk.Label(cm_frame, text='Centímetros:', font=('Arial', 15))
cm_input = tk.Entry(cm_frame, textvariable=cm_valor, width=10)
cm_texto = tk.Label(cm_frame, text='Cm', font=('Arial', 10))

resultado = tk.Label(root, text='', font=('Arial', 13))

botao_converter = tk.Button(root, text='Fazer conversão',
                            command=centimetros_para_metros)

# exibir elementos
titulo_label.pack(pady=(0, 25))

cm_frame.pack()
cm_lebel.grid(row=0, column=0, padx=(5, 10))
cm_input.grid(row=0, column=1)
cm_texto.grid(row=0, column=2, padx=(0, 5))

botao_converter.pack(pady=20)

resultado.pack()

# exibir root em loop
root.mainloop()
