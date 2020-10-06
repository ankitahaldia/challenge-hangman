import random
import typing


class Hangman :

    """
    The hangman class with its methods and attributes
    aims to guess the letters from a randomly chosen word
    till you lose the max number of times(life)

    """
           
         
    def __init__(self):
        '''
        class attributes 

        '''
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word = random.choice(self.possible_words)
        self.word_to_find = [char for char in self.word ]
        self.well_guessed_letters = list('_' * len(self.word_to_find))
        self.bad_guessed_letters = []
        self.life = 5
        self.error_count = 0
        self.game_is_over = False
        self.turn_count = 1
        self.good_answers = []
        
    
    ''' 
        returns the list of indexes where letter is found
         if in multiple positions 
         ''' 
    def letter_pos(self,letter):
       idx = [i for i, char in enumerate(self.word_to_find) if letter == char]    
       return idx


    '''
    Player guesses letters till he loses max attempts
    if letter is found , it is added to good answers list
    and if wrong guess is made, player loses one life ,
    error count is incremented.
    
    '''
    def play(self) :

        count = 1        
        while count <= len(self.word_to_find) and self.life > 0 :
            print(self.word_to_find)
            print(f"turn_count : {self.turn_count} " )
            print(f"life : {self.life } ")
            letter = input("Guess a letter: ")
            
            if letter.isdigit() or len(letter) > 1 :
                print("Please enter only one alphabet !") 
            
            if letter in self.word_to_find:
                idxs = self.letter_pos(letter)
                self.good_answers.append(letter)
                for index in idxs:
                    self.well_guessed_letters[index] = letter
                    count += 1
                print(f"well guessed word : {self.well_guessed_letters } ")
                   
            else :
                self.error_count += 1
                self.life -=1
                self.bad_guessed_letters.append(letter)
                print(f"wrong letter, you have {self.life} turns left !")
                print(f"bad guessed word : {self.bad_guessed_letters } ")
                print("error count  : ",self.error_count)
        return True
                   
                
    # Method to print game is over      
    def game_over(self) :
        print("Your Game is over !!")
        quit()

    # Method to print how player played the game
    def well_played(self) :
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")

    #method called to start the game
    def start_game(self) :
             
        while self.life > 0 and self.game_is_over == False:
            self.game_is_over = self.play()
        
        #if self.well_guessed_letters == self.word_to_find :
        if self.well_guessed_letters.count('_') == 0:
            self.well_played()
        elif self.life == 0 : 
            self.game_over()

 
 