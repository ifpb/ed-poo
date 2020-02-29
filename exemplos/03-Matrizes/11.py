matriz = []
for j in range(3):
    matriz.append(input(f"Digite três elementos da linha {j+1} da matriz 1 separada por espaço: ").split(" "))

transposta = []

for linha in range(len(matriz)):
    linha_transposta = []
    for coluna in range(len(matriz[linha])):
        linha_transposta.append(matriz[coluna][linha])
    transposta.append(linha_transposta)

for item in transposta:
    print(item)
