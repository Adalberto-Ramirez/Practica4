def Ecuacion(x):
    print(f"Al realizar la ecuación nos da un resultado de:{(x*3+5)/2}")

while True:
    print("Bienbenido")
    print("Escribe 1 para realizar la ecuación.\n Escribe 2 para salir.\n")
    
    response = int(input(f"Elige la opción:"))
    a = int(input(f"Escribe el valor:"))


    if response == 1:
        Ecuacion(a)
    elif response == 2:
        break
    else:
        print("Opción incorrecta")