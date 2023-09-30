import random
import time
import helpers
from enum import Enum
from text_adventure_game.player import Player
from text_adventure_game.enemy import Enemy
from text_adventure_game.inventory_item import ItemRarity, WeaponInventoryItem, ArmorInventoryItem, HealingInventoryItem


class AdventureScenario(Enum):
    FOUND_ENEMY = 1
    FOUND_ITEM = 2


class TextAdventureGame:
    def __init__(self):
        self.player = Player(100, 10)
        self.revive_cost = 100
        self.is_game_active = True
        self.__start()

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

    def __open_player_inventory(self):
        formatted_inventory = [f"Inventory ({len(self.player.inventory.slots)}):\n"]
        slot_index = 0

        for inv_slot in self.player.inventory.slots:
            item = inv_slot.item

            base_str = f"x{inv_slot.count:,} {ItemRarity(item.rarity.value).name} {item.label} (Value: {item.sell_price * inv_slot.count:,})"
            additional_str = base_str

            if inv_slot.is_equipped:
                additional_str = f"[Equipped] {additional_str}"

            if type(item) == WeaponInventoryItem:
                additional_str += f" (DMG: {item.damage:,})"
            elif type(item) == ArmorInventoryItem:
                additional_str += f" (Protection: {item.protection:,})"

            final_str = f"[{slot_index}] {additional_str}"
            formatted_inventory.append(final_str)
            slot_index += 1

        helpers.print_string_section('-', formatted_inventory)

        def __try_equip():
            try:
                item_index = int(input("Enter item index: "))

                if not self.player.inventory.is_index_valid(item_index):
                    print("Invalid item index")
                    return

                selected_slot = self.player.inventory.slots[item_index]

                if issubclass(type(selected_slot.item), WeaponInventoryItem):
                    self.player.equip_weapon_slot(selected_slot)
                elif issubclass(type(selected_slot.item), ArmorInventoryItem):
                    self.player.equip_helmet_slot(selected_slot)
            except ValueError:
                print("Invalid input")

        def __try_sell():
            try:
                item_index = int(input("Enter item index: "))

                if not self.player.inventory.is_index_valid(item_index):
                    print("Invalid item index")
                    return

                selected_slot = self.player.inventory.slots[item_index]
                amount_to_sell = int(input(f"Enter amount (Max: {selected_slot.count:,}): "))
                self.__sell_item(selected_slot, amount_to_sell)
            except ValueError:
                print("Invalid input")

        def __try_use():
            try:
                item_index = int(input("Enter item index: "))

                if not self.player.inventory.is_index_valid(item_index):
                    print("Invalid item index")
                    return

                selected_slot = self.player.inventory.slots[item_index]

                if issubclass(type(selected_slot.item), HealingInventoryItem):
                    heal_percentage = selected_slot.item.heal_amount
                    heal_amount = (self.player.current_health / self.player.max_health) * heal_percentage
                    self.player.heal(heal_amount)
                    self.player.inventory.remove_item(selected_slot.identifier, 1)
                    print(f"Healed player for {heal_amount} HP")
            except ValueError:
                print("Invalid input")

        helpers.input_section("Select action:", '-', [
            {"text": "Exit", "func": None},
            {"text": "Equip Item", "func": __try_equip},
            {"text": "Use Item", "func": __try_use},
            {"text": "Sell Item", "func": __try_sell},
        ])

    def __sell_item(self, slot, amount):
        if amount <= slot.count:
            sell_value = slot.item.sell_price * amount
            if self.player.inventory.remove_item(slot.identifier, amount):
                self.player.give_gold(sell_value)
                print(f"Sold x{amount:,} {slot.item.label} for {sell_value:,} gold")
            else:
                print(f"Unable to sell x{amount:,} {slot.item.label}")
        else:
            print(f"Unable to sell x{amount:,} {slot.item.label}")

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
            print("Found enemy!")
            enemy = self.__generate_random_enemy()
            player_turn = True
            while not enemy.is_dead():
                enemy.deal_damage(self.player.damage) if player_turn else self.player.deal_damage(enemy.damage)
                helpers.print_string_section('-', [
                    f"Player dealt {self.player.damage:,} damage to enemy" if player_turn else f"Enemy dealt {enemy.damage:,} damage to player",
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
            print("Found item!")
            self.player.inventory.add_random_item(1)

        self.__do_return_countdown(3)

    def __visit_vendor(self):
        print("Vendor currently unavailable")
        self.__do_return_countdown(3)
        # print("Visiting vendor...")
        # time.sleep(1)
        #
        # items = ["Item 1", "Item 2", "Item 3"]
        # input_entries = []
        #
        # for item in items:
        #     def buy_item():
        #         print(f"buying: {item}")
        #     input_entries.append({"text": item, "func": buy_item})
        #
        # helpers.input_section("What would you like to purchase?", '-', input_entries)

        # try:
        #     player_input = input("What would you like to purchase? (Enter 'x' to leave) ")
        #     if player_input.lower() == "x":
        #         return
        # except ValueError:
        #     print("Invalid input")

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

    def __attempt_player_revive(self):
        if self.player.has_enough_gold(self.revive_cost):
            self.player.revive()
        else:
            print("You don't have enough gold to revive. Game over.")
            self.is_game_active = False

    def __start(self):
        self.player.inventory.randomize_inventory(10)
        while self.is_game_active:
            if self.player.is_dead():
                helpers.input_section("What do you want to do?", '-', [
                    {"text": f"Heal for {self.revive_cost:,} gold", "func": self.__attempt_player_revive}
                ])
            else:
                helpers.input_section("What do you want to do?", '-', [
                    {"text": "Adventure", "func": self.__go_on_adventure},
                    {"text": "Vendor", "func": self.__visit_vendor},
                    {"text": "View Stats", "func": self.__print_player_info},
                    {"text": "View Inventory", "func": self.__open_player_inventory},
                    {"text": f"Heal for {self.player.get_revive_cost():,} gold", "func": self.__heal_player_for_gold},
                ])
