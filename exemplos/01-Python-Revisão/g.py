def calculo1(num1, num2):
    return (num1 * 2) * (num2 / 2)

def calculo2(num1, num3):
    return (num1 * 3) + num3

def calculo3(num3):
    return num3 ** 3;

x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))
z = float(input("Digite um número real: "))

print(f"Cálculo 1 = {calculo1(x,y)}")
print(f"Cálculo 2 = {calculo2(x,z)}")
print(f"Cálculo 3 = {calculo3(z)}")

