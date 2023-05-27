import random

guesses = set()

def begin_game():
    print("\n¡Bienvenido al juego de adivinar el número!")
    print("Tanto tú como la computadora intentarán adivinar un número entre 1 y 100.")
    print("El primero en adivinar el número gana el juego.")

    low = 1
    high = 100
    turns = 0
    guesses.clear()
    finish_game = False
    magic_number = random.randint(low, high)
    
    while finish_game != True:
        turns += 1
        low, high, finish_game = user_guess(magic_number, low, high, turns)

        if not finish_game:
            turns += 1
            finish_game = computer_guess(magic_number, low, high, turns)
    
    print(f"Se termino el juego en {turns} intentos 👾.")

            
def user_guess(magic_number, low, high, turns):  
    while True:
        guess = int(input("\nIngresa un número: "))
        print(f"Tu: {guess}")
        if guess in guesses:
            print(f"Ya ha sido ingresado el número {guess} antes, ingresa otro...")
        else: 
            guesses.add(guess)
            break
    
    if guess > magic_number:
        print("Ijole, el número oculto es menor ⬇😯...")
        high = guess - 1
    elif guess < magic_number:
        print("Ijole, el numero oculto es mayor ⬆😯...")
        low = guess + 1
    else: 
        print("Ese es el número, has ganado 🎉!")
        return guess, guess, True
            
    return low, high, False
        

def computer_guess(magic_number, low, high, turns):
   
    while True:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        print(f"\nComputadora: {guess}")
        if guess in guesses:
            print(f"Ya ha sido ingresado el número {guess} antes, ingresa otro...")
        else: 
            guesses.add(guess)
            break

    if guess > magic_number:
        print("Ijole, el número oculto es menor ⬇😯...")
        #high = guess - 1
    elif guess < magic_number:
        print("Ijole, el numero oculto es mayor ⬆😯...")
        #low = guess + 1
    else: 
        print("La computadora ha ganado 😱!")
        return True
    
    return False