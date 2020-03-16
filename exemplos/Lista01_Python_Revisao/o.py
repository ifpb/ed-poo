inicio = int(input("Início da sequência: "))
termino = int(input("Término da sequência: "))

for i in range(inicio, termino+1):
    if i < termino:
        print(i ** 2, end=", ")
    else:
        print(i ** 2, end="")