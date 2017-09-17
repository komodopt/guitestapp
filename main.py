from tkinter import *

#definir função p/ o botão "About"
def about():
    print("Programa elaborado por RG")

#Cria a Janela
mainWindow = Tk()

#Criar menu superior
mainMenu = Menu(mainWindow)

userMenu = Menu(mainMenu)

#Tamanho da janela
mainWindow.geometry("800x600")

#Título da janela
mainWindow.title = 'Gestão de Equipa de Vendas'

#label bem vindo
labelWelcome = Label(mainWindow, text="Bem Vindo!")

#Forma de organização do layout
labelWelcome.pack()

#loop para manter a janela aberta
mainWindow.mainloop()