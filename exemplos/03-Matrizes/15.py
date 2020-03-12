gabarito = []
for i in range(10):
    gabarito.append(input(f"Digite o gabarito da questão {i+1} (a,b,c,d,e): "))

respostas = []
matriz_resultado = []
for linha in range(3):
    print(f"Aluno {linha + 1}")
    matriz_linha = [input("Digite matricula: ")]
    nota = 0
    for coluna in range(10):
        resposta = input(f"Digite a resposta da questão {coluna+1} (a,b,c,d,e): ")
        matriz_linha.append(resposta)
        if resposta == gabarito[coluna]:
            print("Resposta correta")
            nota += 1
        else:
            print("Resposta errada")
    matriz_linha.append(nota)
    matriz_resultado.append(matriz_linha)

aprovados = 0
for linha in range(len(matriz_resultado)):
    print(f"Resultados do Aluno {linha+1}")
    print("Matrícula = ",matriz_resultado[linha][0])
    for i in range(1,10):
        print(f"Resposta da questão {i} = {matriz_resultado[linha][i]}")
    nota = matriz_resultado[linha][11]
    print("Nota = ", nota)
    if nota > 7:
        aprovados += 1

print("Percentual de aprovados = ", aprovados * 100 / 3, "%")


