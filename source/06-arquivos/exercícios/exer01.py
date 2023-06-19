def carregar_dados(dados_arquivo):
    alunos = []
    with open(dados_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            prontuario, nome, email = linha.strip().split(',')
            aluno = {
                'prontuario': prontuario,
                'nome': nome,
                'email': email
            }
            alunos.append(aluno)
    return alunos

dados_alunos = carregar_dados('source/06-arquivos/exercícios/alunos.txt')
print(dados_alunos)