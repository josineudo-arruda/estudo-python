""" Aula 07 - Entrada e saída de dados I/O """

# saída padrão
print('Hello Wolrd', 'Maria', sep=';', end='$$$$\n')
print('Hello Wolrd', 'Maria', sep=';', end='\n\n')

# coloca no arquivo as info
arquivo = open('nome.txt', 'w', encoding='utf-8')
print('joao@gmail.com', 'maria@gmail.com', 'pedro@gmail.com', file=arquivo, sep=';')


# Entrada
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: ')) # vem como string

if idade >= 19 :
    print(f'{nome}, maior de idade')
else:
    print(f'{nome}, menor de idade')

print(nome)

# file
arquivo_notas = open('notas.txt', 'r', encoding='utf-8')
conteudo = arquivo_notas.read()
notas = conteudo.split(sep=";")

notas = [float(nota) for nota in notas]
print(notas)

media = (notas[0] + notas[1] + notas[2]) / len(notas)
print(media)