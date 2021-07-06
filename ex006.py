# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um numero: '))
n1 = n * 2
n2 = n * 3
n3 = n **(1/2)

print(f'O dobro de {n} é {n1}')
print(f'O triplo de {n} é {n2}')
print(f'A raiz quadrada de {n} é {n3:.2f}')
