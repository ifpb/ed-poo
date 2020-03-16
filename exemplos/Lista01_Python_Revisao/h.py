def salario_bruto(v_hora, total_horas):
    return v_hora * total_horas

def desconto_inss(salario_bruto):
    return salario_bruto * 0.08

def desconto_irpf(salario_bruto):
    return salario_bruto * 0.11

def desconto_sindicado(salario_bruto):
    return salario_bruto * 0.05

def salario_liquido(salario_bruto):
    return salario_bruto - desconto_inss(salario_bruto) - desconto_irpf(salario_bruto) - desconto_sindicado(salario_bruto)

valor_hora = float(input("Quanto você ganha por hora? "))
horas_mes = int(input("Quantas horas você trabalhou no mês? "))
valor_bruto = salario_bruto(valor_hora, horas_mes)

print("Seu salário bruto é: ", valor_bruto)
print("Seu salário líquido é: ", salario_liquido(valor_bruto))
print("Desconto de 8% do INSS: ", desconto_inss(valor_bruto))
print("Desconto de 11% do IRPF: ", desconto_irpf(valor_bruto))
print("Desconto de 5% do Sindicato: ", desconto_sindicado(valor_bruto))