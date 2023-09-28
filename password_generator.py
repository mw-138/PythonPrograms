import random


class PasswordGenerator:
    def __init__(self, length):
        self.length = length
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!£$%^&*"
        password = ""
        for _ in range(self.length):
            char = random.choice(self.chars)
            password += char
        print(f"Password: {password}")
