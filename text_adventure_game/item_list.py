from text_adventure_game.inventory_item import InventoryItem, ItemRarity, WeaponInventoryItem, ArmorInventoryItem, \
    HealingInventoryItem

__max_item_stack = 99999
__max_item_level = 100

item_list = {
    "old_boot": InventoryItem(
        "Old Boot",
        __max_item_stack,
        ItemRarity.Common,
        100,
        1
    ),
    "longsword": WeaponInventoryItem(
        "Longsword",
        1,
        __max_item_level,
        1000,
        20,
        50
    ),
    "helmet": ArmorInventoryItem(
        "Helmet",
        1,
        __max_item_level,
        750,
        10,
        30
    ),
    "lesser_healing_potion": HealingInventoryItem(
        "Lesser Healing Potion",
        __max_item_stack,
        ItemRarity.Common,
        10,
        40,
        5
    ),
    "greater_healing_potion": HealingInventoryItem(
        "Greater Healing Potion",
        __max_item_stack,
        ItemRarity.Rare,
        10,
        25,
        15
    ),
    "superior_healing_potion": HealingInventoryItem(
        "Superior Healing Potion",
        __max_item_stack,
        ItemRarity.Epic,
        10,
        20,
        30
    ),
    "pot_of_healing": HealingInventoryItem(
        "Pot of Healing",
        __max_item_stack,
        ItemRarity.Legendary,
        10,
        5,
        100
    )
}
