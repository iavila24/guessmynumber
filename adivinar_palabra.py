import random
try:
    from main import menu
except ImportError:
    pass

def guess_word():
    words = ["python", "programación", "juego", "computadora", "programa"]
    secret_word = random.choice(words).lower()
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    print("¡Bienvenido al juego Adivina la Palabra!")
    print("La palabra tiene {} letras.".format(len(secret_word)))

    while attempts < max_attempts:
        guess = input("Ingresa una letra: ").lower()

        if len(guess) != 1:
            print("Ingresa solo una letra.")
            continue

        if guess in guessed_letters:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("¡Adivinaste una letra!")
        else:
            attempts += 1
            print("Letra incorrecta. Te quedan {} intentos.".format(max_attempts - attempts))

        if all(letter in guessed_letters for letter in secret_word):
            print("¡Felicidades! Adivinaste la palabra.")
            break

    else:
        print("¡Oh no! Agotaste tus intentos. La palabra era '{}'.".format(secret_word))

    play_again = input("¿Quieres jugar de nuevo? (s/n): ")
    if play_again.lower() == 's':
        menu()
    else:
        print("¡Gracias por jugar!")
