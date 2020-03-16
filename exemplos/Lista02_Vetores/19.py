'''
19. Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene em um vetor com 10 posições.
Preencha um segundo vetor apenas com os números ímpares do primeiro vetor.
Imprima os dois vetores, q2 elementos por linha.
'''

numeros = []
for i in range(10):
    numero = -1
    while numero < 0 or numero > 50:
        numero = int(input(f"Digite o número {i+1}/10 de 0 a 50: "))
    numeros.append(numero)

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Pares = ")
for i in range(len(pares)-1):
    print(pares[i], end=" ")
    if i % 2 != 0:
        print("")