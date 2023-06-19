# open("/caminho", "r")
# r - leitura
# open("/caminho", "a")
# a - incrementar
# open("/caminho", "w")
# w - escrita (limpa o arquivo e escreve novamente)
# open("/caminho", "x")
# x - criar
# open("/caminho", "r+")
# r+ - leitura e escrita

# arquivo_aberto = open("source/06-manipular-arquivos/teste3.txt", "x")

# print(arquivo_aberto.readable())
# print(arquivo_aberto.read())

# print(arquivo_aberto.readline())

# lista = arquivo_aberto.readlines()
# print(lista)

# print(lista[0])

# arquivo_aberto.write("Clarice\n")

# arquivo_aberto.close()

import os

if os.path.exists("source/06-arquivos/teste3.txt"):
    os.remove("source/06-arquivos/teste3.txt")
else:
    print("Arquivo não existe")

os.rmdir("source/06-arquivos/pasta/") # apenas se estiver vazia