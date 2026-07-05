#=========================Tienda de consolas============================

def menu():
    print("""\nMenú Principal
1. Agregar consola
2. Buscar consola por sigla
3. Eliminar consola
4. Mostrar todas las consolas
5. Salir""")
    
def seleccion_opcion():
    try:
        seleccion = int(input("--> "))
        if 1 <= seleccion <= 5:
            return seleccion
    except ValueError:
        return False

#=======================================================================

def validacion_sigla_espacio(sigla):
    return sigla not in consolas

def validacion_sigla(sigla):
    return 2 <= len(sigla.upper().strip()) <= 5 and sigla.isalnum()

def validacion_nombre(nombre):
    return 3 <= len(nombre.title()) <= 40

def validacion_fabricante(fabricante):
    return 2 <= len(fabricante) <= 30

def validacion_anio_lanzamiento(anio_lanzamiento):
    try:
        anio_int = int(anio_lanzamiento)
        return 1972 <= anio_int <= 2025
    except ValueError:
        return False

def validacion_precio(precio):
    try:
        precio_float = float(precio)
        return precio_float > 0
    except ValueError:
        return False

def validacion_stock(stock):
    try:
        stock_float = float(stock)
        return stock_float >= 0
    except ValueError:
        return False


def opcion_agregar(consolas, ventas):
    sigla = input("Ingrese siglas de la consola:\n--> ").upper().strip()
    if not validacion_sigla_espacio(sigla):
        print("ERROR. Nombre de sigla ya agregada.")
        return
    if not validacion_sigla(sigla):
        print("ERROR. Sigla no válida.")
        return

    nombre = input("Ingrese nombre de la consola:\n--> ").title()
    if not validacion_nombre(nombre):
        print("ERROR. Nombre no válido.")
        return

    fabricante = input("Ingrese fabricante de la consola:\n--> ").title()
    if not validacion_fabricante(fabricante):
        print("ERROR. Nombre de fabricante inválido.")
        return

    anio_lanzamiento = input("Ingrese año de lanzamiento de la consola:\n--> ")
    if not validacion_anio_lanzamiento(anio_lanzamiento):
        print("ERROR. Año de lanzamiento no válido.")
        return

    precio = input("Ingrese precio de la consola:\n--> ")
    if not validacion_precio(precio):
        print("ERROR. Precio no válido.")
        return

    stock = input("Ingrese stock de la consola:\n--> ")
    if not validacion_stock(stock):
        print("ERROR. Stock no válido.")
        return

    consolas[sigla] = [nombre, fabricante, int(anio_lanzamiento)]

    ventas[sigla] = [float(precio), int(stock)]

#=======================================================================

def buscar_consola(sigla_buscada, consolas):
    return sigla_buscada in consolas


def opcion_buscar(consolas, ventas):
    sigla_buscada = input("Ingrese nombre de sigla de consola:\n--> ").upper().strip()
    if buscar_consola(sigla_buscada, consolas):  
        detalle_consola(consolas, ventas, sigla_buscada)
    else:
        print(f"ERROR. No existe o no está agregada la consola: {sigla_buscada}")
        return
    
    
#=======================================================================

def detalle_consola(consolas, ventas, sigla_buscada):
    nombre, fabricante, anio_lanzamiento = consolas[sigla_buscada]
    precio, stock = ventas[sigla_buscada]
    print(f"""=== Consola Encontrada ===
Sigla: {sigla_buscada}
Nombre: {nombre}
Fabricante : {fabricante}
Año lanz.: {anio_lanzamiento}
Precio : ${precio}
Stock: {stock} unidades""")


#=======================================================================

def opcion_eliminar(consolas, ventas):
    sigla_buscada = input("Ingrese nombre de sigla de consola a eliminar:\n--> ").upper().strip()
    
    if not buscar_consola(sigla_buscada, consolas):
        print(f"ERROR. No existe o no está agregada la consola: {sigla_buscada}")
        return

    detalle_consola(consolas, ventas, sigla_buscada)
    respuesta = input(f"¿Desea eliminar la consola: {sigla_buscada}? (S/N)\n--> ").upper().strip()

    if respuesta == "S":
        print(f"Eliminación de {sigla_buscada} exitosa.")
        del consolas[sigla_buscada]
        del ventas[sigla_buscada]
    elif respuesta == "N":
        print("Cancelando eliminación...")
    else:
        print("ERROR. Sigla equivocada, cancelando eliminación...")
        
#=======================================================================

def opcion_mostrar(consolas, ventas):
    if len(consolas) == 0:
        print("ERROR. No hay consolas")
        return
    contador = 0
    print("""==============================
LISTADO COMPLETO DE CONSOLAS
==============================""")
    for i in consolas:
        contador += 1
        nombre, fabricante, anio_lanzamiento = consolas[i]
        precio, stock = ventas[i]
        print(f"Sigla: {i} | {nombre} | {fabricante} | {anio_lanzamiento} | ${precio:,.2f} | Stock: {stock}")
    print(f"==============================\nTotal de consolas: {contador}")
#=======================================================================

consolas = {}
ventas = {}

while True:
    menu()
    opcion = seleccion_opcion()
    
    if opcion == 1:
        opcion_agregar(consolas, ventas)

    elif opcion == 2:
        opcion_buscar(consolas, ventas)

    elif opcion == 3:
        opcion_eliminar(consolas, ventas)

    elif opcion == 4:
        opcion_mostrar(consolas, ventas)

    elif opcion == 5:
        print("Saliendo...")
        break

    else:
        print("ERROR. Debe ingresar un número del menú.")