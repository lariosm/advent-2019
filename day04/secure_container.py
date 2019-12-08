import re


def possible_password_combinations():
    count = 0  # Tracks number of passwords meeting criteria in puzzle
    puzzle_input = list(map(int, "193651-649729".split("-")))
    for i in range(puzzle_input[0], puzzle_input[1] + 1, 1):
        if(password_criteria(i)):
            print(i)
            count += 1
    return count


# -----Helper functions-----
def is_six_digits(number):
    return len(str(number)) == 6


def contains_adjacent_digits(number):
    match = re.findall('00+|11+|22+|33+|44+|55+|66+|77+|88+|99+', str(number))
    if match:
        return True
    
    return False


def digit_increase_check(number):
    digits = list(str(number))
    for i in range(len(digits) - 1):
        if(digits[i + 1] < digits[i]):
            return False
    return True


def password_criteria(number):
    return (is_six_digits(number) and
            # contains_adjacent_digits(number) and
            contains_matching_adjacent_digits(number) and  # Part 2
            digit_increase_check(number))


# Part 2
def contains_matching_adjacent_digits(number):
    digits = list(str(number))
    for digit in digits:
        count = digits.count(digit)
        if count == 2:
            return True
    return False


# Answer should be 1102
# -----Main-----
if __name__ == '__main__':
    print(possible_password_combinations())
