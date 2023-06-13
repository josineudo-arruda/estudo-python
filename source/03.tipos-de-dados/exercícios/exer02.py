numero_mes = int(input("Digite o número do mês (tipo: 1 para Janeiro): "))

meses = (
    1, 'Janeiro',
    2, 'Fevereiro',
    3, 'Março',
    4, 'Abril',
    5, 'Maio',
    6, 'Junho',
    7, 'Julho',
    8, 'Agosto',
    9, 'Setembro',
    10, 'Outubro',
    11, 'Novembro',
    12, 'Dezembro'
)

for i in range(len(meses)):
    if numero_mes == meses[i]:
        print("Seu mês é", meses[i+1])