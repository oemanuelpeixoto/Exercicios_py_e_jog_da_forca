
cel = ['Mark', 'Jobs', "Gates","Steve", "Wuldson Franco"]

for covidados in cel:
    print('Venha para minha festa,', covidados)
    print('-'*50)



while True:
    nao_vem= input ("Digite o convidado que não poderá comparecer: \n""(Obs caso digite errado a pergunta se repetira)--->")
    if nao_vem not in cel:
        print(f"Ops, * {nao_vem} * não está na lista de convidados.")
        continue
    else:
        print( f"\nInfelizmente, {nao_vem} não poderá comparecer.\n" )
    break


novo_convidado = "Marcelo"
print(" {}  foi adicionado à lista de convidados.".format(nao_vem , novo_convidado))
cel.append(novo_convidado)  

for convidado in cel:
    print("Enviando convite para", convidado)


   



 


    