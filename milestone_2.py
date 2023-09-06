import random 

word_list = ["watermelon", "grapes", "orange", "banana", "apple"]
random_word_from_list= random.choice(word_list)
print(random_word_from_list)



single_letter_guess = input("Enter a single letter: ")
if len(single_letter_guess) == 1 and single_letter_guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")