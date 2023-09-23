from text_adventure_game.inventory_item import InventoryItem, ItemRarity, WeaponInventoryItem

__max_item_stack = 1000

item_list = {
    "old_boot": InventoryItem("Old Boot", __max_item_stack, ItemRarity.Common, 1),
    "longsword": WeaponInventoryItem("Longsword", 1, ItemRarity.Legendary, 1000, 50)
}
