#CREAR DICCIONARIO
estudiantes = {}
#CREAR UNA KEY Y VALOR
estudiantes["nombre"] = "nicolas"
estudiantes["rut"] = "22429085-3"
estudiantes["edad"] = "18"

print(estudiantes)

#CAMBIAR VALOR
estudiantes["edad"] = "19"
#ELIMINAR UNA UNA KEY Y VALOR
del estudiantes ["rut"]
#ELIMINAR Y GUARDAR EL VALOR DE LA CLAVE ELIMINADA
nombre_eliminado = estudiantes.pop("edad")
print(nombre_eliminado)
#MOSTRAR EL VALOR DE UNA CLAVE
print(estudiantes["nombre"]) #SI LA CLAVE NO EXISTE DA ERROR
print(estudiantes.get("rut")) #EL .get busca la clave SI NO EXISTE DEVUELVE NONE
print(estudiantes.get("rut","No existe"))

#RECORRER LOS DICCIONARIOS
#MOSTRAR SOLO LAS CLAVES DEL DICCIONARIO DE DATOS
for llave in estudiantes.keys():
    print(llave)
#RECORRER Y SI QUIERO MOSTRAR SOLO LOS VALORES
for valor in estudiantes.values():
    print(valor)
#RECORRER Y MOSTRAR TANTO CALVES COMO VALORES
for llave, valor in estudiantes.items():
    print(f"{llave} = {valor }")