#FUNCION
def solicitar_nombre():
    nombre = input("Ingresa tu nombre: ")
    return nombre
    

#CODIGO PRINCIPAL
print("Bienvenido al gimnasio energy")
cliente = solicitar_nombre()
print(f"Bienvenido cliente {cliente}")