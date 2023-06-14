""" Aula 02 - Argumets: positional, keyword, default value """

def somar(n1, n2):
    return n1 + n2

def dividir(dividendo, divisor):
    return dividendo / divisor

# argumentos posicionais
print(somar(10,4))

# unpack list e tuplas
numeros = (6.0, 5.5)
print('somar numeros de uma lista', somar(numeros[0], numeros[1]))
print('somar numeros de uma lista', somar(*numeros)) # posiciona todos os elementos como args

# unpack de dic
numeros = {
    "n1": 20.2,
    "n2": 5.3
}

print('somar numeros de um dict', somar(**numeros))

# argumentos nomeados
print(somar(n1=10,n2=4))
print(somar(n2=10,n1=4))
print(dividir(divisor=3.0, dividendo=10.0))

# nome: saudacoes:
# parametros: nome (obrigatorio), saudacao (opcional)
# retorno: string
def saudacoes(nome, saudacao='Oi'):
    return f'{saudacao} {nome}'


print(saudacoes('Beyonce', 'Olá'))
print(saudacoes('Clara', 'Bom dia'))
print(saudacoes('Marte'))

print(saudacoes(saudacao='Oi Oi', nome='Evelynn'))
print(saudacoes(nome='Katarina'))