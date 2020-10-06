import random
from game import Hangman


def main():
    words = ["violet", "purple" , "magenta"]
    life = 5
    hangman = Hangman(random.choice(words))
    
    Hangman.start_game(hangman,life)
    
if __name__ == '__main__':
    main()


