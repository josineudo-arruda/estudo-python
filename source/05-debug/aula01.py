""" Aula 01 - Debug """
def somar(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma

def calcular_media(n1, n2, n3):
    soma = somar(n1, n2, n3)
    return soma / 3

# next parra para o próxima passo
nota1 = 10.0
nota2 = 3.0
nota3 = 4.0

#breakpoint()
media = calcular_media(nota1, nota2, nota3) # step executa linha das funções, where identifica onde esta
print(media)



