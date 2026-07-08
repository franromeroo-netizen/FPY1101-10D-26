def mostrar_menu():
        print("""========== MENÚ PRINCIPAL ==========
    1. Unidades por tipo de arreglo
    2. Búsqueda de arreglos por rango de precio
    3. Actualizar precio de arreglo
    4. Agregar arreglo
    5. Eliminar arreglo
    6. Salir
    =====================================""")
        
def leer_opcion():
    while True:    
        try:
            opcion = int(input("--> "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("ERROR. Ingrese un número válido.")
        except ValueError:
            print("ERROR. Ingrese un número válido.")

#========================================================

def unidades_tipo(tipo_buscado, diccionario_arreglo, diccionario_bodega):

    tipo_buscado = tipo_buscado.strip().lower()
    acumulador_stock = 0

    for cada_codigo_arreglo, lista_atributos in diccionario_arreglo.items():
        if lista_atributos[1] == tipo_buscado:

            for cada_codigo_stock, lista_bodega in diccionario_bodega.items():
                if cada_codigo_arreglo == cada_codigo_stock:

                    acumulador_stock += lista_bodega[1]
                    break

    print(f"La cantidad de arreglos de {tipo_buscado} en stock son de {acumulador_stock}")

#========================================================

def busqueda_precio(precio_minimo, precio_maximo, diccionario_bodega, diccionario_arreglos):

    lista_arreglos = []

    for cada_codigo_bodega, lista_bodega in diccionario_bodega.items():
        if precio_minimo <= lista_bodega[0] <= precio_maximo:

            for codigo_arreglos, lista_atributos_arreglos in diccionario_arreglos.items():
                if cada_codigo_bodega == codigo_arreglos:
                    
                    lista_arreglos.append(f"{lista_atributos_arreglos[0]} -- {cada_codigo_bodega}")
                    break
    
    if len(lista_arreglos) == 0:
        print("No hay arreglos en esos rangos de precios.")
    else:
        lista_arreglos.sort()

        for arreglo in lista_arreglos:
            print(arreglo)

#========================================================

def buscar_codigo(codigo_buscado, diccionario_bodega):

    for codigo_bodega in diccionario_bodega.keys():
        if codigo_buscado == codigo_bodega:
            return True
    return False

def actualizar_precio(codigo_buscado, nuevo_precio, diccionario_bodega):
    
    if not buscar_codigo(codigo_buscado, diccionario_bodega):
        return False
    else:
        diccionario_bodega[codigo_buscado][0] = nuevo_precio
        return True

#========================================================

def eliminar_arreglo(codigo_buscado, diccionario_bodega, diccionario_arreglos):

    if not buscar_codigo(codigo_buscado):
        return False
    else:
        del diccionario_arreglos[codigo_buscado]
        del diccionario_bodega[codigo_buscado]
        return True

#========================================================

arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}

bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6],
}

#========================================================

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 6:
        print("Programa finalizado.")
        break

    elif opcion == 1:
        tipo = input("Ingrese el tipo buscado:\n--> ")
        unidades_tipo(tipo, arreglos, bodega)

    elif opcion == 2:
        while True:
            try:
                p_minimo = int(input("Ingrese precio mínimo:\n--> "))
                p_maximo = int(input("Ingrese precio máximo:\n--> "))
                
                if (p_minimo < 0) or (p_minimo > p_maximo):
                    print("ERROR. Ingrese valores válidos.")
                else:
                    busqueda(p_minimo, p_maximo, bodega, arreglos)
                    break

            except ValueError:
                print("ERROR. Ingrese valores válidos.")

    elif opcion == 3:
        while True:
            while True:
                codigo = input("Ingrese código del arreglo a actualizar:\n--> ")
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio para el arreglo:\n--> "))
                    
                    if nuevo_precio >= 0:
                        break
                    else:
                        print("ERROR. Debe ingresar valores válidos.")
                except ValueError:
                    print("ERROR. Debe ingresar valores válidos.")

            actualizado = actualizar_precio(codigo, nuevo_precio, bodega)

            if actualizado == True:
                print("Precio actualizado.")
            else:
                print("El código no existe.")

            otro_precio_nuevo = input("¿Desea actualizar otro precio (s/n)?\n--> ").strip().lower()

            if otro_precio_nuevo == "s":
                break
            elif otro_precio_nuevo == "n":
                continue
            else:
                print("ERROR. Valor inválido.")
                break

    elif opcion == 4:
        print

    elif opcion == 5:
        codigo = input("Ingrese código del arreglo a eliminar:\n--> ")

        eliminado = eliminar_arreglo(codigo, bodega, arreglos)

        if not eliminado:
            print("El código no existe")
        else:
            print("Arreglo eliminado")
        