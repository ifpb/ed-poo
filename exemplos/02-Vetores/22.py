'''
22. Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles.
Os conjuntos tem 5 elementos cada. Imprimir os dois conjuntos e o  produto escalar,
sendo que o produto escalar é dado por:  x1 ∗ y1 + x2 ∗ y2 + ... + xn ∗ yn.
'''
a = input("Digite 5 valores reais de A separados por espaço: ").split(" ")
b = input("Digite 5 valores reais de B separados por espaço: ").split(" ")


if len(a) != 5 and len(b) != 5:
    print("A e B precisam ter 5 itens")
    exit(1)

print("A =", a)
print("B =", b)

produto_escalar = 0.0
for i in range(len(a)):
    produto_escalar += float(a[i]) * float(b[i])

print("Produto Escalar =", produto_escalar)