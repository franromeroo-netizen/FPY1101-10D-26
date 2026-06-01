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
        except ValueError:
            print("Ingrese un nú")