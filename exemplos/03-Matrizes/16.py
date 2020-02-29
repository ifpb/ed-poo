notas = []

for i in range(10):
    print(f"Aluno {i+1}")
    linha = []
    pior_nota = 0
    for j in range(3):
        nota = float(input(f"Digite a nota {j+1}: "))
        if j == 0:
            pior_nota = nota
        linha.append(nota)
        if nota < pior_nota:
            pior_nota = nota
    linha.append(pior_nota) #pior nota como posição 3 da matriz
    notas.append(linha)

print("Quadro de notas:")
for linha in notas:
    print(linha)

nota_mais_baixa = [0,0,0] #posição 0 = 1, 1 = 2, 2 = 3
for linha in range(len(notas)):
    if notas[linha][3] == 1.0: # coluna 3 = pior nota
        nota_mais_baixa[0] += 1
    elif notas[linha][3] == 2.0:
        nota_mais_baixa[1] += 1
    elif notas[linha][3] == 3.0:
        nota_mais_baixa[2] += 1

for i in range(3):
    print(f"Alunos cuja nota mais baixa foi {i+1}: {nota_mais_baixa[i]}")