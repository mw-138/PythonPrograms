import os
import random


def get_list_max_length(strings):
    return len(max(strings, key=len))


def print_string_section(char, strings):
    max_width = get_list_max_length(strings)
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
