from adivinar_numero import computer_guess
from adivinar_edad import adivinar_edad
import game_pc_vs_user
from adivinar_palabra import guess_word
from piedra_papel_tijera import jugar_piedra_papel_tijera
from colorama import Fore, Back, Style
from art import *

def menu():

    while True:
         
         print(Back.BLUE)
         print("\n¡Bienvenido al Menú de Juegos!")
         print("1. Adivinar el número")
         print("2. Adivina la edad")
         print("3. Adivina el número User vs. PC")
         print("4. Adivina la palabra")
         print("5. Piedra, Papel o Tijera")
         print("6. Salir")
         seleccion = input("Ingresa el número de juego que deseas jugar (1-6): ")


         if seleccion == '1':
            computer_guess()
         elif seleccion == '2':
            adivinar_edad()
         elif seleccion == '3':
            game_pc_vs_user.begin_game()
         elif seleccion == '4':
           guess_word()
         elif seleccion == '5':
            jugar_piedra_papel_tijera()
         elif seleccion == '6':
            print("¡Gracias por jugar!")
            aprint("Line Brack", number=2)
            break
         else:
            print("Selección inválida. Por favor, ingresa un número válido.")
menu()
