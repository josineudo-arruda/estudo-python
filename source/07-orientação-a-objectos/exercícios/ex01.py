class Aluno:
    def __init__(self, aluno_string):
        prontuario, nome, email = aluno_string.split(',')
        self.prontuario = prontuario.strip()
        self.nome = nome.strip()
        self.email = email.strip()

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, value):
        if value is not None and value.strip() != "":
            self._prontuario = value
        else:
            raise ValueError("O prontuário não pode ser vazio ou nulo.")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if value is not None and value.strip() != "":
            self._nome = value
        else:
            raise ValueError("O nome não pode ser vazio ou nulo.")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value is not None and value.strip() != "":
            self._email = value
        else:
            raise ValueError("O email não pode ser vazio ou nulo.")

    def __eq__(self, other):
        if isinstance(other, Aluno):
            return self.prontuario == other.prontuario
        return False

    def __repr__(self):
        return f'Aluno(prontuario={self.prontuario}, nome={self.nome}, email={self.email})'

aluno1 = Aluno("SP0101,João da Silva,joao@email.com")
aluno2 = Aluno("SP0102,Maria Souza,maria@email.com")
aluno3 = Aluno("SP0101,Carlos Ferreira,carlos@email.com")

print(aluno1)
print(aluno2)
print(aluno3)

print(aluno1 == aluno2)
print(aluno1 == aluno3)