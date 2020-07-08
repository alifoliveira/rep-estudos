import tkinter


class FrontEnd(tkinter.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.resizable(False, False)    


class Rotulo(tkinter.Label):
    def __init__(self, text, row, column):
        super().__init__()

        self.config(text=text)
        self.grid(row=row, column=column)


class Botao(tkinter.Button):
    def __init__(self, text, width, row, column, command):
        super().__init__()

        self.config(text=text, width=width, command=command)
        self.grid(row=row, column=column)
    


class Lauch():
    def __init__(self):

        main = FrontEnd("Janela Principal", [600, 400])
        
        self.teste = Rotulo("Teste de janela", 0, 0)
        self.sair = Botao("Sair", 8, 1, 1, main.destroy)
        self.salvar = Botao("Salvar", 8, 1, 0, '')

        main.mainloop()

start = Lauch()

