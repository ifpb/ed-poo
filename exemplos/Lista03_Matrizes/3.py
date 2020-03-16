matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(i * j)
    matriz.append(linha)

for linha in matriz:
    print(linha)