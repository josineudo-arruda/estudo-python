numero_mes = int(input("Digite o número do mês (tipo: 1 para Janeiro): "))

meses = (
    {
        'numero_mes': 1,
        'nome_mes': 'Janeiro'
    },
    {
        'numero_mes': 2,
        'nome_mes': 'Fevereiro'
    },
    {
        'numero_mes': 3,
        'nome_mes': 'Março'
    },
    {
        'numero_mes': 4,
        'nome_mes': 'Abril'
    },
    {
        'numero_mes': 5,
        'nome_mes': 'Maio'
    },
    {
        'numero_mes': 6,
        'nome_mes': 'Junho'
    },
    {
        'numero_mes': 7,
        'nome_mes': 'Julho'
    },
    {
        'numero_mes': 8,
        'nome_mes': 'Agosto'
    },
    {
        'numero_mes': 9,
        'nome_mes': 'Setembro'
    },
    {
        'numero_mes': 10,
        'nome_mes': 'Outubro'
    },
    {
        'numero_mes': 11,
        'nome_mes': 'Novembro'
    },
    {
        'numero_mes': 12,
        'nome_mes': 'Dezembro'
    }
)

for i in range(len(meses)):
    if numero_mes == meses[i]['numero_mes']:
        print("Seu mês é", meses[i]['nome_mes'])