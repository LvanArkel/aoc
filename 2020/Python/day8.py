def find_loop(prog):
    visited = set()
    acc = 0
    pc = 0
    while True:
        if pc >= len(prog):
            return True, acc
        if pc in visited:
            return False, acc
        visited.add(pc)
        instr = prog[pc]
        if instr[0] == "nop":
            pc += 1
        elif instr[0] == "acc":
            acc += instr[1]
            pc += 1
        elif instr[0] == "jmp":
            pc += instr[1]

def fix_prog(prog):
    for i in range(len(prog)):
        if prog[i][0] == "nop":
            prog[i] = ("jmp", prog[i][1])
            res = find_loop(prog)
            if res[0]:
                return res[1]
            prog[i] = ("nop", prog[i][1])
        elif prog[i][0] == "jmp":
            prog[i] = ("nop", prog[i][1])
            res = find_loop(prog)
            if res[0]:
                return res[1]
            prog[i] = ("jmp", prog[i][1])


testdata = ["""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""]
testresult = [5]

testdata2 = []
testresult2 = []

def read_data(data):
    return list(map(lambda x: (x.split(" ")[0], int(x.split(" ")[1])), data.split("\n")))

print("Q1 testing")
func = lambda x: find_loop(x)[1]
for i in range(len(testdata)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata[i])), testresult[i]))
print("Q2 testing")
func = lambda x: x
for i in range(len(testdata2)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata2[i])), testresult2[i]))
    
with open("input/day8.txt") as f:
    contents = read_data(f.read())
    print("Q1")
    print(find_loop(contents))
    print("Q2")
    print(fix_prog(contents))
