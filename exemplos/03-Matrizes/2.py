matriz = [ [10, 2, 3, 4, 5 ],
           [3, 9, 3, 4, 1],
           [6, 2, 2, 4, 1],
           [1, 2, 5, 4, 1],
           [0, 2, 3, 4, 8]]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if linha == coluna:
            matriz[linha][coluna] = 0

for linha in matriz:
    print(linha)