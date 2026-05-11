DEUDA = 100000

i = True
while i:
    print("""Menú
1. Pago deuda Tarjeta de crédito
2. Simulación de compras
3. Salir""")
    op_menu = int(input("--> "))

    if op_menu == 1:
        monto = int(input("Ingrese Monto para pagar deuda\n--> "))
        if monto > 100000:
            print("El monto excede la deuda, felicidades")
        elif monto == 100000:
            print("El monto paga la deuda, felicidades")
        

    elif op_menu == 2:
        print

    elif op_menu == 3:
        i = False

    else:
        print("Opción equivocada, ingrese uno de los números en las opciones")

