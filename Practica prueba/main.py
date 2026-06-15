def mostrar_menu():
    print("""========== MENÚ PRINCIPAL ==========
1. Agregar vehículo
2. Buscar vehículo
3. Eliminar vehículo
4. Actualizar disponibilidad
5. Mostrar vehículos
6. Salir
=====================================""")
    
def pedir_opcion():
    while True:
        try:
            op_menu = int(input("--> "))
            if 1 <= op_menu <= 6:
                return op_menu
            else:
                print("Ingrese un número respectivo a las opciones")
            
        except ValueError:
            print("Escriba opciones numéricas")

def validar_modelo(modelo):
    if len(modelo) == 0:
        print("No ingresó nombre del modelo del vehículo")
        return False
    
    return True

def validar_anio(anio):
    try:
        anio = float(anio)
        return anio > 1900
    except ValueError:
        return False

def validar_precio(precio):
    try:
        precio = float(precio)
        return precio > 0
    except ValueError:
        print("No puede usar caracteres como precio para ese vehículo")
        return False
    
def agregar(vehiculos):
    modelo = input("Ingrese modelo del vehículo:\n--> ").strip().title()
    if not validar_modelo(modelo):
        print("Error: El modelo no puede estar vacío ni ser solo espacios.")
        return

    anio = int(input("Ingrese año del vehículo:\n--> "))
    if not validar_anio(anio):
        print("Error: El año debe ser un número entero mayor que 1900.")
        return
    
    precio = float(input("Ingrese precio del vehículo:\n--> "))
    if not validar_precio(precio):
        print("Error: El precio debe ser un número decimal mayor que cero.")
        return
    
    diccionario = {
        "Modelo": modelo,
        "Año": int(anio),
        "Precio": float(precio),
        "Disponible": False
    }

    vehiculos.append(diccionario)

    print(f"Vehículo {modelo} agregado con éxito\n")

def buscar(vehiculos, modelo):
    if len(vehiculos) == 0:
        return -1
    
    i = 0
    for vehiculo in vehiculos:
        if vehiculo["Modelo"] == modelo:
            print(vehiculo)
            return i 
        i += 1
    
    return -1

def eliminar(vehiculos, resultados):
    if resultados == -1:
        print("El vehículo 'modelo' no se encuentra registrado.")
    else:
        del vehiculos[resultados]

def actualizar(vehiculos):
    
    for vehiculo in vehiculos:
        if vehiculo["Año"] >= 2020:
            vehiculo["Disponible"] = True

def mostrar(vehiculos):
    print("=== LISTA DE VEHICULOS ===")

    for vehiculo in vehiculos:
        if vehiculo["Disponible"] == True:
            disponibilidad = "DISPONIBLE"
        else:
            disponibilidad = "NO DISPONIBLE"

        print(f"""\nModelo: {vehiculo["Modelo"]}
Año: {vehiculo["Año"]}
Precio: {vehiculo["Precio"]}
Estado: {disponibilidad}
********************************************\n""")


vehiculos = []



valido = True
while valido:
    mostrar_menu()
    opcion = pedir_opcion()
    
    if opcion == 6:
        valido = False
        print("Gracias por usar el sistema. Vuelva Pronto")

    elif opcion == 1:
        agregar(vehiculos)
    
    elif opcion == 2:
        modelo = input("Ingrese nombre de modelo a buscar:\n--> ").strip().title()
        resultados = buscar(vehiculos, modelo)
        print(resultados)

    elif opcion == 3:
        modelo = input("Ingrese nombre de modelo a eliminar:\n--> ").strip().title()
        resultados = buscar(vehiculos, modelo)
        eliminar(vehiculos, resultados)
        print(f"El vehículo {modelo} ha sido eliminado.")

    elif opcion == 4:
        actualizar(vehiculos)
        print("El listado de Vehículos ha sido actualizado")

    elif opcion == 5:
        actualizar(vehiculos)
        mostrar(vehiculos)