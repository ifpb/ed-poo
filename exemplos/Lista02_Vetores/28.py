'''
28. Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições com valor zero.
Para isso, todos os elementos à frente do valor zero, devem ser movidos uma posição para trás no vetor.
'''
vetor = input("Digite 15 números separados por espaço: ").split(" ")
vetor = list(map(int, vetor))

def deslocar_pra_tras(vetor, posicao_inicial):
    contador = len(vetor)
    while contador > posicao_inicial:
        vetor[contador-1] = contador
        contador -= 1

for i in range(len(vetor)):
    if int(vetor[i]) == 0:
        deslocar_pra_tras(vetor, i)

print("Vetor = ",vetor)