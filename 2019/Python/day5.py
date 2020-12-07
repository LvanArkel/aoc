from intcomputer import *

print("Q1 tests")
print(runProgram([3, 0, 4, 0, 99], [42]))
print("Q2 tests")
print(runProgram([3,9,8,9,10,9,4,9,99,-1,8], [8]))
print(runProgram([3,9,7,9,10,9,4,9,99,-1,8], [8]))
print(runProgram([3,3,1108,-1,8,3,4,3,99], [8]))
print(runProgram([3,3,1107,-1,8,3,4,3,99], [8]))
print(runProgram([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], [0]))
print(runProgram([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], [0]))

with open("input/day5.txt") as f:
    contents = list(map(int, f.read().split(",")))
    print("Q1")
    print(runProgram(contents, [1]))
    print("Q2")
    print(runProgram(contents, [5]))
