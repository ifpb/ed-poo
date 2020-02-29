# 12. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior,
# o menor e a média dos valores.
maior = 0
menor = 0
vetor = []
soma = 0
for i in range(5):
    entrada = int(input("Digite o número "+str(i+1)+": "))
    vetor.append(entrada)
    if i == 0:
        maior = entrada
        menor = entrada
    soma += entrada
    if entrada > maior:
        maior = entrada
    elif entrada < menor:
        menor = entrada

media = soma / len(vetor)

for i in vetor:
    print(i, end=" ")

print("\nMaior = ", maior)
print("Menor = ", menor)
print("Média = ", media)