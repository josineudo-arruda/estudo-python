arq = open("source/06-manipular-arquivos/arquivo.txt", "w")

string = "Ola Taylor\n"
lista = ["Ola ", "mini ", "querido\n"]
arq.write(string)
arq.writelines(lista)

arq.close()

with open("source/06-manipular-arquivos/arquivo.txt", "w") as arqs:
    arqs.write("teste")