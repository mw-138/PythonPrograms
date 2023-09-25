import math

from text_adventure_game.inventory_system import InventorySystem
from text_adventure_game.inventory_slot import InventorySlot
from text_adventure_game.levelling_system import LevellingSystem
from text_adventure_game.damageable_object import DamageableObject
import helpers


class Player(DamageableObject):
    def __init__(self, max_health, damage):
        super().__init__(max_health)
        self.gold = 0
        self.inventory = InventorySystem()
        self.levelling = LevellingSystem(100, 0.07, 2)
        self.levelling.level_up_event.on_change += self.__on_level_up
        self.equipped_weapon_slot = None
        self.equipped_helmet_slot = None
        self.damage = damage

    def __del__(self):
        self.levelling.level_up_event.on_change -= self.__on_level_up

    def has_enough_gold(self, amount):
        return self.gold >= amount

    def give_gold(self, amount):
        self.gold += amount

    def remove_gold(self, amount):
        if not self.has_enough_gold(amount):
            return
        self.gold -= amount

    def __on_level_up(self, new_level):
        gold_reward = new_level * 50
        helpers.print_string_section('-', [
            f"Player is now level {new_level}!",
            f"+{gold_reward} gold"
        ])
        self.give_gold(gold_reward)

    def get_revive_cost(self):
        health_missing = self.max_health - self.current_health
        return int(math.pow(health_missing, 0.65))

    def equip_weapon_slot(self, slot: InventorySlot):
        self.equipped_weapon_slot = slot
        self.equipped_weapon_slot.equip()
        self.damage += self.equipped_weapon_slot.item.damage
        print(f"Equipped weapon: {self.equipped_weapon_slot.item.label}")

    def unequip_weapon_slot(self):
        self.damage -= self.equipped_weapon_slot.item.damage
        self.equipped_weapon_slot = None

    def equip_helmet_slot(self, slot: InventorySlot):
        self.equipped_helmet_slot = slot
        self.equipped_helmet_slot.equip()
        self.max_health += self.equipped_helmet_slot.item.protection
        print(f"Equipped helmet: {self.equipped_helmet_slot.item.label}")

    def unequip_helmet_slot(self):
        self.max_health -= self.equipped_helmet_slot.item.protection
        self.equipped_weapon_slot = None
