usuarios_registrados = {
    
}


def ingresar():
    
    nombre = input("Ingrese nombre de usuario: ").strip()
    
    if len(nombre) == 0:
        print("Escriba el nombre")
        return
        
    if nombre in usuarios_registrados:
        print("Escriba otro nombre, este ya está registrado")
        return


    while True:
        sexo = input("Ingrese su sexo (M o F): ").upper()

        if sexo == "M" or sexo == "F":
            break
        else:
            print("Solo puedes escribir M o F, para masculino o femenino")

    contrasena = input("Ingrese contraseña: ")

    if len(contrasena) < 8:
        print("Contraseña muy corta")
        return
    
    if "" not in contrasena:
        print("La contraseña no puede tener espacios")
        return
    
    if contrasena.isdigit() and contrasena.isalpha():
        print("La contraseña debe contener al menos 1 letra y 1 número")
        return

    usuarios_registrados[nombre] = [sexo, contrasena]

def buscar(usuarios_registrados):


    if len(usuarios_registrados) == "":
        print("No hay usuarios registrados...")

    usuario = input("Bucar usuario: ")

    if usuario in usuarios_registrados:
        print("Usuario encontrado:")
        print(usuarios_registrados[0, 1])

    

def eliminar(usuarios_registrados):
    print

opciones = {
    1: ingresar,
    2: buscar,
    3: eliminar
}

menu = True
while menu:
    print("""Menú de usuario
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
 """)
    while True:
        try:
            op_menu = int(input("--> "))
            break
        except ValueError:
            print("Ingrese un número para seleccionar")
    
    if op_menu == 4:
        print("Saliendo...")
        menu = False
    
    elif op_menu in opciones:
        i = ingresar()
        seleccion = [op_menu](i)
    
    else:
        print("Ingrese un número válido para seleccionar")