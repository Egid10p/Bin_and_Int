def mate():
    print("Elegiste una operacion entre numeros enteros ahora elige entre")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.Divicion")
    print("5.Potenciacion \n")
    while True:
        try:
            comando_mates = int(input("elige aqui: "))
            if comando_mates < 6 and comando_mates > 0:
                break
            else:
                print("Error: Debe introducir una de las 5 opciones")
        except ValueError:
            print("Error: Debe introducir un valor entero")
    if comando_mates == 1:
        print("has elegido una suma, elige tus dos numeros \n")
        num_suma1 = int(input("numero uno: "))
        num_suma2 = int(input("numero dos: "))
        resultado_suma = (num_suma1 + num_suma2)
        print("el resultado de la suma es", resultado_suma)
    elif comando_mates == 2:
        print("elegiste una resta, coloca los numeros que quieres restar \n")
        num_resta1 = int(input("numero uno: "))
        num_resta2 = int(input("numero dos: "))
        resultado_resta = (num_resta1 - num_resta2)
        print("el resultado de la resta es", resultado_resta)
    elif comando_mates == 3:
        print("elegiste una multiplicación, elige que numeros quieres multiplicar \n")
        num_multi1 = int(input("numero uno: "))
        num_multi2 = int(input("numero dos: "))
        resultado_multi = (num_multi1 * num_multi2)
        print("el resultado es", resultado_multi)
    elif comando_mates == 4:
        print("elegiste hacer una divición, elige los numeros que deseas dividir \n")
        num_divi1 = int(input("numero uno: "))
        num_divi2 = int(input("numero dos: "))
        resultado_divi = (num_divi1 / num_divi2)
        print("el resultado de la divición es", resultado_divi)
    elif comando_mates == 5:
        print("elegiste potenciación, coloca los numeros que deseas \n")
        num_pot1 = int(input("numero base: "))
        num_pot2 = int(input("numero exponente: "))
        resultado_pot = (num_pot1 ** num_pot2)
        print("el resultado es", resultado_pot)