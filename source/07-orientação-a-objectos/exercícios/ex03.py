class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    def __eq__(self, other):
        if isinstance(other, Projeto):
            return self.codigo == other.codigo
        return False

    def __repr__(self):
        return f'Projeto(codigo={self.codigo}, titulo={self.titulo}, responsavel={self.responsavel})'


class Participacao(Projeto):
    def __init__(self, codigo, titulo, responsavel, data_inicio, data_fim, aluno):
        super().__init__(codigo, titulo, responsavel)
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno

    def __repr__(self):
        return f'Participacao(codigo={self.codigo}, titulo={self.titulo}, responsavel={self.responsavel}, ' \
               f'data_inicio={self.data_inicio}, data_fim={self.data_fim}, aluno={self.aluno})'


projeto1 = Projeto(1, "Projeto de Coreografias", "Beyoncé")
projeto2 = Projeto(2, "Sistema de Produção Musical", "Taylor Swift")
projeto3 = Projeto(3, "Pesquisa em Performance Vocal", "Katy Perry")

participacao1 = Participacao(1, "Projeto de Coreografias", "Beyoncé","2023-01-01", "2023-06-30", "SP0101")
participacao2 = Participacao(2, "Sistema de Produção Musical", "Taylor Swift","2023-02-01", "2023-07-31", "SP0102")
participacao3 = Participacao(3, "Pesquisa em Performance Vocal", "Katy Perry","2023-01-01", "2023-06-30", "SP0103")

print(projeto1)
print(projeto2)
print(projeto3)

print(participacao1)
print(participacao2)
print(participacao3)