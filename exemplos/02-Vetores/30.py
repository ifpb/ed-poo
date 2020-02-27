''''
30. Faça um programa que leia dois números a e b (positivos menores que 10000) e:
• Crie um vetor onde cada posição e um algarismo do número. A primeira posição é
o algarismo menos significativo;
• Crie um vetor que seja a soma de a e b, mas faça-o usando apenas os vetores
construídos anteriormente.
Dica: some as posições correspondentes. Se a soma ultrapassar 10, subtraia 10 do
resultado e some 1 a próxima posição.
'''
a = input("Digite um número menor do que 10000: ")
b = input("Digite outro número menor do que 10000: ")

# tamanho 5 [1,2,3,4,5]
# tamanho 3 [7,8,9]

vetor_a = []
vetor_b = []
vetor_c = []

## Lendo cada caracter como uma posição separada do array
for i in range(len(a)):
    vetor_a.append(int(a[i]))

## Lendo cada caracter como uma posição separada do array
for i in range(len(b)):
    vetor_b.append(int(b[i]))

## Pegando o maior tamanho entre os dois
maior_tamanho = max(len(a),len(b))

## Completando zeros de A
while len(vetor_a) < maior_tamanho:
    vetor_a.insert(0,0)

# Completando zeros de B
while len(vetor_b) < maior_tamanho:
    vetor_b.insert(0,0)

print("Vetor A = ", vetor_a)
print("Vetor B = ", vetor_b)

aux = 0
## Varrendo o vetor ao contrário pra fazer a soma
for i in range(maior_tamanho-1,-1,-1):
    ## Soma aux que é a sobra da soma caso seja >= 10
    soma = vetor_a[i] + vetor_b[i] + aux

    if soma >= 10:
        vetor_c.insert(0,soma-10)
        aux = 1
    else:
        vetor_c.insert(0,soma)
        aux = 0

print("Vetor C = ", vetor_c)