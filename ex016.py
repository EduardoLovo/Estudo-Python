# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
valor = float(input('Digite um valor: '))
print(f'O valor digitato foi {valor} e sua porção inteira é {trunc(valor)}')

### ou 

valor1 = float(input('Digite um valor: '))
print(f'O valor digitato foi {valor1} e sua porção inteira é {int(valor1)}')