import time


def get_input(): 
    with open("2020/day_14/input.txt", "r") as f: 
        return [line.strip().replace(" ", "").split("=") for line in f.readlines()]

def maskify(mask, num): 
    num = bin(int(num))[2:].rjust(36, "0")
    new = ""
    for i in range(len(num)): 
        new += "1" if mask[i] == "1" or (mask[i]=="X" and num[i]=="1") else "0"
    
    return new

def part_1(): 
    instr = get_input()
    d = {}
    mask = "X"*36
    for i in instr: 
        match i[0][:3]: 
            case "mem":
                pos = i[0][4:-1]    
                d[pos]  = maskify(mask, i[1])
            case "mas": 
                mask = i[1]
    return sum(int(d[key], 2) for key in d)

def addr_maskify(mask, addr):
    a = [""]
    num = bin(int(addr))[2:].rjust(36, "0")
    for i in range(len(num)): 
        if mask[i] == "0": 
            a = [l + num[i] for l in a]
        elif mask[i] == "1": 
            a = [l + "1" for l in a]
        else: 
            b = [l + "0" for l in a]
            c = [l + "1" for l in a]
            a = b + c
    return a

def part_2(): 
    instr = get_input()
    d = {}
    mask = ""
    for i in instr: 
        match i[0][:3]:
            case "mem": 
                pos = i[0][4:-1]
                for p in addr_maskify(mask, pos): 
                    d[p] = i[1]
            case "mas": 
                mask = i[1]
    
    return sum(int(d[key]) for key in d)

    
def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")


main()