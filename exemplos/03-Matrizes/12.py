import random

matriz = []

for linha in range(4):
    linha = []
    for coluna in range(4):
        linha.append(random.randrange(1,20))
    matriz.append(linha)

print("Original = ")
for linha in matriz:
    print(linha)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if coluna > linha:
            matriz[linha][coluna] = 0
            
print("Transformada = ")
for linha in matriz:
    print(linha)

