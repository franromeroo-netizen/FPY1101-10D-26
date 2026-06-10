def ingresar():
    
    nombre = input("Ingrese nombre de usuario: ").strip()
    
    if len(nombre) == 0:
        print("Escriba el nombre")
        return
        
    if nombre in usuarios_registrados:
        print("Escriba otro nombre, este ya está registrado")
        return


    
    sexo = input("Ingrese su sexo (M o F): ").upper()

    if sexo != "M" and sexo != "F":
        print("Solo puedes escribir M o F, para masculino o femenino")
        return

    contrasena = input("Ingrese contraseña: ")

    letras = 0
    digitos = 0
    for foo in contrasena:
        if foo.isdigit():
            digitos += 1

        if foo.isalpha():
            letras += 1

    if digitos < 1 and letras < 1:
        print("La contraseña debe tener al menos 1 letra y 1 número")
        return

    if len(contrasena) < 8:
        print("Contraseña muy corta")
        return
        
    if " " in contrasena:
        print("La contraseña no puede tener espacios")
        return
    

    usuarios_registrados[nombre] = {
        "sexo": sexo,
        "contraseña": contrasena
    }

def buscar():

    if len(usuarios_registrados) == 0:
        print("No hay usuarios registrados...")
        return

    usuario = input("Buscar usuario: ").strip()

    if usuario in usuarios_registrados:
        datos = usuarios_registrados[usuario]
        print(f"""Usuario encontrado:
Usuario: {usuario}
Sexo: {datos['sexo']}
Contraseña: {datos['contraseña']}""")
    else:
        print("Usuario no encontrado")
        return

    

def eliminar():
    
    if len(usuarios_registrados) == 0:
        print("No hay usuarios registrados para eliminar...")
        return

    usuario = input("Ingrese el nombre del usuario a eliminar: ").strip()

    if usuario in usuarios_registrados:
        del usuarios_registrados[usuario]
        print(f"Usuario '{usuario}' eliminado correctamente.")
    else:
        print("El usuario no existe.")


#Diccionarios

usuarios_registrados = {}

opciones = {
    1: ingresar,
    2: buscar,
    3: eliminar
}

#Menú

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
        opciones[op_menu]()
    
    else:
        print("Ingrese un número válido para seleccionar")