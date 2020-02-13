import math

tamanho_desejado = float(input("Digite o tamanho em metros da área a ser pintada: "))
valor_lata = 80
litros_lata = 18
cobertura_lata = 3
quantidade_latas = math.ceil( (tamanho_desejado) / (litros_lata * cobertura_lata) )
print(f"Você precisa de {quantidade_latas} latas")
print(f"Isso vai custar: ", quantidade_latas * valor_lata)