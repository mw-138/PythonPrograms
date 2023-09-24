from text_adventure_game.inventory_item import InventoryItem, ItemRarity, WeaponInventoryItem, ArmorInventoryItem

__max_item_stack = 99999

item_list = {
    "old_boot": InventoryItem("Old Boot", __max_item_stack, ItemRarity.Common, 1),
    "longsword": WeaponInventoryItem("Longsword", 1, ItemRarity.Legendary, 1000, 50),
    "helmet": ArmorInventoryItem("Helmet", 1, ItemRarity.Rare, 750, 30)
}
