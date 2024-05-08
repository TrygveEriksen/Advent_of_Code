import time 

def get_input(): 
    with open("2020/day_13/input.txt", "r") as f:
        timestamp = int(f.readline().strip())
        times = f.readline().split(",")
    times = [int(i) for i in times if i.isdigit()]
    return timestamp, times

def get_input_2(): 
    with open("2020/day_13/input.txt", "r") as f:
        timestamp = int(f.readline().strip())
        times = f.readline().split(",")
    times = [(int(times[i]), i) for i in range(len(times)) if times[i].isdigit()]
    return times

def part_1(): 
    timestamp, times = get_input()
    m = max(times)
    t = 0
    for time in times: 
        if time - timestamp % time < m: 
            m = time - timestamp % time 
            t = time 
    return t*m

def part_2(): 
    # Todo : write chinese remainder calculator, solved this one using one on the internet
    return


def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")


main()