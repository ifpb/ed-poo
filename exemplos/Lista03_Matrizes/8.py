
matriz = []
for j in range(3):
    matriz.append(input(f"Digite três elementos da linha {j+1} da matriz 1 separada por espaço: ").split(" "))

soma_abaixo_diagonal = 0
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if coluna < linha:
            soma_abaixo_diagonal += int(matriz[linha][coluna])

print("Soma abaixo da diagonal principal =", soma_abaixo_diagonal)