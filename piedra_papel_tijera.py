import random

def obtener_opcion_jugador():
    while True:
        opcion = input("Elige una opción (piedra, papel, tijera): ").lower()
        if opcion in ["piedra", "papel", "tijera"]:
            return opcion
        else:
            print("Opción inválida. Por favor, elige nuevamente.")

def obtener_opcion_computadora():
    return random.choice(["piedra", "papel", "tijera"])

def determinar_ganador(jugador, computadora):
    resultados = {
        "piedra": {"piedra": "Empate", "papel": "La computadora ha ganado", "tijera": "¡Ganaste!"},
        "papel": {"piedra": "¡Ganaste!", "papel": "Empate", "tijera": "La computadora ha ganado"},
        "tijera": {"piedra": "La computadora ha ganado", "papel": "¡Ganaste!", "tijera": "Empate"}
    }
    return resultados[jugador][computadora]

def jugar_piedra_papel_tijera():
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    jugador = obtener_opcion_jugador()
    computadora = obtener_opcion_computadora()
    print("Tú elegiste:", jugador)
    print("La computadora eligió:", computadora)
    resultado = determinar_ganador(jugador, computadora)
    print(resultado)


