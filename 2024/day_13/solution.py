import numpy as np
from math import isclose
def part_1(): 
    with open("2024/day_13/input.txt", "r") as f: 
        eqs = f.read().split("\n\n")
    sums = 0
    for e in eqs: 
        lines = e.replace("Button A: X+", "").replace("Button B: X+", "").replace("Prize: X=", "").replace(" Y+", "").replace(" Y=", "").splitlines()
        a = [[*map(int, lines[i].split(","))] for i in  [0, 1] ]
        M = np.array(a)
        target = np.array([*map(int, lines[2].split(","))])
        target += 10000000000000
        sol = np.linalg.solve(M.T, target)
        for s in sol: 
            if abs(s - round(s)) > 0.001: 
                print(s) 
                break
        else: 
            sums += 3*sol[0] + sol[1]
    print(sums)
part_1()