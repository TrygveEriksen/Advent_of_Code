import time

def get_slope(): 
    with open("2020/day_3/input.txt", "r") as f: 
        slope = [l.strip() for l in f.readlines()]
    return slope

def part_1() -> int: 
    slope = get_slope()
    w = len(slope[0])
    c = 0
    pos = 0
    for i in range(len(slope)): 
        c += slope[i][pos] == "#"
        pos = (pos + 3) % w
    return c

def part_2() -> int: 
    slope = get_slope()
    w = len(slope[0])
    nums = [1, 3, 5, 7, 0.5]
    p=1
    for n in nums:
        pos = 0
        c = 0
        for i in range(len(slope)): 
            if int(pos) == pos: 
                c += slope[i][int(pos)] == "#"
            pos = (pos + n) % w
        p*=c
    return p

def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")


main()