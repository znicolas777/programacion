#DECLAR DICCIONARIO(VACIO)
producto = {}
#SOLICITAR DATOS

producto["nombre"] = input("Ingresa el nombre del producto: ")
while True:
    try:
        producto["precio"] = int(input("Ingresa el precio del producto: "))
        if producto["precio"] <= 0:
            print("El precio no puede ser negativo")
        else:
            break
    except ValueError:
        print("Debe ingresar un valor valido")
#SOLICITAR EL STOCK DISPONIBLE
while True:
    try:
        producto["stock"] = int (input("Ingrese el stock del producto: "))
        if producto["stock"] < 0:
            print("El stock no puede ser negativo")
        else:
            break
    except ValueError:
        print("Ingresa un valor valido")    
#AGREGAR UNA NUEVA CLAVE AL DICCIONARIO PARA INDICAR EL PRODUCTO ESTA DISPONIBLE O AGOTADO
producto["estado"] = "disponible" if producto["stock"] > 0 else "agotado"
#MOSTRAR LA INFORMACION
print("******* DATOS DEL PRODUCTO *******")
for llave, valor in producto.items():
    print(f"{llave.title()}: {valor}")

