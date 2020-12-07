import sys

template = """
testdata = []
testresult = []

testdata2 = []
testresult2 = []

def read_data(data):
    pass

print("Q1 testing")
func = lambda x: x
for i in range(len(testdata)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata[i])), testresult[i]))
print("Q2 testing")
func = lambda x: x
for i in range(len(testdata2)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata2[i])), testresult2[i]))
    
with open("input/day{}.txt") as f:
    contents = read_data(f.read())
    print("Q1")
    
    print("Q2")
    
"""

if __name__ == "__main__":
    args = sys.argv
    year = args[1]
    day = args[2]
    contents = template.format("{}","{}","{}","{}", day)
    with open("{}/Python/day{}.py".format(year, day), "w") as f:
        f.write(contents)
    f = open("{}/Python/input/day{}.txt".format(year, day), 'x')