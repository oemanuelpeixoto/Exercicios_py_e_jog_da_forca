'''Seja criativo ao desenvolver este programa.
a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome
personalizado.
c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos
convites. Imprima o nome das pessoas que não poderão comparecer.
d. Modifique sua lista, substitua os desistentes por novos convidados.
e. Exiba um novo convite para cada pessoa que continua presente em sua lista.'''

cel= ('Mark', 'Jobs', "Gates","Steve", "WULDSON FRANCO")

for covidados in cel:
    print('Venha para minha festa,', covidados)




# a. Lista de convidados
convidados = ["Angelina Jolie", "Will Smith", "Beyoncé", "Cristiano Ronaldo", "Ellen DeGeneres"]
for convidado in convidados:
    print("Enviando convite para", convidado)
   

# c. Novos convites
nao_vem = input("Digite o nome do convidado que não poderá comparecer: ")
if nao_vem in convidados:
    print("Infelizmente, {} não poderá comparecer.\n".format(nao_vem))
    convidados.remove(nao_vem)  # remove o nome do convidado que não poderá comparecer
    for convidado in convidados:
        print("Enviando convite para", convidado)
       
        print("-" * 50)
else:
    print("Ops, {} não está na lista de convidados.".format(nao_vem))


novo_convidado = "Emma Watson"

print("\n{} foi adicionado à lista de convidados.\n".format(novo_convidado))
convidados.append(novo_convidado)  # adiciona o novo convidado à lista

for convidado in convidados:
    print("Enviando convite para", convidado)
   
