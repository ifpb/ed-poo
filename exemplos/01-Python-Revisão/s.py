hip = int(input("Digite a hipotenusa: "))
c1 = int(input("Digite um cateto: "))
c2 = int(input("Digite o outro cateto: "))

def triangulo_retangulo(num1, num2, num3):
    return (hip ** 2) == (c1 ** 2 + c2 ** 2)

if triangulo_retangulo(hip, c1, c2):
    print("É um triangulo retangulo")
else:
    print("Não é um triangulo retangulo")

## 5, 4, 3