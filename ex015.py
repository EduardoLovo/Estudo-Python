# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos Km rodou com o carro? '))

preço_dias = dias * 60
preço_km = km * 0.15
total = preço_dias + preço_km

print(f'O total a pagar é de R${total:.2f}')

### ou
dias = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos Km rodou com o carro? '))

total2 = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${total2:.2f}')