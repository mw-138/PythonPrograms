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


def input_section(title, char, items):
    index = 0
    strings = [title]
    indexes = []
    for item in items:
        string = f"[{index}] {item['text']}"
        strings.append(string)
        indexes.append(index)
        index += 1
    print_string_section(char, strings)
    try:
        index_input = int(input("Enter number: "))
        if index_input in indexes and items[index_input]['func']:
            items[index_input]['func']()
        else:
            print("no func")
    except ValueError:
        print("Invalid input")


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
