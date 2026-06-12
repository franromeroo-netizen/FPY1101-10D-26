contactos = {}

def pedir_opcion():
    opcion = input("[A] Agregar contacto | [B] Buscar | [S] Salir: ").upper()
    return opcion

def buscar_numero(agenda, nombre_buscado):
    
    if len(nombre_buscado) == 0:
        print("No hay contactos registrados")
        return
    
    if nombre_buscado in agenda:
        return agenda[numero_contacto]
    else:
        return "El contacto no existe"
        

    


menu = True
while menu:
    print("Agenda de contactos:\nBienvenido")
    opcion = pedir_opcion()

    if opcion == "S":
        menu = False
    elif opcion == "A":
        nombre_contacto = input("Ingrese nombre de contacto: ").title()
        numero_contacto = input("Ingrese número de contacto: ").title()
        if (nombre_contacto == 0) or (numero_contacto == 0):
            print("Error al ingresar contacto")

        contactos[nombre_contacto] = [numero_contacto]
        
    elif opcion == "B":
        nombre_buscado = input("Ingrese nombre de contacto: ").title()
        resultado = buscar_numero(agenda, nombre_buscado)
        print(resultado)