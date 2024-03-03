import tkinter as tk

root = tk.Tk()
root.title('Janela com Tkinter')
root.geometry('400x300+200+200')

titulo = tk.Label(root, text='Hello world', font=('Arial', 24))
nome = tk.Label(root, text='Gabriel', font=('Arial', 15))

titulo.pack(pady=15)
nome.pack()

root.mainloop()
