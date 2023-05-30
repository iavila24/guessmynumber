import random


def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)


def jugar():
    rondas_para_ganar = 3
    rondas_j1 = 0
    rondas_j2 = 0
    while rondas_j1 < rondas_para_ganar and rondas_j2 < rondas_para_ganar:
        dado_1_jugador_1, dado_2_jugador_1 = lanzar_dados()
        dado_1_jugador_2, dado_2_jugador_2 = lanzar_dados()
        print(f"Resultados de los dados del jugador 1: [{dado_1_jugador_1}, {dado_2_jugador_1}]")
        print(f"Resultados de los dados del jugador 2: [{dado_1_jugador_2}, {dado_2_jugador_2}]")
        if dado_1_jugador_1 in [dado_1_jugador_2, dado_2_jugador_2] or dado_2_jugador_1 in [dado_1_jugador_2, dado_2_jugador_2]:
            rondas_j1 += 1
            print("Jugador 1 gana la ronda")
        else:
            rondas_j2 += 1
            print("Jugador 2 gana la ronda")
    if rondas_j1 > rondas_j2:
        print("El jugador 1 gana la partida")
    else:
        print("El jugador 2 gana la partida")


jugar()
