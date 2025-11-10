def part_1(): 
    with open("2024/day_10/input.txt", "r") as f: 
        m = [list(map(int, [*line.strip()])) for line in f.readlines()]
    starts = list()
    reached = list()
    directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
    s = 0
    for idx in range(len(m)): 
        for jdx in range(len(m[idx])): 
            if m[idx][jdx] == 0: 
                starts.append((idx, jdx, 0, (idx,jdx)))
    while len(starts): 
        idx, jdx, start, origin = starts.pop()
        for d in directions: 
            if idx+d[0] > -1 and idx+d[0] < len(m) and jdx+d[1] > -1 and jdx+d[1] < len(m[idx]): 
                if m[idx+d[0]][jdx+d[1]] == start+1: 
                    if start == 8: 
                        reached.append((idx+d[0], jdx+d[1], origin))
                    else: 
                        starts.append((idx+d[0], jdx+d[1], start+1, origin))
    print(len(reached))
part_1()