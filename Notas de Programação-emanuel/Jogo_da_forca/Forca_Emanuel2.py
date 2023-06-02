import random
import pygame
pygame.init()
pygame.mixer.music.load('Jogo_da_forca\\jogo_musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()
# lista de palavras para o jogo 
herois = ['Homem Aranha', 'Superman', 'Mulher Maravilha', 'Batman', 'Thor']
animais = ['Elefante', 'Leão', 'Girafa', 'Tigre', 'Macaco']
tecnologia = ['Computador', 'Smartphone', 'Internet', 'Software', 'Programação']

print(""" \n +-+-+-+ +-+-+-+-+-+
 |B|E|M| |V|I|N|D|O|
 +-+-+-+ +-+-+-+-+-+""")
print (""" .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || |     ____     | || |  _______     | || |     ______   | || |      __      | |
| | |_   ___  |  | || |   .'    `.   | || | |_   __ \    | || |   .' ___  |  | || |     /  \     | |
| |   | |_  \_|  | || |  /  .--.  \  | || |   | |__) |   | || |  / .'   \_|  | || |    / /\ \    | |
| |   |  _|      | || |  | |    | |  | || |   |  __ /    | || |  | |         | || |   / ____ \   | |
| |  _| |_       | || |  \  `--'  /  | || |  _| |  \ \_  | || |  \ `.___.'\  | || | _/ /    \ \_ | |
| | |_____|      | || |   `.____.'   | || | |____| |___| | || |   `._____.'  | || ||____|  |____|| |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """)

print("-" * 100)

# Escolha do tema pela sistema
def selecionar_palavra(tema):
    if tema == "Heróis":
        return random.choice(herois)
    elif tema == "Animais":
        return random.choice(animais)
    elif tema == "Tecnologia":
        return random.choice(tecnologia)

# desenho da forca
def desenhar_boneco(vidas):
    if vidas == 1:
        print(" ______")
        print(" |    |")
        print(" |    O")
        print(" |")
        print(" |")
        print(" |")
        print("=========")
        print("=========")
    elif vidas == 2:
        print(" ______")
        print(" |    |")
        print(" |    O")
        print(" |    |")
        print(" |")
        print(" |")
        print("=========")
        print("=========")
    elif vidas == 3:
        print(" ______")
        print(" |    |")
        print(" |    O")
        print(" |   /|")
        print(" |")
        print(" |")
        print("=========")
        print("=========")
    elif vidas == 4:
        print(" ______")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\")
        print(" |")
        print(" |")
        print("=========")
        print("=========")
    elif vidas == 5:
        print(" ______")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\")
        print(" |   /")
        print(" |")
        print("=========")
        print("=========")
    elif vidas == 6:
        print(" ______")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\")
        print(" |   / \\")
        print(" |")
        print("=========")
        print("=========")


# chamada para repetir o jogo quando acabar
def jogar_novamente():
    while True:
        resposta = input("\nDeseja jogar novamente? (S/N): ").upper()
        if resposta == "S" or resposta == "N":
            return resposta == "S"
        else:
            print("Opção inválida. Por favor, digite apenas 'S' ou 'N'.")
    

# Escolha do tema pela usuario 
while True:
    print("*" * 100)

    tema_escolhido = None
    opcoes_validas = ['A', 'B', 'C']

    while tema_escolhido is None:
        escolha = input("Escolha o seu Tema:\n\n A) Heróis\n B) Animais\n C) Tecnologia: \n ----> ")
        print()
        escolha = escolha.upper()

        if escolha in opcoes_validas:
            if escolha == 'A':
                tema_escolhido = "Heróis"
            elif escolha == 'B':
                tema_escolhido = "Animais"
            elif escolha == 'C':
                tema_escolhido = "Tecnologia"
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    palavra_selecionada = selecionar_palavra(tema_escolhido).upper()

    tamanho_palavra = len(palavra_selecionada)
    palavra_codificada = ['_'] * tamanho_palavra
    vidas = 0
    letras_erradas = []

    print("*" * 100)

    print(f"Tema escolhido: {tema_escolhido}. BEM-VINDO AO JOGO :")

    print("*" * 100)

    # jogo da froca

    while "_" in palavra_codificada and vidas < 6:
        print(f'\nSua palavra tem {tamanho_palavra} letras, o tema é {tema_escolhido}.')
        print(f"ERROS: {vidas} de 6")
        for letra in palavra_codificada:
            print(letra, end=" ")
        print()

        letra_escolhida = input("Digite uma letra: ").upper()

        if letra_escolhida in letras_erradas or letra_escolhida in palavra_codificada:
            print('\n****************************')
            print("Você já tentou essa letra!")
            print('****************************')
            continue

        if len(letra_escolhida) != 1 or not letra_escolhida.isalpha():
            print("Por favor, digite apenas letras .")
            continue

        acertou = False
        for i in range(len(palavra_selecionada)):
            if letra_escolhida == palavra_selecionada[i]:
                palavra_codificada[i] = letra_escolhida
                acertou = True

        if acertou:
            print("\nPalavra:", end=" ")
            for letra in palavra_codificada:
                print(letra, end=" ")
            print('\nParabéns! Acertou.')
        else:
            print('Errou, essa letra não existe na palavra')
            vidas += 1
            letras_erradas.append(letra_escolhida)
            desenhar_boneco(vidas)
            print("\nLetras erradas:", letras_erradas)

    if vidas == 6:
        print("*" * 100)
        print('Você perdeu 🙂')
        print(""" __     __           _                   __      
 \ \   / /          | |                  \ \   _ 
  \ \_/ /__  _   _  | | ___  ___  ___     | | (_)
   \   / _ \| | | | | |/ _ \/ __|/ _ \    | |    
    | | (_) | |_| | | | (_) \__ \  __/    | |  _ 
    |_|\___/ \__,_| |_|\___/|___/\___|    | | (_)
                                         /_/     
                                                 """)
        print("*" * 100)
    else:
        print("PARABÉNS! VOCÊ GANHOU")
        print(""" __     __                    _        
 \ \   / /                   (_)       
  \ \_/ /__  _   _  __      ___ _ __   
   \   / _ \| | | | \ \ /\ / / | '_ \  
    | | (_) | |_| |  \ V  V /| | | | | 
    |_|\___/ \__,_|   \_/\_/ |_|_| |_| 
                                       
                                       """)

    print(f'A palavra era: {palavra_selecionada}')

    if not jogar_novamente():
        break

    print("Reiniciando o jogo...\n")

print("Obrigado por jogar!")
