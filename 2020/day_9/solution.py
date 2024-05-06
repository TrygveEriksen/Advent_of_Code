import time 

def get_numbers(): 
    with open("2020/day_9/input.txt","r") as f: 
        nums = f.readlines()
    return [int(n.strip()) for n in nums]

def part_1() -> int: 
    nums = get_numbers()

    for i in range(25, len(nums)): 
        temp = set(nums[i-25:i])
        n = nums[i]
        foo = False
        for a in temp: 
            if n-a in temp: 
                foo = True
        if not foo: 
            return n
    return -1


def part_2() -> int: 
    nums = get_numbers()
    index, goal = 0,0
    for i in range(25, len(nums)): 
        temp = set(nums[i-25:i])
        n = nums[i]
        foo = False
        for a in temp: 
            if n-a in temp: 
                foo = True
        if not foo: 
            index, goal = i, n

    for i in range(len(nums)): 
        s=0
        temp=[]
        j=i
        while s < goal: 
            temp.append(nums[j])
            s+= nums[j]
            j+=1
        if s == goal and len(temp) > 1: 
            return min(temp) + max(temp)



def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")


main()