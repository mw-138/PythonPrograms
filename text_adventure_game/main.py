import random
import time
import helpers
from enum import Enum
from text_adventure_game.player import Player
from text_adventure_game.enemy import Enemy
from text_adventure_game.inventory_item import ItemRarity, WeaponInventoryItem


class AdventureScenario(Enum):
    FOUND_ENEMY = 1
    FOUND_ITEM = 2


class TextAdventureGame:
    def __init__(self):
        self.player = Player(100)
        self.revive_cost = 100

    def __print_player_info(self):
        ply = self.player
        lvl = ply.levelling
        helpers.print_string_section('-', [
            f"HP: {ply.current_health:,}/{ply.max_health:,} {ply.get_health_progress_bar()}",
            f"Gold: {ply.gold:,}",
            f"Level: {lvl.get_current_level():,} -> "
            f"{lvl.experience:,}/{lvl.get_experience_for_next_level():,} -> "
            f"{lvl.get_experience_progress()}% {lvl.get_experience_progress_bar()}"
        ])

    def __print_player_inventory(self):
        formatted_inventory = [f"Inventory ({len(self.player.inventory.slots)}):\n"]
        for inv_slot in self.player.inventory.slots:
            item = self.player.inventory.get_item(inv_slot.identifier)
            base_str = f"x{inv_slot.count:,} {ItemRarity(item.rarity.value).name} {item.label} (Value: {item.sell_price * inv_slot.count:,})"
            if type(item) == WeaponInventoryItem:
                formatted_inventory.append(f"{base_str} (DMG: {item.damage:,})")
            else:
                formatted_inventory.append(base_str)
        helpers.print_string_section('-', formatted_inventory)

    def __do_return_countdown(self, timer):
        for _ in range(timer, 0, -1):
            print(f"Returning in {_}...")
            time.sleep(1)

    def __generate_random_enemy(self):
        return Enemy.generate_random(self.player.levelling.get_current_level())

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

                if player_turn:
                    enemy.deal_damage(player_damage)
                else:
                    self.player.deal_damage(enemy.damage)

                helpers.print_string_section('-', [
                    f"Player dealt {player_damage:,} damage to enemy" if player_turn else f"Enemy dealt {enemy.damage:,} damage to player",
                    f"Player: {self.player.current_health:,}/{self.player.max_health:,} {self.player.get_health_progress_bar()}",
                    f"Enemy: {enemy.current_health:,}/{enemy.max_health:,} {enemy.get_health_progress_bar()}",
                ])

                time.sleep(1)
                player_turn = not player_turn

                if self.player.is_dead():
                    print(f"Player died while fighting enemy")
                    break

            if enemy.is_dead():
                gold_reward = helpers.random_inclusive(3, 9)
                exp_reward = helpers.random_inclusive(1, 100)
                helpers.print_string_section('-', [
                    "Enemy died!",
                    f"+{gold_reward:,} gold",
                    f"+{exp_reward:,} experience"
                ])
                self.player.give_gold(gold_reward)
                self.player.levelling.give_experience(exp_reward)
        elif scenario == AdventureScenario.FOUND_ITEM:
            self.player.inventory.add_random_item(1)

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

    def __heal_player_for_gold(self):
        if self.player.current_health < self.player.max_health:
            if self.player.has_enough_gold(self.player.get_revive_cost()):
                self.player.revive()
                self.player.remove_gold(self.player.get_revive_cost())
            else:
                helpers.print_string_section('-', ["You don't have enough gold to heal!"])
        else:
            helpers.print_string_section('-', ["You don't need to heal!"])

    def start(self):
        while True:
            if self.player.is_dead():
                helpers.print_string_section('-', [
                    "What do you want to do?",
                    f"[0] Heal for {self.revive_cost:,} gold",
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
                    "[2] View Stats",
                    "[3] View Inventory",
                    f"[4] Heal for {self.player.get_revive_cost():,} gold"
                ])
                player_input = int(input("Enter number: "))
                if player_input == 0:
                    self.__go_on_adventure()
                elif player_input == 1:
                    self.__visit_vendor()
                elif player_input == 2:
                    self.__print_player_info()
                elif player_input == 3:
                    self.__print_player_inventory()
                elif player_input == 4:
                    self.__heal_player_for_gold()
