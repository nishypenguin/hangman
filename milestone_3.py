import random 

word_list = ["watermelon", "grapes", "orange", "banana", "apple"]
random_word_from_list= random.choice(word_list)
print(random_word_from_list)



def check_guess(single_letter_guess):
    single_letter_guess = single_letter_guess.lower()
    if single_letter_guess in random_word_from_list:
        print(f"Good guess! {single_letter_guess} is in the word.")  
    else:
        print(f"Sorry, {single_letter_guess} is not in the word. Try again.")


def ask_for_input():
    while True:
        single_letter_guess = input("Enter a single letter: ")
        if len(single_letter_guess) == 1 and single_letter_guess.isalpha() == True:
            break 
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(single_letter_guess)

ask_for_input()