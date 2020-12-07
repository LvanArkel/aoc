def generate_tree(data):
    datamap = {}
    for mapping in map(lambda x: x.split(")"), data.split("\n")):
        if mapping[0] in datamap:
            datamap[mapping[0]].append(mapping[1])
        else:
            datamap[mapping[0]] = [mapping[1]]
    return datamap

def calc_orbits(tree, node, depth):
    if not node in tree:
        return depth
    return sum(map(lambda nd: calc_orbits(tree, nd, depth+1), tree[node]))+depth

def calc_all_orbits(data):
    treemap = generate_tree(data)
    return calc_orbits(treemap, "COM", 0)

def dfs(tree, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            if vertex not in tree:
                continue
            for leaf in tree[vertex]:
                stack.append((leaf, path + [leaf]))

def transit(data, point1, point2):
    tree = generate_tree(data)
    path1 = dfs(tree, "COM", point1)
    path2 = dfs(tree, "COM", point2)
    while(path1[0] == path2[0]):
        path1 = path1[1:]
        path2 = path2[1:]
    return len(path1)+len(path2)-2



print("Q1 tests")
testdata = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""
print(calc_all_orbits(testdata))

print("Q2 tests")
testdata2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""
print(transit(testdata2, "YOU", "SAN"))

with open("input/day6.txt") as f:
    contents = f.read()
    print("Q1")
    print(calc_all_orbits(contents))
    print("Q2")
    print(transit(contents, "YOU", "SAN"))