#uso de diccionarios
diccionario = {
    "Rut" : "22617787-6",
    "Nombre" : "Joaquín",
    "Telefono" : [1234,567,890],
    "Dirección" : "Quilpué"
}

#te permite imprimir un valor del diccionario, entre los corchetes hay que poner el dato elegido
print(diccionario["Nombre"])
#el n*1 es para elegir el dato seleccionado, si se escoje el 2 deberia mostrar: 890
print(diccionario["Telefono"][1])

#podemos insertar datos o claves de la siguiente manera:
diccionario["Email"] = "joaqut@gmail.com"
print(diccionario["Email"])

#ingresando un número más al diccionario
diccionario["Telefono"].append(190)
print(diccionario["Telefono"])

#actualizando...
diccionario["Telefono"][0] = 666
print(diccionario["Telefono"])
diccionario["Dirección"] = "Viña del Mar"
print(diccionario)

#borrando...
del diccionario["Dirección"]
print(diccionario)
print(diccionario["Telefono"])
diccionario["Telefono"].pop(2)
print(diccionario["Telefono"])

print("listo")