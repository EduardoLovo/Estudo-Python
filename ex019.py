# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice

a1 = input('Digiet o nome do primeiro aluno: ').title()
a2 = input('Digete o nome do segundo aluno: ').title()
a3 = input('Digite o nome do terceiro aluno: ').title()
a4 = input('Digiet o nome do quarto aluno: ').title()


l_alunos = [a1, a2, a3, a4]

sorteio = choice(l_alunos)
print(f'\nO aluno sorteado foi {sorteio}')

