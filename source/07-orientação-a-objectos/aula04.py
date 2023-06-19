""" Aula 04 - Propriedades """

# controlar acesso com decorador property
# Classe Retangulo
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    #getter
    @property
    def base(self):
        return self._base

    #setter
    @base.setter
    def base(self, value):
        if value <= 0:
            raise ValueError("A base deve ser maior qeu zero")
        self._base = value

    #getter
    @property
    def altura(self):
        return self._altura

    #setter
    @altura.setter
    def altura(self, value):
        if value <= 0:
            raise ValueError("A base deve ser maior qeu zero")
        self._altura = value

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


retangulo1 = Retangulo(20.0, 4.0)
retangulo1.base = 30.0
print("Retângulo 1:")
print("Base:", retangulo1.base)

retangulo2 = Retangulo(10.0, 5.0)
print("\nRetângulo 2:")
print("Base:", retangulo2.base)
print("Altura:", retangulo2.altura)

retangulo2.base = 15.0
retangulo2.altura = 3.0
print("Novo valor da base:", retangulo2.base)
print("Novo valor da altura:", retangulo2.altura)
print("Área:", retangulo2.calcular_area())
print("Perímetro:", retangulo2.calcular_perimetro())