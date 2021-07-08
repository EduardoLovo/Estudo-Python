# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um numero: '))
num1 = numero / 1 % 10
num2 = numero / 10 % 10
num3 = numero / 100 % 10
num4 = numero / 1000 % 10

print(f'unidade:{num1:.0f} dezena:{num2:.0f} centena:{num3:.0f} milhar:{num4:.0f}')