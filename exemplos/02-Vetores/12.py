# 12. Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior,
# o menor e a média dos valores.
maior = 0
menor = 9999
vetor = []
soma = 0
for i in range(5):
    entrada = int(input("Digite o número "+str(i=1)+": "))
    vetor.append(entrada)
    soma += entrada
    if entrada > maior:
        maior = entrada
    elif entrada < menor:
        menor = entrada

media = soma / 5

for i in vetor:
    print(i, end=" ")

print("Maior = ", maior)
print("Menor = ", menor)
print("Média = ", media)