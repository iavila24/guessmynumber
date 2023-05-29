import random
from pygame import mixer
from colorama import Fore, Back, Style
from art import *



print(Fore.MAGENTA + Back.MAGENTA)
tprint("GRUPO 372","rnd-small")

def computer_guess():
    mixer.init()
    mixer.music.load('music.mp3')
    mixer.music.play()

    (Fore.GREEN + Back.BLUE)
    name = input("Ingresa tu nombre: ")
    aprint("Line Brack", number=2)
    x = int(input("Piensa en un número: "))
    
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'¿Es {guess} demasiado alto (H), demasiado bajo (L), o correcto (C)? ').lower()
        aprint("Line Brack", number=4)

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    mixer.music.stop()

    print(f'¡Yay! ¡La computadora adivinó tu número, {guess}, correctamente!')

    with open('nombres.txt', 'a') as file:
        file.write(f'Nombre: {name}\n')

    with open('nombres.txt', 'r') as file:
        lines = file.readlines()
        last_five_names = lines[-5:]
        print("\nÚltimos 5 nombres almacenados:")
        for name_line in last_five_names:
            print(name_line.strip())

def adivinar_edad():
    print(Fore.GREEN + Back.BLUE)
    print("¡Bienvenido al juego de adivinar la edad!")
    aprint("Line Brack", number=4)
    print("Piensa en un número entre 1 y 100, y trataré de adivinarlo.")
    
    print("Cuando estés listo, presiona ENTER.")
    aprint("Line Brack", number=2)
    input()

    limite_inferior = 1
    limite_superior = 100
    intentos = 0

    while True:
        intentos += 1
        numero_adivinado = random.randint(limite_inferior, limite_superior)

        print("¿Tu edad es {}?".format(numero_adivinado))
        aprint("Line Brack", number=1)
        respuesta = input("Ingresa 's' si es correcto, 'm' si tu edad es mayor o 'l' si es menor: ")
        aprint("Line Brack", number=5)

        if respuesta == 's':
            print("¡Genial! Adiviné tu edad en {} intentos.".format(intentos))
            
            break
        elif respuesta == 'm':
            limite_inferior = numero_adivinado + 1
        elif respuesta == 'l':
            limite_superior = numero_adivinado - 1
        else:
            print("Respuesta inválida. Por favor, ingresa 's', 'm' o 'l'.")

def menu():
    print(Fore.GREEN + Back.BLUE)
    aprint("Line Brack", number=2)
    print("¡Bienvenido al Menú de Juegos!")
    aprint("Line Brack", number=2)
    print("1. Adivinar el número")
   
    print("2. Adivina la edad")
    
    print("3. Salir")
    
   
    while True:
        aprint("Line Brack", number=4)
        seleccion = input("Ingresa el número de juego que deseas jugar (1-3): ")
        aprint("Line Brack", number=4)
        if seleccion == '1':
            computer_guess()
        elif seleccion == '2':
            adivinar_edad()
        elif seleccion == '3':
            print(Fore.GREEN + Back.BLUE)
            print("¡Gracias por jugar!")
            aprint("Line Brack", number=2)
            break
        else:
            print("Selección inválida. Por favor, ingresa un número válido.")

menu()
