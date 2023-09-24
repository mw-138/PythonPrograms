import math

from text_adventure_game.damageable_object import DamageableObject


class Enemy(DamageableObject):
    def __init__(self, max_health, damage):
        super().__init__(max_health)
        self.damage = damage

    @staticmethod
    def generate_random(player_level):
        player_level += 1
        random_max_health = math.ceil(math.pow(player_level / 0.08, 2))
        random_damage = math.ceil(math.pow(player_level / 0.02, 0.5))
        return Enemy(random_max_health, random_damage)
