print("=== CONVERSOR DE PESO ===")

print("\nUnidades disponibles: ")
print("1. kilogramos")
print("2. Gramos")
print("3. Libras")
print("4. Onzas")

unidad_entrada = int(input("\nSelecciona la unidad de origen: "))
unidad_salida = int(input("\nSelecciona la unidad de destino: "))

peso = float(input("Ingresa el peso: "))

if unidad_entrada == 1:
    kilogramos = peso

elif unidad_entrada  == 2:
    kilogramos = peso / 100
    
elif unidad_entrada == 3:
    kilogramos  = peso * 0.453592
    
elif unidad_entrada == 4:
    kilogramos = peso * 0.0283495
    
else:
    print("Unidad de origen no valida.")
    kilogramos = None
    
if kilogramos is not None:
    
    if unidad_salida == 1:
        resultado = kilogramos  
        unidad = "kg"
    
    elif unidad_salida == 2:
        resultado = kilogramos * 100
        unidad = "g"
        
    elif unidad_salida   == 3:
        resultado = kilogramos / 0.453592
        unidad = "lb"
        
    elif unidad_salida == 4:
        resultado = kilogramos / 0.0283495
        unidad = "oz"
        
    else:
        resultado = None
        print("Unidad de destino no valida")
        
    if resultado is not None:
        print(f"\nResultado: {round(resultado, 2)} {unidad}")