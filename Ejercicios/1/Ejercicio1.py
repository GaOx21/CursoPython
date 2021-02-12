print("Escribe las tres calificaciones")
print("Primera calificación: ")
c1 = input()
print("Segunda calificación: ")
c2 = input()
print("Tercera calificación: ")
c3 = input()
sumacalificaciones = float(c1) + float(c2) + float(c3)
promedio = sumacalificaciones/3
print("El promedio es: " + str(promedio))
if(float(c1) >= 6 and float(c1)<=10):
    print("La primer calificación si aprobó")
elif(float(c1) < 0 or float(c1)>10):
    print("Primer calificación incorrecta")
else:
    print("La primer calificación no aprobó")
    
if(float(c2) >= 6 and float(c2)<=10):
    print("La segunda calificación si aprobó")
elif(float(c2) < 0 or float(c2)>10 ):
    print("Segunda calificación incorrecta")
else:
    print("La segunda calificación no aprobó") 
       
if(float(c3) >= 6 and float(c3)<=10):
    print("La tercer calificación si aprobó")
elif(float(c3) < 0 or float(c3)>10):
    print("Tercer calificación incorrecta")    
else:
    print("La tercer calificación no aprobó")

if(float(promedio) >= 6 and float(promedio)<=10):
    print("El promedio aprobó")
elif(float(promedio) < 0 or float(promedio)>10 ):
    print("Promedio incorrecto")    
else:
    print("El promedio no aprobó")