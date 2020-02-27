'''
25. Leia 10 números inteiros e armazene em um vetor.
Em seguida escreva os elementos que são primos e suas respectivas posições no vetor.
'''

def numero_primo(numero):
    primo = True
    for i in range(2,10*100):
        if numero != i and numero % i == 0:
            primo = False
    return primo


a = input("Digite 10 números inteiros separados por espaço: ").split(" ")
primos = []
primos_pos = []

for i in range(len(a)):
    if numero_primo(int(a[i])):
        primos.append(a[i])
        primos_pos.append(i)

print("Números primos =", primos)
print("Posição dos números primos =", primos_pos)

