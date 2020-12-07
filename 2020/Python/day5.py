
testdata = ["FBFBBFFRLR","BFFFBBFRRR","FFFBBBFRRR","BBFFBBFRLL"]
testresult = [357, 567, 119, 820]

testdata2 = []
testresult2 = []

def read_data(data):
    return data.split("\n")

def calc_board_id(boardpass):
    row = 0
    for i in range(7):
        row += (pow(2, 6-i) if boardpass[i] == "B" else 0)
    col = 0
    for i in range(3):
        col += (pow(2, 2-i) if boardpass[i+7] == "R" else 0)
    return row*8+col

def find_unknown(passes):
    for row in range(0,128):
        for col in range(8):
            id = row*8+col
            if not (id in passes) and ((id-1) in passes) and ((id+1) in passes):
                return id

print("Q1 testing")
func = lambda x: calc_board_id(x[0])
for i in range(len(testdata)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata[i])), testresult[i]))
print("Q2 testing")
func = lambda x: x
for i in range(len(testdata2)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata2[i])), testresult2[i]))
    
with open("input/day5.txt") as f:
    contents = read_data(f.read())
    passmap = map(calc_board_id, contents)
    print("Q1")
    print(max(passmap))
    print("Q2")
    print(find_unknown(list(map(calc_board_id, contents))))
    
