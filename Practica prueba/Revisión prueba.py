bd_estudiantes = []

def mostrar_menu():
    print("""=== MENU PRINCIPAL ===
1. Agregar estudiante
2. Buscar estudiante
3. Eliminar estudiante
4. Actualizar estados
5. Mostrar estudiantes
6. Salir""")
    
def leer_opcion():
    opcion = input("--> ")
    if opcion in ["1","2","3","4","5","6"]:
        return int(opcion)
    return False

def validar_nombre(nombre):
    if len(nombre.strip()):
        return True
    return False

def validar_edad(edad):
    if edad.isdigit() and int(edad) > 0:
        return True
    return False

def validar_nota(nota):
    try:
        numero = float(nota)
        if 1.0 <= numero <= 7.0:
            return True
        return False
    except ValueError:
        return False
    
def agregar_estudiante(bd_estudiantes):
    nombre = input("Ingresa el nombre: ")
    if validar_nombre(nombre) == False:
        print("El nombre no es válido.")
        return
    
    edad = input("Ingrese edad: ")
    if validar_edad(edad) == False:
        print("La edad no es válida.")
        return
    
    nota = input("(1.0 a 7.0)\nIngresa la nota: ")
    if validar_nota(nota) == False:
        print("Nota inválida")

    estudiante = {
        "nombre" : nombre,
        "edad" : int(edad),
        "nota" : float(nota),
        "aprobado" : False
    }
    bd_estudiantes.append(estudiante)

def buscar_estudiante(bd_estudiantes,nombre_buscado):
    for i in range(len(bd_estudiantes)):
        if bd_estudiantes[i]["nombre"] == nombre_buscado:
            return i
        return -1

def actualizar_lista(bd_estudiantes):
    for estudiante in bd_estudiantes:
        if estudiante["nota"] >= 4.0:
            estudiante["aprobado"] = True
        else:
            estudiante["aprobado"] = False

def mostrar_estudiantes(bd_estudiantes):
    actualizar_lista()
    if len(bd_estudiantes) == 0:
        print("No hay estudiantes ingresados.")
        return
    
    for mostrar_idx in range(len(bd_estudiantes)):
        if bd_estudiantes[mostrar_idx]["aprobado"]:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"
            
        print(f"""
Nombre: {bd_estudiantes[mostrar_idx]['nombre']}
Edad: {bd_estudiantes[mostrar_idx]['edad']}
Nota: {bd_estudiantes[mostrar_idx]['nota']}
Estado: {estado}
---------------------------""")
        
while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_estudiante(bd_estudiantes)

    elif opcion == 2:
        nombre = input("Ingresa el nombre a buscar: ")
        posicion = buscar_estudiante(bd_estudiantes, nombre)

        if posicion != -1:
            est = bd_estudiantes[posicion]
            print(f"""Nombre: {est["nombre"]}
Edad: {est["edad"]}
Notas: {est["nota"]}
Aprobado: {est["aprobado"]}""")
        else:
            print(f"El estudiante {nombre} no existe.")

    elif opcion == 3:
        nombre = input("Ingresa el nombre a eliminar: ")
        posicion = buscar_estudiante(bd_estudiantes, nombre)

        if posicion != -1:
            bd_estudiantes.pop[posicion]
            print(f"Estudiante {nombre} eliminado")
        else:
            print(f"No hay estudiante {nombre} por eliminar")

    elif opcion == 4:
        actualizar_lista(bd_estudiantes)

    elif opcion == 5:
        mostrar_estudiantes(bd_estudiantes)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break