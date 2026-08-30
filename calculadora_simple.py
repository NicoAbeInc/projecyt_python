print("Calculadora Simple")

print("\nSelecciona una operacion")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("\nSeleccionar una opcion"))

numero1 = float(input("Ingresa un numero: "))
numero2 = float(input("Ingresa otro numero: "))

if opcion == 1:
    resultado = numero1 + numero2
    print(f"Suma: {numero1} + {numero2} = {round(resultado, 2)}")
    
if opcion == 2:
    

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

print("\n=== Resultado ===")

print(f"Suma: {numero1} + {numero2} = {suma}")
print(f"Resta: {numero1} - {numero2} = {resta}")
print(f"Multiplicacion: {numero1} * {numero2} = {multiplicacion}")

if numero2 != 0:
    division = numero1 / numero2
    print(f"Division: {numero1} / {numero2} = {round(division, 2)}")
else:
    print("Division: no es posible dividir entre 0")
    
