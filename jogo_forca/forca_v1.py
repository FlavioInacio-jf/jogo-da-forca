# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
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
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Classe
class Hangman():
   # Método Construtor
   def __init__(self, word):
       self.word  = word
       self.letras_certas = ["_"]*len(word)
       self.letras_erradas = []
   # Método para adivinhar a letra
   def guess(self, letter):    
       if letter not in self.word and letter not in self.letras_erradas:
               self.letras_erradas.append(letter)
       elif letter not in self.letras_certas:
            posicao = [i for i, v in enumerate(self.word) if v  == letter]
            for a in posicao:
                self.letras_certas[a] = letter 
	# Método para verificar se o jogo terminou
   def hangman_over(self):
       return  not self.hangman_won() and len(self.letras_erradas) < 6
		
	# Método para verificar se o jogador venceu
   def hangman_won(self):
       return not '_' in self.letras_certas

	# Método para checar o status do game e imprimir o board na tela
   def print_game_status(self):
       print(board[len(self.letras_erradas)])
       print("Palavra:", end = "")
       print(str([i for i in self.letras_certas]).strip("[]"), end = "")
       print("\nLetras erradas:", end = " ")
       print(str([i for i in self.letras_erradas]).strip("[]"), end ="")
		
# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()

# Função Main - Execução do Programa
def main():
	# Objeto
    game = Hangman(rand_word())

    while (game.hangman_over() ):
        game.print_game_status()
        letra = input("Digite uma letra: ")
        game.guess(letra)
    game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print ('\nParabéns! Você venceu!!')
    else:
        print ('\nGame over! Você perdeu.')
        print ('A palavra era ' + game.word)
		
    print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
