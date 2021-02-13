# Programa para saber si un número es par o impar
print("Inserte su número entero: ")
numero = input()
comparador = int(numero)%2
if(comparador == 1):
    print("El número: " , numero, " es impar.")
else:
    print("El número: ",numero, " es par.")