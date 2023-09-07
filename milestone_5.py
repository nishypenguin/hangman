import random 

class Hangman:

    def __init__(self, word_list, num_lives = 5 ):
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for x in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_single_letter_guess(self, single_letter_guess):
        single_letter_guess = single_letter_guess.lower()
        if single_letter_guess in self.word:
            print(f"Good guess! {single_letter_guess} is in the word.")  


            for index, letter in enumerate(self.word):
                if single_letter_guess == letter:
                    self.word_guessed[index] = single_letter_guess
            self.num_letters -= 1

    

        else:
            self.num_lives -= 1
            print( f"Sorry, the letter {single_letter_guess} is not in the word")
            print(f"You have {self.num_lives} lives left")
            
            

    def ask_for_input(self):
        while self.num_lives > 0 and self.num_letters > 0:
            single_letter_guess = input("Enter a single letter: ")
            if len(single_letter_guess) != 1 or single_letter_guess.isalpha() == False:
                print("Invalid letter. Please enter a single alphabetical character")
            elif single_letter_guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_single_letter_guess(single_letter_guess)
                self.list_of_guesses.append(single_letter_guess)





def play_game(word_list):
    num_lives = 5 
    game = Hangman(word_list, num_lives)
    
    while True:
        

        if game.num_lives == 0:
            print("You lost!")
            break
        
        elif game.num_letters > 0:
            game.ask_for_input()
            

    
        else:
            print("Congratulations. You won the game!")
            break
        

play_game(["apple", "banana", "cherry", "date", "elderberry"])
