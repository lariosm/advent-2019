import re


def inputs_to_arrays():
    with open('input.txt') as file:
        input_one, input_two = file.read().split()
        input_one, input_two = (list(map(str, input_one.split(","))),
                                list(map(str, input_two.split(","))))
        # Testing lists have been split up correctly
        assert input_one[0] == "R990"
        assert input_two[0] == "L998"
        assert input_one[len(input_one) - 1] == "R259"
        assert input_two[len(input_two) - 1] == "L719"
    return input_one, input_two


def wire_map(wire):
    path = [(0, 0)]
    for turn in wire:
        # number of steps to move
        steps = int(re.search(r'\d+', turn).group())
        # coordinates of current iteration
        coord = path[len(path) - 1]
        if "U" in turn:
            # incrementally appends coordinates of each step to list
            for i in range(1, steps + 1, 1):
                path.append((coord[0], coord[1] + i))
        elif "D" in turn:
            for i in range(1, steps + 1, 1):
                path.append((coord[0], coord[1] - i))
        elif "L" in turn:
            for i in range(1, steps + 1, 1):
                path.append((coord[0] - i, coord[1]))
        elif "R" in turn:
            for i in range(1, steps + 1, 1):
                path.append((coord[0] + i, coord[1]))
    path.pop(0)  # Removes (0, 0) from path list
    return path


def manhattan_distance(wire_intersections):
    # Start with an arbitraily large number as min distance
    min_distance = 100000000
    for point in wire_intersections:
        # Manhattan distance formula
        distance = abs(0 - point[0]) + abs(0 - point[1])
        if distance < min_distance:
            min_distance = distance
    return min_distance


if __name__ == '__main__':
    wire_one, wire_two = inputs_to_arrays()
    wire_map_one = set(wire_map(wire_one))
    wire_map_two = set(wire_map(wire_two))
    # Finds intersections between two wires
    intersections = wire_map_one.intersection(wire_map_two)
    shortest_distance = manhattan_distance(intersections)
    print("Manhattan distance:")
    print(shortest_distance)
