""" Aula 02 - Atributos de classe e instancia """

class Pessoa:
    especie = 'Humano' # atributo de instancia

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

pessoa1 = Pessoa('Taylor', 'taylor.cat@gmail.com')
pessoa2 = Pessoa('Beyonce', 'kwolles@gmail.com')

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
pessoa1.especie = 'Alienigena'
print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)