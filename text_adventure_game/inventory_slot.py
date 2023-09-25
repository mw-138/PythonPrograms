class InventorySlot:
    def __init__(self, identifier, item, count):
        self.identifier = identifier
        self.item = item
        self.count = count
        self.is_equipped = False

    def equip(self):
        self.is_equipped = True

    def unequip(self):
        self.is_equipped = False
