
def part_2(): 
    with open("2024/day_12/input.txt", "r") as f: 
        garden = [line.strip() for line in f.readlines()]
    directions = [(0, 1),(-1,0),(0,-1),(1,0)]
    seeds = [(i, j) for i in range(len(garden))for j in range(len(garden[i]))]
    s = 0
    
    def flood(seed, walls:set): 
        if seed not in seeds: 
            return {}
        walls.add(seed)
        seeds.remove(seed)
        for d in directions: 
            if (seed[0]+d[0], seed[1]+d[1]) in seeds and garden[seed[0]+d[0]][seed[1]+d[1]] == garden[seed[0]][seed[1]]: 
                walls = flood((seed[0]+d[0], seed[1]+d[1]), walls)
        return  walls

    while len(seeds): 
        seed = seeds[-1]
        area = flood(seed, set())
        num_walls = 0
        x_min, x_max, y_min, y_max = min(x[0] for x in area), max(x[0] for x in area), min(x[1] for x in area), max(x[1] for x in area)
        for x in range(x_min, x_max+1): 
            y, max_y = min(a[1] for a in area if a[0]==x), max(a[1] for a in area if a[0] == x)
            up_flag = False 
            down_flag = False
            while y <= max_y: 
                if (x-1, y) not in area and (x, y) in area: 
                    num_walls += not up_flag 
                    up_flag = True 
                else: 
                    up_flag = False
                if (x+1, y) not in area and (x, y) in area: 
                    num_walls += not down_flag
                    down_flag = True 
                else: 
                    down_flag = False
                y += 1
        for y in range(y_min, y_max+1): 
            x, max_x = min(a[0] for a in area if a[1]==y), max(a[0] for a in area if a[1] == y)
            left_flag = False
            right_flag = False
            while x <= max_x: 
                if (x, y-1) not in area and (x, y) in area: 
                    num_walls += not left_flag 
                    left_flag = True 
                else: 
                    left_flag = False
                if (x, y+1) not in area and (x, y) in area: 
                    num_walls += not right_flag
                    right_flag = True 
                else: 
                    right_flag = False
                x += 1
        print(f"{garden[seed[0]][seed[1]]}: {len(area)} * {num_walls} = {len(area)*num_walls}")
        s+= len(area)*num_walls
    print(s)

part_2()
