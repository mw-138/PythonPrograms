import random
import helpers

from text_adventure_game.item_list import item_list
from text_adventure_game.inventory_slot import InventorySlot
from text_adventure_game.inventory_item import InventoryItem


class InventorySystem:
    def __init__(self):
        self.slots = []
        self.luck_multiplier = 1

    def is_index_valid(self, index):
        return index >= 0 or index <= len(self.slots) - 1

    def does_item_exist(self, identifier):
        return identifier in item_list

    def get_item_total(self, identifier):
        total = 0
        for slot in self.slots:
            if slot.identifier == identifier:
                total += slot.count
        return total

    def has_enough_of_item(self, identifier, amount):
        return self.get_item_total(identifier) >= amount

    def get_item(self, identifier) -> InventoryItem | None:
        if not self.does_item_exist(identifier):
            return None
        return item_list[identifier]

    def get_random_item_identifier(self, amount=1):
        population = []
        weights = []
        for key in item_list:
            item = item_list[key]
            population.append(key)
            weights.append(item.chance * self.luck_multiplier)
        choices = random.choices(population=population, weights=weights, k=amount)
        return choices[0] if amount == 1 else choices

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
            self.__handle_slot_overflow(slot, False)
        else:
            for _ in range(amount):
                self.__add_new_slot(identifier, 1)

        print(f"Received '{amount}' of item '{identifier}'")

        return True

    def __add_new_slot(self, identifier, amount) -> InventorySlot:
        item = self.get_item(identifier)
        slot = InventorySlot(identifier, item, amount)
        self.slots.append(slot)
        return slot

    def remove_item(self, identifier, amount):
        if not self.has_enough_of_item(identifier, amount):
            return False

        slot = self.__get_slot_for_item(identifier)
        slot.count -= amount
        self.__handle_slot_overflow(slot, True)

        print(f"Removed '{amount}' of item '{identifier}'")

        return True

    def __handle_slot_overflow(self, slot: InventorySlot, is_removing_item: bool):
        if not is_removing_item:
            if slot.count < slot.item.max_stack:
                return
            slot.count = slot.item.max_stack
        else:
            if slot.count <= 0:
                self.slots.remove(slot)

    def add_random_item(self, amount):
        identifier = self.get_random_item_identifier()
        self.add_item(identifier, amount)

    def randomize_inventory(self, amount):
        for _ in range(amount):
            self.add_random_item(helpers.random_inclusive(1, 10))
