""" Aula 02 - Tuplas """

# tuplas
# ordenadas
# imutáveis, diferente da lista
# indexáveis

# com ()
nomes = ('Maria', 'Pedro', 'João')
print(nomes, type(nomes))

# acessar os elementos
print(nomes[0])
print(nomes[0:2])

# modificar elementos (não é possível por ser imutável)
# sem append 
# nomes[0] = 'Taylor Swift'

# Iteração
for nome in nomes:
    print(nome)

print('----')

for i in range(len(nomes)):
    print(nomes[i])


nomes2 = 'Beyonce', 'Aurora', 'Katy'
print(nomes2, type(nomes2))

# unpack
# nome1 = nomes2[0]
# nome2 = nomes2[1]
# nome3 = nomes2[2]

nome1, nome2, nome3 = nomes2
print(nome1, nome2, nome3)


# Juntar duas tuplas
todos_nomes = nomes + nomes2
print(todos_nomes, type(todos_nomes))