""" Aula 01 - Operadores """

# Operadores Aritméticos

n1 = 10.4
n2 = 3.5
resultado = n1 + n2 + 8.5

print('1 + 1', 1+1, type(1+1))
print('1.2 + 1.2', 1.2+1.2, type(1.2+1.2))
print(resultado,type(resultado))
print(3-1)
print(3*2, type(3*2))
print(3/2, type(3/2)) #converte pra float o resultado
print(3 % 2) # resto
print(10 // 3) # divisão sem resto
print(10 ** 3) # potenciação

# Operador Atribuição

x = 10.0
print(x)

# Operadores de Comparação
# resultado booleano

resultado = x > 10
print(resultado, type(resultado))

if x > 20.0:
    print('x é maior que 20')

print('10 == 10',10 == 10, type(10 == 10))
print('10 != 10',10 != 10, type(10 != 10))
print('10 > 10',10 > 10, type(10 > 10))
print('10 >= 10',10 >= 10, type(10 >= 10))
print('10 < 10',10 < 10, type(10 < 10))
print('10 <= 10',10 <= 10, type(10 <= 10))

# condicao = x > 10.0 and resultado < 3.0
# if condicao:
#     pass

# operadores Logicos

print("True and True", True and True, type(True and True))
print("True and False", True and False, type(True and False))
print("False and True", False and True, type(False and True))
print("False and False", False and False, type(False and False))

print("True or True", True or True, type(True or True))
print("True or False", True or False, type(True or False))
print("False or True", False or True, type(False or True))
print("False or False", False or False, type(False or False))

condicao = False

print('not condicao', not condicao, type(not condicao)) # true

# Operadores Especiais

# is
# == comparar se dois valores são iguais
# is verificar se as variaveis apontam para o objeto em memória em memória

a = 10
b = 10.0
c = b

print(a == b, a == c, b == c)
print(a is b, a is c, b is c) # false false true

# in
# str, list, touple, set, dic (chave)

frase = 'você é um palavrão!'
print('palavrão' in frase,type('palavrão' in frase)) # procura na frase inteira
print('Palavrão' in frase,type('palavrão' in frase))


# Mesmo comportamento para listas, tuplas e sets
numeros = [1,5,2,6]
print(1 in numeros, type(1 in numeros))

pessoa = {
    'nome': 'João',
    'idade': 20,
    'email': 'João@email.com',
}

print('nome' in pessoa, type('nome' in pessoa))