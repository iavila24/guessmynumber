from adivinar_numero import computer_guess
from adivinar_palabra import guess_word
from adivinar_edad import adivinar_edad
try:
    from main import menu
except ImportError:
    pass

def menu():
    print("¡Bienvenido al Menú de Juegos!")
    print("1. Adivinar el número")
    print("2. Adivina la edad")
    print("3. Adivina la palabra")
    print("4. Salir")

    while True:
        seleccion = input("Ingresa el número de juego que deseas jugar (1-4): ")

        if seleccion == '1':
            computer_guess()
        elif seleccion == '2':
            adivinar_edad()
        elif seleccion == '3':
            guess_word()
        elif seleccion == '4':
            print("¡Gracias por jugar!")
            break
        else:
            print("Selección inválida. Por favor, ingresa un número válido.")

menu()
