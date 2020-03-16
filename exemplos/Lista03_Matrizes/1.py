matriz = []

for i in range(4):
    matriz.append(input(f"Digite quatro elementos da linha {i+1} da matriz separada por espaço: ").split(" "))

maiores_que_10 = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if int(matriz[i][j]) > 10:
            maiores_que_10 +=1

print("Elementos maiores que 10 na matriz:",maiores_que_10)