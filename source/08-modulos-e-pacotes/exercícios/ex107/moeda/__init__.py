def metade(value):
    return value / 2

def dobro(value):
    return value * 2

def aumentar(value, porcentage):
    return value + (value * (porcentage / 100))

def diminuir(value, porcentage):
    return value - (value * (porcentage / 100))

def moeda(value):
    return f'R$ {value:.2f}'.replace('.', ',')