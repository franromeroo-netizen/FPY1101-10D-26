import casdasda as fn


menu = True
while menu:
    print("""Menú de prueba para funciones
1. sumar
2. restar
3. salir""")
    try:
        op_menu = int(input("--> "))
    except ValueError:
        print("Ingrese un valor del 1 al 3 respectivamente")
        
    if op_menu == 1:
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese otro número: "))
        print(f"La suma de ambos números es: {fn.sumar(num1,num2)}")

    elif op_menu == 2:
        num1 = int(input("Ingrese un número: "))
        num2 = int(input("Ingrese otro número: "))
        print(f"La resta de ambos números es: {fn.restar(num1,num2)}")     

    elif op_menu == 3:
        print("saliendo")
        menu = False 
    else:
        print("Ingrese un valor del 1 al 3 respectivamente")



