print("=== COMPRA CON DESCUENTO ===")

costo_producto = float(input("\nIngresa el costo del prouducto: "))
cantidad_producto = int(input("\nIngresa la cantidad de productos: "))

def formatear_numero(numero):
    if numero.is_integer():
        return int(numero)
    
    return round(numero, 2)

subtotal = cantidad_producto * costo_producto

if subtotal >= 1000:
    descuento = subtotal * 0.10
    total = round(subtotal - descuento, 2)
    
    print(f"\nPrecio: {formatear_numero(costo_producto)} | Cantidad: {formatear_numero(cantidad_producto)} | Subtotal: {formatear_numero(subtotal)} | Descuento: {formatear_numero(descuento)} | Total: {formatear_numero(total)}")
else:
    total = round(subtotal, 2)
    print(f"\nPrecio: {formatear_numero(costo_producto)} | Cantidad: {formatear_numero(cantidad_producto)} | Subtotal: {formatear_numero(subtotal)} | Total: {formatear_numero(total)}")
    
