from tkinter import *
from tkinter import messagebox
#definir função p/ o botão "About" com respectiva janela e label
def about():
    messagebox.showinfo("Sobre", "Programa elaborado por RG")

#Cria a Janela
root = Tk()

#Criar menu superior
mainMenu = Menu(root)
fileMenu = Menu(mainMenu, tearoff=0)
root.config(menu=mainMenu)

#Criar "sub-menu" ficheiro e respectivos botões
mainMenu.add_cascade(label="Ficheiro", menu=fileMenu)
fileMenu.add_command(label="Utilizadores")
fileMenu.add_command(label="Fechar", COMMAND=root.quit())

#Criar "Submenu" Sobre e respectivos botões
sobreMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="Sobre", menu=sobreMenu)
sobreMenu.add_cascade(label="Sobre", COMMAND = about())

#Tamanho da janela
root.geometry("300x250")

#Título da janela
root.title = 'Gestão de Equipa de Vendas'

#label bem vindo
labelWelcome = Label(root, text="Bem Vindo!")

#Forma de organização do layout
labelWelcome.pack()

#loop para manter a janela aberta
root.mainloop()