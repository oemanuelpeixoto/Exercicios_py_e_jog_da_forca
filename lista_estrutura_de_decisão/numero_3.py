'''As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se
forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
compradas, calcule e escreva o custo total da compra'''


while True:
    print("-"*35)
    print ('Olá seja bem vinda a loja de maças')
    print("-"*35)

    maca=int(input('Quantas maças você vai querer ? '))

    if maca < 12 :
        print ( 'o valor da sua compra foi: ',maca*1.30)
    else :
        print ( 'o valor da sua compra foi: ',maca*1.00)
    
    continuar = input("Deseja verificar outro valor? (S/N) ").upper()
    if continuar == "S":
        print("*"*35)
        print ("Nova consulta ")
        print("*"*35)
    else:
        print ("Ok, até a proxima")
        break
    continue

