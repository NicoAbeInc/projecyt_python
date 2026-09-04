print("--- DIRECTORIO ---")

contactos = [
    {"id": 1, "nombre": "Marco", "telefono": "2871104293", "email": "marco@hotmail.com"},
    {"id": 2, "nombre": "Ana", "telefono": "2871122343", "email": "ana@hotmail.com"}
]

while True:

    for contacto in contactos:
        print(f"\n{contacto["nombre"]} {contacto["telefono"]} {contacto["email"]}")
        
    print("\nOpciones")
    print("1. Buscar")
    print("2. Agregar")
    print("3. Elimnar")
    print("4. Salir")

    opcion = int(input("\nElige una opcion: "))

    if opcion == 1:
        nom = input("\nIngresa el nombre: ")
        for contacto in contactos:
            if contacto["nombre"] == nom:
                print(f"\n{contacto["nombre"]} {contacto["telefono"]} {contacto["email"]}")
                print("-------------")
            
    elif opcion == 2:
        id_ult = contactos[-1]["id"] + 1
        nom = input("Nombre: ")
        tel= int(input("Telefono: "))
        ema = input("Email: ")
        
        contactos.append({"id": id_ult, "nombre": nom, "telefono": tel, "email": ema})
        
    elif opcion == 3:
        
        eliminado = False
        
        elim = input("\nContacto a eliminar: ")
        for contacto in contactos:
            if contacto["nombre"] == elim:
                contactos.remove(contacto)
                eliminado = True
                break
            
        if eliminado:
            print("Contacto eliminado.")
        else:
            print("No se encontro un contacto con ese nombre.")
        
    elif opcion == 4:
        break