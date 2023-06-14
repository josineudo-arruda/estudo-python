""" Aula 05 - Dicts """

# dict (dicionário)
# coleção de key-value (chave-valor), é única
# mutável

carro = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1989
}
print(carro, type(carro))

print(carro["marca"])
print(carro.get("marca"))

# pegar todas as chaves, valores, pares
print(carro.keys())
print(carro.values())
print(carro.items())

# verifica se a chave existe
print("cor" in carro)

# adicionar chave/valor de forma dinâmica
carro["cor"] = 'Azul'
print("cor" in carro)
print(carro, type(carro))

# remove a chave
marca = carro.pop("marca")
print(marca)
print(carro)

# loop
for key in carro:
    print(key, carro[key], type(key))

for value in carro.values():
    print(value)

for key in carro.keys():
    print(key)

print(carro.items())

for key, value in carro.items():
    print(key, value)


# lista de Dicionarios

aluno1 = {
    'nome': 'Taylor',
    'email': 'taylor@email.com',
    'notas': [8.0, 5.3, 5.0]
}

aluno2 = {
    'nome': 'Beyonce',
    'email': 'beyonce@email.com',
    'notas': [2.0, 2.3, 4.0]
}

alunos = [
    aluno1, 
    aluno2
]

for aluno in alunos:
    print(aluno['nome'], aluno['email'])
    for nota in aluno['notas']:
        print(nota)