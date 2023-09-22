import random
import time


class Hangman:
    def __init__(self, words):
        self.words = words

    def start(self):
        print("Start guessing...")
        time.sleep(0.5)

        word = self.words[random.randrange(0, len(self.words))]
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
                print("Wrong")
                print(f"You have {turns} more guesses")
                if turns == 0:
                    print("You Lose")
