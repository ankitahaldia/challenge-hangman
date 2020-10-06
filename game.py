import random


class Hangman :
    
    #turn_count = 0
         
    def __init__(self,word):
        self.good_word = [char for char in word ]
        self.well_guessed_letters = list('_' * len(self.good_word))
        self.bad_guessed_letters = ""
        self.error_count = 0
        self.game_is_over = False
        self.turn_count = 0
        
        
   
    def letter_pos(self,letter):
       idx = [i for i, char in enumerate(self.good_word) if letter == char]    
       return idx



    def play(self,life) :
        self.life = life
        
        while self.turn_count <= len(self.good_word) :

            letter = input("Guess a letter: ")
            
            if letter.isdigit() or len(letter) > 1 :
                print("Please enter only one alphabet !") 
                continue
            if letter in self.good_word:
                idxs = self.letter_pos(letter)
                for index in idxs:
                    self.well_guessed_letters[index] = letter
                    self.turn_count += 1
                if self.well_guessed_letters.count('_') == 0:
                    return True
            else:
                self.error_count += 1
                self.bad_guessed_letters += letter
                self.turn_count += 1
                            

        self.life = self.life - self.error_count
        return True
                   
                
    # Method to print game is over      
    def game_over(self) :
        print("Your Game is over !!")
        quit()

    # Method to print how you played the game
    def well_played(self) :
        print(f"You found the word: {self.good_word} in {self.life} turns with {self.error_count} errors!")

    #method called to start the game
    def start_game(self,life) :
        #self.good_word = word
        self.life = life

        try :
            while self.life != 0 and self.game_is_over == False:

                if self.life > 0 and self.game_is_over == False :
                    self.game_is_over = self.play(self.life)
                    if self.well_guessed_letters == self.good_word :
                        self.well_played()
        finally :
            if self.life <= 0 : 
                self.game_over()

 
 