import random

from text_adventure_game.item_list import item_list
from text_adventure_game.inventory_slot import InventorySlot
from text_adventure_game.inventory_item import InventoryItem


class InventorySystem:
    def __init__(self, max_slots):
        self.max_slots = max_slots
        self.slots = []

    def does_item_exist(self, identifier):
        return identifier in item_list

    def get_item(self, identifier) -> InventoryItem | None:
        if not self.does_item_exist(identifier):
            return None
        return item_list[identifier]

    def get_random_item_identifier(self):
        return random.choice(list(item_list.keys()))

    def __get_slot_for_item(self, identifier) -> InventorySlot | None:
        for slot in self.slots:
            if slot.identifier == identifier:
                return slot
        return None

    def add_item(self, identifier, amount):
        if not self.does_item_exist(identifier):
            return False

        slot = self.__get_slot_for_item(identifier)

        if slot is None:
            slot = InventorySlot(identifier, amount)
            self.slots.append(slot)
        else:
            slot.count += amount

        print(f"Received '{amount}' of item '{identifier}'")

        return True

    def add_random_item(self, amount):
        identifier = self.get_random_item_identifier()
        self.add_item(identifier, amount)
