matriz1 = []
matriz2 = []

for j in range(4):
    matriz1.append(input(f"Digite quatro elementos da linha {j+1} da matriz 1 separada por espaço: ").split(" "))

for i in range(4):
    matriz2.append(input(f"Digite quatro elementos da linha {i+1} da matriz 2 separada por espaço: ").split(" "))

matriz_maiores = []
for linha in range(len(matriz1)):
    linha_maiores = []
    for coluna in range(len(matriz1[linha])):
        if int(matriz1[linha][coluna]) > int(matriz2[linha][coluna]):
            linha_maiores.append(matriz1[linha][coluna])
        else:
            linha_maiores.append(matriz2[linha][coluna])
    matriz_maiores.append(linha_maiores)

for linha in matriz_maiores:
    print(linha)