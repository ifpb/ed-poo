matriz = [[]]
for j in range(3):
    matriz.append(input(f"Digite três elementos da linha {j+1} da matriz 1 separada por espaço: ").split(" "))

soma = [0,0,0]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        soma[coluna] += int(matriz[linha][coluna])

print(soma)