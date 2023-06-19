""" Aula 01 - Intro OO """

# paradigma de programação 
# calcular area e perimetro de um retangulo
# area = base * altura
# permietro = 2 * (base + altura)

retangulo1 = {
    'base': 10.0,
    'altura': 5.0
}

retangulo2 = {
    'base': 10.0,
    'altura': 5.0
}

def calcular_area(retangulo):
    return retangulo['base'] * retangulo['altura']

def calcular_perimetro(retangulo):
    return 2 * (retangulo['base'] + retangulo['altura'])

print(calcular_area(retangulo1))
print(calcular_perimetro(retangulo1))

# classe possui métodos
# Classe Retangulo
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Retângulo 1
retangulo1 = Retangulo(10.0, 5.0)
print("Retângulo 1:")
print("Base:", retangulo1.base)
print("Altura:", retangulo1.altura)
print("Área:", retangulo1.calcular_area())
print("Perímetro:", retangulo1.calcular_perimetro())

# Retângulo 2
retangulo2 = Retangulo(20.0, 4.0)
print("\nRetângulo 2:")
print("Base:", retangulo2.base)
print("Altura:", retangulo2.altura)
print("Área:", retangulo2.calcular_area())
print("Perímetro:", retangulo2.calcular_perimetro())

