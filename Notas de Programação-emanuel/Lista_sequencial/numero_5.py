"""Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre
a temperatura em graus Celsius.
1. C = 5 * ((F-32) / 9)"""

f = float(input("Qual a temperatura em graus Fahrenheit? "))
c = round(5 * ((f - 32) / 9), 1)
print("A temperatura em graus Celsius é: ", c, "°C")