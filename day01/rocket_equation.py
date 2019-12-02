import math


def fuel_calculator(module_mass):
    return math.floor(module_mass / 3) - 2


def file_list():
    with open('input.txt') as file:
        values = [int(value.rstrip()) for value in file]
    return values[0]
