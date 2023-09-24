import os
import random


def print_string_section(char, strings):
    max_width = len(max(strings, key=len))
    to_print = char * max_width
    print(to_print)
    for entry in strings:
        print(entry)
    print(to_print)


def clear_terminal():
    print("\n" * 100)


def random_inclusive(start, stop):
    return random.randrange(start, stop + 1)


def progress_bar(current_value, max_value, bar_count=10):
    progress = (current_value / max_value) * bar_count
    retval = ""
    retval += "█" * int(progress)
    retval += "▒" * int(bar_count - progress)
    return retval


# def currency_format(value):
#