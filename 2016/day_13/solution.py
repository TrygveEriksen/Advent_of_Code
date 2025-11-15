import heapq

my_number = 1364
my_target = (31, 39)

def m_dist(point): 
    global my_target 
    return abs(my_target[0] - point[0]) + abs(my_target[1] - point[1])

def neighbours(point): 
    x, y = point
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def valid(point): 
    x,y = point
    if x < 0 or y < 0: 
        return False
    num = x**2 + 3*x + 2*x*y + y + y*y + my_number
    bstr = str(bin(num))
    return bstr.count('1') % 2 == 0

def part_1():
    visited = set()
    #Queue of (dist + heuristic, dist, position)
    q = [(m_dist((1,1)), 0, (1,1))]
    while len(q):
        h, d, cur = heapq.heappop(q)
        if cur == my_target: 
            return d
        for n in neighbours(cur): 
            if valid(n) and n not in visited: 
                print(f"Visiting: {n}, distance= {d+1}")
                heapq.heappush(q, (d + m_dist(n) + 1, d+1, n))
                visited.add(n)
    return -1

def part_2():
    visited = set((1,1))
    #Queue of (dist + heuristic, dist, position)
    q = [(0, (1,1))]
    while len(q):
        d, cur = heapq.heappop(q)
        if d >= 49: 
            continue
        for n in neighbours(cur): 
            if valid(n) and n not in visited: 
                print(f"Visiting: {n}, distance= {d+1}")
                heapq.heappush(q, (d+1, n))
                visited.add(n)
    return len(visited)
print(part_2())

