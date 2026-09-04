import random

juga = 0
compu = 0
empate = 0

while True:
    
    opciones = ["piedra", "papel", "tijera"]
        
    jugador = input("\nElije piedra, papel o tijera ").lower()

    while jugador not in opciones:
        print("\nOpcion no valida")
        jugador = input("\nElije piedra, papel o tijera ").lower()
        
    computadora = random.choice(opciones)

    print(f"\nComputadora: {computadora}")


    if jugador == computadora:
        print("\nEmpate")
        
        empate += 1
        
        print(f"Marcador: Jugador {juga} -- Computadora {compu} -- Empate {empate}")

    elif(jugador == "piedra" and computadora == "tijera") or\
        (jugador == "papel" and computadora == "piedra") or\
        (jugador == "tijera" and computadora == "papel"):
            print("\nGanaste!")
                
            juga += 1
            
            print(f"Marcador: Jugador {juga} -- Computadora {compu} -- Empate {empate}")
            
    else:
        print("\nPerdiste")
        
        compu += 1
        
        print(f"Marcador: Jugador {juga} -- Computadora {compu} -- Empate {empate}")
        
        continuar = input("\nQuieres seguir jugando (s/n): ").lower()
        
        if continuar != "s":
            print("\nGracias por jugar")
            break
    
