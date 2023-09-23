from quiz import Quiz, Question
from blackjack import Blackjack
from number_guesser import NumberGuesser
from password_generator import PasswordGenerator
from hangman import Hangman
from timer import Timer
from rock_paper_scissors import RockPaperScissors
from contact_book import ContactBook
from request_testing import TestRequest
from qr_code_generator import QRCodeGenerator
from text_adventure_game.text_adventure_game import TextAdventureGame


# Quiz([
#     Question("What is 2+2?", "4"),
#     Question("What is the capital of England?", "London")
# ]).start()

# Blackjack().start()

# NumberGuesser(100).start()

# PasswordGenerator(100).generate()

# Hangman(["secret", "hello", "world"]).start()

# Timer(1, 2, 0).start()

# RockPaperScissors().start()

# ContactBook().start()

# TestRequest().start()

# QRCodeGenerator("https://www.google.co.uk").generate()

TextAdventureGame().start()
