def valida_nome(nome):
    return len(nome) > 3

def valida_idade(idade):
    return idade >= 0 and idade <= 150

def valida_salario(salario):
    return salario > 0

def valida_sexo(sexo):
    return sexo == "F" or sexo == "M"

def valida_estado_civil(estado_civil):
    return estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d"

sair = "nao"
while sair == "nao":
    nome = ""
    while not valida_nome(nome):
        nome = input("Digite um nome: ")
        if not valida_nome(nome):
            print("Nome inválido, deve ter mais do que 3 caracteres")

    idade = 0
    while not valida_idade(idade):
        idade = int(input("Digite uma idade: "))
        if not valida_idade(idade):
            print("Idade inválida, deve ser entre 0 e 150")

    salario = 0.0
    while not valida_salario(salario):
        salario = float(input("Digite o salário: "))
        if not valida_salario(salario):
            print("Salário inválido, deve ser maior do que 0")

    sexo = ""
    while not valida_sexo(sexo):
        sexo = input("Digite o sexo: ")
        if not valida_sexo(sexo):
            print("Sexo inválido, deve ser M ou F")

    estado_civil = ""
    while not valida_estado_civil(estado_civil):
        estado_civil = input("Digite o estado civil: ")
        if not valida_estado_civil(estado_civil):
            print("Estado civil inválido, deve ser s (solteiro), c (casado), v (viúvo) e d (divorciado)")
            continue

    sair = input("Deseja sair? (nao, sim)")