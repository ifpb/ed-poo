'''
18. Faça um programa que leia um vetor de 10 números. Leia um número x.
Conte os múltiplos de um número inteiro x num vetor e mostre-os na tela.
'''
vetor = input("Digite 10 números separados por espaço: ").split(" ")

x = int(input("Digite o número que deseja contar os múltiplos: "))

multiplos = []
for item in vetor:
    if int(item) % x == 0:
        multiplos.append(item)

print(f"Total de múltiplos de {x}: {len(multiplos)}")
print(f"Múltiplos de {x}: {multiplos}")