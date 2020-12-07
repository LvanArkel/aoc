class IntMachine:
    def __init__(self, program):
        self.program = program

    def dualInstr(self, pc, function):
        loc1 = self.program[pc+1]
        loc2 = self.program[pc+2]
        dest = self.program[pc+3]
        self.program[dest] = function(self.program[loc1], self.program[loc2])
        return 4

    def run(self):
        pc = 0
        running = True
        while running:
            opcode = self.program[pc]
            if opcode == 1:
                pc += self.dualInstr(pc, lambda i1, y: i1 + y)
            elif opcode == 2:
                pc += self.dualInstr(pc, lambda i1, y: i1 * y)
            elif opcode == 99:
                running = False


def runProgram(prog):
    prog = IntMachine(prog)
    prog.run()
    return prog.program


print(runProgram([1, 0, 0, 0, 99]))
print(runProgram([2, 3, 0, 3, 99]))
print(runProgram([2, 4, 4, 5, 99, 0]))
print(runProgram([1, 1, 1, 4, 99, 5, 6, 0, 99]))

with open("input/day2.txt") as f:
    contents = list(map(int, f.read().split(",")))
    for x in range(100 * 100):
        i = x % 100
        j = x // 100
        prog = contents.copy()
        prog[1] = i
        prog[2] = j
        result = runProgram(prog)[0]
        if i == 12 and j == 2:
            print("i == 12 and j == 2")
            print(result)
        if result == 19690720:
            print("Found it ", i, j)
            break;
    print("finished")
