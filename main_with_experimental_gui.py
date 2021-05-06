import tkinter as tk
import tkinter.font as tkFont

import model
from GUIs import cargos, colaboradores, setores

#
# CLASSE NÃO UTILIZADA!
#

listaCargos = []
listaSetores = []
listaColaboradores = []

COR_FUNDO = "#23272a"
COR_LETRA = "#ffffff"
COR_BOTAO = "#2c2f33"

class App:
    def __init__(self, root):
        #setting title
        root.title("Gerência de Colaboradores")

        # setting window size
        width = 450
        height = 158
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        LabelTitulo = tk.Label(root)
        LabelTitulo["anchor"] = "center"
        ft = tkFont.Font(family='Times', size=22)
        LabelTitulo["font"] = ft
        LabelTitulo["fg"] = COR_LETRA
        LabelTitulo["bg"] = COR_FUNDO
        LabelTitulo["justify"] = "center"
        LabelTitulo["text"] = "Gerência de Colaboradores"
        LabelTitulo.place(x=62,y=20,width=311,height=32)

        ButtonSetores=tk.Button(root)
        ft = tkFont.Font(family='Times',size=10)
        ButtonSetores["font"] = ft
        ButtonSetores["fg"] = COR_LETRA
        ButtonSetores["bg"] = COR_BOTAO
        ButtonSetores["justify"] = "center"
        ButtonSetores["text"] = "Setores"
        ButtonSetores.place(x=40,y=90,width=105,height=37)
        ButtonSetores["command"] = self.ButtonSetores_command

        ButtonColaboradores=tk.Button(root)
        ft = tkFont.Font(family='Times',size=10)
        ButtonColaboradores["font"] = ft
        ButtonColaboradores["fg"] = COR_LETRA
        ButtonColaboradores["bg"] = COR_BOTAO
        ButtonColaboradores["justify"] = "center"
        ButtonColaboradores["text"] = "Colaboradores"
        ButtonColaboradores.place(x=160,y=90,width=105,height=36)
        ButtonColaboradores["command"] = self.ButtonColaboradores_command

        ButtonCargos=tk.Button(root)
        ft = tkFont.Font(family='Times',size=10)
        ButtonCargos["font"] = ft
        ButtonCargos["fg"] = COR_LETRA
        ButtonCargos["bg"] = COR_BOTAO
        ButtonCargos["justify"] = "center"
        ButtonCargos["text"] = "Cargos"
        ButtonCargos.place(x=280,y=90,width=104,height=34)
        ButtonCargos["command"] = self.ButtonCargos_command

    def ButtonSetores_command(self):
        setores.run()

    def ButtonCargos_command(self):
        cargos.run()

    def ButtonColaboradores_command(self):
        colaboradores.run()

if __name__ == "__main__":

    listaSetores.append(model.Setor("Direção"))

    root = tk.Tk()
    root["bg"] = COR_FUNDO

    app = App(root)
    root.mainloop()
