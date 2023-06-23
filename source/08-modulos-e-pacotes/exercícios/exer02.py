import aluno, projeto, participacao

aluno1 = aluno.Aluno("SP0101,João da Silva,joao@email.com")
aluno2 = aluno.Aluno("SP0102,Maria Souza,maria@email.com")
aluno3 = aluno.Aluno("SP0101,Carlos Ferreira,carlos@email.com")

print(aluno1)
print(aluno2)
print(aluno3)

print(aluno1 == aluno2)
print(aluno1 == aluno3)

projeto1 = projeto.Projeto(1, "Projeto de Coreografias", "Beyoncé")
projeto2 = projeto.Projeto(2, "Sistema de Produção Musical", "Taylor Swift")

participacao1 = participacao.Participacao(1, "Projeto de Coreografias", "Beyoncé","2023-01-01", "2023-06-30", "SP0101")
participacao2 = participacao.Participacao(2, "Projeto de Coreografias", "Beyoncé","2023-02-01", "2023-07-31", "SP0102")
participacao3 = participacao.Participacao(3, "Sistema de Produção Musical", "Taylor Swift","2023-01-01", "2023-06-30", "SP0104")
participacao4 = participacao.Participacao(4, "Sistema de Produção Musical", "Taylor Swift","2023-02-01", "2023-07-31", "SP0105")

projeto1.add_participacao(participacao1)
projeto1.add_participacao(participacao2)
projeto2.add_participacao(participacao3)
projeto2.add_participacao(participacao4)

print(projeto1)
print(projeto2)