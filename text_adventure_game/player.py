from text_adventure_game.inventory_system import InventorySystem
from text_adventure_game.levelling_system import LevellingSystem


class Player:
    def __init__(self, starting_health):
        self.max_health = starting_health
        self.current_health = self.max_health
        self.gold = 0
        self.inventory = InventorySystem()
        self.levelling = LevellingSystem(100, 0.07, 2)

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
