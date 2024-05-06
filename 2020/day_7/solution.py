import time
import re    

class Node: 
    def __init__(self, name:str): 
        self.visited = 0
        self.nb = []
        self.name = name
        self.child_sum = 0

d = {}

#vibrant aqua bags contain 1 shiny magenta bag, 2 muted teal bags, 1 dim magenta bag, 1 muted chartreuse bag.
def get_bags(): 
    with open("2020/day_7/input.txt", "r") as f: 
        bags = [line.strip().replace("bags", "").replace("bag","").replace("contain", ",").replace(" .","").replace("  ", "") for line in f.readlines()]
    bags = [line.replace(" ,",",").replace(", ",",").replace(", ",",").split(",") for line in bags]
    return bags


def part_1() -> int: #does not work anymore with new function for input
    bags = get_bags()
    
    for b in bags: 
        if not b[0] in d: 
            d[b[0]] = Node(b[0])
        for i in range(1,len(b)):
            if not b[i] in d: 
                d[b[i]] = Node(b[i])
            d[b[i]].nb.append(d[b[0]])  
    
    q = [d["shiny gold"]] 
    c = -1

    while len(q): 
        N = q.pop(0)
        N.visited = 1 
        c+= 1
        for n in  N.nb: 
            if not (n.visited or n in q): 
                q.append(n)
    return c


def part_2() -> int:
    bags = get_bags()
    
    q = [] 
    for b in bags: 
        if b[1] == "no other": 
            if b[0] not in d: 
                d[b[0]] = Node(b[0])
            continue
        if not b[0] in d: 
            d[b[0]] = Node(b[0])
        for i in range(1,len(b)):
            a,c = b[i].split(" ",1)
            if not c in d: 
                d[c] = Node(c)
            d[b[0]].nb.append((int(a), d[c]))    
    
    return visit_nb(d["shiny gold"]) - 1
    

def visit_nb(node:Node) -> int: 
    s = 1
    if node.child_sum: 
        return node.child_sum

    for n in node.nb: 
        s+= n[0]*visit_nb(n[1])
    node.child_sum  = s
    return s
        

def main():
    start = time.perf_counter()
    print(part_2())
    stop = time.perf_counter()
    print(f"Process used {stop-start} seconds")


main()






    
