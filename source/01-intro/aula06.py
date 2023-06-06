""" Aula 06 - Conversão de Tipo """

# Convsersão de tipo implícita 
leitura = 5.54
peso = 3
total = leitura * peso
print(total, type(total))

# Conversão explícita
soma = 13.5 + float('3.5')
# soma = 13.5 + float('abc')
print(soma, type(soma))

idade = int('32')
print(idade, type(idade))

idade = str(idade)
print(idade, type(idade))