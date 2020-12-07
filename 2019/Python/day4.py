def adjacent(text):
    if len(text) < 2:
        return False
    return text[0] == text[1] or adjacent(text[1:])

def adjacent2(text):
    if len(text) < 2:
        return False
    if text[0] == text[1]:
        if len(text) == 2:
            return True
        if text[0] == text[2]:
            digit = text[0]
            while text[0] == digit:
                text = text[1:]
                if len(text) == 0:
                    return False
            return adjacent2(text)
        return True
    return adjacent2(text[1:])

def increasing(text):
    if len(text) < 2:
        return True
    return (not text[0] > text[1]) and increasing(text[1:])


def accept_password(number, adj_fun):
    strnum = str(number)
    return adj_fun(strnum) and increasing(strnum)

print("Q1")
print(len([x for x in range(245182, 790572) if accept_password(x, adjacent)]))
print("Q2")
print(adjacent2("112233"))
print(adjacent2("123444"))
print(adjacent2("111122"))
print(adjacent2("123544"))
print(adjacent2("114789"))
print(len([x for x in range(245182, 790572) if accept_password(x, adjacent2)]))
