def calcular():
    while True:
        try:
            num1 = float(input("Introduzca los números a calcular:\n--> "))
            num2 = float(input("--> "))
            return num1, num2
        except ValueError:
            print("Ingrese no número válido")
    

def sumar(num1,num2):
    
    return num1 + num2

def restar(num1,num2):
    
    return num1 - num2
    

def multiplicar(num1,num2):
    
    return num1 * num2
    
def dividir(num1,num2):
    
    if num2 == 0:
        return "¡Error! No dividir entre cero."
    return num1 / num2


operaciones = {
    1: sumar,
    2: restar,
    3: multiplicar,
    4: dividir
}


menu = True
while menu:
    print("""Calculadora por terminal
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir""")
    while True:
        try:
            op_calcu = int(input("--> "))
            break
        except ValueError:
            print("Ingrese solo números para calcular")

    if op_calcu == 5:
        print("¡Hasta luego!")
        menu = False

    elif op_calcu in operaciones:
        num1, num2 = calcular()

        resultado = operaciones[op_calcu](num1, num2)

        print(f"El resultado es: {resultado}")

    else:
        print("Ingrese solo números ya mencionados para calcular")