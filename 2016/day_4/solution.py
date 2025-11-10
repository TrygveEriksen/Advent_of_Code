from collections import Counter

def part_1():
    with open("2016/day_4/input.txt", "r") as f: 
        lines = [line.strip().split("-") for line in f.readlines()]
    s = 0 
    for line in lines:
        l = "".join(line[:-1])
        num, pat = line[-1].split("[")
        occs = dict(Counter(l))
        letters = "".join(sorted(sorted(set(l), key= lambda x : x), key=lambda y: occs[y], reverse=True))
        if letters[:5] == pat[:-1]:
            s += int(num)
    return s

def part_2():
    with open("2016/day_4/input.txt", "r") as f: 
        lines = [line.strip().split("-") for line in f.readlines()]
    s = []
    for line in lines:
        l = "".join(line[:-1])
        num, pat = line[-1].split("[")
        w = [ord(a)-97 for a in l]
        w = [a + int(num) for a in w]
        w = [chr((a%26)+97) for a in w]
        if "northpole" in "".join(w): 
            s.append(num)
    return s

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")






