import bin_and_int
while True:
    bin_and_int.bin_and_int()
    respuesta = None
    while respuesta not in ["n", "s"]:
        respuesta = input("Quieres volver a ejecutar el programa (s/n): ")
    if respuesta.lower() == "n":
        break