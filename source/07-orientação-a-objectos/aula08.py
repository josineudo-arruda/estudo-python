""" Aula 08 - Orientação a oo / Programando com Paulo """

# herança 
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def obtem_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    def __repr__(self):
        return f'Pessoa(nome={self.nome}, sobrenome={self.sobrenome}, cpf={self.cpf})'

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.compras = []

    def salvar_compras(self, *values):
        self.compras.extend(values)

    def __repr__(self):
        return f'Cliente(nome={self.nome}, sobrenome={self.sobrenome}, cpf={self.cpf}, compras={self.compras})'

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario - ((10/100) * self.salario)

    def __repr__(self):
        return f'Funcionario(nome={self.nome}, sobrenome={self.sobrenome}, cpf={self.cpf}, salario={self.salario})'

class Programador(Funcionario):
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus

    def calcular_pagamento(self):
        return super().calcular_pagamento() + self.bonus

    def __repr__(self):
        return f'Programador(nome={self.nome}, sobrenome={self.sobrenome}, cpf={self.cpf}, salario={self.salario}, bonus={self.bonus})'

# Teste com objetos

cliente = Cliente('Paulo', 'Kenji', '39483202')
cliente.salvar_compras('Payday', 'LeagueOfLegends', 'Valorant')
funcionario = Funcionario('Isabella', 'Mazará', '394453202', 1000)
programador = Programador('João', 'Silva', '123456789', 2000, 500)

print(cliente)
print(funcionario)
print(programador)