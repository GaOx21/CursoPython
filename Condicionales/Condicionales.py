# Decir si es mayor o menor de edad
edad = input("Escribe tu edad: ")
edad = int(edad)
if(edad >= 18 ):
    print("Mayor de Edad")
elif(edad < 0):
    print("Edad incorrecta")
else:
    print("Menor de edad")