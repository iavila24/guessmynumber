import random
from colorama import Fore, Back, Style
from art import *


def adivinar_edad():
    print("¡Bienvenido al juego de adivinar la edad!")

    print("Piensa en un número entre 1 y 100, y trataré de adivinarlo.")
    print("Cuando estés listo, presiona ENTER.")
    input()

    limite_inferior = 1
    limite_superior = 100
    intentos = 0

    while True:
        intentos += 1
        numero_adivinado = random.randint(limite_inferior, limite_superior)

        print("¿Tu edad es {}?".format(numero_adivinado))
        respuesta = input("Ingresa 's' si es correcto, 'm' si tu edad es mayor o 'l' si es menor: ")

        if respuesta == 's':
            print("¡Genial! Adiviné tu edad en {} intentos.".format(intentos))
            break
        elif respuesta == 'm':
            limite_inferior = numero_adivinado + 1
        elif respuesta == 'l':
            limite_superior = numero_adivinado - 1
        else:
            print("Respuesta inválida. Por favor, ingresa 's', 'm' o 'l'.")

        if limite_inferior > limite_superior:
            print("¡Has hecho trampa cambiando tus respuestas! Eres un tramposo.")
            return

