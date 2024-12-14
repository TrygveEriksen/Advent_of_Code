
def part_1(): 
    with open("2024/day_14/input.txt", "r") as f: 
        robots = [line.split() for line in f.read().replace("p=", "").replace("v=", "").replace(",", " ").splitlines()]
    positions = [(int(a[0]), int(a[1])) for a in robots]
    directions = [(int(a[2]), int(a[3])) for a in robots]
    cols = 101
    rows = 103
    seconds = 0

    while 1:  
        seconds += 1
        print_flag = False

        for i in range(rows): 
            s= ""
            for j in range(cols): 
                c = len([a for a in positions if a[1]==i and a[0]==j])
                s += "#" if c else " "
            if "#######" in s: 
                print_flag = True
                break

        if print_flag: 
            for i in range(rows): 
                s=""
                for j in range(cols): 
                    c = len([a for a in positions if a[1]==i and a[0]==j])
                    s += "#" if c else " "
                print(s)
            if (q := input(str(seconds))) =="q": 
                break

        new_positions = []
        for i in range(len(positions)): 
            new_pos = ((positions[i][0] + directions[i][0])%cols, (positions[i][1] + directions[i][1])%rows)
            new_positions.append(new_pos)

        positions = new_positions
        print(seconds)

    p=len([a for a in positions if a[1] < rows//2 and a[0] < cols//2])
    p*=len([a for a in positions if a[1] > rows//2 and a[0] < cols//2])
    p*=len([a for a in positions if  a[1] > rows//2 and a[0] > cols//2])
    p*=len([a for a in positions if a[1] < rows//2 and a[0] > cols//2])


            

    print(p)
part_1()