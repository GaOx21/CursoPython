from datetime import datetime
# Programa para determinar la edad de una persona conociendo el año actual y el año de nacimiento.
print("Inserte su año de nacimiento:")
by = input()
by = int(by)
now = datetime.now()
ty = now.year
ty = int(ty)
if(by>ty or by<1920):
    print("Año inválido")
    by = input()
else:
    print("Año válido")
by = int(by)
edad = ty-by
print("Su edad es: ", str(edad), " años.")
 