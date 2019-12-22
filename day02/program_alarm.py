def intcode_as_array():
    with open('input.txt') as file:
        int_list = (list(map(int, file.read().split(","))))
    return int_list


def list_operation(noun=12, verb=2):
    intcode_list = intcode_as_array()

    # Preliminary data swap as requested by puzzle
    intcode_list[1] = noun
    intcode_list[2] = verb

    # Looping through list, performing operations
    for index in range(0, len(intcode_list) - 1, 4):
        opcode = intcode_list[index]
        if opcode == 99:
            break
        input_one = intcode_list[index + 1]
        input_two = intcode_list[index + 2]
        output_index = intcode_list[index + 3]

        if opcode == 1:
            intcode_list[output_index] = (intcode_list[input_one] +
                                          intcode_list[input_two])
        elif opcode == 2:
            intcode_list[output_index] = (intcode_list[input_one] *
                                          intcode_list[input_two])
        else:  # Any other opcode read results in an error
            return "This program has encountered an error"

    return intcode_list[0]


def search_noun_verb():
    for noun in range(100):
        for verb in range(100):
            if(list_operation(noun, verb) == 19690720):
                return 100 * noun + verb


if __name__ == '__main__':
    print(list_operation())  # part 1
    print(search_noun_verb())  # part 2
