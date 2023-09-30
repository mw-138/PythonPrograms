import random
from enum import Enum

import helpers
from text_adventure_game.levelling_system import LevellingSystem


class ItemRarity(Enum):
    Common = 1,
    Uncommon = 2,
    Rare = 3,
    Epic = 4,
    Legendary = 5


rarity_weights = {
    ItemRarity.Common: 80,
    ItemRarity.Uncommon: 70,
    ItemRarity.Rare: 50,
    ItemRarity.Epic: 10,
    ItemRarity.Legendary: 5
}


# TODO: Make rarity weight chances increase based on player level
class InventoryItem:
    def __init__(self, label, max_stack, rarity, sell_price, chance):
        self.label = label
        self.max_stack = max_stack
        self.rarity = rarity
        self.sell_price = sell_price
        self.chance = chance
        self.can_be_equipped = False

    def _generate_random_rarity(self):
        population, weights = helpers.dictionary_to_random_choices(rarity_weights)
        random_rarity = random.choices(weights=weights, population=population, k=1)[0]
        return random_rarity


class WeaponInventoryItem(InventoryItem):
    def __init__(self, label, max_stack, max_level, sell_price, chance, damage):
        super().__init__(label, max_stack, self._generate_random_rarity(), sell_price, chance)
        self.damage = damage
        self.can_be_equipped = True
        self.levelling = LevellingSystem(max_level, 0.07, 2)


class ArmorInventoryItem(InventoryItem):
    def __init__(self, label, max_stack, max_level, sell_price, chance, protection):
        super().__init__(label, max_stack, self._generate_random_rarity(), sell_price, chance)
        self.protection = protection
        self.can_be_equipped = True
        self.levelling = LevellingSystem(max_level, 0.07, 2)


class HealingInventoryItem(InventoryItem):
    def __init__(self, label, max_stack, rarity, sell_price, chance, heal_amount):
        super().__init__(label, max_stack, rarity, sell_price, chance)
        self.heal_amount = heal_amount
