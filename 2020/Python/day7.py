import re

testdata = ["""light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""]
testresult = [4]

testdata2 = [testdata[0], """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""]
testresult2 = [32, 126]

pattern = "((\d+ )?((?:(?:\w+)\s){2})bags?(?: contain)?)"


def read_data(data):
    words = re.findall(pattern, data)
    return words

def bottom_up(words):
    bagmap = {}
    i = 0
    while i < len(words):
        word = words[i]
        i += 1
        while i < len(words):
            content = words[i]
            if content[1] == "":
                break
            if content[2] == "no other ":
                i += 1
                break
            if content[2] in bagmap:
                bagmap[content[2]].add((word[2], int(content[1][:-1])))
            else:
                bagmap[content[2]] = {(word[2], int(content[1][:-1]))}
            i += 1
    return bagmap

def top_down(words):
    bagmap = {}
    i = 0
    while i < len(words):
        word = words[i]
        children = []
        i += 1
        while i < len(words):
            content = words[i]
            if content[1] == "":
                break
            if content[2] == "no other ":
                i += 1
                break
            children.append((content[2], int(content[1][:-1])))
            i += 1
        bagmap[word[2]] = children
    return bagmap


def find_contents(data, toFind):
    bags = bottom_up(data)
    expanded = set()
    scope = [toFind]
    while len(scope) > 0:
        bag = scope.pop(0)
        if bag not in bags:
            continue
        for container in bags[bag]:
            if container[0] not in expanded:
                expanded.add(container[0])
                scope.append(container[0])
    return len(expanded)

def calc_total(data, toFind):
    return calc_amount(top_down(data), toFind, {})-1

def calc_amount(data, toFind, bookkeep):
    res = 1
    for child in data[toFind]:
        amount = bookkeep[child[0]] if child in bookkeep else calc_amount(data, child[0], bookkeep)
        res += amount * child[1]
    bookkeep[toFind] = res
    return res

print("Q1 testing")
func = lambda x: find_contents(x, "shiny gold ")
for i in range(len(testdata)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata[i])), testresult[i]))
print("Q2 testing")
func = lambda x: calc_total(x, "shiny gold ")
for i in range(len(testdata2)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata2[i])), testresult2[i]))

with open("input/day7.txt") as f:
    contents = read_data(f.read())
    print("Q1")
    print(find_contents(contents, "shiny gold "))
    print("Q2")
    print(calc_total(contents, "shiny gold "))