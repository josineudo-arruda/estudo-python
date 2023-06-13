notas_input = input("Digite as notas no formato 'n1, n2, n3, nm': ")

notas = notas_input.split(", ")

notas = [float(nota) for nota in notas]
media = sum(notas) / len(notas)

if media >= 6.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("Média: {:.2f}".format(media)) # O programa deve funcionar com apenas um número apos a vigula
print("Situação: {}".format(situacao))