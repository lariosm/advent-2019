def possible_password_combinations():
    count = 0  # Tracks number of passwords meeting criteria in puzzle
    puzzle_input = list(map(int, "193651-649729".split("-")))
    for i in range(puzzle_input[0], puzzle_input[1] + 1, 1):
        if(password_criteria(i)):
            count += 1
    return count


if __name__ == '__main__':
    print(possible_password_combinations())  # part 1


# -----Helper functions-----
def is_six_digits(number):
    return len(str(number)) == 6


def contains_adjacent_digits(number):
    digits = list(str(number))
    for i in range(len(digits) - 1):
        if(digits[i] == digits[i + 1]):
            return True
    return False


def digit_increase_check(number):
    digits = list(str(number))
    for i in range(len(digits) - 1):
        if(digits[i + 1] < digits[i]):
            return False
    return True


def password_criteria(number):
    return (is_six_digits(number) and contains_adjacent_digits(number) and
            digit_increase_check(number))


def contains_special_adjacent_digits(number):
    digits = list(str(number))
    for i in range(0, len(digits) - 1, 2):
        if(digits[i] != digits[i + 1]):
            return False
    '''
    if(digits[0] == digits[1]):
        if(digits[2] == digits[3]):
            if(digits[4] == digits[5]):
                return True
    '''
    return True
