comprimento = float(input("Digite o comprimento do aquário (cm): "))
altura = float(input("Digite a altura do aquário (cm): "))
largura = float(input("Digite a largura do aquário (cm): "))
temperatura_desejada = float(input("Digite a temperatura desejada (°C): "))
temperatura_ambiente = float(input("Digite a temperatura ambiente (°C): "))

def calcular_volume(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

def calcular_potencia(volume, temperatura_desejada, temperatura_ambiente):
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)

def calcular_filtragem(volume):
    return volume * 2 

volume = calcular_volume(comprimento, altura, largura)
potencia = calcular_potencia(volume, temperatura_desejada, temperatura_ambiente)
filtragem = calcular_filtragem(volume)


print("Resultados:")
print(f"Volume do aquário: {volume}")
print(f"Potência do termostato necessária: {potencia}")
print(f"Quantidade de filtragem necessária: {filtragem}")