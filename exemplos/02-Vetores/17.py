'''
17. Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuírem valores negativos.
'''

vetor = input("Digite 10 valores separados por espaço").split(" ")

for i in range(len(vetor)-1):
    if int(vetor[i]) < 0:
        vetor[i] = 0

print(vetor)