# Bucles for y while ejercicio
print("Tabla del numero 7")
tabla = 7
for numero in range(1,11):
    print(f"{tabla} x {numero} = {tabla * numero}")
print("")
print("")

print("Suma del 1 al 100")
suma = 0
for numero in range(1, 101):
    suma_anterior = suma
    suma += numero
    print(f"{suma_anterior} + {numero} = {suma}")

print("")
print("")

#Otra version de suma del 1 al 100
suma = 0
for numero in range(1, 101):
    print(f"{suma} + {numero} = {suma + numero}")
    suma += numero
    
print("")
print("")

print("3 intentos de password")
intentos = 0
password = "Nico"
while intentos < 3:
    passw = input("Ingresa tu password")
    if password == passw:
        print("Acceso valido")
        break
    if password != passw:
        print("Acceso invalido")
    intentos += 1
print("")
print("")



