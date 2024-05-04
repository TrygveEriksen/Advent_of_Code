import time

def get_nums() -> set: 
    with open("2020/day_1/input.txt", "r") as f: 
        nums = {int(i) for i in f.readlines()}
    return nums


def part_1() -> int:
    nums = get_nums()
    for num in nums: 
        if 2020 - num in nums: 
            return (2020-num)*num
    return -1 #found nothing


def part_2() -> int:  
    nums = get_nums()
    for num1 in nums: 
        for num2 in nums: 
            if 2020 - (num1 + num2) in nums: 
                return (2020 - (num1 + num2)) * num1 * num2
    return -1 #found nothing

     

    
def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")

main()