def addWires(locset, pos, command, lengthmap):
    direction = command[0]
    distance = int(command[1:])
    newdirs = []
    if direction == "R":
        newdirs = list(map(lambda t: (pos[0]+t+1, pos[1]), range(distance)))
        npos = (pos[0]+distance,pos[1])
    elif direction == "D":
        newdirs = list(map(lambda t: (pos[0], pos[1]-t-1), range(distance)))
        npos = (pos[0],pos[1]-distance)
    elif direction == "L":
        newdirs = list(map(lambda t: (pos[0]-t-1, pos[1]), range(distance)))
        npos = (pos[0]-distance,pos[1])
    elif direction == "U":
        newdirs = list(map(lambda t: (pos[0], pos[1]+t+1), range(distance)))
        npos = (pos[0],pos[1]+distance)

    for j in range(len(newdirs)):
        newdir = newdirs[j]
        locset.add(newdir)
        lengthmap[newdir] = lengthmap[pos]+j+1
    return npos

with open("input/day3.txt") as f:
    wires = list(map(lambda lst: lst.split(","), f.read().split("\n")))
    wiresets = []
    distmaps = []
    for i in range(len(wires)):
        wireset = set()
        pos = (0,0)
        distmap = {pos: 0}
        distmaps.append(distmap)
        for direction in wires[i]:
            pos = addWires(wireset, pos, direction, distmap)
        wiresets.append(wireset)
    intersects = wiresets[0].intersection(wiresets[1])
    print("Q1")
    print(min(map(lambda x: abs(x[0])+abs(x[1]), intersects)))
    print("Q2")
    print(min(map(lambda x: distmaps[0][x]+distmaps[1][x], intersects)))

