#Declarar un arreglo
print("Arreglo Original")
arreglo = ["Si" , 1 , 121.32 , False , "Hola" , True , 3 , 2]
for item in arreglo:
    print(item)
arreglo[0] = "México"
arreglo[1] = 123
arreglo[2] = -23.21321 
arreglo[3] = True
arreglo[4] = "Sabritas"
arreglo[5] = False
arreglo[6] = 321-123
arreglo[7] = 23*232 
#Sangría o Identación
print("Nuevo Arreglo")
for item in arreglo:
    print(item)

print(type(arreglo))