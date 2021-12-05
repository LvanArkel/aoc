path = "C:/Users/Lars/Documents/Programming/aoc/inputs/{year}/day{day}.txt"

def parse_puzzle(data):
  return data

def puzzle_input():
  with open(path) as f:
    return parse_puzzle(f.read())

def puzzle1(data):
  pass

def puzzle2(data):
  pass


print(puzzle1(puzzle_input()))
print(puzzle2(puzzle_input()))