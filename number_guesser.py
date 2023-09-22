import random


class NumberGuesser:
    def __init__(self, max_range):
        self.max_range = max_range

    def start(self):
        random_number = random.randrange(0, self.max_range + 1)
        player_input = -1
        tries = 0
        while player_input != random_number:
            player_input = int(input("Enter number: "))
            tries += 1
            if player_input < random_number:
                print("Higher")
            elif player_input > random_number:
                print("Lower")
        print(f"You guessed it! The number was {random_number}. Took {tries} tries.")
