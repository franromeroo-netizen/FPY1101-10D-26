def agregar_producto(productos):
    nombre = input("Nombre del producto: ").strip()

    if nombre == "":
        print("El nombre no puede ser vacío")
        return
    
    if nombre in productos:
        print("¡El producto ya existe!")
        return

    stock = int(input("Ingrese stock: "))
    precio = int(input("Ingrese precio: $"))

    productos[nombre] = [stock, precio]
    print("¡Productos agregados correctamente!")


productos = {
    "Mouse" : [10, 15000],
    "Teclado" : [5, 25000],
    "Monitor" : [3, 18000]
}



menu = True
while menu:
    print("""======Menu======
1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Producto mas caro
5. Salir""")
    try:
        op_menu = int(input("--> "))

        if op_menu == 1:
            agregar_producto(productos)

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