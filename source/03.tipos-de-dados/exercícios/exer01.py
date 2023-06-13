numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

lista_numeros = [numero1, numero2, numero3]

menor_numero = 0
maior_numero = 0

for numero in lista_numeros:
    if numero > maior_numero:
        maior_numero = numero
        menor_numero = numero
    if numero < menor_numero:
        menor_numero =  numero

print("O maior número é: ", maior_numero)
print("O menor número é: ", menor_numero)