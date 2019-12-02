import math


def fuel_calculator(module_mass):
    """
    returns amount of fuel needed for a given module.
    Parameters:
    module_mass (int): mass of module

    Returns:
    int: Amount of fuel needed for the module
    """
    return math.floor(module_mass / 3) - 2


def fuel_requirement_sum():
    """returns sum amount of fuel needed for all modules"""
    fuel_counter = 0  # Tracks total sum of fuel needed for all modules

    with open('input.txt') as file:
        for value in file:
            fuel_counter += fuel_calculator(int(value.rstrip()))
    return fuel_counter


if __name__ == '__main__':
    print(fuel_requirement_sum())
