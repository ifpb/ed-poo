#7. Escreva um programa que leia 10 números inteiros e os armazene em um vetor.
# Imprima o vetor, o maior elemento e a posição que ele se encontra.

vetor = []
maior = 0
maior_pos = -1
menor = 9999
menor_pos = -1
for i in range(10):
    entrada = int(input("Digite o número "+str(i+1)+": "))
    vetor.append(entrada)
    if entrada < menor:
        menor = entrada
        menor_pos = i
    if entrada > maior:
        maior = entrada
        maior_pos = i

print("Menor = ", menor)
print("Posição do Menor = ", menor_pos)
print("Maior = ", maior)
print("Posição do Maior= ", maior_pos)