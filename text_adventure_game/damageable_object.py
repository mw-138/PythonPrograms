import helpers


class DamageableObject:
    def __init__(self, max_health):
        self.max_health = max_health
        self.current_health = self.max_health

    def deal_damage(self, amount):
        self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0

    def heal(self, amount):
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def is_dead(self):
        return self.current_health <= 0

    def revive(self):
        if not self.is_dead():
            return
        self.current_health = self.max_health

    def get_health_progress_bar(self):
        return helpers.progress_bar(self.current_health, self.max_health)
