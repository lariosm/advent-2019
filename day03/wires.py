import re

wire_one = ["R8", "U5", "L5", "D3"]
wire_two = ["U7", "R6", "D4", "L4"]


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


def find_intersections(wire_map, wire_map_two):
    intersections = []
    for location in wire_map:
        for location_two in wire_map_two:
            if location == location_two:
                intersections.append(location)
    return intersections


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
    wire_map_one = wire_map(wire_one)
    wire_map_two = wire_map(wire_two)
    intersection_map = find_intersections(wire_map_one, wire_map_two)
    shortest_distance = manhattan_distance(intersection_map)
    print("Wire 1:")
    print(wire_map_one)
    print("\n")
    print("Wire 2:")
    print(wire_map_two)
    print("\n")
    print("Intersection list:")
    print(intersection_map)
    print("\n")
    print("Manhattan distance:")
    print(shortest_distance)
