class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []

    def add_participacao(self, participacao):
        self.participacoes.append(participacao)

    def __eq__(self, other):
        if isinstance(other, Projeto):
            return self.codigo == other.codigo
        return False

    def __repr__(self):
        return f'Projeto(codigo={self.codigo}, titulo={self.titulo}, responsavel={self.responsavel}, ' \
               f'participacoes={self.participacoes})'


class Participacao:
    def __init__(self, codigo, titulo, responsavel, data_inicio, data_fim, aluno):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno

    def __repr__(self):
        return f'Participacao(codigo={self.codigo}, titulo={self.titulo}, responsavel={self.responsavel}, ' \
               f'data_inicio={self.data_inicio}, data_fim={self.data_fim}, aluno={self.aluno})'


# Exemplo de uso
projeto1 = Projeto(1, "Projeto de Coreografias", "Beyoncé")
projeto2 = Projeto(2, "Sistema de Produção Musical", "Taylor Swift")

participacao1 = Participacao(1, "Projeto de Coreografias", "Beyoncé","2023-01-01", "2023-06-30", "SP0101")
participacao2 = Participacao(2, "Projeto de Coreografias", "Beyoncé","2023-02-01", "2023-07-31", "SP0102")
participacao3 = Participacao(3, "Sistema de Produção Musical", "Taylor Swift","2023-01-01", "2023-06-30", "SP0104")
participacao4 = Participacao(4, "Sistema de Produção Musical", "Taylor Swift","2023-02-01", "2023-07-31", "SP0105")

projeto1.add_participacao(participacao1)
projeto1.add_participacao(participacao2)
projeto2.add_participacao(participacao3)
projeto2.add_participacao(participacao4)

print(projeto1)
print(projeto2)