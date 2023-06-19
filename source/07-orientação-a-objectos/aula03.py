""" aula 03 - Métodos de classe """

# classe possui métodos
# Classe Retangulo
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # decorator 
    @classmethod
    def from_list(cls, lista):
        return cls(lista[0], lista[1])

    @classmethod
    def from_string(cls, rep_retangulo):
        base, altura = rep_retangulo.split(sep=',')
        return cls(float(base), float(altura))

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
retangulo2 = Retangulo.from_list([13.0, 4.0])
print("Retângulo 2:")
print("Base:", retangulo2.base)
print("Altura:", retangulo2.altura)
print("Área:", retangulo2.calcular_area())
print("Perímetro:", retangulo2.calcular_perimetro())

# Retângulo 3
retangulo3 = Retangulo.from_string('13.0, 4.0')
print("Retângulo 3:")
print("Base:", retangulo3.base)
print("Altura:", retangulo3.altura)
print("Área:", retangulo3.calcular_area())
print("Perímetro:", retangulo3.calcular_perimetro())