import time

def get_input(): 
    
    c = [["."]*20 for i in range(6)]
    d=[]

    with open("2020/day_17/input.txt", "r") as f: 
        lines = f.readlines()

    for line in lines:
        c.append([*(6*"."+line.strip()+6*".")])

    c.extend([["."]*20 for i in range(6)])

    for i in range(6): 
        d.append([["."]*20 for i in range(20)])

    d.append(c)

    for i in range(6):
        d.append([["."]*20 for i in range(20)])

    return d

def get_input_2(): 

    c = [["."]*20 for i in range(6)]
    d=[]

    with open("2020/day_17/input.txt", "r") as f: 
        lines = f.readlines()

    for line in lines:
        c.append([*(6*"."+line.strip()+6*".")])

    c.extend([["."]*20 for i in range(6)])

    for i in range(6): 
        d.append([["."]*20 for i in range(20)])

    d.append(c)

    for i in range(6):
        d.append([["."]*20 for i in range(20)])

    e = [[[["."]*20 for i in range(20)]for j in range(13)]for k in  range(8)]
    e.append(d)
    e.extend([[[["."]*20 for i in range(20)]for j in range(13)]for k in  range(8)])

    return e

def part_1(): 
    cubes = get_input()
    for r in range(6): 
        c = [[[0]*len(cubes[0][0])for i in range(len(cubes[0]))] for j in range(len(cubes))]

        for i in range(len(cubes)): 
            for j in range(len(cubes[0])): 
                for k in range(len(cubes[0][0])): 
                    i1 = max(0, i-1)
                    i2 = min(len(cubes), i+2)
                    j1 = max(0, j-1)
                    j2 = min(len(cubes[0]), j+2)
                    k1 = max(0, k-1)
                    k2 = min(len(cubes[0][0]), k+2)
                    temp = [[[a for a in l1[k1: k2]] for l1 in l2[j1:j2]]for l2 in cubes[i1: i2]]
                    c[i][j][k] = sum(sum(l.count("#") for l in l1) for l1 in temp) - cubes[i][j][k].count("#")

        for i in range(len(cubes)): 
            for j in range(len(cubes[0])): 
                for k in range(len(cubes[0][0])):
                    n =  c[i][j][k]
                    match cubes[i][j][k]: 
                        case ".": 
                            cubes[i][j][k] = "#" if n == 3 else "."
                        case "#": 
                            cubes[i][j][k] = "#" if n == 2 or n==3 else "."


    return sum(sum(l.count("#") for l in l1) for l1 in cubes) 

def part_2(): 
    cubes = get_input_2()
    for r in range(6): 
        c = [[[[0]*len(cubes[0][0][0])for i in range(len(cubes[0][0]))] for j in range(len(cubes[0]))]for k in range(len(cubes))]
        for h in range(len(cubes)):
            for i in range(len(cubes[h])): 
                for j in range(len(cubes[h][i])): 
                    for k in range(len(cubes[h][i][j])): 
                        h1 = max(0, h-1)
                        h2 = min(len(cubes), h+2)
                        i1 = max(0, i-1)
                        i2 = min(len(cubes[h]), i+2)
                        j1 = max(0, j-1)
                        j2 = min(len(cubes[h][i]), j+2)
                        k1 = max(0, k-1)
                        k2 = min(len(cubes[h][i][j]), k+2)
                        temp = [[[[a for a in l1[k1: k2]] for l1 in l2[j1:j2]]for l2 in l3[i1: i2]]for l3 in cubes[h1:h2]]
                        c[h][i][j][k] = sum(sum(sum(l.count("#") for l in l1) for l1 in l2) for l2 in temp) - cubes[h][i][j][k].count("#")

        for h in range(len(cubes)):
            for i in range(len(cubes[h])): 
                for j in range(len(cubes[h][i])): 
                    for k in range(len(cubes[h][i][j])):
                        n =  c[h][i][j][k]
                        match cubes[h][i][j][k]: 
                            case ".": 
                                cubes[h][i][j][k] = "#" if n == 3 else "."
                            case "#": 
                                cubes[h][i][j][k] = "#" if n == 2 or n==3 else "."


    return sum(sum(sum(l.count("#") for l in l1) for l1 in l2) for l2 in cubes)
                

    
print(part_2())