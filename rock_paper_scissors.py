import random
import time


class RockPaperScissors:
    def __init__(self):
        self.__start()

    def __is_win(self, player, computer):
        return (player == "r" and computer == "s") or (player == "s" and computer == "p") or (
                player == "p" and computer == "r")

    def __get_option_label(self, option):
        option_labels = {
            "r": "Rock",
            "p": "Paper",
            "s": "Scissors"
        }
        return option_labels[option]

    def __start(self):
        player_choice = input("Enter choice (r/p/s): ")
        random_choice = random.choice(["r", "p", "s"])

        for intro_label in ["Rock...", "Paper...", "Scissors...", "Shoot..."]:
            print(intro_label)
            time.sleep(0.75)

        print(f"Computer chose: {self.__get_option_label(random_choice)}")

        if player_choice == random_choice:
            print("It's a draw!")
            return

        if self.__is_win(player_choice, random_choice):
            print("Player won!")
            return

        print("Computer won!")
        return
