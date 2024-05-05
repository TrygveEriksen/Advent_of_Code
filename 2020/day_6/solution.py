import time 


def get_answers(): 
    with open("2020/day_6/input.txt", "r") as f:  
        lines = [line.strip() for line in f.readlines()]
    
    ret=[]
    l=""
    n=0
    for line in lines: 
        line = line.strip()
        if line == "": 
            ret.append([n,l])
            l=""
            n=0
        else: 
            l+=line
            n+=1
    ret.append([n,l])
    return ret

def part_1() -> int: #Does not work with new input method for part 2
    ans = get_answers()
    return sum(len(set(line)) for line in ans) 

def part_2() -> int: 
    ans = get_answers()
    c=0
    for a in ans: 
        for l in set(a[1]): 
            c+= int(a[0]) == a[1].count(l)
    return c

def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")


main()