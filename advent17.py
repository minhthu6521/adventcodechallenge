INPUT = """####...#
......#.
#..#.##.
.#...#.#
..###.#.
##.###..
.#...###
.##....#"""


def add_to_dimension(dimensions):
    for d, all in dimensions.items():
        all.append(all[-1] + 1)
        all.insert(0, all[0] - 1)
        dimensions[d] = all
    return dimensions


def check_same_position(num1, num2):
    for k in num1.keys():
        if k != "value":
            if num1[k] != num2[k]:
                return False
    return True


def format_to_str(x, y, z, w):
    return "{},{},{},{}".format(str(x), str(y), str(z), str(w))


def get_compare_range(num):
    return num, num + 1, num - 1


def change_state(num, actives):
    is_active = num in actives
    count_active = 0
    coord = num.split(",")
    coord = [int(c) for c in coord]
    for x in get_compare_range(coord[0]):
        for y in get_compare_range(coord[1]):
            for z in get_compare_range(coord[2]):
                for w in get_compare_range(coord[3]):
                    num_to_check = format_to_str(x, y, z, w)
                    if num_to_check != num:
                        if num_to_check in actives:
                            count_active += 1
    if (not is_active and count_active == 3) or (is_active and count_active in (2, 3)):
        return True


def expand_dimension(actives, dimensions):
    dimensions = add_to_dimension(dimensions)
    result = []
    for x in dimensions["x"]:
        for y in dimensions["y"]:
            for z in dimensions["z"]:
                for w in dimensions["w"]:
                    possible = format_to_str(x, y, z, w)
                    is_active = change_state(possible, actives)
                    if is_active:
                        result.append(possible)
    return result, dimensions


def input_to_actives(input):
    actives = []
    for y_index, y in enumerate(input):
        for x_index, x in enumerate(y):
            if x == "#":
                active = format_to_str(x_index, y_index, 0, 0)
                actives.append(active)
    return actives


def execute(input, cycle):
    dimension = {
        "x": list(range(0, len(input[0]))),
        "y": list(range(0, len(input))),
        "z": [0],
        "w": [0]
    }
    actives = input_to_actives(input)
    for i in range(0, cycle):
        actives, dimension = expand_dimension(actives, dimension)
    return len(actives)


if __name__ == '__main__':
    input = INPUT.split("\n")
    print(execute(input, 6))
