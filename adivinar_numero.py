import random
from pygame import mixer


def computer_guess():
    mixer.init()
    mixer.music.load('music.mp3')
    mixer.music.play()

    name = input("Ingresa tu nombre: ")
    x = 0
    while x <= 1:
        try:
            x = int(input("Piensa en un número mayor que 1: "))
            if x <= 1:
                print("El número debe ser mayor que 1. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero mayor que 1. Intenta de nuevo.")

    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'¿Es {guess} demasiado alto (H), demasiado bajo (L), o correcto (C)? ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

        if high < low:
            print("¡Has hecho trampa cambiando tus respuestas! Eres un tramposo.")
            return

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
