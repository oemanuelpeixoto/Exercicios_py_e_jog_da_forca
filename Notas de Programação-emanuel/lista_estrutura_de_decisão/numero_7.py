'''Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também
testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
senão escrever a mensagem 'Saldo Negativo'''


n_cli= input ("Número da conta do cliente ? ***** (5 digitos)")
while len(n_cli) != 5:
    print("Número inválido. Digite novamente.")
    n_cli = input("Número da conta do cliente (5 dígitos): ")

print("-"*60)
print("Bem-vindo, cliente", n_cli)
print("-"*60)



saldo= float(input ("Qual o saldo ? "))
debito = float(input ("Qual o débito ? "))
credito = float(input ("Qual o credito ? "))

print("-"*60)
saldo_atual = (saldo - debito + credito)
print(f'O cliente de numero {n_cli} possui o saldo atual de {saldo_atual}')
print("-"*60)

if saldo_atual > 0:
    print ("SALDO POSITIVO")
else:
    print ('SALDO NEGATIVO')


