'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
conceito for D ou E'''

n1 = float(input("Qual a primeiro nota ? "))
while n1> 10:
    print("Nota inválida. A nota máxima é 10.")
    n1= float(input("Digite novamente a primeira nota: "))

n2 = float(input("Qual a segunda nota ? "))
while n1> 10:
    print("Nota inválida. A nota máxima é 10.")
    n1= float(input("Digite novamente a primeira nota: "))

m = (n1 + n2 ) / 2
print(m)

if m >= 9 :
    print (f"PARABÉNS, SUA MEDIA FOI {m} E VOCÊ tirou A ")
    print ("APROVADO")
elif m >= 7.5:
    print (f"PARABÉNS, SUA MEDIA FOI {m} E VOCÊ tirou B ")
    print ("APROVADO")
elif m >= 6:
    print (f"PARABÉNS, SUA MEDIA FOI {m} E VOCÊ tirou C ")
    print ("APROVADO") 
elif m >= 4:
    print (f"TENTE NOVAMENTE , SUA MEDIA FOI {m} E VOCÊ tirou D ")
    print ("REPROVADO")   
else:
    print (f"TENTE NOVAMENTE , SUA MEDIA FOI {m} E VOCÊ tirou E ")
    print ("REPROVADO")                