print("=== CONVERSOR DE PESO ===")

print("\nUnidades disponibles: ")
print("1. kilogramos")
print("2. Gramos")
print("3. Libras")
print("4. Onzas")

unidad_entrada = int(input("\nSelecciona la unidad de origen: "))
unidad_salida = int(input("\nSelecciona la unidad de destino: "))

peso = float(input("\nIngresa el peso: "))

def formatear_numero(numero):
    if numero.is_integer():
        return int(numero)
    
    return round(numero, 2)

if unidad_entrada == 1:
    kilogramos = peso
    unidad_origen = "kg"

elif unidad_entrada  == 2:
    kilogramos = peso / 100
    unidad_origen = "g"
    
elif unidad_entrada == 3:
    kilogramos  = peso * 0.453592
    unidad_origen = "lb"
    
elif unidad_entrada == 4:
    kilogramos = peso * 0.0283495
    unidad_origen = "oz"
    
else:
    print("\nUnidad de origen no valida.")
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
        print("\nUnidad de destino no valida")
        
    if resultado is not None:
        print(f"\n{formatear_numero(peso)} {unidad_origen} = {formatear_numero(resultado)} {unidad}")