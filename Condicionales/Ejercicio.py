print("Escribe las tres calificaciones: ")
print("Primera calificación: ")
c1 = input()
print("Segunda calificación: ")
c2 = input()
print("Tercera calificación: ")
c3 = input()
sumacalificaciones = float(c1) + float(c2) + float(c3)
promedio = sumacalificaciones/3
print("El promedio es: " + str(promedio))
if(float(c1) >= 6):
    print("La primer calificación si aprobó")
elif(float(c1) < 0 ):
    print("Calificación incorrecta")
else:
    print("La primer calificación no aprobó")
    
if(float(c2) >= 6):
    print("La segunda calificación si aprobó")
elif(float(c2) < 0 ):
    print("Calificación incorrecta")
else:
    print("La segunda calificación no aprobó") 
       
if(float(c3) >= 6):
    print("La tercer calificación si aprobó")
elif(float(c3) < 0 ):
    print("Calificación incorrecta")    
else:
    print("La tercer calificación no aprobó")

if(float(promedio) >= 6):
    print("El promedio aprobó")
elif(float(promedio) < 0 ):
    print("Promedio incorrecto")    
else:
    print("El promedio no aprobó")        