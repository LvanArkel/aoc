def intersperse(seq, sep):
    res = ""
    nf = False
    for item in seq:
        if nf:
            res += sep
        res += str(item)
        nf = True
    return res

pream = [i for i in range(1,26)]
testdata = list(map(lambda x: (intersperse(x[0], "\n"),x[1]), [(pream + [26],25), (pream + [49],25), (pream + [100],25), (pream + [50],25)])) + [
    ("""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""",5)
]
testresult = [-1, -1, 100, 50, 127]

testdata2 = [testdata[-1]]
testresult2 = [62]

def read_data(package):
    return list(map(int, package[0].split("\n"))), package[1]

def find_first_error(package):
    data = package[0]
    preamlen = package[1]
    for i in range(preamlen, len(data)):
        found = False
        for a in range(i-preamlen, i-1):
            if found:
                break
            for b in range(a, i):
                if data[a]+data[b] == data[i]:
                    found = True
                    break
        if not found:
            return data[i]
    return -1

def find_weakness(package, tofind):
    data = package[0]
    for i in range(len(data)):
        tot = []
        j = i
        while sum(tot) < tofind:
            j += 1
            tot.append(data[j])
        if sum(tot) == tofind:
            return min(tot)+max(tot)
    return -1

print("Q1 testing")
func = find_first_error
for i in range(len(testdata)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata[i])), testresult[i]))
print("Q2 testing")
func = lambda x: find_weakness(x, 127)
for i in range(len(testdata2)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata2[i])), testresult2[i]))
    
with open("input/day9.txt") as f:
    contents = (read_data((f.read(),25)))
    print("Q1")
    ferror = find_first_error(contents)
    print(ferror)
    print("Q2")
    print(find_weakness(contents, ferror))
