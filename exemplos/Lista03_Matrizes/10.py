
matriz = []
for j in range(3):
    matriz.append(input(f"Digite três elementos da linha {j+1} da matriz 1 separada por espaço: ").split(" "))

soma_diagonal_secundaria = 0
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if coluna == len(matriz[linha])-1 - linha:
            soma_diagonal_secundaria += int(matriz[linha][coluna])

print("Soma da diagonal secundária =", soma_diagonal_secundaria)