from functools import cache
from itertools import permutations
import math
dir_pad = {">": (1,2), "<": (1,0), "^": (0,1), "v": (1,1), "A":(0,2)}
num_pad = {"7": (0,0), "8":(0,1), "9":(0,2), "4":(1,0), "5":(1,1), "6":(1,2), "1":(2,0), "2":(2,1), "3":(2,2), "0":(3,1), "A":(3,2)}

@cache
def num_pad_check(fr, to):
    f_pos = num_pad[fr]
    t_pos = num_pad[to]
    m = math.inf
    c = []
    if f_pos[0] > t_pos[0]: 
        c.extend(["^" for _ in range(f_pos[0] - t_pos[0])])
    if f_pos[0] < t_pos[0]: 
        c.extend(["v" for _ in range(t_pos[0] - f_pos[0])])
    if f_pos[1] < t_pos[1]: 
        c.extend([">" for _ in range(t_pos[1] - f_pos[1])])
    if f_pos[1] > t_pos[1]: 
        c.extend(["<" for _ in range(f_pos[1] - t_pos[1])])
    comb = permutations(c, len(c))
    for co in comb: 
        y,x = f_pos
        for sign in co: 
            match sign: 
                case "^": 
                    y -= 1
                case "v": 
                    y += 1
                case ">": 
                    x += 1
                case "<": 
                    x-= 1
            if (y,x) == (3,0): 
                break
        else: 
            seq = "A" + "".join(co) + "A"
            s = 0
            for i in range(len(seq)-1): 
                s+= dir_pad_check(seq[i], seq[i+1], 25)
            m = min(m, s)
            print(m)
    return m



@cache
def dir_pad_check(fr, to, depth): 
    if depth == 0: 
        return 1
    f_pos = dir_pad[fr]
    t_pos = dir_pad[to]
    m = math.inf
    c = []
    if f_pos[0] > t_pos[0]: 
        c.extend(["^" for _ in range(f_pos[0] - t_pos[0])])
    if f_pos[0] < t_pos[0]: 
        c.extend(["v" for _ in range(t_pos[0] - f_pos[0])])
    if f_pos[1] < t_pos[1]: 
        c.extend([">" for _ in range(t_pos[1] - f_pos[1])])
    if f_pos[1] > t_pos[1]: 
        c.extend(["<" for _ in range(f_pos[1] - t_pos[1])])
    comb = permutations(c, len(c))
    for co in comb: 
        y,x = f_pos
        for sign in co: 
            match sign: 
                case "^": 
                    y -= 1
                case "v": 
                    y += 1
                case ">": 
                    x += 1
                case "<": 
                    x-= 1
            if (y,x) == (0,0): 
                print("what")
                break

        else: 
            seq = "A" + "".join(co) + "A"
            s = 0
            for i in range(len(seq)-1): 
                s+= dir_pad_check(seq[i], seq[i+1], depth-1)
            m = min(s, m)
    
    return m


def part_1(): 
    codes = ["A" + c.strip() for c in open("2024/day_21/input.txt", "r").readlines()]
    s = 0
    for code in codes:
        l = sum(num_pad_check(code[i], code[i+1]) for i in range(len(code)-1))
        s += int(code[1 : -1]) * l
        print(l)
    print(s)

#num_pad_check("A", "7")       


part_1()