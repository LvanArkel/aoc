from intcomputer import *

testdata = []
testresult = []

testdata2 = []
testresult2 = []

class Turtle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 0
    def turn(self, direction):
        self.dir = (self.dir + (1 if direction == 1 else -1)) % 4
    def move(self):
        if self.dir == 0:
            self.y += 1
        elif self.dir == 1:
            self.x += 1
        elif self.dir == 2:
            self.y -= 1
        elif self.dir == 3:
            self.x -= 1
        else:
            raise Exception("Unknown direction " + str(self.dir))


def read(turtle, hull):
    if (turtle.x, turtle.y) in hull:
        return hull[(turtle.x, turtle.y)]
    return 0


def paint(turtle, hull, panels, instruction):
    pos = (turtle.x, turtle.y)
    hull[pos] = instruction
    panels.add(pos)

def execute_program(prog, init):
    hull = {}
    panels = set()
    turtle = Turtle()
    input = [init]
    output = []
    computer = IntMachine(prog, input, output)
    while computer.running:
        computer.run()
        paint(turtle, hull, panels, output.pop(0))
        turtle.turn(output.pop(0))
        turtle.move()
        input.append(read(turtle, hull))
    return hull, panels




print("Q1 testing")
func = lambda x: x
for i in range(len(testdata)):
    print("Actual: {}. Expected {}".format(func(testdata[i]), testresult[i]))
print("Q1 testing")
func = lambda x: x
for i in range(len(testdata2)):
    print("Actual: {}. Expected {}".format(func(testdata2[i]), testresult2[i]))
    
with open("input/day11.txt") as f:
    contents = list(map(int, f.read().split(",")))
    print("Q1")
    print(len(execute_program(contents, 0)[0]))
    print("Q2")
    (hull, panels) = execute_program(contents, 1)
    minx = min(map(lambda x: x[0], hull))
    maxx = max(map(lambda x: x[0], hull))
    miny = min(map(lambda x: x[1], hull))
    maxy = max(map(lambda x: x[1], hull))
    for y in range(maxy, miny, -1):
        line = ""
        for x in range(minx, maxx):
            if (x,y) in hull:
                line += " " if hull[(x,y)] == 0 else "█"
            else:
                line += " "
        print(line)
    
