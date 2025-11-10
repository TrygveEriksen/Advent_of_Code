from collections import Counter

def part_1():
    with open("2016/day_6/input.txt", "r") as f: 
        lines = [line.strip() for line in f.readlines()]
    newlines = [[l[i] for l in lines] for  i in range(len(lines[0]))]
    s = ""
    for line in newlines: 
        d = dict(Counter(line))
        l = max(d.keys(), key= lambda x : d[x])
        s += l
    return s

def part_2():
    with open("2016/day_6/input.txt", "r") as f: 
        lines = [line.strip() for line in f.readlines()]
    newlines = [[l[i] for l in lines] for  i in range(len(lines[0]))]
    s = ""
    for line in newlines: 
        d = dict(Counter(line))
        l = min(d.keys(), key= lambda x : d[x])
        s += l
    return s

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
