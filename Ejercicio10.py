# DEFINIR FUNCIONES
def calcular_propina(subtotal,porcentaje):
    propina = subtotal * porcentaje / 100
    return propina

def calcular_total(subtotal,propina):
    total = subtotal + propina
    return total

def desglose_total(subtotal,total,propina,porcentaje):
    print("********************")
    print(f"El subtotal de la cuenta es ${subtotal}")
    print(f"La propina a pagar es ${propina}")
    print(f"El total a pagar es ${total}")
    print("********************")


# CODIGO PRINCIPAL
while True:
    try:
        subtotal = float(input("Ingresa el subtotal de la cuenta :"))
        break
    except ValueError:
        print("Debe ingresar un valor valido")
while True:
    try:
        porcentaje = int(input("Ingrese el porcentaje de propina (10/15/20) : "))
        if porcentaje in (10,15,20):
            break
        else:
            print("Debes ingresar un porcentaje de 10, 15 o 20")

        break
    except ValueError:
        print("Ingresa un porcentaje valido 10/15/20")
    
# LLAMAR FUNCIONES
propina = calcular_propina(subtotal, porcentaje)
total = calcular_total(subtotal, propina)
desglose_total(subtotal,total,propina,porcentaje)

