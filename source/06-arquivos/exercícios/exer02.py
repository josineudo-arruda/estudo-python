def carregar_dados(dados_arquivo):
    projetos = []
    with open(dados_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            codigo, titulo, responsavel = linha.strip().split(',')
            projeto = {
                'codigo': codigo,
                'titulo': titulo,
                'responsavel': responsavel
            }
            projetos.append(projeto)
    return projetos

dados_projetos = carregar_dados('source/06-arquivos/exercícios/projetos.txt')
print(dados_projetos)