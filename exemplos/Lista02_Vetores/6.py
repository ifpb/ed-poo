#6. Faça um programa que receba do usuário um vetor com 10 posições.
# Em seguida deverá ser impresso o maior e o menor elemento do vetor.

vetor = []
maior = 0
menor = 0
for i in range(10):
    entrada = int(input("Digite o número "+str(i+1)+": "))
    vetor.append(entrada)
    if i == 0:
        maior = entrada
        menor = entrada
    if entrada < menor:
        menor = entrada
    if entrada > maior:
        maior = entrada

print("Menor = ", menor)
print("Maior = ", maior)