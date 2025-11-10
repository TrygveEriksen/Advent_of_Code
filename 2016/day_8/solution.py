def part_1():
    screen = [[" " for i in range(50)] for j in range(6)]
    with open("2016/day_8/input.txt") as f: 
        lines = [line.strip() for line in f.readlines()]
    for line in lines: 
        if line[:4] == "rect":
            line = line.replace("rect ", "")
            w,h = [int(i) for i in line.split("x")]
            for hdx in range(h): 
                for wdx in range(w):
                    screen[hdx][wdx] = "#"
        elif line[:len("rotate column")] == "rotate column":
            line = line.removeprefix("rotate column x=")
            col, dist = [int(i) for i in line.split(" by ")]
            column = [row[col] for row in screen]
            dist %= len(column)
            for d in range(dist):
                column.insert(0, column.pop(-1))
            for idx, row in enumerate(screen): 
                row[col] = column[idx]

        elif line[:len("rotate row")] == "rotate row":
            line = line.removeprefix("rotate row y=")
            r, dist = [int(i) for i in line.split(" by ")]
            row = screen[r]
            dist %= len(row)
            for d in range(dist):
                row.insert(0, row.pop(-1))
            screen[r] = row
    s = 0
    for row in screen: 
        s += [a == "#" for a in row].count(True)
        print("".join(row))
    print(f"Part 1: {s}")


part_1()
