INPUT = [7, 14, 0, 17, 11, 1, 2]


def get_next_num(occurences):
    return occurences[-1] - occurences[-2] if len(occurences) > 1 else 0


def determine_the_nth_number(input, num):
    mem = {
    }
    for n in input:
        mem[n] = [input.index(n)]
    last_num = input[-1]
    for i in range(0, num - len(input)):
        index = len(input) + i
        last_num = get_next_num(mem[last_num] or [])
        indexes = mem.get(last_num) or []
        indexes.append(index)
        mem[last_num] = indexes[-2:] if len(indexes) > 2 else indexes
    print(last_num)


if __name__ == '__main__':
    determine_the_nth_number(INPUT, 30000000)
