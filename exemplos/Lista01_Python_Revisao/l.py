nome1 = input("Digite o nome do primeiro produto: ")
preco1 = float(input("Digite o preço do primeiro produto: "))
nome2 = input("Digite o nome do segundo produto: ")
preco2 = float(input("Digite o preço do segundo produto: "))
nome3 = input("Digite o nome do terceiro produto: ")
preco3 = float(input("Digite o preço do terceiro produto: "))

if preco1 < preco2 and preco1 < preco3:
    print("Compre o",nome1)
elif preco2 < preco1 and preco2 < preco3:
    print("Compre o", nome2)
else:
    print("Compre o", nome3)