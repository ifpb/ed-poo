valor_hora = float(input("Quando você ganha por hora? "))
horas_dia = int(input("Quantas horas você trabalha por dia? "))
dias_trabalhados = int(input("Quantos dias você trabalhou no mês? "))

valor_mes = valor_hora * (horas_dia * dias_trabalhados)

print("O seu salário é: ", str(valor_mes))