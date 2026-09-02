import random

opciones = ["piedra", "papel", "tijera"]

jugador = input("\nElije piedra, papel o tijera ").lower()

while jugador not in opciones:
    print("\nOpcion no valida")
    jugador = input("\nElije piedra, papel o tijera ").lower()
    
computadora = random.choice(opciones)

print(f"\nComputadora: {computadora}")

if jugador == computadora:
    print("\nEmpate")

elif(jugador == "piedra" and computadora == "tijera") or\
    (jugador == "papel" and computadora == "piedra") or\
    (jugador == "tijera" and computadora == "papel"):
        print("\nGanaste!")
        
else:
    print("\nPerdiste")
    
