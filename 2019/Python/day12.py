from math import gcd

def read_data(data):
    lines = data.split("\n")
    sections = list(map(lambda x: list(map(lambda y: int(y.split("=")[1]), x[1:-1].split(", "))), lines))
    return sections


def timestep(positions, velocities):
    velocitiesNew = list(map(lambda ls: ls.copy(), velocities))
    # Apply gravity
    for i in range(len(positions)):
        for j in range(i, len(positions)):
            for d in range(3):
                if not positions[i][d] == positions[j][d]:
                    delta = -1 if positions[i][d] > positions[j][d] else 1
                    velocitiesNew[i][d] += delta
                    velocitiesNew[j][d] -= delta

    positionsNew = list(map(lambda ls: ls.copy(), positions))
    # Apply velocities
    for i in range(len(positionsNew)):
        for d in range(3):
            positionsNew[i][d] += velocitiesNew[i][d]
    return positionsNew, velocitiesNew

def timestep_coord(positions: [int], velocities: [int]):
    velocitiesNew = velocities.copy()
    # Apply gravity
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            if not positions[i] == positions[j]:
                delta = -1 if positions[i] > positions[j] else 1
                velocitiesNew[i] += delta
                velocitiesNew[j] -= delta
    positionsNew = positions.copy()
    # Apply velocities
    for i in range(len(positionsNew)):
        positionsNew[i] += velocitiesNew[i]
    return positionsNew, velocitiesNew

def calc_energy(pos, vel):
    return sum(map(abs, pos)) * sum(map(abs, vel))



def simulate(positions, length, debug=False):
    velocities = [[0, 0, 0]] * len(positions)
    for i in range(length):
        if debug:
            print("State at t=" + str(i))
            print(positions)
            print(velocities)
        positions, velocities = timestep(positions, velocities)
    if debug:
        print("State at t=" + str(length))
        print(positions)
        print(velocities)
    energy = 0
    for i in range(len(positions)):
        energy += calc_energy(positions[i], velocities[i])
    return positions, velocities, energy


def calc_cycle(positions: [int], velocities: [int]):
    initialPos = positions.copy()
    initialVel = velocities.copy()
    cycle = 0
    while True:
        positions, velocities = timestep_coord(positions, velocities)
        cycle += 1
        if positions == initialPos and velocities == initialVel:
            return cycle

def find_cycle(positions: [[int]]):
    velocities = [[0, 0, 0]] * len(positions)
    cycles = [0]*3
    for i in range(3):
        cycles[i] = calc_cycle(list(map(lambda x: x[i], positions)), list(map(lambda x: x[i], velocities)))
    a = cycles[0]*cycles[1]//gcd(cycles[0],cycles[1])
    return a*cycles[2]//gcd(a,cycles[2])


testdata = [("""<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""", 10)]
testresult = [179]

testdata2 = [testdata[0][0], """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""]
testresult2 = [2772, 4686774924]

print("Q1 testing")
func = lambda x: simulate(read_data(x[0]), x[1])
for i in range(len(testdata)):
    print("Actual: {}. Expected {}".format(func(testdata[i]), testresult[i]))
print("Q2 testing")
func = lambda x: find_cycle(read_data(x))
for i in range(len(testdata2)):
    print("Actual: {}. Expected {}".format(func(testdata2[i]), testresult2[i]))

with open("input/day12.txt") as f:
    contents = f.read()
    data = read_data(contents)
    print("Q1")
    print(simulate(data, 1000))
    print("Q2")
    print(find_cycle(data))
