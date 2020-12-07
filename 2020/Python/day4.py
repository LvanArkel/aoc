import re
testdata = ["""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""]
testresult = [2]

testdata2 = ["""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""","""pid:087499704 hgt:190cm ecl:grn iyr:2012 eyr:2030 byr:2002
hcl:#123abc

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""]
testresult2 = [0, 4]

def read_data(data):
    return list(map(lambda x: list(map(lambda y: y.split(":"), x)), map(lambda x: x.replace("\n", " ").split(" "), data.split("\n\n"))))

def check_valid(data, required, check2 = False):
    valids = []
    for password in data:
        fields = list(map(lambda x: x[0], password))
        valid = True
        for req_field in required:
            if req_field not in fields:
                valid = False
                break
        if check2:
            for field in password:
                if field[0] == "byr":
                    if int(field[1]) < 1920 or int(field[1]) > 2002:
                        valid = False
                        break
                elif field[0] == "iyr":
                    if int(field[1]) < 2010 or int(field[1]) > 2020:
                        valid = False
                        break
                elif field[0] == "eyr":
                    if int(field[1]) < 2020 or int(field[1]) > 2030:
                        valid = False
                        break
                elif field[0] == "hgt":
                    if not re.match("[0-9]+[(cm)(in)]", field[1]):
                        valid = False
                        break
                    value = int(field[1][:-2])
                    unit = field[1][-2:]
                    if (unit == "cm" and (value < 150 or value > 193)) or (unit == "in" and (value < 59 or value > 76)):
                        valid = False
                        break
                elif field[0] == "hcl":
                    if not re.match('#[0-9a-f]{6}$', field[1]):
                        valid = False
                        break
                elif field[0] == "ecl":
                    if not (field[1] in ["amb","blu","brn","gry","grn","hzl","oth"]):
                        valid = False
                        break
                elif field[0] == "pid":
                    if not re.match("[0-9]{9}$", field[1]):
                        valid = False
                        break
        if valid:
            valids.append(password)
    return valids


Q1valids = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

print("Q1 testing")
func = lambda x: len(check_valid(x, Q1valids))
for i in range(len(testdata)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata[i])), testresult[i]))
print("Q2 testing")
func = lambda x: len(check_valid(x, Q1valids, True))
for i in range(len(testdata2)):
    print("Actual: {}. Expected {}".format(func(read_data(testdata2[i])), testresult2[i]))
    
with open("input/day4.txt") as f:
    contents = read_data(f.read())
    print("Q1")
    print(len(check_valid(contents, Q1valids)))
    print("Q2")
    print(len(check_valid(contents, Q1valids, True)))
