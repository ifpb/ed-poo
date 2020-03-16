gabarito = []
for i in range(10):
    gabarito.append(input(f"Digite o gabarito da questão {i+1} (a,b,c,d,e): "))

respostas = []
for linha in range(5):
    resultado = 0
    print(f"Aluno {linha+1}")
    for coluna in range(10):
        resposta = input(f"Digite a resposta da questão {coluna+1} (a,b,c,d,e): ")
        if resposta == gabarito[coluna]:
            print("Resposta correta")
            resultado += 1
        else:
            print("Resposta errada")
    print(f"Acertou {resultado} de 10 questões")