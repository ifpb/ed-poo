#4. Faça um programa que leia um vetor de 8 posições e, em seguida,
# leia também dois valores X e Y quaisquer correspondentes a duas posições
# no vetor. Ao final, seu programa deverá escrever a soma dos valores
# encontrados nas respectivas posições X e Y.

vetor = []
for i in range(8):
    vetor.append(int(input("Digite o valor nº"+str(i+1)+": ")))

x = int(input("Digite o valor para x"))
y = int(input("Digite o valor para y"))

print("Soma dos valores de x + y = ", vetor[x]+vetor[y])