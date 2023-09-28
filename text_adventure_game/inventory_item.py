from enum import Enum


class ItemRarity(Enum):
    Common = 1,
    Uncommon = 2,
    Rare = 3,
    Epic = 4,
    Legendary = 5


__rarity_weights = {
    ItemRarity.Common: 80,
    ItemRarity.Uncommon: 70,
    ItemRarity.Rare: 50,
    ItemRarity.Epic: 10,
    ItemRarity.Legendary: 5
}


# TODO: Make rarity weight chances increase based on player level
# TODO: Maybe add levelling to item
# TODO: Remove rarity from constructor, add weighted chances to rarity and give item random rarity on construction
class InventoryItem:
    def __init__(self, label, max_stack, rarity, sell_price, chance):
        self.label = label
        self.max_stack = max_stack
        self.rarity = rarity
        self.sell_price = sell_price
        self.chance = chance
        self.can_be_equipped = False


class WeaponInventoryItem(InventoryItem):
    def __init__(self, label, max_stack, rarity, sell_price, chance, damage):
        super().__init__(label, max_stack, rarity, sell_price, chance)
        self.damage = damage
        self.can_be_equipped = True


class ArmorInventoryItem(InventoryItem):
    def __init__(self, label, max_stack, rarity, sell_price, chance, protection):
        super().__init__(label, max_stack, rarity, sell_price, chance)
        self.protection = protection
        self.can_be_equipped = True
