import random


class PasswordGenerator:
    def __init__(self, length):
        self.length = length
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!£$%^&*"

    def generate(self):
        password = ""
        for _ in range(self.length):
            char = self.chars[random.randrange(0, len(self.chars))]
            password += char
        print(f"Password: {password}")
