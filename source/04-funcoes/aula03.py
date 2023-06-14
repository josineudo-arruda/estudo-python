""" Aula 03 - args, kwargs... """

# *args
# conveção 
# funciona como um envio de dados que acompanha a resposta, além de poser ser uma lista
# se utiliza args no final para enviar a quantidade que quiser

def titulos_copa(pais, *args):
    print('País: ', pais)
    for titulo in args:
        print('ano: ', titulo)

titulos_copa('Brasil', '1958', '1962', '1970', '1994', '2002')

# **kwargs 
# parecido com a ideai de *args, porém com ele é necessário keword
# porém é opcional

def calcular_preco(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value

print(calcular_preco(100.0))
print(calcular_preco(100.0, discount=5))
print(calcular_preco(100.0, discount=10, tax_percentage=7))