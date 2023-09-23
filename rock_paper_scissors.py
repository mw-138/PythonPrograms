import random
import time


class RockPaperScissors:
    def __init__(self):
        self.options = ["r", "p", "s"]
        self.intro_sleep_interval = 0.75

    def is_win(self, player, computer):
        return (player == "r" and computer == "s") or (player == "s" and computer == "p") or (
                player == "p" and computer == "r")

    def get_option_label(self, option):
        option_labels = {
            "r": "Rock",
            "p": "Paper",
            "s": "Scissors"
        }
        return option_labels[option]

    def start(self):
        player_choice = input("Enter choice (r/p/s): ")
        random_choice = random.choice(self.options)

        print("Rock...")
        time.sleep(self.intro_sleep_interval)
        print("Paper...")
        time.sleep(self.intro_sleep_interval)
        print("Scissors...")
        time.sleep(self.intro_sleep_interval)
        print("Shoot!")
        time.sleep(self.intro_sleep_interval)

        print(f"Computer chose: {self.get_option_label(random_choice)}")

        if player_choice == random_choice:
            print("It's a draw!")
            return

        if self.is_win(player_choice, random_choice):
            print("Player won!")
            return

        print("Computer won!")
        return
