import tkinter as tk
import tkinter.font as tkFont
import main_with_experimental_gui

class App:
    def __init__(self, root):
        #setting title
        root.title("Gerência de Colaboradores")
        #setting window size
        width=398
        height=286
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        ListBoxColaboradores=tk.Listbox(root)
        ListBoxColaboradores["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        ListBoxColaboradores["font"] = ft
        ListBoxColaboradores["fg"] = main_with_experimental_gui.COR_LETRA
        ListBoxColaboradores["bg"] = main_with_experimental_gui.COR_BOTAO
        ListBoxColaboradores["justify"] = "center"
        ListBoxColaboradores.place(x=30,y=70,width=218,height=188)

        LabelTitulo=tk.Label(root)
        ft = tkFont.Font(family='Times',size=20)
        LabelTitulo["font"] = ft
        LabelTitulo["fg"] = main_with_experimental_gui.COR_LETRA
        LabelTitulo["bg"] = main_with_experimental_gui.COR_FUNDO
        LabelTitulo["justify"] = "center"
        LabelTitulo["text"] = "Colaboradores"
        LabelTitulo.place(x=62,y=20,width=165,height=30)

        ButtonAdicionar=tk.Button(root)
        ButtonAdicionar["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        ButtonAdicionar["font"] = ft
        ButtonAdicionar["fg"] = main_with_experimental_gui.COR_LETRA
        ButtonAdicionar["bg"] = main_with_experimental_gui.COR_BOTAO
        ButtonAdicionar["justify"] = "center"
        ButtonAdicionar["text"] = "Adicionar"
        ButtonAdicionar.place(x=270,y=70,width=105,height=38)
        ButtonAdicionar["command"] = self.ButtonAdicionar_command

        ButtonEditar=tk.Button(root)
        ButtonEditar["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        ButtonEditar["font"] = ft
        ButtonEditar["fg"] = main_with_experimental_gui.COR_LETRA
        ButtonEditar["bg"] = main_with_experimental_gui.COR_BOTAO
        ButtonEditar["justify"] = "center"
        ButtonEditar["text"] = "Editar"
        ButtonEditar.place(x=270,y=130,width=104,height=41)
        ButtonEditar["command"] = self.ButtonEditar_command

        ButtonRemover=tk.Button(root)
        ButtonRemover["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=14)
        ButtonRemover["font"] = ft
        ButtonRemover["fg"] = main_with_experimental_gui.COR_LETRA
        ButtonRemover["bg"] = main_with_experimental_gui.COR_BOTAO
        ButtonRemover["justify"] = "center"
        ButtonRemover["text"] = "Remover"
        ButtonRemover.place(x=270, y=190, width=103, height=41)
        ButtonRemover["command"] = self.ButtonRemover_command

    def ButtonAdicionar_command(self):
        print("command")


    def ButtonEditar_command(self):
        print("command")


    def ButtonRemover_command(self):
        print("command")

def run():
    root = tk.Tk()
    root["bg"] = main_with_experimental_gui.COR_FUNDO

    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root["bg"] = main_with_experimental_gui.COR_FUNDO

    app = App(root)
    root.mainloop()
