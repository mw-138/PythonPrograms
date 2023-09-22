import random


class Blackjack:
    def __init__(self):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4

    def __get_card_value(self, card):
        if card == 'J' or card == 'Q' or card == 'K' or card == 'A':
            return 10
        return card

    def __deal_card(self):
        card = self.cards[0]
        self.cards.remove(card)
        return self.__get_card_value(card)

    def __player_win(self):
        print("Player won!")

    def __dealer_win(self):
        print("Dealer won!")

    def __bust(self):
        print("Bust! No one won!")

    def start(self):
        random.shuffle(self.cards)
        player_hand_value = 0
        dealer_hand_value = 0

        for _ in range(2):
            player_hand_value += self.__deal_card()
            dealer_hand_value += self.__deal_card()

        print(f"Player: {player_hand_value} | Dealer: {dealer_hand_value}")

        while True:
            answer = input("Hit or stand? (h/s): ")
            if answer.lower() == "h":
                player_hand_value += self.__deal_card()
                if player_hand_value > 21:
                    break
            elif answer.lower() == "s":
                break
            else:
                print("Invalid response! Type either 'h' or 's'")

            print(f"Player: {player_hand_value} | Dealer: {dealer_hand_value}")

        print(f"Player: {player_hand_value} | Dealer: {dealer_hand_value}")

        if player_hand_value <= 21:
            while dealer_hand_value < player_hand_value:
                dealer_hand_value += self.__deal_card()
                print(f"Player: {player_hand_value} | Dealer: {dealer_hand_value}")

        if player_hand_value > 21:
            self.__dealer_win()
        elif dealer_hand_value == 17 and player_hand_value < dealer_hand_value:
            self.__dealer_win()
        elif dealer_hand_value > 21 > player_hand_value:
            self.__player_win()
        elif 21 >= dealer_hand_value > player_hand_value:
            self.__dealer_win()
        elif dealer_hand_value == player_hand_value:
            self.__bust()
