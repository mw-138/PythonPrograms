from enum import Enum


class ItemRarity(Enum):
    Common = 1,
    Uncommon = 2,
    Rare = 3,
    Epic = 4,
    Legendary = 5


class InventoryItem:
    def __init__(self, label, max_stack, rarity, sell_price, chance):
        self.label = label
        self.max_stack = max_stack
        self.rarity = rarity
        self.sell_price = sell_price
        self.chance = chance


class WeaponInventoryItem(InventoryItem):
    def __init__(self, label, max_stack, rarity, sell_price, chance, damage):
        super().__init__(label, max_stack, rarity, sell_price, chance)
        self.damage = damage


class ArmorInventoryItem(InventoryItem):
    def __init__(self, label, max_stack, rarity, sell_price, chance, protection):
        super().__init__(label, max_stack, rarity, sell_price, chance)
        self.protection = protection
