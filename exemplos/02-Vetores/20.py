a = input("Digite 10 valores de A separados por espaço: ").split(" ")
b = input("Digite 10 valores de B separados por espaço: ").split(" ")

if len(a) != 10 and len(b) != 10:
    print("A e B precisam ter 10 itens")
    exit(1)

c = []

for i in range(0,len(a)):
    c.append(int(a[i]) - int(b[i]))

print("A = ", a)
print("B = ", b)
print("C = ", c)