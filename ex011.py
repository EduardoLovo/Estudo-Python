# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

area = largura * altura
pintar = area / 2

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua area é {area}m².')
print(f'Para pintar essa parede, você precisara de {pintar}l de tinta.')