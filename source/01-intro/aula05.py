""" Aula 05 - Tipos de dados """

# Númericos
# int, float

idade = 20
peso = 70.5

print(idade, type(idade))
print(peso, type(peso))

# String
nome = 'João'
sobrenome = 'Silva'
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

produto = 'Coca-cola'
print(f'O CLiente {nome} {sobrenome} comprou o produto {produto}')

# Captar letra
print(nome[0], nome[-1])

print(nome.lower())
print(nome.upper())

print(nome, sobrenome)
print(1, 2, sep='XXXXXX')

# Boolean
ligado = True
print(ligado)

resultado = 10 < 3
print(resultado)

# listas
frutas = ['banana', 'laranja']
print(frutas[0])
print(frutas[1])

frutas[0] = 'banana nanica'
print(frutas)
print(len(frutas))

for fruta in frutas:
    print(fruta.upper())

# Tupla
codigos = ('SP1', 'SP2', 'SP3')
# codigos[2] =  'SP4' # não da

# Conjuntos
resultado_sorteio = [10, 3, 5, 7, 3]
resultado_sorteio = {10, 3, 5, 7, 3} # sem repetir

resultado_sorteio.add(23)

#dicionário
funcionario = {
    'codigo': 123,
    'nome': 'Maria da Silva'
}

print(funcionario)
print(funcionario['codigo'])

print(funcionario.keys())
print(funcionario.values())