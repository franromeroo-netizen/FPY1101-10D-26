pera = "pera"
manzana = "manzana"
naranja = "naranja"

frutas = [pera,manzana,naranja]
#           0     1      2
print(frutas[0])

print("\n")

for i in range(3):
    print(frutas[i])

print("\n")

for i in frutas:
    print(i)

frutas.append("frutilla") #Agregar el elemento al final

print("\n",frutas)

frutas.append(2356) #Agregar el elemento al final

print("\n",frutas)


frutas.insert(1,1234)
print("\n",frutas)

frutas.remove(1,1234)
print("\n",frutas)