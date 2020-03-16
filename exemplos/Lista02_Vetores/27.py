'''
27. Faça um programa que leia dois vetores de 10 elementos.
Crie um vetor que seja a união entre os q2 vetores anteriores, ou seja,
que contém os números dos dois vetores. Não deve conter números repetidos.
'''

a = input("Digite 10 números separados por espaço: ").split(" ")
b = input("Digite 10 números separadas por espaço: ").split(" ")

if len(a) != 10 and len(b) != 10:
    print("Precisa digitar 10 itens para cada")
    exit(1)

uniao = a
for i in b:
    if i not in uniao:
        uniao.append(i)

print("União = ", uniao)