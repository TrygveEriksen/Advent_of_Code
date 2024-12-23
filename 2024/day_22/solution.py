import sys

sys.setrecursionlimit(1000000)

def mix(n1, n2): 
    return n1 ^n2

def prune(num): 
    return num % 16777216

def next_secret(num):
    num = prune(mix(num, num *64))
    num = prune(mix(num, num//32))
    num = prune(mix(num, num*2048))
    return num

def part_1(): 
    data = [*map(int, open("2024/day_22/input.txt", "r").read().split("\n"))]
    prices = []
    changes = []
    for d in data:
        res = [d] 
        for _ in range(2001): 
            res.append(next_secret(res[-1]))
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