from text_adventure_game.damageable_object import DamageableObject


class Enemy(DamageableObject):
    def __init__(self, max_health, damage):
        super().__init__(max_health)
        self.damage = damage
