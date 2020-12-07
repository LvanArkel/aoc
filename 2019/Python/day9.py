from intcomputer import *

print("Q1 tests")
print(runProgram([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99],[]))
print(runProgram([1102,34915192,34915192,7,4,7,99,0],[]))
print(runProgram([104,1125899906842624,99],[]))


with open("input/day9.txt") as f:
    contents = list(map(int, f.read().split(",")))
    print("Q1")
    print(runProgram(contents, [1]))
    print("Q2")
    print(runProgram(contents, [2]))