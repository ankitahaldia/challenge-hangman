from game import Hangman


def main():
    
    '''
    instantiating hangman class object 
    to play the game
    '''

    hangman = Hangman()
    Hangman.start_game(hangman)
    
if __name__ == '__main__':
    main()


