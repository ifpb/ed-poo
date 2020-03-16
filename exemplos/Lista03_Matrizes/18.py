# matriz_entrada = [
#     [100, 7.0, 6.0, 6.5],
#     [101, 7.0, 6.0, 6.5],
#     [102, 7.0, 7.0, 7.0],
#     [103, 7.0, 6.0, 6.5],
#     [104, 7.0, 6.0, 6.5],
# ]
matriz_entrada = []
for j in range(5):
    matriz_entrada.append(input(f"Digite quatro elementos da linha {j+1} separada por espaço: ").split(" "))

def ler_tres_primeiras_informacoes(matriz_entrada):
    return map(lambda item: item[0:3], matriz_entrada)

def calcular_nota_final(matriz_entrada):
    nota_final = []
    for item in matriz_entrada:
        linha = []
        linha.append(item[0]) # matricula
        linha.append(item[1]+item[2])
        nota_final.append(linha)
    print("Nova nota final")
    print(nota_final)
    return nota_final

def matricula_maior_nota_final(matriz_entrada):
    notas_finais = calcular_nota_final(matriz_entrada)
    maior_nota = 0.0
    maior_nota_matricula = 0
    for linha in range(len(notas_finais)):
        if float(notas_finais[linha][1]) > maior_nota:
            maior_nota = float(notas_finais[linha][1])
            maior_nota_matricula = int(notas_finais[linha][0])

    print(f"Matrícula de maior nota foi a {maior_nota_matricula} com nota {maior_nota}")

def media_notas_finais(matriz_entrada):
    notas_finais = calcular_nota_final(matriz_entrada)
    soma = 0.0
    for linha in range(len(notas_finais)):
        soma += float(notas_finais[linha][1])
    return soma / len(notas_finais)

print("Média das notas finais =",media_notas_finais(matriz_entrada))
