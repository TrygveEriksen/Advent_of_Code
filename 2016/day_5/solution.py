import hashlib
from typing import Any
def part_1():
    password = open("2016/day_5/input.txt").read().strip()
    s = ""
    n = 0
    while len(s) < 8:
        h = hashlib.md5((password + str(n)).encode()).hexdigest()
        if h[:5] == "00000":
            s += h[5]
            print(s)
        n+=1
    return s

def part_2():
    password = open("2016/day_5/input.txt").read().strip()
    s: list[None | str] = [None for _ in range(8)]
    n = 0
    while None in s:
        h = hashlib.md5((password + str(n)).encode()).hexdigest()
        n+=1
        if h[:5] == "00000":
            idx = h[5]
            if not idx.isdigit() or not int(idx) < 8 or not s[int(idx)] is None:
                continue
            s[int(idx)] = h[6]
            print("".join(a if a is not None else "_" for a in s))
    return "".join(s)

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
