""" Aula 07 - Relacionametos entre classes """

class Endereco:
    def __init__(self, cep, numero):
        self.cep = cep
        self.numero = numero

    def __str__(self):
        return f'Endereco[cep={self.cep}, numero={self.numero}]'


class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f'Telefone[ddd={self.ddd}, numero={self.numero}]'


class Pessoa:
    def __init__(self, cpf, nome, telefone):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.enderecos = []

    def add_endereco(self, value):
        self.enderecos.append(value)

    def __str__(self):
        endereco_str = ', '.join(str(endereco) for endereco in self.enderecos)
        return f'Pessoa[cpf={self.cpf}, nome={self.nome}, telefone={self.telefone}, enderecos={endereco_str}]'


telefone1 = Telefone("11", "999999999")
telefone2 = Telefone("22", "888888888")

endereco1 = Endereco("12345-678", "123")
endereco2 = Endereco("98765-432", "456")

pessoa1 = Pessoa("123456789", "João", telefone1)
pessoa2 = Pessoa("987654321", "Maria", telefone2)
pessoa3 = Pessoa("445555321", "Clara", telefone2)

pessoa1.add_endereco(endereco1)
pessoa2.add_endereco(endereco2)
pessoa3.add_endereco(endereco1)
pessoa3.add_endereco(endereco2)

print(telefone1)
print(telefone2)

print(pessoa1)
print(pessoa2)
print(pessoa3)