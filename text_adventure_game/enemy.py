class Enemy:
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def is_dead(self):
        return self.health <= 0

    def deal_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
