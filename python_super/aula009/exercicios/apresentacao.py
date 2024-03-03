import tkinter as tk

root = tk.Tk()
root.title('Apresentação')
root.geometry('350x400')

nome = tk.Label(root, text='Meu nome é Gabriel Iuri', font=('Arial', 20))
idade = tk.Label(root, text='Tenho 18 anos', font=('Arial', 16))
hobby = tk.Label(root, text='Jogar FPS', font=('Arial', 16))

nome.pack(pady=(20, 15))
idade.pack()
hobby.pack()

root.mainloop()
