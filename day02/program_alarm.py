def intcode_as_array():
    with open('input.txt') as file:
        int_list = (list(map(int, file.read().split(","))))
    return int_list
