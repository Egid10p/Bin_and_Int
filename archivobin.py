def Bin():
    print("¿Que tipo de operacion matematica quieres hacer?")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.Divicion")
    print("5.Potenciacion \n")
    #El bucle de la linea 63 se encarga de saber cual de las opciones eligio el usuario
    while True:
        try:
            condi2 = int(input("Introduce tu elección: "))
            if condi2 < 6 and condi2 > 0:
                break
            else:
                print("Error: Debe introducir una de las 5 opciones")
        except ValueError:
            print("Error: Debe introducir un valor entero")
    #Esta condición lógica se encarga de ejecutar lo que se debe ejecutar si el usuario elige la opción 1
    if condi2 == 1:
        print("========")
        print("==SUMA==")
        print("========\n")
        while True:
            try:
                numero_binario = int(input("Introduce el primer numero binario: "))
                numero_binario = str(numero_binario)
                if numero_binario.isnumeric():
                    if any([int(i) > 1 for i in numero_binario]):
                        print("Error: Debe introducir un valor binario")
                    else:
                        break
            except ValueError:
                print("Error: Debe introducir un valor binario")
        while True:
            try:
                numero_binario2 = int(input("Introduce el segundo numero binario: "))
                numero_binario2 = str(numero_binario2)
                if numero_binario2.isnumeric():
                    if any([int(i) > 1 for i in numero_binario2]):
                        print("Error: Usted debe introducir un valor binario")
                    else:
                        break
            except ValueError:
                print("Error: Debe introducir un valor binario")
        numero_binario = int(numero_binario, 2)
        numero_binario2 = int(numero_binario2, 2)
        resultado = numero_binario + numero_binario2
        resultado = bin(resultado)
        resultado = resultado.lstrip("0b")
        print(f"El resultado de la suma es {resultado}")
        #Aqui comienza otra opción
    elif condi2 == 2:
        print("=========")
        print("==RESTA==")
        print("=========\n")

        while True:
            try:
                numero_binario = int(input("Introduce el primer numero binario: "))
                numero_binario = str(numero_binario)
                if numero_binario.isnumeric():
                    if any([int(i) > 1 for i in numero_binario]):
                        print("Error: Debe introducir un valor binario")
                    else:
                        break
            except ValueError:
                print("Error: Debe introducir un valor binario")
        
        while True:
            try:
                numero_binario2 = int(input("Introduce el segundo numero binario: "))
                numero_binario2 = str(numero_binario2)
                if numero_binario2.isnumeric():
                    if any([int(i) > 1 for i in numero_binario2]):
                        print("Error: Usted debe introducir un valor binario")
                    else:
                        break
            except ValueError:
                print("Error: Debe introducir un valor binario")
        numero_binario = int(numero_binario, 2)
        numero_binario2 = int(numero_binario2, 2)
        resultado = numero_binario - numero_binario2
        resultado = bin(resultado)
        resultado = resultado.lstrip("0b")
        print(f"El resultado de la resta es {resultado}")
    #Aqui comienza otra opcion
    elif condi2 == 3:
        print("===================")
        print("==Multicplicación==")
        print("===================")
        while True:
            try:
                numero_binario = int(input("Introduce el primer numero binario: "))
                numero_binario = str(numero_binario)
                if numero_binario.isnumeric():
                    if any([int(i) > 1 for i in numero_binario]):
                        print("Error: Debe introducir un valor binario")
                    else:
                        break
            except ValueError:
                print("Error: Debe introducir un valor binario")
        
        while True:
            try:
                numero_binario2 = int(input("Introduce el segundo numero binario: "))
                numero_binario2 = str(numero_binario2)
                if numero_binario2.isnumeric():
                    if any([int(i) > 1 for i in numero_binario2]):
                        print("Error: Usted debe introducir un valor binario")
                    else:
                        break
            except ValueError:
                print("Error: Debe introducir un valor binario")
        numero_binario = int(numero_binario, 2)
        numero_binario2 = int(numero_binario2, 2)
        resultado = numero_binario * numero_binario2
        resultado = bin(resultado)
        resultado = resultado.lstrip("0b")
        print(f"El resultado de la multiplicación es {resultado}")
    elif condi2 == 4:
        print("============")
        print("==Divición==")
        print("============\n")
        while True:
            try:
                numero_binario = int(input("Introduce el primer numero binario: "))
                numero_binario = str(numero_binario)
                if numero_binario.isnumeric():
                    if any([int(i) > 1 for i in numero_binario]):
                        print("Error: Debe introducir un valor binario")
                    else:
                        break
            except ValueError:
                print("Error: Debe introducir un valor binario")
        
        while True:
            try:
                numero_binario2 = int(input("Introduce el segundo numero binario: "))
                numero_binario2 = str(numero_binario2)
                if numero_binario2.isnumeric():
                    if any([int(i) > 1 for i in numero_binario2]):
                        print("Error: Usted debe introducir un valor binario")
                    else:
                        break
            except ValueError:
                print("Error: Debe introducir un valor binario")
        numero_binario = int(numero_binario, 2)
        numero_binario2 = int(numero_binario2, 2)
        resultado = numero_binario / numero_binario2
        resultado = int(resultado)
        resultado = bin(resultado)
        resultado = resultado.lstrip("0b")
        print(f"El resultado de la divición es {resultado}")
    elif condi2 == 5:
        while True:
            try:
                numero_binario = int(input("Introduce el primer numero binario: "))
                numero_binario = str(numero_binario)
                if numero_binario.isnumeric():
                    if any([int(i) > 1 for i in numero_binario]):
                        print("Error: Debe introducir un valor binario")
                    else:
                        break
            except ValueError:
                print("Error: Debe introducir un valor binario")
        
        while True:
            try:
                numero_binario2 = int(input("Introduce el segundo numero binario: "))
                numero_binario2 = str(numero_binario2)
                if numero_binario2.isnumeric():
                    if any([int(i) > 1 for i in numero_binario2]):
                        print("Error: Usted debe introducir un valor binario")
                    else:
                        break
            except ValueError:
                print("Error: Debe introducir un valor binario")
        numero_binario = int(numero_binario, 2)
        numero_binario2 = int(numero_binario2, 2)
        resultado = numero_binario ** numero_binario2
        resultado = bin(resultado)
        resultado = resultado.lstrip("0b")
        print(f"El resultado de la potenciación es {resultado}")