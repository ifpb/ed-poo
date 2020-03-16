
matriz = []
for j in range(3):
    matriz.append(input(f"Digite três elementos da linha {j+1} da matriz 1 separada por espaço: ").split(" "))

soma_acima_diagonal = 0
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if coluna > linha:
            soma_acima_diagonal += int(matriz[linha][coluna])

print("Soma acima da diagonal principal =", soma_acima_diagonal)