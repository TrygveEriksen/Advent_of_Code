import time

def get_input(): 
    return [(line.split(" ")[0], int(line.split(" ")[1])) for line in open("2019/day_2/input.txt","r").read().split("\n")]


def part_1():
    h = 0
    v = 0
    for l in get_input(): 
        match l[0]: 
            case "up":
                v-= l[1]
            case "down": 
                v+= l[1]
            case "forward": 
                h += l[1]
    return h*v

def part_2():
    li = get_input()
    h = 0
    v = 0
    a = 0

    for l in li: 
        match l[0]: 
            case "up":
                a-= l[1]
            case "down": 
                a+= l[1]
            case "forward": 
                h += l[1]
                v += a* l[1]
    return h*v

def main():
    start = time.perf_counter()
    print(part_1())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")

main()