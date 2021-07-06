# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

palavra = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(palavra)}')
print(f'Só tem espaços?', palavra.isspace())
print(f'Só tem numeros?', palavra.isnumeric())
print(f'É alfabetico?', palavra.isalpha())
print(f'É alphanumérico?', palavra.isalnum())
print(f'Esta em maiusculas?', palavra.isupper())
print(f'Esta em minusculas?', palavra.islower())
print(f'Esta capitalizada?', palavra.istitle())