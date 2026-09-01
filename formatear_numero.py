def formatear_numeros(numero):
    if numero.is_integer():
        return int(numero)
    
    return round(numero, 2)