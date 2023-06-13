identificador = input("Digite o identificador de funcionário: ")

if len(identificador) == 7 and identificador.startswith("BR") and identificador.endswith("X"):
    numero = identificador[2:6]
    if numero.isdigit() and 1 <= int(numero) <= 9999:
        print("Identificador válido")
    else:
        print("Identificador inválido")
else:
    print("Identificador inválido")