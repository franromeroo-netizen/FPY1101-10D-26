productos = {
    "Mouse" : [10, 15000],
    "Teclado" : [5, 25000],
    "Monitor" : [3, 18000]
}

print(productos["Mouse"])

dicc = {
    "rut" : "1234-5"
}

lista = [1, 2, True, "Juan"]
    #    0  1    2      3
print(lista[3])


menu = True
while menu:
    print("""====Menu====
1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Producto mas caro
5. Salir""")
    try:
        op_menu = int(input("--> "))

        if op_menu == 1:
            print

        elif op_menu == 2:
            print

        elif op_menu == 3:
            print

        elif op_menu == 4:
            print

        elif op_menu == 5:
            print("\nCerrando sesión...\n")
            menu = False

        else:
            print("\nIngrese un número válido, por favor.\n")

    except ValueError:
        print("\nIngrese un número válido, por favor.\n")