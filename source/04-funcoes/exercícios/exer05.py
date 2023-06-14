peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite a sua altura em metros: "))

individuo = {
    'altura': altura,
    'peso': peso
}

imc = calcular_imc(individuo['peso'], individuo['altura'])
classificacao = classificar_imc(imc)
situacao = verificar_situacao(imc)

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc < 25.0:
        return "Peso normal"
    elif 25.0 <= imc < 30.0:
        return "Excesso de peso"
    elif 30.0 <= imc < 35.0:
        return "Obesidade de Classe 1"
    elif 35.0 <= imc < 40.0:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

def verificar_situacao(imc):
    if imc < 18.5:
        return "Ganhar peso"
    elif 18.5 <= imc < 25.0:
        return "Normal"
    else:
        return "Perder peso"

print("Dados do indivíduo:")
for chave, valor in individuo.items():
    print(f"{chave.capitalize()}: {valor}")
print(f"Classificação: {classificacao}")
print(f"Situação: {situacao}")