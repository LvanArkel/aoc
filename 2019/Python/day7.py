from intcomputer import *
from itertools import permutations

def thrusters(program, setting):
    previous = 0
    for i in range(len(setting)):
        previous = runProgram(program, [setting[i], previous])[0]
    return previous

def max_signal(program):
    best_setting = []
    best_power = -1
    perms = permutations([0,1,2,3,4])
    for setting in perms:
        power = thrusters(program, setting)
        if power > best_power:
            best_setting = setting
            best_power = power
    return best_setting, best_power

def multithread(program, setting):
    computers = []
    queues = []
    for i in range(len(setting)):
        queues.append([setting[i]])
    queues[0].append(0)
    for i in range(len(setting)):
        outqueue = queues[i+1] if i < len(setting)-1 else queues[0]
        computers.append(IntMachine(program, queues[i], outqueue))
    ci = 0
    while computers[-1].running:
        code = computers[ci].run()
        ci = (ci+1)%len(computers)
    return computers[-1].output[0]

def max_multi(program):
    best_setting = []
    best_power = -1
    perms = permutations([5,6,7,8,9])
    for setting in perms:
        power = multithread(program, setting)
        if power > best_power:
            best_setting = setting
            best_power = power
    return best_setting, best_power


print("Q1 tests")
print(max_signal([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]))
print(max_signal([3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0]))
print(max_signal([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]))
print("Q2 tests")
print(max_multi([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]))
print(max_multi([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]))

with open("input/day7.txt") as f:
    contents = list(map(int, f.read().split(",")))
    print("Q1")
    print(max_signal(contents))
    print("Q2")
    print(max_multi(contents))
