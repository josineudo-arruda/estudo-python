""" Aula 01 - introdução a funções """

# bloco de atividade que pode ser utilizada em outras pates do código (modularizar)
# função é u bloco que realiza uma tarefa especiíca
# evita duplicação de código

# 1. Standard Library Functions
# ja vem com o python
# ex: len, print

print('Olá', 123)

nomes = ['João', 'Maria']

# 2. User Defined Functions
# pelo user

# nome: saudacoes
# parametros: nenhum
# retorno: nenhum
# def saudacoes():
#     print("Olá")

# saudades()

# nome: saudacoes
# parametros: nome
# retorno: nenhum
def saudacoes(nome):
    print(f'Olá {nome}')


saudacoes('Taylor') # argumento para o parametro nome

# nome: calcular_media
# parametros: nota1, nota2
# retorno: nenhum
def calcular_media(nota1, nota2):
    print((nota1 + nota2)/2)

calcular_media(4,4)

# nome: calcular_media
# parametros: nota1, nota2
# retorno: media
def calcular_media(nota1, nota2):
    return ((nota1 + nota2)/2)

print(calcular_media(6,4))


