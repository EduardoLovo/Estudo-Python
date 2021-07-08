# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual o preço do produto? R$'))
desconto = (5/100)*preço
resultado = preço - desconto
print(f'O produto que custava {preço:.2f}, na promoção com desconto de 5% vai custar {resultado:.2f}')

### ou

preço2 = float(input('Qual o preço do produto? R$'))
desconto2 = preço - (preço * 5/100)
print(f'O produto que custava R${preço2:.2f}, na promoção com desconto de 5% vai custar R${desconto2:.2f}')