import random
from pygame import mixer

def dibujar_ahorcado(intentos):
    partes_ahorcado = [
        '''
           ____
          |    |
          |    
          |     
          |    
          |   
          -
        ''',
        '''
           ____
          |    |
          |    O
          |     
          |    
          |   
          -
        ''',
        '''
           ____
          |    |
          |    O
          |    |
          |    
          |   
          -
        ''',
        '''
           ____
          |    |
          |    O
          |   /|
          |    
          |   
          -
        ''',
        '''
           ____
          |    |
          |    O
          |   /|\\
          |    
          |   
          -
        ''',
        '''
           ____
          |    |
          |    O
          |   /|\\
          |   / 
          |   
          -
        ''',
        '''
           ____
          |    |
          |    O
          |   /|\\
          |   / \\
          |   
          -
        '''
    ]

    print(partes_ahorcado[intentos])

def ahorcado():
    mixer.init()
    mixer.music.load('john.mp3')
    mixer.music.play()

    palabras = ['python', 'programacion', 'computadora', 'juego', 'desarrollo']
    palabra_secreta = random.choice(palabras).lower()
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido a 'Ahorcado'!")
    print("Estoy pensando en una palabra relacionada con la programación.")

    while intentos > 0:
        print("\nPalabra:", ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra_secreta]))
        print("Intentos restantes:", intentos)
        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una letra válida.")
            continue

        if letra in letras_adivinadas:
            print("Ya has intentado esa letra antes.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            if ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra_secreta]) == palabra_secreta:
                print("¡Felicidades! ¡Has adivinado la palabra correctamente!")
                break
        elif letra not in palabra_secreta:
            intentos -= 1
            dibujar_ahorcado(6 - intentos)
            print("Letra incorrecta. ¡Inténtalo de nuevo!")

        if set(palabra_secreta) != set(letras_adivinadas):
            print("¡Oh no! Se te acabaron los intentos.")
            print("La palabra correcta era:", palabra_secreta)

    mixer.music.stop()