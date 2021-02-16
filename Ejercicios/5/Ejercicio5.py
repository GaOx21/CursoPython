# Pedir la cantidad en grados y convertilos en °C, °F y °K
while True:
    print("Elija en que formato ingresaras los grados:", "\n", "1) Centígrados", "\n", "2) Fahrenheit" , "\n", "c) Kelvin")
    opcion = input()
    if (int(opcion) == 1):
        print("Ingresa los grados:")
        cg = input()
        cg = float(cg)
        fh = (1.8*cg) + 32
        kv = cg + 273.15
        print(f"\t La conversión de {cg}°C a Fahrenheit es {fh}°F y la conversión a Kelvin es {kv}°K")
        break
    elif(int(opcion) == 2):
        print("Ingresa los grados:")
        fh = input()
        fh = float(fh)
        cg = (fh - 32)/1.8
        kv = (fh - 32)/1.8 + 273.15
        print(f"\"La conversión de {fh}°F a Centígrados es {cg}°C y la conversión a Kelvin es {kv}°K")
        break
    elif(int(opcion) == 3):
        print("Ingresa los grados:")
        kv = input()
        kv = float(kv)
        cg = kv - 273.15
        fh = (1.8*(kv - 273.15)) + 32
        print(f"\"La conversión de {kv}°K a Centígrados es {cg}°C y la conversión a Farenheit es {fh}°K")
        break
    else:
        print("Ingrese un valor correcto")
