from functools import reduce
testdata = ["""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""]
testresult = [7]

testdata2 = [testdata[0]]
testresult2 = [336]
paths = [(1,1),(3,1),(5,1),(7,1),(1,2)]

def read_data(data):
    return data.split("\n")


def count_trees(land, deltax, deltay):
    count = 0
    x = 0
    y = 0
    while y < len(land):
        count += 1 if land[y][x % len(land[y])] == "#" else 0
        x += deltax
        y += deltay
    return count

def all_paths(land):
    return reduce(lambda a,b: a*b, map(lambda x: count_trees(land, x[0],x[1]),paths))

print("Q1 testing")
func = lambda x: count_trees(x, 3, 1)
for i in range(len(testdata)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata[i])), testresult[i]))
print("Q2 testing")
func = lambda x: all_paths(x)
for i in range(len(testdata2)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata2[i])), testresult2[i]))

with open("input/day3.txt") as f:
    contents = read_data(f.read())
    print("Q1")
    print(count_trees(contents, 3, 1))
    print("Q2")
    print(all_paths(contents))
