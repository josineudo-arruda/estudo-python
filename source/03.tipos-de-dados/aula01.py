""" 01 - Lista """

# listas
# ordenadas
# mutáveis
# indexaveis, acessar posição etc

nomes = []
print(nomes, type(nomes)) # vazio

# criação de lista
nomes = ['Maria', 'Pedro', 'João']
print(nomes, type(nomes))
print(nomes[0:2])
print(nomes[1:])

print(len(nomes)) # tamanho

nomes.append('Marta Gomes')
print(nomes) # final

nomes.insert(0, 'Marta Gomes')
print(nomes) # começo

nomes2 = ['Caio Silva', 'Carlos Gomes']
print(len(nomes))
nomes.extend(nomes2)
print(len(nomes))
print(nomes)

# remover

nomes.remove('Marta Gomes')
print(nomes)

# del

del nomes[0]
print(nomes)

# remove da memória
# del nomes

# limpar a lista com clear
nomes.clear()
print(nomes)

# iteração em lista
for nome in nomes:
    print(nome)

print('----')

for i in range(len(nomes)):
    print(nomes[i])