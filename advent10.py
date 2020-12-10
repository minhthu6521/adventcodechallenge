from copy import deepcopy

INPUT = """165
78
151
15
138
97
152
64
4
111
7
90
91
156
73
113
93
135
100
70
119
54
80
170
139
33
123
92
86
57
39
173
22
106
166
142
53
96
158
63
51
81
46
36
126
59
98
2
16
141
120
35
140
99
121
122
58
1
60
47
10
87
103
42
132
17
75
12
29
112
3
145
131
18
153
74
161
174
68
34
21
24
85
164
52
69
65
45
109
148
11
23
129
84
167
27
28
116
110
79
48
32
157
130"""


def get_difference(input, start=0):
    input = sorted(input)
    highest = input[-1] + 3
    input.append(highest)
    count = {}
    for i in input:
        diff = i - start
        count.setdefault(diff, 0)
        count[diff] += 1
        start = i
    return count


def get_possible_next(input, current):
    result = []
    for i in range(1, 4):
        if current + i < len(input) and input[current + i] - input[current] <= 3:
            result.append(input[current + i])
    return result

def add_to_ways(ways, current, solutions):
    if solutions:
        for solution in solutions:
            ways.setdefault(solution, 0)
            ways[solution] = ways[solution] + ways[current]
        ways.pop(current, None)
    return ways


def get_ways(input):
    input = input + [0, (max(input) + 3)]
    input = sorted(input)
    ways = {0: 1}
    for i in range(0, len(input)):
        solutions = get_possible_next(input, i)
        ways = add_to_ways(ways, input[i], solutions)
    return ways


if __name__ == '__main__':
    input = INPUT.split("\n")
    input = [int(i) for i in input]

    # differences = get_difference(input)
    # print(differences[1] * differences[3])

    print(get_ways(input))
