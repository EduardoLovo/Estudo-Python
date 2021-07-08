# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual seu salario? '))
aumento = salario + (salario * 15/100)
print(f'Seu salario era de R${salario}, com aumento de 15%, agora é R${aumento}!')