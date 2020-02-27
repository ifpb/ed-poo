# 5. Leia um vetor de 10 posições. Contar e escrever quantos
# valores pares ele possui.

vetor = []
pares = 0
for i in range(10):
    entrada = int(input("Digite o número " + str(i + 1) + ": "))
    vetor.append(entrada)
    pares += 1 if entrada % 2 == 0 else 0

print("Total de pares = ",pares)