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
        item = self.get_item(identifier)
        is_stackable = item.max_stack != 1

        if is_stackable:
            if slot is None:
                slot = self.__add_new_slot(identifier, amount)
            else:
                slot.count += amount
            self.__handle_slot_overflow(slot)
        else:
            for _ in range(amount):
                self.__add_new_slot(identifier, 1)

        print(f"Received '{amount}' of item '{identifier}'")

        return True

    def __add_new_slot(self, identifier, amount) -> InventorySlot:
        slot = InventorySlot(identifier, amount)
        self.slots.append(slot)
        return slot

    def __handle_slot_overflow(self, slot: InventorySlot):
        item = self.get_item(slot.identifier)

        if slot.count < item.max_stack:
            return

        slot.count = item.max_stack

        # count_diff = abs(slot.count - item.max_stack)
        # slot.count = item.max_stack
        # if count_diff > 0:
        #     self.__add_new_slot(slot.identifier, count_diff)

    def add_random_item(self, amount):
        identifier = self.get_random_item_identifier()
        self.add_item(identifier, amount)
