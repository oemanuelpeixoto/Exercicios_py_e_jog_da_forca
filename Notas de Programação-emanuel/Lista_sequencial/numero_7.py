""" Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1. o produto do dobro do primeiro com metade do segundo .
2. a soma do triplo do primeiro com o terceiro.
3. o terceiro elevado ao cubo."""

n1 = int(input("Digite o primeiro número inteiro,  -3, -2, -1, 0, 1, 2, 3, 4, 5,...: "))
n2 = int(input("Digite o segundo número inteiro, -3, -2, -1, 0, 1, 2, 3, 4, 5, ....: "))
n3 = float(input("Digite um número real 1,2,3,4,5....: "))

d = (n1 * 2) * (n2 / 2)
s = (n1 * 3) + n3
c = n3 ** 3

print("O produto do dobro do primeiro com metade do segundo é:", d)
print("A soma do triplo do primeiro com o terceiro é:", s)
print("O terceiro elevado ao cubo é:", c)