'''
29. Faça um programa para ler 10 números DIFERENTES a serem armazenados em um vetor.
Os dados deverão ser armazenados no vetor na ordem que forem sendo lidos, sendo que caso o usuário digite
um número que já foi digitado anteriormente, o programa deverá pedir para ele digitar outro número.
Note que cada valor digitado pelo usuário deve ser pesquisado no vetor, verificando se ele existe entre os números
que já foram fornecidos. Exibir na tela o vetor final que foi digitado.
'''

def item_existe(item, vetor):
    existe = False
    for i in vetor:
        if i == item:
            existe = True
    return existe

vetor = []

for i in range(10):
    entrada = None
    entrada = int(input(f"Digite um número único ({i + 1}/{10}): "))
    while(item_existe(entrada, vetor)):
        entrada = int(input(f"Número já existente. Digite outro número ({i+1}/{10}): "))
    vetor.append(entrada)

print("Vetor = ",vetor)