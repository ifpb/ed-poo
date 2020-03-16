notas = []

quantidade_notas = int(input("Quantas notas deseja cadastrar? "))

for i in range(1,quantidade_notas+1):
    notas.append(int(input(f"Digite a nota numero {i}: ")))

soma = 0.0
for nota in notas:
    soma += nota

media = soma / quantidade_notas

print("Média = ",media)