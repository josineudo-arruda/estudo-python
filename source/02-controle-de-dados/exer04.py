identificador = input("Digite o identificador de funcionário: ")
erros = []

if not identificador.startswith("BR"):
    erros.append("O identificador não inicia com a sequência 'BR'")

if not identificador.endswith("X"):
    erros.append("O identificador não finaliza com o caractere 'X'")

numero = identificador[2:6]

if not (numero.isdigit() and 1 <= int(numero) <= 9999):
    erros.append("O identificador não apresenta um número inteiro entre 0001 e 9999")

if erros:
    print("Identificador inválido. Erros encontrados:")
    for erro in erros:
        print("- " + erro)
else:
    print("Identificador válido")