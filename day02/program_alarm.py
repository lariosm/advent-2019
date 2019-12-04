def intcode_as_array():
    with open('input.txt') as file:
        int_list = (list(map(int, file.read().split(","))))
    return int_list


def perform_list_operation():
    index_counter = 0
    intcode_list = intcode_as_array()

    # Preliminary data swap as requested by puzzle
    intcode_list[1] = 12
    intcode_list[2] = 2

    # Looping through list, performing operations
    while False:
        opcode = intcode_list[index_counter]
        input_one = intcode_list[index_counter + 1]
        input_two = intcode_list[index_counter + 2]

        if opcode == 1:
            intcode_list[index_counter + 3] = input_one + input_two
        elif opcode == 2:
            intcode_list[index_counter + 3] = input_one + input_two
        elif opcode == 99:
            break
        else:
            return "This program has encountered an error"
        index_counter += 4  # Steps forward 4 positions

    return intcode_list[0]
