# 8. Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos
# na ordem inversa.
vetor = []
for i in range(6):
    vetor.append(int(input("Forneça o número: ")))

i = len(vetor)
while(i >= 0):
    print(vetor[i-1])
    i -= 1