# 14. Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela.
vetor = []
for i in range(10):
    entrada = int(input("Digite o número "+str(i+1)+": "))
    vetor.append(entrada)

contem_duplicado = False
duplicados = set([])

for i in range(0,len(vetor)):
    for j in range(i+1,len(vetor)):
        if vetor[i] == vetor[j]:
            contem_duplicado = True
            duplicados.add(vetor[i])

if contem_duplicado:
    print("Contém duplicados: ", duplicados)
else:
    print("Não contém duplicado")