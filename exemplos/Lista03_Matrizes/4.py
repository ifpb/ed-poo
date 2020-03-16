matriz = [ [10, 2, 3, 4 ],
           [3, 9, 3, 4],
           [6, 2, 22, 4],
           [1, 2, 5, 4]]

maior_numero = 0
maior_pos = [0,0]
for linha in range(len(matriz)):
    for coluna in range(len(matriz)):
        if matriz[linha][coluna] > maior_numero:
            maior_numero = matriz[linha][coluna]
            maior_pos = [linha, coluna]

print("Maior número =", maior_numero)
print("Posição do maior =", maior_pos)