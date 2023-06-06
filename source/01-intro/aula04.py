""" Aula 04 - Variáveis, Constantes e Literais """

# Container para guardar dados

numero = 10
print(numero, type(numero))

# int numero = 10 (não precisa)
# entende o tipo da variável com a própria variável

numero = 20.5
print(numero, type(numero))

# multiplas atribuições
# não é boa prática
nome, idade, endereco = 'Maria', 20, 'Rua Maracapa'
print(nome, idade, endereco)

# atribui o mesmo valor para várias vairáveis
# não é ponteiro
nome_01 = nome_02 = 'Carlos'
print(nome_01, nome_02)

# snake_case
id_funcionario = 209
salario_funcionario = 1000.00

# Constantes
# Uppercase

PI = 3.14
MAIORIDADE_CIVIL = 21
print(PI, MAIORIDADE_CIVIL)


# Literais 
idade = 27
print(idade)
print(27)

# Literais Numéricos
print(10, type(10))
print(10.5, type(10.5))

# Literal String
print('Maria', type('Maria'))
print("Maria", type("Maria"))
print("John's house")
print('The movie is "great"')

# Literal Booleano
print(True, type(True))
print(False, type(False))

# None
print(None, type(None))

# Coleções

#-Lista
# não é igual é array
numero = [1, 2, 3]
print(numero)

#-Tupla
emails = ('ma@gmail.com', 'ge@gmail.com')
print((emails))

#-Conjunto
nomes = {'maria', 'josão', 'maria'}
print(nomes)

#-Dicionário
aluno = {
    'prontuario': 1233456,
    'nome': 'Josineudo',
    'idade': 18
}
print(aluno)