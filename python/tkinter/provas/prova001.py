'''
[PY-A09] Desenvolva um código utilizando seus conhecimentos de Tkinter para converter uma unidade de medida de centímetros para metros
'''

import tkinter as tk

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
cm_input = tk.Entry(cm_frame, textvariable=cm_valor, width=5)
cm_texto = tk.Label(cm_frame, text='Cm', font=('Arial', 10))

# exibir elementos
titulo_label.pack(pady=(0, 25))

cm_frame.pack()
cm_lebel.grid(row=0, column=0, padx=(5, 10))
cm_input.grid(row=0, column=1)
cm_texto.grid(row=0, column=2, padx=(0, 5))

# exibir root em loop
root.mainloop()
