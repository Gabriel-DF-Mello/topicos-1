from models.ata import Ata
from models.usuario import Usuario


class Menu:
    def __init__(self):
        self.active = True

    def display(self):
        while self.active:
            print("1 - Teste")
            print("2 - Teste")

            ans = input("Selecione: ")


menu = Menu()

menu.display()
