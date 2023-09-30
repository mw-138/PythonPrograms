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


def clamp(n, min_value, max_value):
    if n < min_value:
        return min_value
    elif n > max_value:
        return max_value
    return n


def does_file_exist(file_name):
    return os.path.exists(file_name)


def save_to_file(file_name, content):
    file_action = "w" if does_file_exist(file_name) else "x"
    with open(file_name, file_action) as file:
        file.write(content)


def is_list_index_valid(list_to_check, index):
    return index >= 0 or index <= len(list_to_check) - 1


def dictionary_to_random_choices(dictionary):
    population = []
    weights = []
    for key in dictionary:
        value = dictionary[key]
        population.append(key)
        weights.append(value)
    return population, weights
