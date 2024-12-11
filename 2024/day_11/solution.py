from functools import cache

@cache
def check(n, d): 
    if not d: 
        return 1
    if n == 0: 
        return check(1, d-1)
    elif not len(str(n))%2: 
        return check(int(str(n)[:len(str(n))//2]), d-1) + check(int(str(n)[len(str(n))//2:]), d-1)
    else: 
        return check(n*2024, d-1)

def part_1(): 
    nums = [*map(int, "28 4 3179 96938 0 6617406 490 816207".split())]
    s = 0
    for num in nums: 
        s+= check(num, 75)
    print(s)

part_1()