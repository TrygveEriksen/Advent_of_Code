
def check(pos, direction, _map):
    px, py = pos
    dx, dy = direction
    if _map[px][py] == "#": 
        return False
    if _map[px][py] == ".": 
        return True
    elif _map[px][py] == "[": 
        return all([check((px+dx, py+dy), direction, _map), check((px+dx, py+dy+1), direction, _map)])
    elif _map[px][py] == "]": 
        return all([check((px+dx, py+dy), direction, _map), check((px+dx, py+dy-1), direction, _map)])

def map_replace(leftmost_pos, direction, _map): 
    posx, posy = leftmost_pos
    next_posx = posx+direction[0]
    if _map[posx+direction[0]][posy] == "]": 
        _map = map_replace((next_posx, posy-1), direction, _map)
    elif _map[posx+direction[0]][posy] == "[":
        _map = map_replace((next_posx, posy), direction, _map)
    if _map[posx+direction[0]][posy+1] == "[":
        _map = map_replace((next_posx, posy+1), direction, _map)

    if next_posx < posx: 
        clear_lines_before = _map[:next_posx]
        new_line = _map[next_posx]
        new_line = new_line[:posy] + ["[", "]"] + new_line[posy + 2: ]
        old_line = _map[posx]
        old_line = old_line[:posy] + [".", "."] + old_line[posy + 2:]
        clear_lines_after = _map[posx+1:]

        _map =clear_lines_before + [new_line] + [old_line] + clear_lines_after
    else: 
        clear_lines_before = _map[:posx]
        old_line = _map[posx]
        old_line = old_line[:posy] + [".", "."] + old_line[posy + 2:]
        new_line = _map[next_posx]
        new_line = new_line[:posy] + ["[", "]"] + new_line[posy + 2: ]

        clear_lines_after = _map[next_posx+1:]

        _map =clear_lines_before + [old_line] + [new_line] + clear_lines_after

    return _map






def part_1(): 
    with open("2024/day_15/input.txt", "r") as f: 
        _map , moves = f.read().split("\n\n")
    _map = _map.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@","@.")
    _map = [[a for a in b]for b in _map.splitlines()]
    posx, posy = 0,0
    cnt = 0
    for idx in range(len(_map)): 
        find=False
        for jdx in range(len(_map[0])): 
            if _map[idx][jdx] == "@": 
                posx, posy = idx, jdx
                find=True
                break
        if find:
            break
    d = (0,0)    
    hor = False
    for move in moves: 
        _map2 = ["".join(a for a in line) for line in _map]
        match move: 
            case "^": 
                d = (-1,0)
                hor = False
            case "v": 
                d = (1,0)
                hor = False
            case ">": 
                d = (0,1)
                hor = True
            case "<": 
                d = (0,-1)
                hor = True
            case "\n": 
                continue

        new_posx, new_posy = posx + d[0], posy + d[1]
        if _map[new_posx][new_posy] == ".": 
            _map[posx][posy] = "."
            posx, posy = new_posx, new_posy
            _map[posx][posy] = "@"
        elif _map[new_posx][new_posy] == "#": 
            continue
        else: 
            new2_posx, new2_posy = new_posx + d[0], new_posy + d[1]
            if (_map[new_posx][new_posy] == "[" or _map[new_posx][new_posy] == "]")  and hor: 
                while _map[new2_posx][new2_posy] != "." and _map[new2_posx][new2_posy] != "#": 
                    new2_posx, new2_posy = new2_posx + d[0], new2_posy + d[1]
                else: 
                    if _map[new2_posx][new2_posy] == "#": 
                        continue
                    if d == (0, 1): 
                        mapline = _map[posx][:posy] + [".", "@"] + _map[posx][posy+1:new2_posy]+_map[posx][new2_posy+1:]
                        posx, posy = new_posx, new_posy
                        _map = _map[:posx] + [mapline] + _map[posx+1:]
                    else: 
                        mapline = _map[posx][:new2_posy] + _map[posx][new2_posy+1: new_posy+1] + ["@", "."] + _map[posx][posy+1:]
                        posx, posy = new_posx, new_posy
                        _map = _map[:posx] + [mapline] + _map[posx+1:]
            
            elif _map[new_posx][new_posy] == "[": 
                if all([check((new_posx, new_posy), d, _map), check((new_posx, new_posy+1), d, _map)]): 
                    _map = map_replace((new_posx, posy), d, _map)
                    _map[posx][posy] = "."
                    posx, posy = new_posx, new_posy
                    _map[posx][posy] = "@"
            elif _map[new_posx][new_posy] == "]":
                if all([check((new_posx, new_posy), d, _map), check((new_posx, new_posy-1), d, _map)]): 
                    _map = map_replace((new_posx, posy-1), d, _map)
                    _map[posx][posy] = "."
                    posx, posy = new_posx, new_posy
                    _map[posx][posy] = "@"
             


    _map2 = ["".join(a for a in line) for line in _map]
    for idx in range(len(_map)): 
        for jdx in range(len(_map[0])): 
            if _map[idx][jdx] == "[": 
                cnt += 100 * idx + jdx
    print(cnt)
part_1()