def recalc(n):
    return n // 3 - 2 + (0 if n <= 0 else max(0, recalc(n//3-2)))

print(recalc(12))
print(recalc(14))
print(recalc(1969))
print(recalc(100756))
with open("input/day1.txt") as f:
    contents = map(int, f.read().split("\n"))
    print(sum(map(recalc, contents)))