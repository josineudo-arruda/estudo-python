def linha_dic(linha, chaves):
    valores = linha.split(',')
    dicionario = {}
    for i in range(len(chaves)):
        dicionario[chaves[i]] = valores[i]
    return dicionario

linha = "SP000001,Maria da Silva,maria@email.com"
chaves = ['prontuario', 'nome', 'email']
dicionario = linha_dic(linha, chaves)
print(dicionario)

linha_banana = "banana,3"
chaves_banana = ['item', 'quantidade']
dicionario_banana = linha_dic(linha_banana, chaves_banana)
print(dicionario_banana)