print("SUMA DE NUMEROS ACUMULADOS")

numero_total = int(input("\nIngresa el numero acumulado"))

suma = 0

for numero in range(1, numero_total + 1):
    numero_anterior = suma
    suma += numero
    print(f"{numero_anterior} + {numero} = {suma}")