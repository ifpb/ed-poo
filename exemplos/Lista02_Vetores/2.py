# q2. Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
valores = []

for i in range(6):
    valores.append(int(input("Digite o valor "+str(i+1)+": ")))

for v in valores:
    print(v)