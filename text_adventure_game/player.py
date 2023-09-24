from text_adventure_game.inventory_system import InventorySystem
from text_adventure_game.levelling_system import LevellingSystem
from text_adventure_game.damageable_object import DamageableObject
import helpers


class Player(DamageableObject):
    def __init__(self, max_health):
        super().__init__(max_health)
        self.gold = 0
        self.inventory = InventorySystem()
        self.levelling = LevellingSystem(100, 0.07, 2)
        self.levelling.level_up_event.on_change += self.__on_level_up

    def __del__(self):
        self.levelling.level_up_event.on_change -= self.__on_level_up

    def has_enough_gold(self, amount):
        return self.gold >= amount

    def give_gold(self, amount):
        self.gold += amount

    def remove_gold(self, amount):
        if not self.has_enough_gold(amount):
            return
        self.gold -= amount

    def __on_level_up(self, times_levelled_up):
        gold_reward = times_levelled_up * 50
        helpers.print_string_section('-', [
            f"Player levelled up {times_levelled_up} times!",
            f"+{gold_reward} gold"
        ])
        self.give_gold(gold_reward)
