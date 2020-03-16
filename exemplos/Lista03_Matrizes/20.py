matriz1 = [
    [1.0, 3.0],
    [5.5, 2.0]
]

matriz2 = [
    [3.5, 0.5],
    [4.7, 8.2]
]

def somar_matrizes(matriz1, matriz2):
    matriz_soma = [ [0, 0], [0, 0]]
    for linha in range(len(matriz1)):
        for coluna in range(len(matriz1)):
            matriz_soma[linha][coluna] = matriz1[linha][coluna] + matriz2[linha][coluna]
    return matriz_soma

def substrair_matrizes(matriz1, matriz2):
    matriz_subtracao = [[0, 0], [0, 0]]
    for linha in range(len(matriz1)):
        for coluna in range(len(matriz1)):
            matriz_subtracao[linha][coluna] = matriz1[linha][coluna] - matriz2[linha][coluna]
    return matriz_subtracao

def adicionar_constante(matriz1, matriz2, constante):
    for linha in range(len(matriz1)):
        for coluna in range(len(matriz1)):
            matriz1[linha][coluna] = matriz1[linha][coluna] + constante
            matriz2[linha][coluna] = matriz2[linha][coluna] + constante
    return matriz1, matriz2

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)

sair = "n"
while(sair == "n"):
    print("Menu de opções:")
    print("(a) somar duas matrizes")
    print("(b) subtrair a primeira matriz da segunda")
    print("(c) adicionar uma constante às duas matrizes")
    print("(d) imprimir as matrizes")
    opcao = input("Digite a opção desejada: ")

    if opcao == "a":
        matriz_soma = somar_matrizes(matriz1, matriz2)
        for linha in matriz_soma:
            print(linha)

    if opcao == "b":
        matriz_subtracao = substrair_matrizes(matriz1, matriz2)
        for linha in matriz_subtracao:
            print(linha)

    if opcao == "c":
        constante = float(input("Digite a constante que deseja adicionar: "))
        matriz1, matriz2 = adicionar_constante(matriz1, matriz2, constante)
        print("Matriz 1 = ")
        imprimir_matriz(matriz1)
        print("Matriz q2 = ")
        imprimir_matriz(matriz2)

    if opcao == "d":
        print("Matriz 1 = ")
        imprimir_matriz(matriz1)
        print("Matriz q2 = ")
        imprimir_matriz(matriz2)

    sair = input("Deseja sair? (s, n)")

