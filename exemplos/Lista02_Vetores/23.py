'''
23. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
 representando a sua altura em metros. Encontre o aluno mais baixo e o mais alto.
 Mostre o número do aluno mais baixo e do mais alto, juntamente com suas alturas.
'''
a = input("Digite 10 números de alunos separados por espaço: ").split(" ")
b = input("Digite as alturas dos 10 alunos separadas por espaço: ").split(" ")

if len(a) != 10 and len(b) != 10:
    print("Precisa digitar 10 itens para cada")
    exit(1)

aluno_mais_alto = a[0]
aluno_mais_baixo = a[0]
maior_altura = float(b[0])
menor_altura = float(b[0])

for i in range(len(a)):
    if float(b[i]) < menor_altura:
        menor_altura = float(b[i])
        aluno_mais_baixo = a[i]

    if float(b[i]) > maior_altura:
        maior_altura = float(b[i])
        aluno_mais_alto = a[i]

print("Número do aluno mais baixo =", aluno_mais_baixo)
print("Altura do aluno mais baixo =", menor_altura)
print("Número do aluno mais alto  =", aluno_mais_alto)
print("Altura do aluno mais alto =", maior_altura)