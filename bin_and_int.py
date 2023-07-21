def bin_and_int():
    import archivoint
    import archivobin
    #El codigo de la linea 2 a la 4 es el titulo del programa
    print("=============")
    print("=Bin and Int=")
    print("=============\n")
    #Esto le da al usario 3 opciones a elegir
    print("Quieres")
    print("1.Convertir numeros enteros a numeros binarios")
    print("2.Convertir numeros binarios a numeros enteros")
    print("3.Quieres hacer operaciones matematicas con numeros binarios")
    print("4.Quieres hacer operaciones matematicas con numeros enteros \n")

    #Este bucle se encarga de que si hay algun error sepa como controlarlo el bucle continua hasta la linea 22
    while True:
        try:
            #La linea de abajo le pide al usuario que introdusca el numero de una opción
            condi = int(input("Escribe el numero de la opción para elegirla: "))
            #La siguiente linea es una condicion lógica
            if condi <= 4 and condi >= 1:
                break
            else:
                print("Error: Debe ingrasar un valor de 1 o 4")
        except ValueError:
            print("Error: Debe ingresar un numero entero")

    #Esta linea ejecuta lo que se debe ejecutar en la opción 1
    if condi == 1:
        while True:
            try:
                numero_entero = int(input("Introduce un numero entero: "))
                break
            except ValueError:
                print("Error: Usted debe ingresar un numero entero")
        numero_binario = bin(numero_entero)
        numero_binario = numero_binario.lstrip("0b")
        print(f"{numero_entero} en binario es igual a {numero_binario}")

    #Esta es otra condición lógica que se encarga de ejucutar lo que le corresponde a la opcion 2
    elif condi == 2:
        while True:
            try:
                numero_binario = int(input("Introduce un numero binario: "))
                numero_binario = str(numero_binario)
                if numero_binario.isnumeric():
                    #La linea de codigo 44 se encarga de saber si el numero ingrasado es binario
                    if any([int(i) > 1 for i in numero_binario]):
                        print("Error: Debe introducir un valor binario")
                    else:
                        break
            except ValueError:
                print("Error: Debe introducir un valor binario")
        numero_entero = int(numero_binario, 2)
        print(f"{numero_binario} es igual a {numero_entero}")

    #La linea 54 es otra condicion lógica
    elif condi == 3:
        archivobin.Bin()
    elif condi == 4:
        archivoint.mate()