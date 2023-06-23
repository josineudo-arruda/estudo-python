""" Modulo e Pacotes """

# modularizar é criar modulos
# objetivo é facilitar a reutilização de codigo em diversas partes do codigo

from uteis import numeros

num=int(input("Digita um valor: "))
fat=numeros.fatorial(num)
dobro=numeros.dobro(num)
print(f'O fatorial do numero {num} é {fat}')
print(f'O dobro do numero {num} é {dobro}')

# pacote é um conjunto de funções

