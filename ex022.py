# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input('Digiete seu nome completo: ').strip()
print(f'Seu nome com todas letras maiusculas {nome.upper()}')
print(f'Seu nome com todas letras minusculas {nome.lower()}')
n = nome.replace(' ', '')
print(f'Seu nome tem ao todo tem {len(n)} letras')
n2 = nome.find(' ')
print(f'Seu primeiro nome tem {n2}')

### ou

nome = input('Digiete seu nome completo: ').strip()
print(f'Seu nome com todas letras maiusculas {nome.upper()}')
print(f'Seu nome com todas letras minusculas {nome.lower()}')
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))