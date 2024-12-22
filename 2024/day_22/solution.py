from functools import cache
import sys

sys.setrecursionlimit(1000000)

def next_secret(num, d):
    if d == 0: 
        return []
    ret = [num]
    new = num * 64 
    num = new ^ num
    num %= 16777216

    new = num // 32
    num = new ^ num
    num %= 16777216

    new = num * 2048
    num = new ^ num
    num %= 16777216
    return ret + next_secret(num, d-1)

def part_1(): 
    data = [*map(int, open("2024/day_22/input.txt", "r").read().split("\n"))]
    prices = []
    changes = []
    for d in data: 
        res = next_secret(d, 2001)
        res = [r%10 for r in res]
        prices.append(res)
        changes.append([res[i+1]-res[i] for i in range(len(res)-1)])  

    change_map = {}
    for i in range(len(changes)): 
        cur = set()
        for j in range(len(changes[i])-3): 
            seq = (changes[i][j], changes[i][j+1], changes[i][j+2], changes[i][j+3])
            price = prices[i][j+4]
            if seq not in cur: 
                cur.add(seq)
                if seq in change_map: 
                    change_map[seq] = change_map[seq] + price
                else: 
                    change_map[seq] = price
    print(max(change_map.values()))

part_1()