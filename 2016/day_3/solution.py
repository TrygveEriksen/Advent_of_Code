def part_1():
    with open("2016/day_3/input.txt", "r") as f:
        t = [[int(i) for i in line.strip().split()] for line in f.readlines()]
    return [x[0] < x[1] + x[2] and x[1] < x[2] + x[0] and x[2] < x[0] + x[1] for x in t].count(True)

def part_2():
    with open("2016/day_3/input.txt", "r") as f:
        t = [[int(i) for i in line.strip().split()] for line in f.readlines()]
    t2 = [[a[x] for a in t] for x in range(3)]
    t3 = []
    for t1 in t2: 
        for i in range(0, len(t1), 3): 
            t3.append(t1[i:i+3]) 
    return [x[0] < x[1] + x[2] and x[1] < x[2] + x[0] and x[2] < x[0] + x[1] for x in t3].count(True)

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
