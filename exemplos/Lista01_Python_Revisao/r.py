entrada = input("Digite a entrada: ")

def palindromo(entrada):
    p = False
    for i in range(0,len(entrada)):
        for j in reversed(range(0, len(entrada))):
            p = entrada[i] == entrada[j]
    return p

# def palindromo(entrada):
#     return entrada.lower() == entrada.lower()[::-1]

if palindromo(entrada):
    print("É palíndromo!")
else:
    print("Não é palíndromo")



