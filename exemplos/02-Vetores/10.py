# 8. Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos
# na ordem inversa.
vetor = []
for i in range(6):
    entrada = int(input("Forneça o número par nº "+str(i+1)+": "))
    while entrada % 2 > 0:
        entrada = int(input("Forneça um número par: "))
    vetor.append(entrada)

for i in reversed(vetor):
    print(i)