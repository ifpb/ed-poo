#11. Faça um programa que preencha um vetor com 10 números reais,
# calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor.
vetor = []
negativos = 0
soma_positivos = 0.0
for i in range(10):
    entrada = float(input("Digite o número real nº "+str(i+1)+": "))
    vetor.append(entrada)
    soma_positivos += entrada if entrada >= 0 else 0
    negativos += 1 if entrada < 0 else 0

print("Total de números negativos = ", negativos)
print("Soma dos números positivos = ", soma_positivos)