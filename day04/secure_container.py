def possible_password_combinations():
    count = 0  # Tracks number of passwords meeting criteria in puzzle
    puzzle_input = list(map(int, "193651-649729".split("-")))
    for i in range(puzzle_input[0], puzzle_input[1] + 1, 1):
        if(password_criteria(i)):
            count += 1
    return count


# -----Helper functions-----
# Part 1
def contains_adjacent_digits(number):
    digits = list(str(number))
    for digit in digits:
        count = digits.count(digit)
        if count >= 2:
            return True
    return False


def digit_increase_check(number):
    digits = list(str(number))
    return digits == sorted(digits)


def password_criteria(number):
    return (contains_matching_adjacent_digits(number) and  # Part 2
            digit_increase_check(number))


# Part 2
def contains_matching_adjacent_digits(number):
    digits = list(str(number))
    for digit in digits:
        count = digits.count(digit)
        if count == 2:  # is there at least one pair of matching digits
            return True
    return False


# -----Main-----
if __name__ == '__main__':
    print(possible_password_combinations())
