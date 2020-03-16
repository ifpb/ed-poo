matriz = [ [10, 2, 3, 4, 5 ],
           [3, 9, 3, 4, 1],
           [6, 2, 2, 4, 1],
           [1, 2, 5, 4, 1],
           [0, 2, 3, 4, 8]]

x = int(input("Digite um valor para buscar na matriz: "))

posicao = [-1,-1]
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if matriz[linha][coluna] == x:
            posicao = [linha, coluna]
            break
    else:
        continue
    break
    ## http://psung.blogspot.com/2007/12/for-else-in-python.html

if posicao == [-1, -1]:
    print("Número não encontrado")
else:
    print("A posição do elemento é: ", posicao)