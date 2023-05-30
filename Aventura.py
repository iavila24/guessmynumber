import pygame

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load('aventurero.mp3')
    pygame.mixer.music.play()

play_music()

print("¡Bienvenido a la historia interactiva!")
print("Eres un aventurero en busca de un tesoro legendario en un antiguo templo.")
print("Tienes tres opciones. Elige sabiamente...\n")

print("Opción 1: Entras sigilosamente por una puerta lateral.")
print("Opción 2: Sigues el pasillo principal hasta la sala del trono.")
print("Opción 3: Exploras los oscuros pasajes subterráneos.")

opcion = input("Ingresa el número de la opción que deseas elegir (1, 2 o 3): ")

if opcion == "1":
    print("\nAvanzas con cautela por el pasillo lateral. De repente, activas una trampa y una enorme roca cae del techo. ¡Corres rápidamente y logras esquivarla por poco! Sigues tu camino.")

    print("Opción 1.1: Continúas explorando los pasajes laterales.")
    print("Opción 1.2: Regresas al pasillo principal.")
    print("Opción 1.3: Te adentras en una sala misteriosa que se encuentra frente a ti.")
    print("Opción 1.4: Te retiras del templo y buscas otro lugar para explorar.")
    print("Opción 1.5: Utilizas tus herramientas para desactivar las trampas restantes en el pasillo.")

    opcion_1 = input("Ingresa el número de la opción que deseas elegir (1.1, 1.2, 1.3, 1.4 o 1.5): ")

    if opcion_1 == "1.1":
        print("\nSigues explorando los pasajes laterales y descubres una antigua inscripción que te brinda una pista sobre la ubicación del tesoro. Continúas tu búsqueda con renovado entusiasmo.")
    elif opcion_1 == "1.2":
        print("\nRegresas al pasillo principal y te encuentras con un guardia del templo. Decides luchar contra él y, tras una feroz batalla, logras vencerlo. Continúas tu camino.")
    elif opcion_1 == "1.3":
        print("\nTe adentras en la sala misteriosa y encuentras un mapa detallado del templo. Ahora tienes una valiosa herramienta para avanzar en tu búsqueda.")
    elif opcion_1 == "1.4":
        print("\nDecides retirarte del templo y buscar otro lugar para explorar. Aunque no encuentras el tesoro en esta ocasión, sigues siendo un valiente aventurero.")
    else:
        print("\nUtilizas tus habilidades y herramientas para desactivar las trampas restantes en el pasillo. Ahora puedes explorar con mayor seguridad y continuar en tu búsqueda del tesoro.")

elif opcion == "2":
    print("\nTe adentras en la majestuosa sala del trono. De repente, los guardianes del templo se despiertan y te atacan. ¡Luchas valientemente pero eres superado en número! Tu búsqueda ha llegado a su fin.")

    print("Opción 2.1: Intentas escapar corriendo.")
    print("Opción 2.2: Buscas refugio detrás de un antiguo altar.")
    print("Opción 2.3: Luchas hasta el último aliento.")
    print("Opción 2.4: Suplicas por tu vida y ofreces compartir el tesoro con los guardianes.")
    print("Opción 2.5: Utilizas una reliquia especial para invocar a una poderosa criatura que te ayude en la batalla.")

    opcion_2 = input("Ingresa el número de la opción que deseas elegir (2.1, 2.2, 2.3, 2.4 o 2.5): ")

    if opcion_2 == "2.1":
        print("\nCorres a toda velocidad tratando de escapar de los guardianes. Logras llegar a una salida secreta y te alejas del templo, ileso pero sin el tesoro.")
    elif opcion_2 == "2.2":
        print("\nTe refugias detrás de un antiguo altar y los guardianes no te encuentran. Aprovechas la oportunidad para observar mejor la sala y descubres un compartimento oculto con un tesoro invaluable.")
    elif opcion_2 == "2.3":
        print("\nLuchas valientemente contra los guardianes, pero su fuerza es abrumadora. A pesar de tus esfuerzos, no logras sobrevivir.")
    elif opcion_2 == "2.4":
        print("\nSuplicas por tu vida y ofreces compartir el tesoro con los guardianes. Sorprendentemente, aceptan tu oferta y te permiten salir del templo con parte del tesoro.")
    else:
        print("\nUtilizas una reliquia especial que invoca a una poderosa criatura para que te ayude en la batalla contra los guardianes. Juntos, logran derrotar a los enemigos y aseguras el tesoro para ti.")

else:
    print("\nDecides explorar los oscuros pasajes subterráneos. A medida que avanzas, una trampa se activa y una enorme bola de piedra empieza a perseguirte. ¡Corres por tu vida!")

    print("Opción 3.1: Intentas negociar con la criatura.")
    print("Opción 3.2: Luchas contra la criatura con todas tus fuerzas.")
    print("Opción 3.3: Buscas una salida alternativa para escapar.")
    print("Opción 3.4: Utilizas un artefacto mágico para detener la bola de piedra.")
    print("Opción 3.5: Te detienes y enfrentas valientemente a la bola de piedra.")

    opcion_3 = input("Ingresa el número de la opción que deseas elegir (3.1, 3.2, 3.3, 3.4 o 3.5): ")

    if opcion_3 == "3.1":
        print("\nIntentas comunicarte con la criatura y descubres que es amigable. Te guía a través de los pasajes subterráneos y te lleva hasta el tesoro.")
    elif opcion_3 == "3.2":
        print("\nLuchas con todas tus fuerzas contra la criatura, pero resulta ser invencible. Tu valentía no es suficiente y pierdes la batalla.")
    elif opcion_3 == "3.3":
        print("\nLogras encontrar una salida alternativa y escapas de la criatura. Aunque no encuentras el tesoro, has sobrevivido para contar la historia.")
    elif opcion_3 == "3.4":
        print("\nUtilizas un artefacto mágico que detiene la bola de piedra en su camino. Ahora puedes continuar tu exploración sin peligro y descubres el tesoro al final de los pasajes subterráneos.")
    else:
        print("\nTe detienes y enfrentas valientemente a la bola de piedra. A medida que se acerca, logras esquivarla hábilmente y sobrevives. Continúas tu camino y finalmente encuentras el tesoro esperado.")

print("\nGracias por jugar. ¡Hasta la próxima!")


