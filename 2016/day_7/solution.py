import re 

def legal(s):
    o = False
    found = False
    for idx in range(len(s)-3):
        if s[idx] == "[": 
            o = True
            continue
        if s[idx] == "]": 
            o = False
            continue
        if s[idx] == s[idx+3] and s[idx+1] == s[idx+2] and s[idx] != s[idx+1]: 
            if o: 
                return False
            found =  True
    return found

def part_1():
    with open("2016/day_7/input.txt") as f: 
        lines =[line.strip() for line in f.readlines()] 
    s = 0
    for line in lines:
        if legal(line): 
            s += 1
    return s

def ssl(s):
    s = re.split(r'\[|\]', s)
    sn = "".join(s[::2])
    hn = "".join(s[1::2])
    for a,b,c in zip(sn, sn[1:], sn[2:]): 
        if a == c and a != b:
            if b+a+b in hn:
                return True
    return False


def part_2():
    with open("2016/day_7/input.txt") as f: 
        lines =[line.strip() for line in f.readlines()] 
    s = 0
    for line in lines:
        if ssl(line): 
            s += 1
    return s


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
