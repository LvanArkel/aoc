def pincer(data):
    data.sort()
    lower = 0
    upper = len(data)-1
    while lower < upper:
        if data[lower] + data[upper] == 2020:
            return data[lower],data[upper],data[lower]*data[upper]
        if data[lower] + data[upper] > 2020:
            upper -= 1
            continue
        lower += 1
    return None

def pincer2(data):
    data.sort()
    for i in range(len(data)-1):
        lower = i+1
        upper = len(data)-1
        while lower < upper:
            if data[lower] + data[upper] + data[i] == 2020:
                return data[i] * data[lower] * data[upper]
            if data[lower] + data[upper] + data[i] > 2020:
                upper -= 1
                continue
            lower += 1
    return None

testdata = [[1721, 979, 366, 299, 675, 1456]]
testresult = [514579]

testdata2 = [testdata[0]]
testresult2 = [241861950]

print("Q1 testing")
func = pincer
for i in range(len(testdata)):
    print("Actual: {}. Expected {}".format(func(testdata[i]), testresult[i]))
print("Q1 testing")
func = pincer2
for i in range(len(testdata2)):
    print("Actual: {}. Expected {}".format(func(testdata2[i]), testresult2[i]))

with open("input/day1.txt") as f:
    contents = list(map(int, f.read().split("\n")))
    print("Q1")
    q1 = pincer(contents)
    print(q1[2])
    print("Q2")
    print(pincer2(contents))
