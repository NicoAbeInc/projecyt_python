print("--- DIRECTORIO ---\n")

contactos = [
    {"id": 1, "nombre": "Marco", "telefono": "2871104293", "email": "marco@hotmail.com"},
    {"id": 2, "nombre": "Ana", "telefono": "2871122343", "email": "ana@hotmail.com"}
]

while True:

    # for contacto in contactos:
    #     print(f"\n{contacto["nombre"]} {contacto["telefono"]} {contacto["email"]}")
    
    for numero, cont in enumerate(contactos, start=1):
        print(f"{numero}. {cont["nombre"]} {cont["telefono"]} {cont["email"]}")
        
    print("\nOpciones")
    print("1. Buscar")
    print("2. Agregar")
    print("3. Elimnar")
    print("4. Actualizar contacto")
    print("5. Salir")

    opcion = int(input("\nElige una opcion: "))

    if opcion == 1:
        nom = input("\nIngresa el nombre: ")
        for contacto in contactos:
            if contacto["nombre"] == nom:
                print(f"\n{contacto["nombre"]} {contacto["telefono"]} {contacto["email"]}")
                print("\n-------------\n")
            
    elif opcion == 2:
        id_ult = contactos[-1]["id"] + 1
        nom = input("Nombre: ")
        tel= int(input("Telefono: "))
        ema = input("Email: ")
        
        contactos.append({"id": id_ult, "nombre": nom, "telefono": tel, "email": ema})
        
    elif opcion == 3:
        
        eliminado = False
        
        elim = input("\nNombre del contacto a eliminar: ")
        # for contacto in contactos:
        #     if contacto["nombre"] == elim:
        #         contactos.remove(contacto)
        #         eliminado = True
        #         break
            
        for indice, contacto in enumerate(contactos):
            if contacto["nombre"] == elim:
                contactos.pop(indice)
                eliminado = True
                break
            
        if eliminado:
            print("\nContacto eliminado.\n")
        else:
            print("\nNo se encontro un contacto con ese nombre.\n")
        
    elif opcion == 4:
        
        print("\nActualizar contacto")
        print("1. Nombre")
        print("2. Telefono")
        print("3. Email")
        
        opcion = int(input("\nElige una opcion: "))
        
        actualizar = False
        
        if opcion == 1:
            nom = input("\nNombre del contacto: ")
            nom_nuevo = input("Ingresa nuevo nombre ")
            for contacto in contactos:
                if contacto["nombre"] == nom:
                    contacto["nombre"] = nom_nuevo
                    actualizar = True
                    break
                
            if actualizar:
                print("\nContacto actualizado.\n")
            else:
                print("\nNo se encontro un contacto con ese nombre.\n")
        
        elif opcion == 2:
            nom = input("\nNombre del contacto: ")
            tel_nuevo = int(input("Ingresa nuevo numero telefonico "))
            for contacto in contactos:
                if contacto["nombre"] == nom:
                    contacto["telefono"] = tel_nuevo
                    actualizar = True
                    break
                
            if actualizar:
                print("\nContacto actualizado.\n")
            else:
                print("\nNo se encontro un contacto con ese nombre.\n")
        
        elif opcion == 3:
            nom = input("\nNombre del contacto: ")
            ema_nuevo = input("Ingresa nuevo email ")
            for contacto in contactos:
                if contacto["nombre"] == nom:
                    contacto["email"] == ema_nuevo
                    actualizar = True
                    break
            
            if actualizar:
                print("\nContacto actualizado.\n")
            else:
                print("\nNo se encontro un contacto con ese nombre.\n")
        
    elif opcion == 5:
        break