import random
import time
import helpers
import enum


class Player:
    def __init__(self, starting_health):
        self.max_health = starting_health
        self.current_health = self.max_health
        self.gold = 0

    def has_enough_gold(self, amount):
        return self.gold >= amount

    def give_gold(self, amount):
        self.gold += amount

    def remove_gold(self, amount):
        if not self.has_enough_gold(amount):
            return
        self.gold -= amount

    def damage(self, amount):
        self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0

    def heal(self, amount):
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def is_dead(self):
        return self.current_health <= 0

    def revive(self):
        if not self.is_dead():
            return
        self.current_health = self.max_health


class AdventureScenario(enum.Enum):
    FOUND_ENEMY = 1
    FOUND_ITEM = 2


class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def is_dead(self):
        return self.health <= 0

    def deal_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0


class TextAdventureGame:
    def __init__(self):
        self.player = Player(100)
        self.revive_cost = 100

    def __print_player_info(self):
        helpers.print_string_section('-', [
            f"HP: {self.player.current_health}/{self.player.max_health}",
            f"Gold: {self.player.gold}"
        ])

    def __do_return_countdown(self, timer):
        for _ in range(timer, 0, -1):
            print(f"Returning in {_}...")
            time.sleep(1)

    def __generate_random_enemy(self):
        return Enemy(helpers.random_inclusive(50, 100), helpers.random_inclusive(1, 10))

    def __go_on_adventure(self):
        helpers.print_string_section('-', ["Adventuring..."])
        time.sleep(1)
        scenario = self.__get_random_adventure_scenario()

        if scenario == AdventureScenario.FOUND_ENEMY:
            print("Found enemy")
            enemy = self.__generate_random_enemy()
            player_turn = True
            while not enemy.is_dead():
                player_damage = helpers.random_inclusive(10, 20)
                print(
                    f"Player dealt {player_damage} damage to enemy" if player_turn else f"Enemy dealt {enemy.damage} damage to player")

                if player_turn:
                    enemy.deal_damage(player_damage)
                else:
                    self.player.damage(enemy.damage)

                print(f"Player: {self.player.current_health}/{self.player.max_health} | Enemy: {enemy.health}")

                time.sleep(1)
                player_turn = not player_turn

                if self.player.is_dead():
                    print(f"Player died while fighting enemy")
                    break

            if enemy.is_dead():
                helpers.print_string_section('-', [
                    "Enemy died!",
                    "Giving player rewards from enemy death..."
                ])
        elif scenario == AdventureScenario.FOUND_ITEM:
            print("Found item")

        self.__do_return_countdown(3)

    def __visit_vendor(self):
        print("Visiting vendor...")
        time.sleep(1)

        item_index = 0
        for item in ["Item 1", "Item 2", "Item 3"]:
            print(f"[{item_index}] {item} - 0 Gold")
            item_index += 1

        player_input = input("What would you like to purchase? (Enter 'x' to leave) ")
        if player_input.lower() == "x":
            return

    def __get_random_adventure_scenario(self):
        return random.choice(list(AdventureScenario))

    def start(self):
        # self.player.damage(self.player.max_health)
        while True:
            if self.player.is_dead():
                helpers.print_string_section('-', [
                    "What do you want to do?",
                    f"[0] Heal for {self.revive_cost} gold",
                ])
                player_input = int(input("Enter number: "))
                if player_input == 0:
                    if self.player.has_enough_gold(self.revive_cost):
                        self.player.revive()
                    else:
                        print("You don't have enough gold to revive. Game over.")
                        break
            else:
                helpers.print_string_section('-', [
                    "What do you want to do?",
                    "[0] Adventure",
                    "[1] Vendor",
                    "[2] View Player Info",
                ])
                player_input = int(input("Enter number: "))
                if player_input == 0:
                    self.__go_on_adventure()
                elif player_input == 1:
                    self.__visit_vendor()
                elif player_input == 2:
                    self.__print_player_info()
