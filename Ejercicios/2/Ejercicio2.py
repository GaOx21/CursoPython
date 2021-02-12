from math import pi
# Programa para calcular el área y périmetro de círculo
print("Inserté el radio del círculo")
radio = input()
radio = int(radio)
if(radio<0):
    print("Radio inválido vuelvalo a insertar")
    radio = input()
else:
    print("Radio válido")
radio = int(radio)
area = pi*(radio**2)
perimetro = 2 * pi * radio
print("El área del círculo con radio ", str(radio), " es: ", str(area))
print("El perímetro del círculo con radio ", str(radio), " es: ", str(perimetro))
