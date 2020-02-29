'''
16. Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro.
Se o código for zero, finalize o programa; se for 1, mostre o vetor na ordem direta;
se for 2, mostre o vetor na ordem inversa.
Caso, o código for diferente de 1 e 2 escreva uma mensagem informando que o código e inválido.
'''

vetor = input("Informe 5 números reais separados por espaço: ").split(" ")

codigo = int(input("Digite um código inteiro (0=sair, 1=normal, 2=inversa)"))
if codigo == 0:
    exit(0)
elif codigo == 1:
    for i in vetor:
        print(float(i), end=" ")
elif codigo == 2:
    for i in range(len(vetor)-1, -1, -1):
        print(float(vetor[i]), end=" ")
else:
    print("Código inválido")