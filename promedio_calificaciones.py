print("CALIFICACION ALUMNO")

calif1 = int(input("\nIngresa calificacion 1: "))
calif2 = int(input("\nIngresa calificacion 2: "))
calif3 = int(input("\nIngresa calificacion 3: "))

promedio = (calif1 + calif2 + calif3) / 3

if promedio >= 70:
    print(f"\nCalificaciones {calif1}, {calif2}, {calif3} | Promedio: {round(promedio, 2)} | Resultado: Aprobado ")
else:
    print(f"\nCalidicacion {calif1}, {calif2}, {calif3} | Promedio: {round(promedio, 2)} | Resultado: Reprobado")