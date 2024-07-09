import time

def get_input(): 
    with open("2019/day_1/input.txt", "r") as f: 
        return [int(i.strip()) for i in f.readlines()]

def part_1(): 
    lines = get_input()
    c=0
    for i in range(1, len(lines)): 
        c += lines[i] > lines[i-1]
    return c

def part_2(): 
    lines = get_input()
    s = lines[0]
    c=0
    for i in range(3, len(lines)): 
        n = sum(lines[max(i-3, 0): i])
        c += n > s
        s=n
    
    return c

def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")

main()