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