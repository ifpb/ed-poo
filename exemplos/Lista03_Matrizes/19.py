# matriz = [
#     [1.0, q2.0, 3.1, 3.1, 8.4, 9.3],
#     [5.0, 4.0, 3.0, q2.0, q2.0, 5.5],
#     [5.0, 4.0, 3.0, 5.0, 4.0, 3.0]
# ]
matriz = []
for j in range(3):
    matriz.append(input(f"Digite seis elementos da linha {j+1} separada por espaço: ").split(" "))

print("Matriz original: ")
print(matriz)

def soma_elementos_impares(matriz):
    soma = 0.0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if float(matriz[linha][coluna]) % 2 != 0:
                soma += float(matriz[linha][coluna])
    return soma

def media_segunda_quarta_colunas(matriz):
    media = []
    for linha in range(len(matriz)):
        soma = 0.0
        for coluna in range(len(matriz[linha])):
            if coluna == 1 or coluna == 3:
                soma += float(matriz[linha][coluna])
        media.append(soma / 2)
    return media

def substituir_valores_sexta_coluna_soma_1_e_2(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            matriz[linha][5] = matriz[linha][0] + matriz[linha][1]
    return matriz

print(f"Soma dos números impares = {soma_elementos_impares(matriz)}")
print(f"Média da segunda e quarta colunas = {media_segunda_quarta_colunas(matriz)}")
print(f"Substituir valores da sexta coluna pela soma da primeira com a segunda = ")

for linha in substituir_valores_sexta_coluna_soma_1_e_2(matriz):
    print(linha)