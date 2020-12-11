import operator
from functools import reduce
testdata = ["""16
10
15
5
1
11
7
19
6
12
4""", """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""]
testresult = [7 * 5, 22 * 10]

testdata2 = [testdata[0], testdata[1]]
testresult2 = [8, 19208]

arrangements = {0: 1, 1: 1}

def read_data(data):
    return list(map(int, data.split("\n")))

def calc_diffs(data : [int]):
    adapters = [0] + sorted(data) + [max(data) + 3]
    return [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]

def calc_adapters(data : [int]):
    newlist = calc_diffs(data)
    return newlist.count(1)*newlist.count(3)

def diff_split(data):
    lasti = 0
    for i, val in enumerate(data):
        if val == 3:
            yield i-lasti
            lasti = i+1

def section(i):
    if i == 0:
        return 1
    if i < 0:
        return 0
    return sum([arrangements[(i-j)] if (i-j) in arrangements else section(i-j) for j in range(1,4)])

def calc_arrangements(data : [int]):
    diffs = calc_diffs(data)
    return reduce(operator.mul, map(section, diff_split(diffs)))

print("Q1 testing")
func = calc_adapters
for i in range(len(testdata)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata[i])), testresult[i]))
print("Q2 testing")
func = calc_arrangements
for i in range(len(testdata2)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata2[i])), testresult2[i]))

with open("input/day10.txt") as f:
    contents = read_data(f.read())
    print("Q1")
    print(calc_adapters(contents))
    print("Q2")
    print(calc_arrangements(contents))
