import math

INPUT = """1005162
19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,823,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,443,x,x,x,x,x,37,x,x,x,x,x,x,13"""


def part1(time, buses):
    buses = [int(bus) for bus in buses if bus != "x"]
    while (True):
        for bus in buses:
            if time % bus == 0:
                return bus, time
        time += 1


def find_largest(buses):
    largest_index = 0
    largest = int(buses[0])
    for index, bus in enumerate(buses):
        if bus != "x" and int(bus) > largest:
            largest = int(bus)
            largest_index = index
    return largest, largest_index


def find_match(pair, iteration, start):
    while start < (iteration * pair[0]):
        start = start + iteration
        if start % pair[0] == pair[1]:
            return start


def part2(buses):
    to_pair = []
    for index, bus in enumerate(buses):
        if bus != "x":
            to_pair.append((int(bus), index - int(bus) * math.floor(index / int(bus))))
    to_pair = sorted(to_pair, key=lambda x: x[0])
    iteration = 1
    start = 1
    for pair in to_pair:
        start = find_match(pair, iteration, start)
        iteration = iteration * pair[0]
    return iteration - start


if __name__ == '__main__':
    [possible_depart_time, buses] = INPUT.split("\n")
    possible_depart_time = int(possible_depart_time)
    buses = buses.split(",")
    # bus, time = part1(possible_depart_time, buses)
    # print(bus * (time - possible_depart_time))
    print(part2(buses))
