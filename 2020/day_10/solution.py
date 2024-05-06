import time 

def get_input(): 
    with open("2020/day_10/input.txt", "r") as f: 
        return [int(a.strip()) for a in f.readlines()]


def part_1(): 
    a = get_input()
    b=1
    s=0
    a.sort(reverse = True)
    prev = 0
    while len(a): 
        temp = a.pop()
        match temp - prev: 
            case 1: 
                s += 1
            case 3: 
                b += 1
        prev = temp
    return s*b


def part_2(): 
    a = set(get_input())
    arr = [0]*(max(a)+1)
    arr[0] = 1
    for i in range(1, max(a)+1):
        if i in a: 
            arr[i] = arr[i-1]+arr[i-2]+arr[i-3]
    return arr[-1] 


def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")


main()