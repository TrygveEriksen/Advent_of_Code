import time

def get_input(): 
    with open("2020/day_11/input.txt", "r") as f: 
        return [[*l.strip()] for l in f.readlines()]

def shuffle(positions): 
    c = [[0]*len(positions[0]) for i in range(len(positions))]
    foo = False
    for i in range(len(positions)): 
        for j in range(len(positions[0])): 
            if positions[i][j] == "." :  
                continue
            l = max(0, j-1)
            r = min(len(positions[0]),j+2)
            t = max(0, i-1)
            b = min(len(positions), i+2)
            temp = [line[l:r] for line in positions[t:b]]
            c[i][j] = sum(line.count("#") for line in temp) - (positions[i][j] == "#")

    for i in range(len(positions)): 
        for j in range(len(positions[0])):
            if positions[i][j] == "L" and c[i][j] == 0: 
                positions[i][j] = "#"
                foo = True
            elif positions[i][j] == "#" and c[i][j] > 3: 
                positions[i][j] = "L"
                foo = True
    return foo

def shuffle_2(positions): 
    foo = False
    c = [[0]*len(positions[0]) for i in range(len(positions))]
    for i in range(len(positions)): 
        for j in range(len(positions[0])):
            for k in range(1, len(positions[0])): 
                if j + k == len(positions[0]): break
                if positions[i][j+k] == "L": 
                    c[i][j+k] += positions[i][j] == "#"
                    break
                if positions[i][j+k] == "#": 
                    c[i][j] += 1 
                    c[i][j+k] += positions[i][j] == "#"
                    break
            for k in range(1, len(positions)): 
                if i + k == len(positions): break
                if positions[i+k][j] == "L":
                    c[i+k][j] += positions[i][j] == "#"
                    break
                if positions[i+k][j] == "#": 
                    c[i][j] += 1 
                    c[i+k][j] += positions[i][j] == "#"
                    break
            for k in range(1, len(positions)): 
                if j + k == len(positions[0]) or i + k == len(positions): break
                if positions[i+k][j+k] == "L": 
                    c[i+k][j+k] += positions[i][j] == "#"
                    break
                if positions[i+k][j+k] == "#": 
                    c[i][j] += 1 
                    c[i+k][j+k] += positions[i][j] == "#"
                    break
            for k in range(1, len(positions)): 
                if i + k == len(positions) or j - k < 0: break
                if positions[i+k][j-k] == "L": 
                    c[i+k][j-k] += positions[i][j] == "#"
                    break
                if positions[i+k][j-k] == "#": 
                    c[i][j] += 1 
                    c[i+k][j-k] += positions[i][j] == "#"
                    break    

            
    for i in range(len(positions)): 
        for j in range(len(positions[0])):
            if positions[i][j] == "L" and c[i][j] == 0: 
                positions[i][j] = "#"
                foo = True
            elif positions[i][j] == "#" and c[i][j] > 4: 
                positions[i][j] = "L"
                foo = True
    return foo


def part_1(): 
    pos = get_input()

    while shuffle(pos): 
        pass
    
    return sum(line.count("#") for line in pos)

def part_2(): 
    pos = get_input()
    while shuffle_2(pos): 
        pass
    return sum(line.count("#") for line in pos)
def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")


main()