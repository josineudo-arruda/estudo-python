class Projeto:
    def __init__(self, projeto_string):
        codigo, titulo, responsavel = projeto_string.split(',')
        self.codigo = int(codigo.strip())
        self.titulo = titulo.strip()
        self.responsavel = responsavel.strip()

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if isinstance(value, int):
            self._codigo = value
        else:
            raise ValueError("O código do projeto deve ser um número inteiro.")

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if value:
            self._titulo = value
        else:
            raise ValueError("O título do projeto não pode ser vazio.")

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, value):
        if value:
            self._responsavel = value
        else:
            raise ValueError("O responsável pelo projeto não pode ser vazio.")

    def __eq__(self, other):
        if isinstance(other, Projeto):
            return self.codigo == other.codigo
        return False

    def __repr__(self):
        return f'Projeto(codigo={self.codigo}, titulo={self.titulo}, responsavel={self.responsavel})'


projeto1 = Projeto("1,Laboratório de Desenvolvimento de Software,Pedro Gomes")
projeto2 = Projeto("2,Sistema de Controle de Estoque,Maria Silva")
projeto3 = Projeto("1,Projeto de Pesquisa em Inteligência Artificial,João Santos")
projeto4 = Projeto("3,Projeto de Pesquisa em Inteligência Artificial,Josineudo Arruda")

print(projeto1)
print(projeto2)
print(projeto3)
print(projeto4)

print(projeto1 == projeto2)
print(projeto1 == projeto3)
print(projeto4 == projeto3)