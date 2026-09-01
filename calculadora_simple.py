print("Calculadora Simple")

print("\nSelecciona una operacion")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("\nSelecciona una opcion: "))

numero1 = float(input("Ingresa un numero: "))
numero2 = float(input("Ingresa otro numero: "))

def mostrar_resultado(resultado):
    if resultado.is_integer():
        return int(resultado)
    else:
        return round(resultado, 2)

if opcion == 1:
    resultado = numero1 + numero2
    print(f"\nResultado: {mostrar_resultado(numero1)} + {mostrar_resultado(numero2)} = {mostrar_resultado(resultado)}")
    
elif opcion == 2:
    resultado = numero1 - numero2
    print(f"\nResultado: {mostrar_resultado(numero1)} - {mostrar_resultado(numero2)} = {mostrar_resultado(resultado)}")
    
elif opcion == 3:
    resultado = numero1 * numero2
    print(f"\nResultado: {mostrar_resultado(numero1)} * {mostrar_resultado(numero2)} = {mostrar_resultado(resultado)}")
    
elif opcion == 4:
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"\nResultado: {mostrar_resultado(numero1)} / {mostrar_resultado(numero2)} = {mostrar_resultado(resultado)}")
    else:
        print("\nError: No puedes dividir entre cero.")
        
else:
    print("\nOpcion no valida")


