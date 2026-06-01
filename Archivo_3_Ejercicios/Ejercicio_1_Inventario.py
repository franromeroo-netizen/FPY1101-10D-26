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

def mostrar_productos(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
    for nombre in productos:
        print(nombre, "--Stock:",productos[nombre][0],"--Precio:",productos[nombre][1])

def buscar_producto(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
    nombre = input("Nombre del producto: ").strip()

    if nombre in productos:
        print(f"""Producto encontrado!
Stock: {productos[nombre][0]}
Precio: ${productos[nombre][1]}""")
    
def producto_mas_caro(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
    
    mayor = 0
    mayor_nombre = nombre

    for nombre in productos:
        precio = productos[nombre][1]

        if precio > mayor:
            print

productos = {
    "Mouse" : [10, 15000],
    "Teclado" : [5, 25000],
    "Monitor" : [3, 18000]
}



menu = True
while menu:
    print("""\n======Menu======
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
            mostrar_productos(productos)

        elif op_menu == 3:
            buscar_producto(productos)

        elif op_menu == 4:
            producto_mas_caro(productos)

        elif op_menu == 5:
            print("Cerrando sesión...")
            menu = False

        else:
            print("Ingrese un número válido, por favor.")

    except ValueError:
        print("Ingrese un número válido, por favor.")