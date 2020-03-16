'''
21. Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo,
nas posições pares os valores do primeiro e nas posições ímpares os valores do segundo.
'''
a = input("Digite 10 valores de A separados por espaço: ").split(" ")
b = input("Digite 10 valores de B separados por espaço: ").split(" ")

c = []
contador = 0
while contador < len(a):
    if contador % 2 == 0:
        c.append(a[contador])
    else:
        c.append(b[contador])
    contador += 1

print("C = ", c)