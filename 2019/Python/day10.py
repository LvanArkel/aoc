from math import floor, atan2, sqrt, pi

testdata = [""".#..#
.....
#####
....#
...##""",
            """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####""",
            """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.""",
            """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..""",
            """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""
            ]
test_result = [((3, 4), 8), ((5, 8), 33), ((1, 2), 35), ((6, 3), 41), ((11, 13), 210)]

testdata2 = [(""".#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##""", (8,3), 18), (testdata[4], (11,13), 200)]

test_result2 = [(4,4), (8,2)]

def load_asteroids(data):
    splitted = data.split("\n")
    asteroids = []
    for y in range(len(splitted)):
        for x in range(len(splitted[y])):
            if (splitted[y][x] == "#"):
                asteroids.append((x, y))
    return asteroids


def lineofsight(asteroids, src, dest):
    if (dest == src):
        return 0
    dx = dest[0] - src[0]
    dy = dest[1] - src[1]
    if dx == 0:
        # go in a straight line from src to dest
        direction = int(dy / abs(dy))
        for i in range(src[1] + direction, dest[1], direction):
            if (src[0], i) in asteroids:
                return 0
        return 1
    if dy == 0:
        # go in a straight line from src to dest
        direction = int(dx / abs(dx))
        for i in range(src[0]+direction, dest[0], direction):
            if (i, src[1]) in asteroids:
                return 0
        return 1
    xstep = dx/dy
    for i in range(int(dy/abs(dy)), dy, int(dy/abs(dy))):
        if xstep*i == floor(xstep*i):
            if (src[0]+xstep*i, src[1]+i) in asteroids:
                return 0
    return 1


def calc_visible(asteroids, src):
    return sum(map(lambda ass: lineofsight(asteroids, src, ass), asteroids))


def find_best(asteroids):
    best_state = None
    best_value = 0
    for asteroid in asteroids:
        value = calc_visible(asteroids, asteroid)
        if value > best_value:
            best_state = asteroid
            best_value = value
    return best_state, best_value

def calc_angles(src, asteroids):
    angles = []
    for asteroid in asteroids:
        if src != asteroid:
            dy = asteroid[1]-src[1]
            dx = asteroid[0]-src[0]
            dist = sqrt(pow(dx,2)+pow(dy,2))
            angle = (atan2(dx, -dy) + 2*pi) % (2*pi)
            angles.append((angle, dist, asteroid))
    angles.sort()
    return angles

def shoot_asteroids(angles, amount):
    i = 0
    counter = 0
    while counter < amount:
        curAngle = angles[i][0]
        last = angles[i]
        angles.pop(i)
        counter += 1
        while angles[i][0] == curAngle:
            i = (i+1) % len(angles)
    return last

print("Q1 tests")
for i in range(len(testdata)):
    print("Result:  " + str(find_best(load_asteroids(testdata[i]))) + ". Expected " + str(test_result[i]))
print("Q2 tests")
for i in range(len(testdata2)):
    asteroids = load_asteroids(testdata2[i][0])
    angles = calc_angles(testdata2[i][1], asteroids)
    print("Result: " + str(shoot_asteroids(angles, testdata2[i][2])) + ". Expected " + str(test_result2[i]))

with open("input/day10.txt") as f:
    contents = f.read()
    asteroids = load_asteroids(contents)
    print("Q1")
    best = find_best(asteroids)
    print(best)
    print("Q2")
    angles = calc_angles(best[0], asteroids)
    print(shoot_asteroids(angles, 200))
