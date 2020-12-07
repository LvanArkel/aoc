from intcomputer import *

def draw_screen(program):
    output = []
    screen = {}
    computer = IntMachine(program, [], output)
    while computer.running:
        computer.run()
        while len(output) > 0:
            x = output.pop(0)
            y = output.pop(0)
            id = output.pop(0)
            screen[(x,y)] = id
    return screen

def count_blocks(screen):
    return len(list(filter(lambda x: x == 2, screen.values())))

def play_game(program):
    instream = []
    outstream = []
    screen = {}
    score = -1
    computer = IntMachine(program, instream, outstream)
    computer.write(0, 2)
    while computer.running:
        computer.run()
        while len(outstream) > 0:
            x = outstream.pop(0)
            y = outstream.pop(0)
            id = outstream.pop(0)
            if x == -1 and y == 0:
                score = id
            else:
                screen[(x, y)] = id
                if id == 3:
                    paddle = (x,y)
                elif id == 4:
                    ball = (x,y)
        if paddle[0] == ball[0]:
            instream.append(0)
        else:
            instream.append(-1 if ball[0] < paddle[0] else 1)
    return score

def print_screen(screen):
    minx = min(map(lambda x: x[0], screen.keys()))
    maxx = max(map(lambda x: x[0], screen.keys()))
    miny = min(map(lambda x: x[1], screen.keys()))
    maxy = max(map(lambda x: x[1], screen.keys()))
    for y in range(miny, maxy):
        line = ""
        for x in range(minx, maxx):
            line += print_char(screen[(x,y)])
        print(line)

def print_char(char):
    if char == 0:
        return " "
    elif char == 1:
        return "X"
    elif char == 2:
        return "█"
    elif char == 3:
        return "_"
    elif char == 4:
        return "0"

testdata = []
testresult = []

testdata2 = []
testresult2 = []

print("Q1 testing")
func = lambda x: x
for i in range(len(testdata)):
    print("Actual: {}. Expected {}".format(func(testdata[i]), testresult[i]))
print("Q2 testing")
func = lambda x: x
for i in range(len(testdata2)):
    print("Actual: {}. Expected {}".format(func(testdata2[i]), testresult2[i]))
    
with open("input/day13.txt") as f:
    contents = list(map(int, f.read().split(",")))
    print("Q1")
    screen = draw_screen(contents)
    print(count_blocks(screen))
    print(print_screen(screen))
    print("Q2")
    print(play_game(contents))
    
