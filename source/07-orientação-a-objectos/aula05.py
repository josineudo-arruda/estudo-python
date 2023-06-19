""" Aula 05 - Metodos especiais """

# __str__(self)
# representação como string, print
# __repr__(self)
# representação como string, mas pra recriar
# representação canônica

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f'Retangulo base={self.base} altura={self.altura}'
    
    # formato correto
    def __repr__(self):
        return f'Retangulo(base={self.base} altura={self.altura})'

retangulo1 = Retangulo(20.0, 4.0)
print(retangulo1)  # Exibe a representação do retângulo como string
print(repr(retangulo1))  # Exibe a representação do retângulo como string de representação

retangulo2 = Retangulo(10.0, 5.0)
print(retangulo2)
print(repr(retangulo2))