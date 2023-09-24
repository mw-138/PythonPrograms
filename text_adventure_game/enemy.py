import math
import helpers
from text_adventure_game.damageable_object import DamageableObject


class Enemy(DamageableObject):
    def __init__(self, max_health, damage, level):
        super().__init__(max_health)
        self.damage = damage
        self.level = level

    @staticmethod
    def generate_random(player_level):
        player_level += 1
        random_level = helpers.random_inclusive(1, player_level)
        random_max_health = math.ceil(math.pow(random_level / 0.08, 1.6))
        random_damage = math.ceil(math.pow(random_level / 0.02, 0.5))
        return Enemy(random_max_health, random_damage, random_level)
