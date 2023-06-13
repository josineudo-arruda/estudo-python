""" Aula 05 - break e continue """

for i in range(10):
    if i == 4:
        break
    print(i) # 0 1 2 3

# Encontrar a posicao de um numero em uma lista de inteiros
# Caso não encontre posicao é igual a -1

busca = 7
numeros = [1, 5, 9, 7, 3, 3, 2, 1, 7]
posicao = -1 # nao encontrado

contador = 0
for numero in numeros:
    print('Procurando na posicao:', contador)
    if numero == busca:
        posicao = contador
        break
    contador += 1

print(posicao)

# continue
# Pular a iteração atual
print('-----')
for numero in numeros:
    if numero == 3:
        continue
    print(numero)