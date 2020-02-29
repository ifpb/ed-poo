# 15. Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos.

vetor = []
for i in range(20):
    entrada = int(input("Digite o número "+str(i+1)+": "))
    vetor.append(entrada)
print(vetor)
print(set(vetor))