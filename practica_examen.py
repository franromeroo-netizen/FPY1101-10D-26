def validacion_siglas_existe(sigla):
    if sigla not in consolas:
        return True
    else:
        return False
        
def validacion_siglas(sigla):
    return 2 <= len(sigla.upper().strip().isalpha()) <= 5

def validacion_nombre(nombre):
    return 3 <= len(nombre.strip().title()) <= 40

def validacion_fabricante(fabricante):
    return 2 <= len(fabricante.strip().title()) <= 30

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
        stock_int = int(stock)
        return stock_int >= 0
    except ValueError:
        return False
    

def agregar(consolas, ventas):
    sigla = input("Ingrese siglas de la consola a agregar:\n--> ").upper().strip()
    if not validacion_siglas(sigla):
        print("ERROR. Siglas inválidas.")
        return
    if not validacion_siglas_existe(sigla):
        print("ERROR. Siglas inválidas, al parecer el vehículo ya está registrado.")
        return
    
    nombre = input("Ingrese nombre de la consola a agregar:\n--> ").strip().title()
    if not validacion_nombre(nombre):
        print("ERROR. Nombre inválido.")
        return

    fabricante = input("Ingrese nombre del fabricante de la consola a agregar:\n--> ").strip().title()
    if not validacion_fabricante(fabricante):
        print("ERROR. Nombre del fabricante inválido.")
        return

    anio_lanzamiento = input("Ingrese año de lanzamiento de la consola a agregar:\n--> ")
    if not validacion_anio_lanzamiento(anio_lanzamiento):
        print("ERROR. Año inválido.")
        return

    precio = input("Ingrese el precio de la consola a agregar:\n--> ")
    if not validacion_precio(precio):
        print("ERROR. Precio inválido.")
        return

    stock = input("Ingrese el stock de la consola a agregar:\n--> ")
    if not validacion_stock(stock):
        print("ERROR. Stock inválido.")
        return
#==========================================================
   
    lista_consola = [nombre, fabricante, anio_lanzamiento]

    consola_agregada = {

        sigla : lista_consola
    }

    consolas.append(consola_agregada)
     
#==========================================================

    lista_ventas = [precio, stock]
    
    precio_stock_consola = {

        sigla : lista_ventas
    }
    ventas.append(precio_stock_consola)
            
#==========================================================
    
    

#=============================================================================================


#=============================================================================================

consolas = {}
ventas = {}

while True:
    print("""Menú Principal
1.	Agregar consola
2.	Buscar consola por sigla
3.	Eliminar consola
4.	Mostrar todas las consolas
5.	Salir""")
    try:
        opcion = int(input("--> "))
    except ValueError:
        print("ERROR. Selección inválida, ingrese nuevamente un número respectivo al menú.")

    if opcion == 1:
        agregar(consolas, ventas)

    elif opcion == 2:
        print

    elif opcion == 3:
        print

    elif opcion == 4:
        print

    elif opcion == 5:
        print("Gracias por preferirnos.\nSaliendo...")
        break

    else:
        print("ERROR. Selección inválida, ingrese nuevamente un número respectivo al menú.")