from ascii_art import type_something_art
ascii_art = type_something_art()

import random

print(type_something_art)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

game_over = False
easy_level_guess_attempts = 0
hard_level_guess_attempts = 0
random_number = random.randint(1, 100)
guesses = 0
print(random_number)

def easy_level():
        global game_over, easy_level_guess_attempts, guesses
        print(f"You have {10 - easy_level_guess_attempts} attempts remaining to guess the number.")
        if easy_level_guess_attempts < 10: #first if loop check guess attempts
            guesses = int(input("Make a guess: "))
            easy_level_guess_attempts += 1
            if compare_calc(guesses, random_number):#second if loop checks if guess is correct
                return True 
        else:
            print("You have run out of guesses. You lose!")
            return True
        return False 

def hard_level():
        global game_over, hard_level_guess_attempts, guesses
        print(f"You have {5 - hard_level_guess_attempts } attempts remaining to guess the number.")
        if hard_level_guess_attempts < 5:
            guesses = int(input("Make a guess: "))
            hard_level_guess_attempts += 1
            if compare_calc(guesses, random_number):#second if loop checks if guess is correct
                return True 
        else:
            print("You have run out of guesses. You lose!")
            return True
        return False

def compare_calc(guesses, random_number):
    if random_number > guesses:
        print("guess higher")
    elif random_number < guesses:
        print("Guess lower")
    else:
        print("Guessed correctly, you win!")
        return True #game should end 
    return False #loop continues till attempts are used up

while not game_over:
    if difficulty == "easy":
        game_over = easy_level()
    elif difficulty == "hard":
        game_over = hard_level()
    else:
        print("Pick a level by typing easy or hard")


