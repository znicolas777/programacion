numeros = []

for dato in range(8):
    valido = False
    while not valido:
        try:
            num =int(input("Ingresa 8 numeros enteros: "))
            valido = True
            numeros.append(num)
        except ValueError:
            print("Ingresa un numero entero")
#SOLICITAMOS EL NUMERO A BUSCAR
valido = False
while not valido:
    try:
        buscar =int(input("Ingrese el numero a buscar: "))
        valido = True
    except ValueError:
        print("Ingresa un numero entero")
#DECLARAMOS VARIABLES PARA LOS DATOS SOLICITADOS
conteo = 0 #CANTIDAD DE VECES QUE CONSIGUE EL NUMERO EN LA LISTA
posicion = [] #GUARDAR CADA POSICION DE LA LISTA DONDE CONSIGA EL NUMERO ACTUAL DE LA LISTA
#RECORRER LISTA
for i in range(8):
    if buscar == numeros[i]:
        conteo += 1 #AUMENTO CONTADOR
        posicion.append(i) #GUARDO LA POSICION DE LA CAJA ACTUAL DE LA LISTA

if conteo > 0: #ENCONTRE EL NUMERO
    print(f"El numero {buscar} se encuentra {conteo} veces en la lista")
    print("Se encontro en las siguientes posiciones: ")
    for x in range(len(posicion)):
        print(posicion[x], end="")
        print() #SALTO DE LINEA
else:
    print(f"El  numero {buscar} no se encontro en la lista")

