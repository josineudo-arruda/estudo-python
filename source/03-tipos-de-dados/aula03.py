""" Aula 03 - Sets """

# set (conjunto)
# não ordenado
# mutáveis
# não indexáveis
# não aceitam elementos duplicados

# com {}
numeros = {
    1, 12, 5, 7, 4, 3, 3, 1
}
print(numeros, type(numeros)) # {1, 3, 4, 5, 7, 12} <class 'set'>

for numero in numeros:
    print(numero) # todos numeros

print(3 in numeros) # true
print(5054 in numeros) # false

# adicionar itens no set
print(numeros)
numeros.add(8)
print(numeros) # ele organiza

# adicionar elementos de um set em outro
print(numeros)
numeros2 = {1, 5, 4, 4, 3, 11, 9}
print(numeros2)
numeros.update(numeros2) # adiciona os elementos diferentes tp 11
print(numeros)