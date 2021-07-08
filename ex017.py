# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = (oposto**2 + adjacente**2) **(1/2)

print(f'A hipotenusa vai medir {hipotenusa:.2f} ')

### ou

from math import hypot

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = hypot(oposto, adjacente)

print(f'A hipotenusa vai medir {hipotenusa:.2f} ')
