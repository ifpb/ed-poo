'''
24. Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que não
são múltiplos de 7 ou que terminam com 7.
'''
numero = 0
vetor = []

while len(vetor) <= 100:
    if numero % 7 == 0 or str(numero).endswith("7"):
        numero += 1
        continue
    vetor.append(numero)
    numero += 1

print(vetor)