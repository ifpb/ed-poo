matriz = [[14, 25, 36],
          [47, 58, 69],
          [70, 81, 92]]

def criar():
    matriz = [
        ["PB", "Paraíba"],
        ["PE", "Pernambuco"]
    ]

    print(matriz)

def ler(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print(matriz[linha][coluna], end=" ")  # exibe elementos de uma linha sem quebrar
        print()  # quebra de linha


def remocao(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if coluna == len(matriz) - 1:
                matriz[linha].remove(matriz[linha][coluna])

    ler(matriz)


def insercao(matriz):
    fixo = int(input("Digite um valor: "))

    for linha in matriz:
        linha.append(fixo)

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print(matriz[linha][coluna], end=" ")
        print()

