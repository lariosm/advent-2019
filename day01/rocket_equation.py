import math


def fuel_calculator(module_mass):
    """returns amount of fuel needed for a given module"""
    return math.floor(module_mass / 3) - 2


def fuel_requirement_sum():
    """returns sum amount of fuel needed for all modules"""
    fuel_counter = 0  # Tracks total sum of fuel needed

    with open('input.txt') as file:
        for value in file:
            fuel_counter += fuel_calculator(int(value.rstrip()))
    return fuel_counter


def module_with_fuel_cost(fuel_mass, fuel_sum=0):
    """returns amount of fuel needed for a given module with added fuel mass"""
    if fuel_mass <= 0:
        return fuel_sum
    else:
        required_fuel = fuel_calculator(fuel_mass)
        return module_with_fuel_cost(required_fuel, fuel_sum +
                                     max(0, required_fuel))


if __name__ == '__main__':
    print(fuel_requirement_sum())  # Part 1
