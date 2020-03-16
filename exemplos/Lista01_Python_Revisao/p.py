entrada = int(input("Digite o número para calcular o fatorial: "))

fatorial = 1
for i in range(1,entrada+1):
    fatorial *= i
    if i < entrada:
        print(f"{i}", end=" x ")
    else:
        print(i, end=" = ")

print(fatorial)