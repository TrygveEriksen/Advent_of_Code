import time

def get_passwords() -> list:
    with open("2020/day_2/input.txt", "r") as f: 
        passwords = [line.strip().replace("-"," ").replace(":","").split(" ") for line in f.readlines()]
    return passwords

def part_1() -> int: 
    i = 0
    passwords = get_passwords
    for p in passwords:
        c = p[3].count(p[2])
        i += (int(p[0]) <= c and c <= int(p[1]))
    return i

def part_2() -> int: 
    i = 0
    passwords = get_passwords()
    for p in passwords: 
        n1 = int(p[0]) - 1
        n2 = int(p[1]) - 1
        l = p[2]
        w = p[3]
        i += (w[n1] == l) ^ (w[n2] == l)

    return i

def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")


main()