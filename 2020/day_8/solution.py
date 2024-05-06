import time

def get_calls():
    with open("2020/day_8/input.txt", "r") as f: 
        return [(a.strip().split(" ")[0], int(a.strip().split(" ")[1])) for a in f.readlines()] 

def check_round(calls): 
    a = 0 
    i = 0
    s = set()
    while i not in s and i < len(calls): 
        s.add(i)
        match calls[i][0]: 
            case "acc": 
                a += calls[i][1]
                i += 1
            case "nop": 
                i += 1
            
            case "jmp": 
                i += calls[i][1]

    return i>=len(calls), a


def part_1(): 
    return check_round(get_calls())[1]

def part_2(): 
    b = get_calls()
    for i in range(len(b)): 
        foo = False
        a = 0
        match b[i][0]: 
            case "jmp":
                old=b[i]
                b[i] = ("nop", b[i][1])
                foo, a = check_round(b)
                b[i]=old
            case "nop": 
                old=b[i]
                b[i] = ("nop", b[i][1])
                foo, a = check_round(b)
                b[i]=old
        if foo : 
            return a
    return -1



def main():
    start = time.process_time()
    print(part_2())
    stop = time.process_time()
    print(f"Process used {stop-start} seconds")


main()