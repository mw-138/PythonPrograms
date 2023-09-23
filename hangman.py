import random
import time


class Hangman:
    def __init__(self, words):
        self.words = words

    def start(self):
        print("Start guessing...")
        time.sleep(0.5)

        word = random.choice(self.words)
        guesses = ""
        turns = 10

        while turns > 0:
            failed = 0

            for char in word:
                if char in guesses:
                    print(char, end="")
                else:
                    print("_", end="")
                    failed += 1

            if failed == 0:
                print("\nYou won")
                break

            guess = input("\nGuess a character: ")
            guesses += guess

            if guess not in word:
                turns -= 1
                print(f"Incorrect! You have {turns} more turns remaining.")
                if turns == 0:
                    print("You Lose")
