# ========================================================
# 1. FUNCIONES DEL SISTEMA
# ========================================================

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
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

# --- Opción 1 ---
def unidades_tipo(tipo_buscado, diccionario_arreglo, diccionario_bodega):
    tipo_buscado = tipo_buscado.strip().lower()
    acumulador_stock = 0

    for cada_codigo_arreglo, lista_atributos in diccionario_arreglo.items():
        # Validamos el tipo sin importar mayúsculas/minúsculas
        if lista_atributos[1].lower() == tipo_buscado:
            # Acceso directo por clave (más eficiente que un segundo for)
            if cada_codigo_arreglo in diccionario_bodega:
                acumulador_stock += diccionario_bodega[cada_codigo_arreglo][1]

    print(f"Total de unidades para el tipo '{tipo_buscado}': {acumulador_stock}")

# --- Opción 2 ---
def busqueda_precio(p_min, p_max, diccionario_bodega, diccionario_arreglos):
    lista_arreglos = []

    for cada_codigo_bodega, lista_bodega in diccionario_bodega.items():
        precio = lista_bodega[0]
        unidades = lista_bodega[1]
        
        # El precio debe estar en rango Y debe haber unidades disponibles (unidades > 0)
        if p_min <= precio <= p_max and unidades > 0:
            if cada_codigo_baodega in diccionario_arreglos:
                nombre_arreglo = diccionario_arreglos[cada_codigo_bodega][0]
                lista_arreglos.append(f"{nombre_arreglo}--{cada_codigo_bodega}")
    
    if len(lista_arreglos) == 0:
        print("No hay arreglos en ese rango de precios.")
    else:
        lista_arreglos.sort()
        for arreglo in lista_arreglos:
            print(arreglo)

# --- Opción 3 y 5 (Auxiliar) ---
def buscar_codigo(codigo_buscado, diccionario_bodega):
    # La búsqueda se hace en mayúsculas para que sea insensible
    return codigo_buscado.upper().strip() in diccionario_bodega

def actualizar_precio(codigo_buscado, nuevo_precio, diccionario_bodega):
    codigo_buscado = codigo_buscado.upper().strip()
    if not buscar_codigo(codigo_buscado, diccionario_bodega):
        return False
    else:
        diccionario_bodega[codigo_buscado][0] = nuevo_precio
        return True

# --- Opción 5 ---
def eliminar_arreglo(codigo_buscado, diccionario_bodega, diccionario_arreglos):
    codigo_buscado = codigo_buscado.upper().strip()
    if not buscar_codigo(codigo_buscado, diccionario_bodega):
        return False
    else:
        del diccionario_arreglos[codigo_buscado]
        del diccionario_bodega[codigo_buscado]
        return True

# ========================================================
# 2. DICCIONARIOS INICIALES
# ========================================================

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

# ========================================================
# 3. PROGRAMA PRINCIPAL (MENÚ)
# ========================================================

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
                
                if p_minimo < 0 or p_maximo < 0 or p_minimo > p_maximo:
                    print("Debe ingresar valores enteros válidos (mínimo <= máximo).")
                else:
                    busqueda_precio(p_minimo, p_maximo, bodega, arreglos)
                    break
            except ValueError:
                print("Debe ingresar valores enteros")

    elif opcion == 3:
        procesando = True
        while procesando:
            codigo = input("Ingrese código del arreglo a actualizar:\n--> ")
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio para el arreglo:\n--> "))
                if nuevo_precio <= 0:
                    print("ERROR. Debe ingresar un valor mayor a cero.")
                    continue
            except ValueError:
                print("ERROR. Debe ingresar un número entero.")
                continue

            # El programa principal decide qué imprimir según el booleano devuelto
            if actualizar_precio(codigo, nuevo_precio, bodega):
                print("Precio actualizado.")
            else:
                print("El código no existe.")

            # Bucle secundario para validar exclusivamente el (s/n)
            while True:
                otro = input("¿Desea actualizar otro precio (s/n)?\n--> ").strip().lower()
                if otro == "s":
                    break # Rompe este bucle pequeño para continuar en el bucle 'procesando'
                elif otro == "n":
                    procesando = False # Apaga el bucle principal de la opción 3
                    break
                else:
                    print("ERROR. Valor inválido. Ingrese 's' o 'n'.")

    elif opcion == 4:
        # TODO: Aquí va tu desarrollo del Punto 4
        print("Opción en desarrollo por el estudiante...")

    elif opcion == 5:
        codigo = input("Ingrese código del arreglo a eliminar:\n--> ")

        # El programa principal decide qué imprimir basándose exclusivamente en el booleano
        if eliminar_arreglo(codigo, bodega, arreglos):
            print("Arreglo eliminado")
        else:
            print("El código no existe")