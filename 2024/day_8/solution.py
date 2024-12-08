from itertools import permutations

def part_1(): 
    with open("2024/day_8/input.txt", "r") as f: 
        data = [line.strip() for line in f.readlines()]
    letters = set()
    for d1 in data: 
        for d2 in d1: 
            if d2 != ".": 
                letters.add(d2)
    antinodes = set()
    for letter in letters: 
        positions = []
        for idx in range(len(data)): 
            for jdx in range(len(data[idx])): 
                if data[idx][jdx] == letter: 
                    positions.append((idx, jdx))
                    
        perm = permutations(positions, 2)
        for p in perm: 
            pos1 = p[0]
            pos2 = p[1]
            dx = pos1[0]-pos2[0]
            dy = pos1[1]-pos2[1]
            new = (pos1[0], pos1[1])
            while new[0] > -1 and new[0] < len(data) and new[1] > -1 and new[1] < len(data[1]): 
                antinodes.add(new)
                new = (new[0]+dx, new[1]+dy)
    print(len(antinodes))








part_1()
