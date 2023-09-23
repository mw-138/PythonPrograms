from enum import Enum


class ItemRarity(Enum):
    Common = 1,
    Uncommon = 2,
    Rare = 3,
    Epic = 4,
    Legendary = 5


class InventoryItem:
    def __init__(self, label, max_stack, rarity):
        self.label = label
        self.max_stack = max_stack
        self.rarity = rarity
