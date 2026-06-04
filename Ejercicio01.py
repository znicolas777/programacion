    #CREAR LISTA
numero = []
    #SOLICITAR LOS NUMEROS AL USUARIO
for dato in range (10):
    valido = False
    while not valido:
        try:
            num =int(input("Ingresa 10 numeros enteros "))
            valido = True
            numero.append(num)
        except ValueError:
            print("Ingrese un numero entero")
    #VARIABLES PARA RESOLVER EL EJERCICIO
cant_pares = 0
cant_impares = 0
suma_pares = 0
suma_impares = 0
    #RECORRER LA LISTA PARA VERIFICAR LOS DATOS
for i in range(10):
    #SI EL NUMERO ES PAR
    if numero[i] % 2 == 0:
        cant_pares += 1
        suma_pares += numero[i]
    else:   #SI EL NUMERO ES IMPAR
        cant_impares += 1
        suma_impares += numero[i]

print(f"Cantidad de pares: {cant_pares} suma total de pares: {suma_pares}")
print(f"Cantidad de impares: {cant_impares} suma total de impares: {suma_impares}")
