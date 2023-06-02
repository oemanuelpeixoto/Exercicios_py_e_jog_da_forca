'''Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ounegativo (considere o valor zero como positivo).'''

    
while True:
    numero= float(input('esoclha seu numero: '))

    if numero >= 0:
        print(f"Seu numero,{numero},é POSITIVO")
    
    else:
        print(f"Seu numero,{numero},é NEGATIVO")
    continue