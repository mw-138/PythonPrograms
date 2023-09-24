import math
import helpers
from text_adventure_game.damageable_object import DamageableObject


class Enemy(DamageableObject):
    def __init__(self, max_health, damage, player_level):
        super().__init__(max_health)
        self.level = helpers.random_inclusive(1, player_level + 1)
        self.damage = damage

    @staticmethod
    def generate_random(player_level):
        player_level += 1
        enemy = Enemy(0, 0, player_level)
        random_max_health = math.ceil(math.pow(enemy.level / 0.08, 1.6))
        random_damage = math.ceil(math.pow(enemy.level / 0.02, 0.5))
        enemy.max_health = random_max_health
        enemy.current_health = enemy.max_health
        enemy.damage = random_damage
        return enemy
