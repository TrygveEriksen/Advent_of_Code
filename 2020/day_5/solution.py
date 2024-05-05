import time 

def get_boarding_passes(): 
    with open("2020/day_5/input.txt", "r") as f: 
        boarding_passes = f.readlines()
    return [bp.strip() for bp in boarding_passes]


def part_1() -> int: 
    bp = get_boarding_passes()
    m = 0
    for p in bp:
        b = 0
        t = 128
        l = 0
        r = 8
        for i in range(10): 
            match p[i]: 
                case "F": 
                    t = (t+b)/2
                case "B":
                    b = (t+b)/2
                case "R": 
                    l = (r+l)/2
                case "L":
                    r = (r+l)/2

        row = t - 1
        seat = r - 1
        m = max(m, row * 8 + seat)
    return m

def part_2() -> int:
    bp = get_boarding_passes()
    m = []
    for p in bp:
        b = 0
        t = 128
        l = 0
        r = 8
        for i in range(10): 
            match p[i]: 
                case "F": 
                    t = (t+b)/2
                case "B":
                    b = (t+b)/2
                case "R": 
                    l = (r+l)/2
                case "L":
                    r = (r+l)/2

        row = t - 1
        seat = r - 1
        m.append(int(row * 8 + seat))
    m = set(m)
    for n in range(min(m)+1, max(m)):
        if not n in m: 
            return n
    return -1









def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")

main()