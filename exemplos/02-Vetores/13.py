#13. Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e o menor valor.

pos_maior = -1
pos_menor = -1
maior = 0
menor = 9999
vetor = []
for i in range(5):
    entrada = int(input("Digite o número "+str(i+1)+": "))
    if entrada > maior:
        pos_maior = i
    elif entrada < menor:
        pos_menor = i

print("Posição do Maior = ", pos_maior)
print("Posição do Menor = ", pos_menor)
