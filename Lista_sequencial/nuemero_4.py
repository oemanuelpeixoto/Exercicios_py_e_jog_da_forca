"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

sal= float(input('Quanto você ganha por hora? '))
dia= float(input('Quanto o número de horas trabalhadas no dia? '))


diasal= sal *dia 
mes= diasal*22
print(f'Vocé recebe R${diasal}por dia , então no mês voce recebe R${mes} ')