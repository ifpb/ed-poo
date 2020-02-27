# 10. Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor,
# calcule e imprima a média geral.
notas = []
soma = 0
for i in range(15):
    entrada = float(input("Digite a nota do aluno nº "+str(i+1)+": "))
    notas.append(entrada)
    soma += entrada

print("Média geral = ", soma / len(notas))