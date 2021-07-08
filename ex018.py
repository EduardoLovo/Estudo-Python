# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

a = float(input('Digite o angulo: '))
seno = math.sin(math.radians(a))
print(f'O angulo de {a} tem o seno de {seno:.2f}')

cosseno = math.cos(math.radians(a))
print(f'O angulo de {a} tem o cosseno de {cosseno:.2f}')

tangente = math.tan(math.radians(a))
print(f'O angulo de {a} tem a tangente de {tangente:.2f}')