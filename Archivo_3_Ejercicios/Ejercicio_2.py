def leer_nota(mensaje):
    while True:
        try: 
            nota = float(input(mensaje))
            if nota >= 1.0 and nota <= 7.0:
                return nota    
            print("La nota debe estar entre 1.0 y 7.0")
        except ValueError:
            print("La nota debe ser númerica y estar entre 1.0 y 7.0")


def agregar_alumno(alumnos):

    nombre = input("Ingrese nombre del alumno: ").strip
    if nombre == "":
        print("El nombre no puede estar vacío")
        return
    
    if nombre in alumnos:
        print("El alumno ya está ingresado!!")

    if nombre.isdigit():
        print("Debe ingresar el nombre con letras")

    cantidad = int(input("Cantidad de notas: "))

    notas = []

    for i in range(cantidad):
        nota = leer_nota(f"Ingrese la nota {i+1}: ")
        notas.append(nota)

    alumnos[nombre] = notas
    print("Alumno agregado correctamente!!")

def mostrar_alumnos(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados!!")
        return
    for nombre in alumnos;i

def ver_promedios(alumnos):
    


alumnos = {
"Ana": [5.5, 6.0, 4.8],
"Luis": [3.9, 4.1, 5.0],
"Pedro": [6.5, 6.8, 7.0]
}

menu = True
while menu:
    print("""=======Menú=======
1. Agregar alumno
2. Mostrar alumnos
3. Ver promedios
4. Mejor alumno
5. Cantidad de aprobados
6. Salir""")
    while True:
        try:
            op_menu = int(input("--> "))
            break
        except ValueError:
            print("Ingrese un número válido")

    if op_menu == 1:
        agregar_alumno(alumnos)

    elif op_menu == 2:
        print(alumnos)

    elif op_menu == 3:
        ver_promedios(alumnos)

    elif op_menu == 4:
        print

    elif op_menu == 5:
        print

    elif op_menu == 5:
        menu = False

    else:
        print("Ingrese un número válido")