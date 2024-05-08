import time

def get_input(): 
    with open("2020/day_15/input.txt", "r") as f: 
        return [int(i) for i in f.readline().strip().split(",")]

def part_1(): 
    nums = get_input()
    ret = nums[-1]
    nums = nums[:-1]
    d = set(nums)

    def check(let): 
        a = 0
        for i in range(len(nums)): 
            if nums[i] == let: 
                a = i 
        return a

    for i in range(2, 2020): 
        old = ret
        if ret in d : 
            ret = i - check(ret)
            nums.append(old)
        else: 
            ret = 0
            nums.append(old)
            d.add(old)
    
    return old

def part_2(): 
    nums = get_input()
    ret = nums[-1]
    d = {nums[i]:i for i in range(len(nums)-1)}
    
    for i in range(5, 30000000-1): 
        if ret in d: 
            new = i - d[ret]
            d[ret] = i
            ret = new 

        else: 
            d[ret] = i
            ret = 0

    return ret

def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")


main()