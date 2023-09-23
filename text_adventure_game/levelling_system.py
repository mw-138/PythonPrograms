import math


class LevellingSystem:
    def __init__(self, max_level, constant, power):
        self.max_level = max_level
        self.constant = constant
        self.power = power
        self.experience = 0
        self.starting_level = 1

    def get_current_level(self):
        return self.starting_level + math.floor(self.constant * math.sqrt(self.experience))

    def get_previous_level(self):
        level = self.get_current_level()
        return self.starting_level if level <= self.starting_level else level - 1

    def get_next_level(self):
        return self.max_level if self.has_reached_max_level() else self.get_current_level() + 1

    def has_reached_max_level(self):
        return self.get_current_level() >= self.max_level

    def get_experience_for_level(self, level):
        return math.ceil(math.pow(level / self.constant, self.power))

    def get_experience_for_next_level(self):
        return self.get_experience_for_level(self.get_next_level())

    def get_experience_for_previous_level(self):
        return self.get_experience_for_level(self.get_previous_level())

    def give_experience(self, amount):
        if self.has_reached_max_level():
            return
        self.experience += amount

    def remove_experience(self, amount):
        if self.experience <= 0:
            return
        self.experience -= amount

    def get_experience_progress(self):
        return math.floor(self.experience / self.get_experience_for_next_level() * 100)

    def get_remaining_experience(self):
        return self.get_experience_for_next_level() - self.experience
