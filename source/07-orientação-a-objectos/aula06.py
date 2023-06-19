""" Aula06 - Hash e Equals """

nome1 = 'Joh'
nome2 = 'Joh'

print(nome1 == nome2)

class Pessoa:
    def __init__(self, cpf, nome):
        self.nome = nome
        self.cpf = cpf
    
    # define para o uso em coleções
    # não cria objetos considerados iguais por atributos unicos, como o cpf
    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.cpf == value.cpf
        return False

    # hash
    def __hash__(self):
        return hash(self.cpf)

    def __str__(self):
        return  f'Pessoa[nome={self.nome} cpf={self.cpf}]'

pessoa1 = Pessoa("123456789", "João")
pessoa2 = Pessoa("987654321", "Maria")
pessoa3 = Pessoa("123456789", "João")

pessoas = {pessoa1, pessoa2, pessoa3}
print(pessoas)

print(pessoa1)
print(pessoa2)
print(pessoa3)

print(pessoa1 == pessoa2)
print(hash(pessoa1))
print(hash(pessoa2))