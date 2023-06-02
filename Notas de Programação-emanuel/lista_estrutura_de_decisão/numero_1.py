'''
1. Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou
menor que 10. O programa deve escrever a mensagem correspondente (maior ou
menor) e informar o valor digitado pelo usuário.

'''
n1= float(input("Escolha seu numero: "))

if n1 > 10:
    print (f"Seu numero,{n1},é maior que 10")
elif n1 == 10:
    print (f"Seu numero,{n1},é igual a 10")
else:
    print(f"Seu numero[{n1}, é menor que 10")


    ''' Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou
negativo (considere o valor zero como positivo).'''

numero= float(input('esoclha seu numero: '))

if numero > 0:
    print (f"Seu numero,{n1},é NEGATIVO)")
else:
    print(f"Seu numero,{n1},é NEGATIVO")