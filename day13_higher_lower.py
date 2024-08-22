from ascii_art import higher_lower_art
from game_data import data
import random

ascii_art = higher_lower_art()
game_data = data
print(ascii_art)

class HigherLower:
    def __init__(self):
        self.choice = None
        self.score = 0
        self.random_card_a = None
        self.random_card_b = None
        print("Welcome to the game Higher or Lower!")

    def game(self):
        # Choose random cards
        self.random_card_a = random.choice(data)
        self.random_card_b = random.choice(data)

        # Ensure both cards are not the same
        while self.random_card_a == self.random_card_b:
            self.random_card_b = random.choice(data)

        # Display cards
        print(f"Compare A: {self.random_card_a['name']}, a {self.random_card_a['description']}, from {self.random_card_a['country']}")
        print("\n" * 3)
        print(f"Compare B: {self.random_card_b['name']}, a {self.random_card_b['description']}, from {self.random_card_b['country']}")

        # Get user input
        self.choice = input("Which has a higher follower count? Type 'A' or 'B': ").lower()
        self.compare()

    def compare(self):
        if self.random_card_a['follower_count'] > self.random_card_b['follower_count']:
            correct_choice = "a"
        else:
            correct_choice = "b"

        if self.choice == correct_choice:
            self.score += 1
            print(f"Guessed correctly, your score is: {self.score}")
            self.game()  # Restart the game with a new set of cards
        else:
            print(f"You lose, game over. Your final score is: {self.score}")

# Create an instance of the class and start the game
obj = HigherLower()
obj.game()
