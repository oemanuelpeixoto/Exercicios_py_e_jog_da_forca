
''' . Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em
ordem crescente.'''




n1= float(input("Escolha o seu 1° numero: "))
n2= float(input("Escolha o seu 2°numero: "))

while n1 == n2:
     print("Os valores não podem ser iguais. Tente novamente.")
     n1= float(input("Escolha o seu 1° numero: "))
     n2= float(input("Escolha o seu 2°numero: "))
 
if n1 < n2:
    print( f'o nuemro { n1}, {n2}')
else:
    print( f'o nuemro { n2} ,{n1}')