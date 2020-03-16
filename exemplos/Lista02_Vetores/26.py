'''
26. Faça um programa que leia dois vetores de 10 elementos.
Crie um vetor que seja a intersecção entre os q2 vetores anteriores, ou seja,
que contêm apenas os números que estão em ambos os vetores. Não deve conter números repetidos.
'''
a = input("Digite 10 números de alunos separados por espaço: ").split(" ")
b = input("Digite as alturas dos 10 alunos separadas por espaço: ").split(" ")

if len(a) != 10 and len(b) != 10:
    print("Precisa digitar 10 itens para cada")
    exit(1)

intersec = []

for i in a:
    for j in b:
        if j == i:
            intersec.append(i)

print("Intersecção = ", intersec)