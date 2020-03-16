import random

cartela = []
numeros_gerados = []

for linha in range(5):
    cartela_linha = []
    for coluna in range(5):
        numero = random.randrange(0, 99)
        while numero in numeros_gerados:
            numero = random.randrange(0, 99)
        numeros_gerados.append(numero)
        cartela_linha.append(numero)
    cartela.append(cartela_linha)

print("Cartela = ")
for linha in cartela:
    print(linha)