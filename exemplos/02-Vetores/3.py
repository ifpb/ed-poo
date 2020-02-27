# 3. Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado dos componentes deste vetor,
# armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.

vetor1 = []
vetor2 = []
for i in range(10):
    entrada = float(input("Digite o número nº"+str(i+1)+": "))
    vetor1.append(entrada)
    vetor2.append(entrada ** 2)

print("***** Vetor 1: *****")
for e in vetor1:
    print(e, end=", ")

print("***** Vetor 2: *****")
for e in vetor2:
    print(e)
