def menu():
    """Muestra el menú principal en pantalla."""
    print("""=== MENU PRINCIPAL ===
1. Agregar estudiante
2. Buscar estudiante
3. Eliminar estudiante
4. Actualizar estados
5. Mostrar estudiantes
6. Salir""")

def seleccion():
    """Solicita y valida la opción seleccionada por el usuario."""
    while True:
        try:
            menu()
            op_menu = int(input("> "))
            # Valida que la opción esté en el rango correcto (1 al 6)
            if 1 <= op_menu <= 6:
                return op_menu
            else:
                print("Solo puede ingresar los números respectivos al menú. Intente nuevamente:")
        except ValueError:
            print("Solo puede ingresar los números respectivos al menú. Intente nuevamente:")

def validacion_nombre(nombre):
    """Valida que el nombre no esté vacío."""
    return len(nombre.strip().title()) > 0

def validacion_edad(edad):
    """Valida que la edad sea un número entero positivo."""
    try:
        edad_int = int(edad)
        return edad_int > 0
    except ValueError:
        return False

def validacion_nota(nota):
    """Valida que la nota sea un número flotante entre 1.0 y 7.0."""
    try:
        nota_float = float(nota)
        return 1.0 <= nota_float <= 7.0
    except ValueError:
        return False

def agregar(estudiantes):
    """Solicita los datos de un estudiante y lo agrega a la lista."""
    nombre = input("Ingrese nombre del estudiante:\n--> ")
    if not validacion_nombre(nombre):
        print("ERROR. Ingrese un nombre de estudiante válido.")
        return

    edad = input("Ingrese edad del estudiante: \n--> ")
    if not validacion_edad(edad):
        print("ERROR. Ingrese una edad válida de estudiante.")
        return

    nota = input("Ingrese nota del estudiante:\n--> ")
    if not validacion_nota(nota):
        print("ERROR. Ingrese una nota válida de estudiante.")
        return

    # Crea el diccionario del nuevo estudiante
    estudiante_agregado = {
        "nombre": nombre.strip().title(),
        "edad": int(edad),
        "nota": float(nota),
        "aprobado": False
    }
    
    estudiantes.append(estudiante_agregado)
    print(f"Estudiante {nombre.strip().title()} agregado/a con éxito.")

def buscar(estudiantes, buscado):
    """Busca a un estudiante por su nombre y retorna su índice. Si no lo encuentra, retorna -1."""
    for i in range(len(estudiantes)):
        if estudiantes[i]["nombre"] == buscado:
            return i
    return -1

def actualizar(estudiantes):
    """Actualiza el estado de aprobación de los estudiantes según su nota."""
    for actualizacion in range(len(estudiantes)):
        # En Chile se aprueba con nota mayor o igual a 4.0
        if estudiantes[actualizacion]["nota"] >= 4.0:
            estudiantes[actualizacion]["aprobado"] = True
        else:
            estudiantes[actualizacion]["aprobado"] = False

def mostrar(estudiantes):
    """Muestra la lista completa de estudiantes con sus respectivos estados."""
    actualizar(estudiantes)  # Sincroniza los estados antes de mostrar
    print("\n=== LISTA DE ESTUDIANTES ===")
    
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    for mostrar_idx in range(len(estudiantes)):
        if estudiantes[mostrar_idx]["aprobado"]:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"
            
        print(f"""
Nombre: {estudiantes[mostrar_idx]['nombre']}
Edad: {estudiantes[mostrar_idx]['edad']}
Nota: {estudiantes[mostrar_idx]['nota']}
Estado: {estado}
---------------------------""")

# --- FLUJO PRINCIPAL DEL PROGRAMA ---
estudiantes = []
repetir = True

while repetir:
    opcion = seleccion()
    
    if opcion == 1:
        agregar(estudiantes)
        
    elif opcion == 2:
        buscado = input("Ingrese nombre del estudiante a buscar:\n--> ").strip().title()
        posicion = buscar(estudiantes, buscado)
        if posicion != -1:
            print(f"Estudiante encontrado/a en la posición: {posicion}")
            print(f"Datos: {estudiantes[posicion]}")
        else:
            print("Estudiante no encontrado/a")
            
    elif opcion == 3:
        buscado = input("Ingrese nombre del estudiante a eliminar:\n--> ").strip().title()
        posicion = buscar(estudiantes, buscado)
        if posicion != -1:
            del estudiantes[posicion]
            print(f"Estudiante [{buscado}] eliminado.")
        else:
            print(f"El estudiante {buscado} no se encuentra registrado.")
            
    elif opcion == 4:
        actualizar(estudiantes)
        print("Estados de aprobación actualizados con éxito.")
        
    elif opcion == 5:
        mostrar(estudiantes)
        
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        repetir = False