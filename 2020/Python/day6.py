from functools import reduce

testdata = ["""abc

a
b
c

ab
ac

a
a
a
a

b"""]
testresult = [11]

testdata2 = [testdata[0]]
testresult2 = [-1]

def read_data(data):
    groups = data.split("\n\n")
    res = []
    for group in groups:
        indivs = group.split("\n")
        res.append(list(map(set, indivs)))
    return res

def calcsets(func, sets):
        return sum(map(lambda x: sum(map(len, reduce(func, x))), sets))

print("Q1 testing")
func = lambda x: calcsets(lambda a,b: a|b, x)
for i in range(len(testdata)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata[i])), testresult[i]))
print("Q2 testing")
func = lambda x: x
for i in range(len(testdata2)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata2[i])), testresult2[i]))
    
with open("input/day6.txt") as f:
    contents = read_data(f.read())
    print("Q1")
    print(calcsets(lambda a,b: a|b, contents))
    print("Q2")
    print(calcsets(lambda a,b: a&b, contents))
    
