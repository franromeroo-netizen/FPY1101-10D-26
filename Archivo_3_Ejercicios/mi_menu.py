


calcu = True
while calcu:
    print(("""===Calculadora===
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
h. Historial de calculos
s. Salir"""))
    try:
        op_calcu = int(input("--> "))

    except ValueError:
        print("Solo puede ingresar números o 'h' o 's' para seleccionar una opción")