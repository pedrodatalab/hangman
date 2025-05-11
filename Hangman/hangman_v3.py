# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name
import csv


# Função para limpar a tela a cada execução
def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========''']


# Classe
class Hangman:
     
	# Método Construtor
     def __init__(self, palavra):
          self.palavra = palavra
          self.letras_erradas = letras_erradas
          self.letrascorretas = letras_corretas
          self.tentativas = tentativas
          
	# Método para adivinhar a letra
     
	# Método para verificar se o jogo terminou
		
	# Método para verificar se o jogador venceu
		
	# Método para não mostrar a letra no board
		
	# Método para checar o status do game e imprimir o board na tela

def escolha_palavra():
    with open(r"E:\Estudos\DSA\Projetos DSA\Hangman\palavras_ptbr.csv", 'r', encoding='utf8') as palavras:
        linhas = palavras.readlines()
        palavra = random.choice(linhas).strip()  # .strip() remove quebras de linha
    
    print(palavra)

escolha_palavra()

    
    


