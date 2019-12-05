def is_six_digits(number):
    return len(str(number)) == 6


def contains_adjacent_digits(number):
    digits = list(str(number))
    for i in range(len(digits) - 1):
        if(digits[i] == digits[i + 1]):
            return True
    return False


def password_criteria():
    puzzle_input = list(map(int, "193651-649729".split("-")))
    for i in range(puzzle_input[0], puzzle_input[1] + 1, 1):
        if(i == 193651):
            print("193651 was read")
        if(i == 649729):
            print("649729 was read")


if __name__ == '__main__':
    password_criteria()
