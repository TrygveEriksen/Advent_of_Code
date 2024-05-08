import time 

def get_input(): 
    with open("2020/day_12/input.txt", "r") as f: 
        return [line.strip() for line in f.readlines()]

def rotate_l(vector): 
    n_e =  - 1 * vector[1]
    n_n =  vector[0]
    return [n_e, n_n]

def part_1(): 
    north = 0
    east = 0 
    dir_ = [1, 0]
    for line in get_input(): 
        instruction = line[:1]
        num = int(line[1:])

        match instruction: 
            case "F": 
                east += num * dir_[0]
                north += num * dir_[1]
            case "R": 
                for i in range(4 - (num // 90)): 
                    dir_ = rotate_l(dir_)
            case "L": 
                for i in range(num // 90): 
                    dir_ = rotate_l(dir_)
            case "N": 
                north += num
            case "S": 
                north -= num
            case "E": 
                east += num
            case "W": 
                east -= num
    return abs(north) + abs(east)

def part_2(): 
    ship = [0, 0]
    wp = [10, 1]


    for line in get_input(): 
        instruction = line[:1]
        num = int(line[1:])

        match instruction: 
            case "F": 
                ship[0] += num * (wp[0])
                ship[1] += num * (wp[1])
            case "R": 
                for i in range(4 - (num // 90)): 
                    wp = rotate_l(wp)
            case "L": 
                for i in range(num // 90): 
                    wp = rotate_l(wp)
            case "N": 
                wp[1] += num
            case "S": 
                wp[1] -= num
            case "E": 
                wp[0] += num
            case "W": 
                wp[0] -= num
    return abs(ship[0]) + abs(ship[1])

def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")


main()