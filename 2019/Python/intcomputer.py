class IntMachine:
    def __init__(self, program, instream=None, outstream=None):
        if outstream is None:
            outstream = []
        self.program = {}
        for i in range(len(program)):
            self.program[i] = program[i]
        self.input = instream
        self.output = outstream
        self.pc = 0
        self.running = True
        self.rel_base = 0

    def get_location(self, opcode, offset, value):
        if (opcode // pow(10, offset)) % 10 == 0:
            return self.read(value)
        elif (opcode // pow(10, offset)) % 10 == 1:
            return value
        elif (opcode // pow(10, offset)) % 10 == 2:
            return self.rel_base + self.read(value)
        else:
            raise Exception("Unknown parameter mode " + str(opcode // pow(10, offset)) % 10)

    def dualInstr(self, opcode, function):
        loc1 = self.get_location(opcode, 2, self.pc + 1)
        loc2 = self.get_location(opcode, 3, self.pc + 2)
        dest = self.get_location(opcode, 4, self.pc + 3)
        self.write(dest, function(self.read(loc1), self.read(loc2)))
        self.pc += 4

    def jump(self, opcode, predicate):
        loc1 = self.get_location(opcode, 2, self.pc + 1)
        loc2 = self.get_location(opcode, 3, self.pc + 2)
        if predicate(self.read(loc1)):
            self.pc = self.read(loc2)
        else:
            self.pc += 3

    def compare(self, opcode, predicate):
        loc1 = self.get_location(opcode, 2, self.pc + 1)
        loc2 = self.get_location(opcode, 3, self.pc + 2)
        dest = self.get_location(opcode, 4, self.pc + 3)
        if predicate(self.read(loc1), self.read(loc2)):
            self.write(dest, 1)
        else:
            self.write(dest, 0)
        self.pc += 4

    def read(self, loc):
        if loc in self.program:
            return self.program[loc]
        return 0

    def write(self, loc, val):
        self.program[loc] = val

    def run(self):
        while self.running:
            opcode = self.read(self.pc)
            op = opcode % 100
            if op == 1:
                self.dualInstr(opcode, lambda i1, y: i1 + y)
            elif op == 2:
                self.dualInstr(opcode, lambda i1, y: i1 * y)
            elif op == 3:
                if len(self.input) == 0:
                    return 2
                dest = self.get_location(
                    opcode, 2, self.pc + 1
                )
                self.write(dest, self.input.pop(0))
                self.pc += 2
            elif op == 4:
                dest = self.get_location(
                    opcode, 2, self.pc + 1
                )
                self.output.append(self.read(dest))
                self.pc += 2
            elif op == 5:
                self.jump(opcode, lambda a: a != 0)
            elif op == 6:
                self.jump(opcode, lambda a: a == 0)
            elif op == 7:
                self.compare(opcode, lambda a, b: a < b)
            elif op == 8:
                self.compare(opcode, lambda a, b: a == b)
            elif op == 9:
                self.rel_base += self.read(self.get_location(opcode, 2, self.pc + 1))
                self.pc += 2
            elif op == 99:
                self.running = False
            else:
                raise Exception("Unknown opcode: " + str(opcode))
        # Return codes:
        # 0: Successful run
        # 1: Error
        # 2: paused
        return 0


def runProgram(prog, instream):
    prog = IntMachine(prog, instream)
    prog.run()
    return prog.output
