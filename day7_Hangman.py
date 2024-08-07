import random
from word_list import get_word_list #created module for word list 
from hangman_ascii_art import get_hangman_ascii_art  #created modules for art

hangman_ascii_art = get_hangman_ascii_art()
word_list = get_word_list()
random_word = random.choice(word_list)
display = ""
placeholder = ""
word_length = len(random_word)
correct_letters = []
lives = 6
game_over = False

#ask for input until user runs out
while not game_over:
    user_input = str((input("Guess a random letter: ")).lower())
    display = ""

    #add correct letters to the display and include correct letters for each print
    for letter in random_word:
        if letter == user_input:
            display += letter
            correct_letters.append(user_input)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    # checks if letter is incorrect, if so - a life and if no lives left GAMEOVER!
    if user_input not in random_word:
        lives -= 1
        print()
        print(f"Bad guess, you have {lives} lives left")
        if lives == 0:
            game_over = True
            print(f"You lose, the correct word was: {random_word}")

    if "_" not in display:
        game_over = True
        print("You win")

    print(hangman_ascii_art[lives])





