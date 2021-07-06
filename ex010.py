# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quantos reais deseja converter para dolar? '))
conv = real / 5.20
print(f'O valor de R${real} em dolar é ${conv:.2f}')