# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 1

#import

import random
from os import system, name

# Função para limpar a tela a cada execução

def limpa_tela():
    # Windows.
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux.
    else:
        _ = system ('clear')

# Função

def game():

    limpa_tela()

    print("\nBem-Vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo:

    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # Escolhece randomicamente uma palavra
    palavra = random.choice(palavras)

    #list comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Chances
    chances = 6

    # Lista para letras erradas
    letras_erradas = []

    while chances > 0:

        print(" ".join(letras_descobertas))
        print("\nChances restantes: ", chances)
        print("Letras erradas: ", "".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palvra era:", palavra)

if __name__ == "__main__":
    game()
    