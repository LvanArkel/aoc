def read_data(data):
    res = []
    for line in data.split("\n"):
        lrange, letter, word = line.split(" ")
        low, high = list(map(int, lrange.split("-")))
        res.append((low, high, letter[0], word))
    return res

def check_password(password):
    return password[0] <= len(list(filter(lambda x: x == password[2], password[3]))) <= password[1]

def valid_passwords(passwords):
    return len(list(filter(check_password, passwords)))

def valid_passwords2(passwords):
    func = lambda x: (x[3][x[0]-1] == x[2]) != (x[3][x[1]-1] == x[2])
    return len(list(filter(func, passwords)))

testdata = ["""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""]
testresult = [2]

testdata2 = [testdata[0]]
testresult2 = [1]

print("Q1 testing")
func = lambda x: valid_passwords(read_data(x))
for i in range(len(testdata)):
    print("Actual: {}. Expected {}".format(func(testdata[i]), testresult[i]))
print("Q2 testing")
func = lambda x: valid_passwords2(read_data(x))
for i in range(len(testdata2)):
    print("Actual: {}. Expected {}".format(func(testdata2[i]), testresult2[i]))
    
with open("input/day2.txt") as f:
    contents = read_data(f.read())
    print("Q1")
    print(valid_passwords(contents))
    print("Q2")
    print(valid_passwords2(contents))
